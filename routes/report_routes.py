from fastapi import APIRouter,HTTPException
from database.mission_db import MissionDB
from database.agent_db import AgentDB
import logging

logger = logging.getLogger(__name__)

report_router = APIRouter()
agent = AgentDB()
miss = MissionDB()

@report_router.get("/summary")
def get_summary():
    try:    
        logger.info("Request sent to database")
        active_agents_count = agent.count_active_agents()
        total_missions = miss.count_all_missions()
        open_missions = miss.count_open_missions()
        completed_missions = miss.count_by_status("COMPLETED")
        failed_missions = miss.count_by_status("FAILED")
        critical_mission = miss.count_critical_missions()
        logger.info("Request found Sent from get_summary")
        return {
            "active_agents_count":{active_agents_count},
            "total_missions":{total_missions},
            "open_missions":{open_missions},
            "completed_missions":{completed_missions},
            "failed_missions":{failed_missions},
            "critical_mission":{critical_mission}
        }
    except Exception as e:
        logger.error(f"Request failed due to{e}")
        raise HTTPException(400, f"Request failed due to {e}")
    
@report_router.get("/missions-by-status")
def get_missions_by_status():
    try:    
        logger.info("Request sent to database")
        new =  miss.count_by_status("new")
        assigned = miss.count_by_status("ASSIGNED")
        in_progress = miss.count_by_status("IN_PROGRESS")
        completed = miss.count_by_status("COMPLETED")
        faild = miss.count_by_status("FAILED")
        cancelled = miss.count_by_status("CANCELLED")
        return {
            "NEW" : new,
            "ASSIGNED" : assigned,
            "IN_PROGRESS" : in_progress,
            "COMPLETED": completed,
            "FAILED": faild,
            "cancelled":cancelled
        }
    except Exception as e:
        logger.error(f"Request failed due to{e}")
        raise HTTPException(400, f"Request failed due to {e}")    


@report_router.get("/top-agent")
def get_top_agent():
     logger.info("Request sent to database")
     top = miss.get_top_agent()
     logger.info("Request found Sent from get_top_agent")
     return f"top_agent {top}"
