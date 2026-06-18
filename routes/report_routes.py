from fastapi import APIRouter,HTTPException
from database.mission_db import MissionDB
from database.agent_db import AgentDB
import logging

logger = logging.getLogger(__name__)

report_router = APIRouter()
agent = AgentDB()
mission = MissionDB()

@report_router.get("/summary")
def get_summary():
    try:    
        logger.info("Request sent to database")
        active_agents_count = agent.count_active_agents()
        print(1)
        total_missions = mission.count_all_missions()
        print(1)
        open_missions = mission.count_open_missions()
        print(2)
        completed_missions = mission.count_by_status("COMPLETED")
        print(3)
        failed_missions = mission.count_by_status("FAILED")
        print(4)
        critical_mission = mission.count_critical_missions()
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
        new =  mission.count_by_status("new")
        assigned = mission.count_by_status("ASSIGNED")
        in_progress = mission.count_by_status("IN_PROGRESS")
        completed = mission.count_by_status("COMPLETED")
        faild = mission.count_by_status("FAILED")
        cancelled = mission.count_by_status("CANCELLED")
        return {
            "NEW" : new,
            "ASSIGNED" : assigned,
            "IN_PROGRESS" :  
        }

    except Exception as e:
        logger.error(f"Request failed due to{e}")
        raise HTTPException(400, f"Request failed due to {e}")    


@report_router.get("/top-agent")
def get_top_agent():
     logger.info("Request sent to database")
     top = mission.get_top_agent()
     logger.info("Request found Sent from get_top_agent")
     return f"top_agent {top}"
