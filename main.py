from database.db_connection import DB_connection
from routes.agent_routes import routes_agent
from routes.mission_routes import mission_routes
from routes.report_routes import report_router
from fastapi import FastAPI
import uvicorn
import logging

con = DB_connection()
app = FastAPI()
con.create_tables()

logger = logging.basicConfig(filename='app.log', level=logging.DEBUG,format="%(levelname)s:%(message)s:%(asctime)s")

logger = logging.getLogger(__name__)

app.include_router(routes_agent,prefix="/agents",tags=["agents"])

app.include_router(mission_routes,prefix="/missions",tags=["mission"])

app.include_router(report_router,prefix="/reports",tags=["report"])


if __name__ == "__maim__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)