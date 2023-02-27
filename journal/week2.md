# Week 2 — Distributed Tracing

## Required Homework/Tasks

“Observability” is being able to fully understand our systems. In control theory, observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs. The observability and controllability of a system are mathematical duals.

[WIKIPEDIA](https://en.wikipedia.org/wiki/Observability)

#### Honeycomb
-------------
Observability for Production Systems. Debug using Events, Traces, and Logs in one tool. Instrument code automatically, surface outliers instantly.

#### Honeycomb's Features
* High-performance querying against high-cardinality or sparse events.
* Accepts any structured JSON objects with a write key.
* Submit events via API.
* Open source agents, log tailers, SDKs, and integrations.
* Customizable high-performance query windows.
* Customizable storage windows provide control over retention and costs.
* Always have access to the the raw data behind query results and graphs.
* Shared boards.
* Individual and team query histories.
* Triggers and notifications.
* Secure Tenancy for data compliance.


##### steps to start your observability journey with Honeycomb.

1. Create a free Honeycomb account
2. Name your team
3. Instrument Your Application to Send Telemetry Data to Honeycomb
4. Explore your data

##### Install Packages
Install these packages to instrument a Flask app with OpenTelemetry:
```
pip install opentelemetry-api
pip install opentelemetry-sdk
pip install opentelemetry-exporter-otlp-proto-http
pip install opentelemetry-instrumentation-flask
pip install opentelemetry-instrumentation-requests
```

##### Initialize
```
# app.py updates
    
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```

##### Configure and Run
```
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=tG937G8HLMb0tgQEnoCRTB"
export OTEL_SERVICE_NAME="your-service-name"
python app.py
```
![week-2-honeycomb-1](https://user-images.githubusercontent.com/88502375/221677153-a3828096-b04f-4cd7-a498-468f322cfa39.jpg)

![week-2-honeycomb-id-1](https://user-images.githubusercontent.com/88502375/221677182-5c48415d-31d4-4f04-9c9b-e8fbcaa0fda9.jpg)





#### AWS X-Ray
--------------
