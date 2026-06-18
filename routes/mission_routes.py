from fastapi import APIRouter,HTTPException
from database.mission_db import MissionDB
from database.agent_db import AgentDB
import logging


logger = logging.getLogger(__name__)

mission_routes = APIRouter()
agent = AgentDB()
mission  = MissionDB()

@mission_routes.post("")
def creat_mission(data:dict):
    if 0< data["difficulty"] <= 10:
        logger.error("Mission must be within range of  0< difficulty <= 10")
        raise HTTPException(400,"Mission must be within range of")
    if 0< data["importance"] <= 10:
           logger.error("Mission must be within range of  0< importance <= 10")
           raise HTTPException(400,"Mission must be within range of")
    logger.info("Request sent to database")
    mission_bool = mission.create_mission(data)
    if mission_bool:
        logger.info("Request found, sent from create_mission")
        return "Mission completed, new mission created"
    logger.error("An error occurred while creating a new mission")
    return "An error occurred while creating a new mission"

@mission_routes.get("")
def get_all_misiion():
    try:
        logger.info("Request sent to database")
        logger.info("Request found, sent from get_all_missions")
        return mission.get_all_missions()
    except Exception as e:
        logger.error(f"An error occurred {e}")
        return f"An error occurred :{e}"


@mission_routes.get("/{id}")
def get_mission_id(id:int):
    try:
        logger.info("Request sent to database")
        logger.info(f"Request found, sent from get missions by {id}")
        return mission.get_mission_by_id(id)
    except Exception as e:
        logger.error(f"An error occurred {e}")
        return f"An error occurred :{e}"

# @mission_routes.put("/{id}/assign/{agent_id}")
# def assign_by_id(id:int,agent_id:int):
#     mision = mission.get_mission_by_id(id)
#     if mision is None:
#         logger.error("Mission exists")
#         raise HTTPException(404,"Mission not found") 
#     agent_variable = agent.get_agent_by_id(agent_id)
#     if agent_variable is None:
#         logger.error("Agent not found")
#         raise HTTPException (404,"Agent not found")
#     mission_variable = dict(mision)
#     if  mission_variable["status"] != "NEW":
#         logger.error("Mission not available")
#         raise HTTPException(400,"Mission not available")
#     if agent_variable["is_active"] == "false":
#         logger.error("Agent is not active")
#         raise HTTPException(400,"Agent is not active")
#     o

# @mission_routes.put("/{id}/start")
# def start_misiion(id: int):



