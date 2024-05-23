"""FastAPI REST APIs"""

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from views import shops, profile, banner, help_videos


app = FastAPI()
app.add_middleware(GZipMiddleware)
app.include_router(shops.router)
app.include_router(profile.router)
app.include_router(banner.router)
app.include_router(help_videos.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


