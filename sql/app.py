import sqlite3 as lite
import os;


# con = lite.connect("test.db")

# print(lite.version)
# with lite.connect("test.db") as con:
#     with open("rest.sql") as f:
#         schema = f.read()
#     con.executescript(schema)
#     print("Schema created")


# con.close()


with lite.connect("test.db") as con:
    # con.executescript("""
    # INSERT INTO people (name, address, datetime) VALUES ('Tom Cat', '1 Cats str., Catcity', '2021-11-09');
    # INSERT INTO people (name, address, datetime) VALUES ('Angry Dog', '1 Dogs str., Dogcity', '2021-11-09');
    # """)
    # print("Row created")
    
    cursor = con.cursor()
    # cursor.execute("SELECT * FROM people")
    
    # for row in cursor.fetchall():
    #     name, address, datetime = row
    #     print(name, address, datetime)


    cursor.execute("SELECT * FROM people WHERE name='Tom Cat'")
    
    for row in cursor.fetchall():
        name, address, datetime = row
        print(name, address, datetime)
