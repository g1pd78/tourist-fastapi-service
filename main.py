from fastapi import FastAPI, Request

from admin import manager
from login import user
from feedback import post
from places import destination
from tourist import visit

app = FastAPI()

app.include_router(manager.router)
app.include_router(user.router)
app.include_router(destination.router)
app.include_router(visit.router)
app.include_router(post.router, prefix="/post")
