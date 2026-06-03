FROM python:3.12-slim

WORKDIR /app

# Certificado corporativo (Zscaler) — necessário em redes que fazem TLS inspection
COPY certs/ /usr/local/share/ca-certificates/extra/
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        gcc \
    && cp /usr/local/share/ca-certificates/extra/*.pem /usr/local/share/ca-certificates/ 2>/dev/null || true \
    && for f in /usr/local/share/ca-certificates/extra/*.pem; do \
           cp "$f" "/usr/local/share/ca-certificates/$(basename "${f%.pem}").crt"; \
       done \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Faz pip / requests / SSL usarem o bundle do sistema (já com o cert corporativo)
ENV PIP_CERT=/etc/ssl/certs/ca-certificates.crt \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
