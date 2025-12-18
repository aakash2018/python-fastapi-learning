from fastapi import Request, Response


# creating middleware
async def my_firsy_middleware(request: Request, call_next):
    print("Middleware :Before processing the request")
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print("Middleware :After processing the request,before returning response")
    print(f"Response: {response.status_code}")
    print("Middleware :After returning response")

    return response
