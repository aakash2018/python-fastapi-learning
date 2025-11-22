FROM python:3.13-slim as base
WORKDIR /app

FROM base as builder
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --prefix=/install -r requirements.txt

FROM base as runtime
COPY --from=builder /install /usr/local
COPY backend /app
ENV PYTHONPATH=/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--loop", "asyncio"]
