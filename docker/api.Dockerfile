FROM python:3.12-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x docker/api-entrypoint.sh

CMD ["./docker/api-entrypoint.sh"]
