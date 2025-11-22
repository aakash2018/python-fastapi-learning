import asyncio
import json
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
from .middleware import TenantMiddleware
from .db import get_db
from bson import ObjectId


app = FastAPI(title="AI Multi-tenant Demo Backend")
app.add_middleware(TenantMiddleware)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/ready")
async def ready():
    db = get_db()
    # very lightweight check
    try:
        await db.list_collection_names()
        return {"ready": True}
    except Exception:
        raise HTTPException(status_code=503, detail="DB not available")


@app.get("/chat/stream")
async def chat_stream(request: Request):
    """Mock streaming chat endpoint returning newline-delimited JSON chunks.

    Each yielded line is a JSON object with `type` and `content`.
    Types: text, markdown, chart
    """
    tenant = getattr(request.state, "tenant", "demo_tenant")

    db = get_db()

    async def event_gen():
        # create a session document
        session = {"tenant_id": tenant, "user_id": "demo_user", "use_case_id": "demo_usecase"}
        session_result = await db["chat_sessions"].insert_one(session)
        session_id = str(session_result.inserted_id)

        # Simulate an assistant that first sends text, then markdown/code, then chart data
        messages = [
            {"type": "text", "content": f"Hello from tenant: {tenant}. This is a demo response."},
            {"type": "markdown", "content": "**Sample** response with code:\n```python\nprint('hello')\n```"},
            {"type": "chart", "content": {"type": "line", "data": {"labels": ["Jan","Feb","Mar"], "datasets": [{"label": "Demo", "data": [10, 20, 15]}]}}}
        ]

        for chunk in messages:
            # if client disconnects, stop
            if await request.is_disconnected():
                break
            await asyncio.sleep(0.6)

            # persist the message per tenant/session
            msg_doc = {
                "tenant_id": tenant,
                "session_id": session_id,
                "user_id": "demo_user",
                "role": "assistant",
                "content": chunk,
            }
            await db["messages"].insert_one(msg_doc)

            yield json.dumps(chunk) + "\n"

    return StreamingResponse(event_gen(), media_type="application/x-ndjson")
