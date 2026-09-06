# Uses an older base image with known CVEs
FROM python:3.7-slim

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
