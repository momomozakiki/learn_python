from flask import Flask, request

app = Flask(__name__)
all_request_loggers = []


def request_logger(f):
    all_request_loggers.append(f)
    return f


def invoke_request_loggers(request):
    for logger in all_request_loggers:
        logger(request)


@request_logger
def log_a_request(request):
    print(request.method, request.path)


@app.route('/')
def index():
    invoke_request_loggers(request)
    return 'Hello World!'
