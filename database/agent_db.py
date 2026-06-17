from db_connection import DB_connection


class AgentDB:
    def __init__(self):
        self.db_maneger = DB_connection()

    def create_agent(self,data):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql ="""INSERT INTO table_name (name,specialty, is_active, completed_mission,
        failed_missions,agent_rank)
        VALUES (%s,%s,%s,%s,%s,%s);"""
        cursor.execute(sql,(data["name"],data["specialty"],data["is_active"],data["completed_mission"],data["failed_missions"],data["agent_rank"]))
        conn.commit()
        cursor.close()
        conn.close()
        return data

    def get_all_agents(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor(dictionary= True)
        cursor.execute("SELECT * FROM agents;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    def get_agent_by_id(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM agents WHERE id = %s;"
        cursor.execute(sql,(id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def update_agent(self,id, data):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql ="""UPDATE agents SET  name = %s,  specialty = %s, is_active = %s, completed_mission = %s,
        failed_missions	= %s ,agent_rank =%s WHERE id = %s;"""
        cursor.execute(sql,(data["name"],data["specialty"],data["is_active"],data["completed_mission"],data["failed_missions"],data["agent_rank"],id))
        conn.commit()
        cursor.close()
        conn.close()
        return "COMPLETED"

    def agent_rank(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE agents SET  is_active = %s WHERE id = %s;"
        cursor.execute(sql,("False",id))
        conn.commit()
        cursor.close()
        conn.close()
        return "COMPLETED"
    

    def increment_completed(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT completed_missions FROM agents WHERE id = %s;"
        cursor.execute(sql,(id,))
        completed = cursor.fetchone()
        num_completed=  completed[0]
        cursor.close()
        conn.close()
        return f"number of completed : {num_completed}"
    

    def increment_failed(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT failed_missions FROM agents WHERE id = %s;"
        cursor.execute(sql,(id,))
        failed = cursor.fetchone()
        num_failed=  failed[0]
        cursor.close()
        conn.close()
        return f"number of failed : {num_failed}"
    
    def get_agent_performance(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor(dictionary= True)
        sql = "SELECT * FROM agents WHERE id = %s;"
        cursor.execute(sql,(id,))
        row = cursor.fetchall()
        total = int(row["completed_mission"]) + int(row["completed_mission"])
        completed =row["completed_mission"]
        failed = row["failed_missions"]
        success_rate = (100 * completed )/total
        cursor.close()
        conn.close()
        return f"total : {total} , failed : {failed} , completed : {completed} ,  success_rate : {success_rate}"
    
    def count_active_agents(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM agents WHERE is_active = true;")
        count = cursor.fetchone()
        count_active = count[0]
        cursor.close()
        conn.close()
        return count_active


    
