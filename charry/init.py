import os
import sqlite3

with sqlite3.connect('product.db') as con:
    with open('schema.sql') as f:
        schema = f.read()
    con.executescript(schema)