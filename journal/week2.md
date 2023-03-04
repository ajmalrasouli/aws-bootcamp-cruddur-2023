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
```sh
pip install opentelemetry-api
pip install opentelemetry-sdk
pip install opentelemetry-exporter-otlp-proto-http
pip install opentelemetry-instrumentation-flask
pip install opentelemetry-instrumentation-requests
```

##### Initialize
```py
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
```py
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=tG937G8HLMb0tgQEnoCRTB"
export OTEL_SERVICE_NAME="your-service-name"
python app.py
```
![week-2-honeycomb-1](https://user-images.githubusercontent.com/88502375/221677153-a3828096-b04f-4cd7-a498-468f322cfa39.jpg)

![week-2-honeycomb-id-1](https://user-images.githubusercontent.com/88502375/221677182-5c48415d-31d4-4f04-9c9b-e8fbcaa0fda9.jpg)





#### AWS X-Ray
--------------

##### Install aws-sdk
Add to the requirements.txt
```sh
aws-xray-sdk
```

use pip to install python inpendencies
```sh
pip install -r requirements.txt
```

Add to app.py

```py
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
```
![Xray](https://user-images.githubusercontent.com/88502375/221696030-5b48cebc-8eb4-4423-b89d-b23baa90b9a7.png)

![xray backend](https://user-images.githubusercontent.com/88502375/221696202-6079fde6-d428-45cf-a85e-3aee23acc158.png)

Note: I have not been able to see the Group 'backend-flask' on the AWS Cloud Watch.


#### CloudWatch Logs
--------------------
Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.

![Product-Page-Diagram_Amazon-CloudWatch](https://user-images.githubusercontent.com/88502375/221828823-24d149c6-d9e8-411b-b1bf-bf444c2fa973.png)

Add to the requirements.txt

```
watchtower
```
```sh
pip install -r requirements.txt
```

In app.py

```
import watchtower
import logging
from time import strftime
```

```py
# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("some message")
```
![week-2-cloudwatch-1](https://user-images.githubusercontent.com/88502375/221993796-06bec413-01ea-4a73-adda-a72391f6a167.jpg)


![week-2-cloudwatch-2](https://user-images.githubusercontent.com/88502375/221994868-f8358cff-a46f-422e-9d21-1f1670b1d895.jpg)


#### Rollbar
--------------
Instrument any application and capture all app crashes, errors and exceptions as they happen. Turn errors into signals you can use to focus on what’s wrong. Don’t get stuck digging through logs or creating queries and filters just to find the problem.

Created a new project in Rollbar called Cruddur

![week-2-rollbar-1](https://user-images.githubusercontent.com/88502375/222267239-90b370f2-2694-4eae-b709-e28713a75da6.jpg)

I have included to requirements.txt


```
blinker
rollbar
```

Installed dependencies

```sh
pip install -r requirements.txt
```

Aslo , I need to set the access token for Rollbar through environment variable.

```sh
export ROLLBAR_ACCESS_TOKEN=""
gp env ROLLBAR_ACCESS_TOKEN=""
```

Added to backend-flask for docker-compose.yml

```yml
ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}"
```

Import for Rollbar

```py
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
```

```py
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        rollbar_access_token,
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
```

For testing let's add an endpoint to app.py

```py
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"
```

![week-2-rollbar-test-2](https://user-images.githubusercontent.com/88502375/222273547-c1191629-b2d1-4731-9d67-91ed74db57c8.jpg)


![week-2-rollbar-dashboard-3](https://user-images.githubusercontent.com/88502375/222273981-2bbe64ad-f9ea-4c37-b163-50598fac1892.jpg)


![week-2-rollbar-4](https://user-images.githubusercontent.com/88502375/222274360-5b68863e-6abb-4f46-b87c-6ad0a524cf49.jpg)


## Github Codespaces CDE
GitHub Codespaces is a cloud-based development environment that enables developers to code from anywhere.
Every GitHub users have free access to 60 hours of GitHub Codespaces a month, and you can upgrade to a paid plan if you need more hours.
I have setup the Cruddur app on Github Codespaces.



![week-2-codespaces-1](https://user-images.githubusercontent.com/88502375/222907745-c4df3393-5740-4fdd-8ee0-d1e048f59afa.jpg)


![week-2-codespaces-2](https://user-images.githubusercontent.com/88502375/222907755-7e9fa3b2-ecbc-45ca-a71e-3c41ba51668c.jpg)


![week-2-codespaces-cruddur-app](https://user-images.githubusercontent.com/88502375/222907765-17f67c1d-7202-40ee-a3fe-69784b4efa96.jpg)


![week-2-codespaces-cruddur-app-2](https://user-images.githubusercontent.com/88502375/222907770-e12a77dc-a3a3-457b-a1d1-125a994e3ac1.jpg)


## Homework Challenges

1. Run custom queries in Honeycomb and save them
For example, consider a query on Visualize COUNT, P95(duration_ms), Group By endpoint. The results table from this query might look something like this:

![week-2-honeycombquery-1](https://user-images.githubusercontent.com/88502375/222572590-7631a109-e97c-4645-a2d1-e11355b2f141.jpg)


2.Run custom queries in Honeycomb and save them


![week-2-honeycombquery-2](https://user-images.githubusercontent.com/88502375/222575137-ac8eab49-4d38-4d68-8631-c1b2af8fac43.jpg)





References: https://aws.amazon.com/cloudwatch/
