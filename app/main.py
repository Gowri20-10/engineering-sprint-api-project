from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from app.core.database import Base, engine
from app.core.exceptions import http_exception_handler, general_exception_handler
from app.controllers import auth_controller, ai_controller

app = FastAPI(title="Engineering Sprint API")

Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(ai_controller.router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)
