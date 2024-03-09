from fastapi import FastAPI, Request, HTTPException
import uvicorn


app = FastAPI()


@app.get("/")


def read_main(token: str = None):


   if token != "carlos_soria":


      raise HTTPException(status_code=401, detail="Unauthorized")


   return {"message": "Hello, I am Carlos Soria"}
