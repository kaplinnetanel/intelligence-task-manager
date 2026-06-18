from database.agent_db import  AgentDB
from fastapi import APIRouter,HTTPException
import logging

logger = logging.getLogger(__name__)


routes_agent = APIRouter() 

agenr = AgentDB()

@routes_agent.post("")
def creat_new_agent(data:dict):
    if data["agent_rank"] not in ("Junior, Senior,Commander"):
        logger.error("the agent_rank not in Junior, Senior,Commander")
        raise HTTPException(400,"the agent_rank not in Junior, Senior,Commander")
    return agenr.create_agent(data)


@routes_agent.get("")
def get_all_agent():
    logger.info("A request has been sent to the database.")
    all = agenr.get_all_agents()
    logger.info("Found Request sent from get_all_agents")
    return all

@routes_agent.get("/{id}")
def get_agent_id(id: int):
     logger.info("A request has been sent to the database.")
     agent_id = agenr.get_agent_by_id(id)
     if not agent_id :
         logger.error("Requested soldier not found")
         raise HTTPException(400,"Requested soldier not found")
     return agent_id

@routes_agent.put("/{id}")
def update_agent_by_id(id: int,data:dict):
    agent_id = agenr.get_agent_by_id(id)
    if not agent_id :
         logger.error("A request has been sent to the database")
         raise HTTPException(404,"Requested soldier not found")
    logger.info("RRequest found sent from update_agent")
    return agenr.update_agent(id,data) 

@routes_agent.put("/{id}/deactivate")
def deactivate(id:int):
    logger.info("A request has been sent to the database")
    agenr.deactivate_agent(id)
    logger.info("Request found sent from deactivate_agent")


@routes_agent.get("/{id}/performance")
def agent_performance_by_id(id: int):
    agent_id = agenr.get_agent_by_id(id)
    if not agent_id:
         logger.error("A request has been sent to the database")
         raise HTTPException(404,"Requested soldier not found")
    logger.info("Request found sent from get agent performance")
    return agenr.get_agent_performance(id)