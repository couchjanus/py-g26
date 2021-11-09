import sqlite3 as lite

class Task:
    def __init__(self, detail, deadline, status = 1, project='project1') -> None:
        self.detail = detail
        self.status = status
        self.project = project
        self.priority = 1
        self.deadline = deadline
        self.completed_at = ''
        
        
class TodoList:
    def __init__(self) -> None:
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM task WHERE project = 'project1' ORDER BY deadline")
            self.tasks = cursor.fetchall()
    
    def all(self):
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM task WHERE project = 'project1' ORDER BY deadline")
            self.tasks = cursor.fetchall()
            
    def create(self, detail, deadline):
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            sql = "INSERT INTO task (detail, deadline, project) VALUES (?, ?, ?)"
            
            cursor.execute(sql, (detail, deadline, 'myproject'))
            con.commit()
    
    def update(self, id, status):
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            sql = "UPDATE task SET status = :status WHERE id = :id"
            
            cursor.execute(sql, {'status': status, 'id': id})
            con.commit()
        
    def delete(self, id):
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            sql = "DELETE FROM task WHERE id = :id"
            
            cursor.execute(sql, {'id': id})
            con.commit()
            
    def search(self, q):
        with lite.connect("todo.db") as con:
            cursor = con.cursor()
            sql = "SELECT * FROM task WHERE detail LIKE ?"
            
            cursor.execute(sql, (f'%{q}%',))
            return cursor.fetchall()
           