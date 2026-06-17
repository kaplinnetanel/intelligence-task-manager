import mysql.connector

class DB_connection:

    def get_connection(self):
        return mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "1234",
            database = "Intelligence_db"
        )
    def create_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db;")
        conn.commit()
        cursor.close()
        conn.close()   

    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        agents = """CREATE TABLE IF NOT EXISTS agents(
            id	int PRIMARY KEY AUTO_INCREMENT,
            name varchar(255) NOT NULL,	
            specialty varchar(255) NOT NULL,	
            is_active varchar(255) DEFAULT 'true',
            completed_missions	int	DEFAULT 0,
            failed_missions	int	DEFAULT 0,
            agent_rank ENUM('Junior','Senior','Commande') NOT NULL);"""      
        missions = """CREATE TABLE IF NOT EXISTS missions(
            id	int PRIMARY KEY AUTO_INCREMENT,
            title varchar(255),	
            description TEXT NOT NULL,	
            location varchar(255),
            difficulty	int,	
            importance	int,
            status varchar(255) DEFAULT 'NEW',
            risk_level varchar(255),
            assigned_agent_id int );""" 
        cursor.execute(agents)
        cursor.execute(missions)
        conn.commit()
        cursor.close()
        conn.close()


