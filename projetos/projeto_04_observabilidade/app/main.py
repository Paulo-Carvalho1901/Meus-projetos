import time
import random
import logging

from fastapi import FastAPI, HTTPException
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# ─────────────────────────────────────────────
# Recurso compartilhado entre sinais
# ─────────────────────────────────────────────
resource = Resource.create({
    "service.name": "api-observabilidade",
    "service.version": "1.0.0",
    "deployment.environment": "desenvolvimento",
})

OTEL_ENDPOINT = "http://otel-collector:4317"

# ─────────────────────────────────────────────
# Traces
# ─────────────────────────────────────────────
tracer_provider = TracerProvider(resource=resource)
otlp_span_exporter = OTLPSpanExporter(endpoint=OTEL_ENDPOINT, insecure=True)
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_span_exporter))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

# ─────────────────────────────────────────────
# Métricas
# ─────────────────────────────────────────────
otlp_metric_exporter = OTLPMetricExporter(endpoint=OTEL_ENDPOINT, insecure=True)
metric_reader = PeriodicExportingMetricReader(otlp_metric_exporter, export_interval_millis=5000)
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

requisicoes_counter = meter.create_counter(
    name="api.requisicoes.total",
    description="Total de requisições recebidas",
    unit="1",
)

latencia_histogram = meter.create_histogram(
    name="api.latencia.ms",
    description="Latência das requisições em milissegundos",
    unit="ms",
)

erros_counter = meter.create_counter(
    name="api.erros.total",
    description="Total de erros retornados",
    unit="1",
)

# ─────────────────────────────────────────────
# Logs
# ─────────────────────────────────────────────
logger_provider = LoggerProvider(resource=resource)
otlp_log_exporter = OTLPLogExporter(endpoint=OTEL_ENDPOINT, insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(otlp_log_exporter))
set_logger_provider(logger_provider)

otel_handler = LoggingHandler(level=logging.DEBUG, logger_provider=logger_provider)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api-observabilidade")
logger.addHandler(otel_handler)

# ─────────────────────────────────────────────
# Aplicação FastAPI
# ─────────────────────────────────────────────
app = FastAPI(title="API de Observabilidade com OpenTelemetry")


@app.get("/")
def raiz():
    """Endpoint raiz — verifica se a API está no ar."""
    with tracer.start_as_current_span("raiz") as span:
        span.set_attribute("endpoint", "/")
        logger.info("Endpoint raiz acessado")
        requisicoes_counter.add(1, {"endpoint": "/", "metodo": "GET"})
        return {"mensagem": "API com OpenTelemetry rodando!", "status": "ok"}


@app.get("/pedido/{pedido_id}")
def processar_pedido(pedido_id: int):
    """Simula o processamento de um pedido com trace, métrica e log."""
    inicio = time.time()

    with tracer.start_as_current_span("processar-pedido") as span:
        span.set_attribute("pedido.id", pedido_id)
        logger.info(f"Iniciando processamento do pedido {pedido_id}")

        # Simula validação
        with tracer.start_as_current_span("validar-pedido"):
            time.sleep(random.uniform(0.01, 0.05))
            if pedido_id <= 0:
                erros_counter.add(1, {"endpoint": "/pedido", "tipo": "validacao"})
                logger.error(f"Pedido inválido: id={pedido_id}")
                raise HTTPException(status_code=400, detail="ID de pedido inválido")

        # Simula persistência
        with tracer.start_as_current_span("persistir-pedido"):
            time.sleep(random.uniform(0.05, 0.15))
            if random.random() < 0.1:          # 10 % de falha simulada
                erros_counter.add(1, {"endpoint": "/pedido", "tipo": "persistencia"})
                logger.error("Falha simulada ao persistir pedido")
                raise HTTPException(status_code=500, detail="Erro interno ao salvar pedido")

        # Simula notificação
        with tracer.start_as_current_span("notificar-cliente"):
            time.sleep(random.uniform(0.01, 0.03))

        latencia = (time.time() - inicio) * 1000
        latencia_histogram.record(latencia, {"endpoint": "/pedido"})
        requisicoes_counter.add(1, {"endpoint": "/pedido", "metodo": "GET"})

        logger.info(f"Pedido {pedido_id} processado em {latencia:.2f} ms")
        span.set_attribute("pedido.latencia_ms", latencia)

        return {
            "pedido_id": pedido_id,
            "status": "processado",
            "latencia_ms": round(latencia, 2),
        }


@app.get("/saude")
def saude():
    """Health-check da aplicação."""
    with tracer.start_as_current_span("health-check") as span:
        span.set_attribute("endpoint", "/saude")
        logger.info("Health-check realizado")
        requisicoes_counter.add(1, {"endpoint": "/saude", "metodo": "GET"})
        return {"status": "saudável"}


@app.get("/carga")
def gerar_carga(quantidade: int = 10):
    """Gera múltiplas operações para popular os dashboards."""
    with tracer.start_as_current_span("gerar-carga") as span:
        span.set_attribute("carga.quantidade", quantidade)
        logger.info(f"Gerando carga com {quantidade} operações")

        resultados = []
        for i in range(1, quantidade + 1):
            with tracer.start_as_current_span(f"operacao-{i}"):
                duracao = random.uniform(0.01, 0.1)
                time.sleep(duracao)
                latencia_histogram.record(duracao * 1000, {"endpoint": "/carga"})
                requisicoes_counter.add(1, {"endpoint": "/carga", "metodo": "GET"})
                resultados.append({"operacao": i, "duracao_ms": round(duracao * 1000, 2)})

        return {"operacoes_realizadas": quantidade, "resultados": resultados}
