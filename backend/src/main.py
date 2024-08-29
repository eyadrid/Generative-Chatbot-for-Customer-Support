import os
from fastapi import FastAPI
from controller import router
from dotenv import load_dotenv

load_dotenv() 

# Créer une instance de l'application FastAPI
app = FastAPI()

# Inclure le routeur défini dans le fichier 'controller.py'
app.include_router(router)

# Démarrer le serveur FastAPI avec Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("UVICORN_HOST"), port=int(os.getenv("UVICORN_PORT")))

