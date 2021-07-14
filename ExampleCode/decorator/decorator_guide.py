# https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-i-function-registration
"""
def request_logger(f):
    return f


@request_logger
def log_a_request(request):
    pass


log_a_request = request_logger(log_a_request)
"""
all_request_logger = []


def request_logger(f):
    all_request_logger.append(f)
    return f


@request_logger
def log_a_request(request):
    print(request.method, request.path)