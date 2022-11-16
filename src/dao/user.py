import sqlite3

from models.user import User


class UserDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[0], nome=resultado[1], preco=resultado[2]))
        self.cursor.close()
        return resultados
    
    def insert_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users (name, password)
            VALUES(?,?,?);
        """, (user.name, user.password))
        self.conn.commit()
        self.cursor.close()
        
    def delete_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                            DELETE FROM Users WHERE name = ?; """
        ,(user.get_user_name(),))
        self.conn.commit()
        self.cursor.close()
    
    def get_user(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                            SELECT * FROM Users WHERE name = ?;
                            """,(name,))
        result = self.cursor.fetchone()
        self.cursor.close()
        return User(name = result[0], password = result[1])