from fastapi import FastAPI

# import settings 
from app.core.config import settings

# import packages

from beanie import init_beanie

from motor.motor_asyncio import AsyncIOMotorClient






# start dev


app = FastAPI(
    title=settings.PROJECT_NAME
)



@app.on_event("startup")
async def app_init():
    """
    initialize application
    """

    db_client = AsyncIOMotorClient(settings.DATABASE_URL).fastapiMongo

    await init_beanie(
        database=db_client,
        document_models=[]
    )

@app.get("/")
async def hello():
    return {
        "message" : "api working"
    }