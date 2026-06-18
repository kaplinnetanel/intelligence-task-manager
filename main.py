from routes.agent_routes import routes_agent
from fastapi import FastAPI
import uvicorn
import logging

app = FastAPI()

logger = logging.basicConfig(filename='app.log', level=logging.DEBUG,format="%(levelname)s:%(message)s:%(asctime)s")

logger = logging.getLogger(__name__)

app.include_router(routes_agent,prefix="/agents",tags=["agents"])



if __name__ == "__maim__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)