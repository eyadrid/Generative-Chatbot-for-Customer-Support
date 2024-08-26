import os
from fastapi import FastAPI
from controller import router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("UVICORN_HOST"), port=int(os.getenv("UVICORN_PORT")))

