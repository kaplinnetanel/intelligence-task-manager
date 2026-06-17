from db_connection import DB_connection


class MissionDB:
    def __init__(self):
        self.db_maneger = DB_connection()

    def create_mission(self,data):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql ="""INSERT INTO table_name (title, description, location, difficulty, importance, risk_level)
        VALUES (%s,%s,%s,%s,%s,%s);"""
        risk_level = (data["difficulty"] * 2) + data["importance"] 
        cursor.execute(sql,(data["status"],data["description"],data["location"],data["importance"],risk_level))
        conn.commit()
        cursor.close()
        conn.close()


    def get_all_missions(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor(dictionary= True)
        cursor.execute("SELECT * FROM missions;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    
    def get_mission_by_id(self,id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM missions WHERE id = %s;"
        cursor.execute(sql,(id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def assign_mission(self,m_id, a_id):
        try:
            conn = self.db_maneger.get_connection()
            cursor = conn.cursor()
            sql = "UPDATE missions SET assigned_agent_id = %s WHERE id = %s;"
            cursor.execute(sql,(a_id,m_id))
            return "ASSIGENED"
        except Exception as e:
            print(f"Your problem :{e}") 
            return "FAILED"
        finally:       
            conn.commit()
            cursor.close()
            cursor.close()

    def update_mission_status(self, id, status):        
        try:
            conn = self.db_maneger.get_connection()
            cursor = conn.cursor()
            sql = "UPDATE missions SET status = %s WHERE id = %s;"
            cursor.execute(sql,(status,id))
            return "COMPLETED"
        except Exception as e:
            print(f"Your problem :{e}") 
            return "FAILED"
        finally:       
            conn.commit()
            cursor.close()
            cursor.close()

    def get_open_missions_by_agent(self, id):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM missions WHERE id = %s AND status = ASSIGNED  OR  status = IN_PROGRESS;"
        cursor.execute(sql,(id,))
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row

    def count_all_missions(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM missions ;")
        count = cursor.fetchone()
        count_missions = count[0]
        cursor.close()
        conn.close()
        return count_missions 
    
    def count_by_status(self,status):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        sql = "SELECT COUNT(*) FROM missions WHERE status = %s ;"
        cursor.execute(sql,(status,))
        count = cursor.fetchone()
        count_missions = count[0]
        cursor.close()
        conn.close()
        return count_missions
    
    def count_open_missions(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM missions WHERE status = ASSIGNED OR status = IN_PROGRESS;")
        count = cursor.fetchone()
        count_missions = count[0]
        cursor.close()
        conn.close()
        return count_missions


    def count_critical_missions(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM missions WHERE risk_level BETWEEN 25 AND 100000;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
        

    def get_top_agent(self):
        conn = self.db_maneger.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Price) completed_missions FROM agents;")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
        