from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from jose import jwt, JWTError
import os

# Very small middleware to resolve tenant from subdomain or JWT claim
class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        tenant_id = None
        host = request.headers.get("host", "")
        # try subdomain like tenant1.app.local or tenant1.local
        if host:
            parts = host.split(".")
            if len(parts) >= 3:
                tenant_id = parts[0]

        # fallback: try Authorization: Bearer <jwt>
        auth = request.headers.get("authorization")
        if not tenant_id and auth and auth.lower().startswith("bearer "):
            token = auth.split(" ", 1)[1]
            try:
                # if public key or secret configured we can decode - for now don't verify
                # but extract claims
                claims = jwt.get_unverified_claims(token)
                tenant_id = claims.get("tenant_id") or claims.get("tid")
            except JWTError:
                tenant_id = None

        # attach to request state
        request.state.tenant = tenant_id or os.environ.get("DEFAULT_TENANT", "demo_tenant")
        return await call_next(request)
