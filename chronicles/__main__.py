# from chainlit.cli import cli
from chronicles.cli import cli
import asyncio
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def start():
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port="8090",
    )
    server = uvicorn.Server(config)
    await server.serve()

    # Run the asyncio event loop instead of uvloop to enable re entrance
    asyncio.run(start())

if __name__ == "__main__":
    # cli(app_name="chronicles")

    async def hello_world(request):
        return JSONResponse({"message": "Hello, World!"})

    routes = [
        Route("/", endpoint=hello_world)
    ]
    app = Starlette(routes=routes)

    # asyncio.run(start())
    print ("START MAIN")
