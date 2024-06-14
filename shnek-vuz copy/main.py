import uvicorn

from fastapi import FastAPI

from source.controllers import api, pages

app = FastAPI()

app.include_router(api.router)
app.include_router(pages.router)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=3000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
