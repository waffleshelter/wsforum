FROM python:3.11.9-slim

WORKDIR /backend

COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY . .

ENV PYTHONPATH=/backend/src

CMD ["python", "-m", "src.main"]