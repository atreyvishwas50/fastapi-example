from fastapi import FastAPI
from model import db_config, models
from router import train_router, daily_data_router

models.db_config.Base.metadata.create_all(bind=db_config.engine)


app = FastAPI()


app.include_router(train_router.router)
app.include_router(daily_data_router.router)
