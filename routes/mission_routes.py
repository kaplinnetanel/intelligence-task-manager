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

@mission_routes.put("/{id}/assign/{agent_id}")
def assign_by_id(id:int,agent_id:int):
    mision = mission.get_mission_by_id(id)
    if not mision:
        logger.error("Mission exists")
        raise HTTPException(404,"Mission not found") 
    agent_variable = agent.get_agent_by_id(agent_id)
    if not agent_variable:
        logger.error("Agent not found")
        raise HTTPException (404,"Agent not found")
    if  mision["status"] != "NEW":
        logger.error("Mission not available")
        raise HTTPException(400,"Mission not available")
    if agent_variable["is_active"] == "false":
        logger.error("Agent is not active")
        raise HTTPException(400,"Agent is not active")
    num_mission = mission.get_open_missions_by_agent(agent_id)
    if len(num_mission) > 3:
        logger.error("Agent has reached maximum missions")
        raise HTTPException (400,"gent has reached maximum missions")
    g = agent.get_agent_by_id(agent_id)
    if g["agent_id"] == "CRITICAL":
        logger.error("Only Commander can handle critical mission ")
        raise HTTPException (400 ,"Only Commander can handle critical")
    bool =mission.assign_mission(id,agent_id)
    if bool:
        mission.update_mission_status(id,"ASSIGNED")
        logger.info("Mission completed assign_by_id")
    logger.error("Request failed due")
    raise HTTPException(404,"Request failed due to")   


@mission_routes.put("/{id}/start")
def start_misiion(id: int):
    miss = mission.get_mission_by_id(id)
    if not miss:
        if miss["status"] == "ASSIGNED":
            logger.info("Request sent to database")
            logger.info("Request found, sent from get")
            mission.update_mission_status(id,"NEW")
        logger.error("Request failed due to start_misiion") 
        raise HTTPException(404,"Request failed due to")  
    raise HTTPException(40,"not faond")  
     
   
@mission_routes.put("/{id}/complet")
def complet_mission(id:int):
    miss = mission.get_mission_by_id(id)
    if miss["status"] == " IN_PROGRESS":
        logger.info("Request sent to database")
        logger.info("Request found, sent from get")
        mission.update_mission_status(id,"completed")
    logger.error("Request failed due to complet_mission") 
    raise HTTPException(404,"Request failed due to complet_mission")   
     
@mission_routes.put("/{id}/fail")
def fail_mission(id:int):
    miss = mission.get_mission_by_id(id)
    if miss["status"] == "IN_PROGRESS":
        logger.info("Request sent to database")
        logger.info("Request found, sent from get")
        mission.update_mission_status(id,"FAILED")
    logger.error("Request failed due to fail_mission") 
    raise HTTPException(404,"Request failed due to fail_mission")  


@mission_routes.put("/{id}/cancel")
def cancel_mission(id:int):
    miss = mission.get_mission_by_id(id)
    if miss["status"] == " NEW" or miss["status"] == "ASSIGNED ":
        logger.info("Request sent to database")
        logger.info("Request found, sent from get")
        mission.update_mission_status(id,"CANCELLED")
    logger.error("Request failed due becouse status != NEW or status != ASSIGNED ") 
    raise HTTPException(404,"Request failed due to complet_mission")  

