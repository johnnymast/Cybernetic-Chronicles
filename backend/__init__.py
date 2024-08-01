from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def hello_world(request):
    return JSONResponse({"message": "Hello, World!"})

routes = [
    Route("/", endpoint=hello_world)
]
app = Starlette(routes=routes)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
