"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd
import pathlib
import sqlite3


def create_dataframe():
    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    db_con = None
    table_names = []
    db_path = pathlib.Path('app2.db').resolve() # or 'absolute_path/to/the/file'
    print('path:', db_path)
    if db_path.exists():
        db_con = sqlite3.connect(db_path)
    else:
        assert(False), 'failed to find database'
        
    if db_con:    
        cursor = db_con.cursor()    
        cursor.execute(sql_query)
        table_names = cursor.fetchall()
        print('table name:', *table_names[0])   
    else:
        print('db connection failed')    
    
    df = pd.read_sql_query("""SELECT * from 'flasklogin-users'""", db_con)
    return df