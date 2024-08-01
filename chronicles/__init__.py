from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def server():
    async def hello_world(request):
        return JSONResponse({"message": "Hello, World@!"})

    routes = [
        Route("/", endpoint=hello_world)
    ]

    return Starlette(routes=routes)


__all__ = ['server']


def __dir__():
    return __all__
