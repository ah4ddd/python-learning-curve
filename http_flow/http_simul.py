class Request:
    def __init__(self, method, path, data=None):
        self.method = method
        self.path = path
        self.data = data or {}

class Response:
    def __init__(self, content):
        self.content = content

def home(request):
    return Response("Welcome to home page")

def topics(request):
    return Response("Topics: Life, Freedom")

def new_topic(request):
    if request.method == 'POST':
        return Response(f"Saved topic: {request.data.get('text')}")
    else:
        return Response("Show new topic form")

URLS = {
    "/": home,
    "/topics/": topics,
    "/new_topic/": new_topic,
}

def handle_request(request):
    print(f"Incoming request: {request.method} {request.path}")

    view_function = URLS.get(request.path)

    if not view_function:
        return Response("404 not found")
    return view_function(request)

request = Request("GET", "/topics/")
response = handle_request(request)
print(response.content)

request = Request(
    method="POST",
    path="/new_topic/",
    data={"text": "Space race"}
)

response = handle_request(request)
print(response.content)

