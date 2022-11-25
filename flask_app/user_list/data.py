"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd
import pathlib
import sqlite3

def create_dataframe():
    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    db_con = None
    table_names = []
    # db_path = pathlib.Path('../../app2.db').resolve() # or 'absolute_path/to/the/file'
    db_path = pathlib.Path('./app2.db').resolve() # or 'absolute_path/to/the/file'
    print('path to db:', db_path)
    if db_path.exists():
        db_con = sqlite3.connect(db_path)
    else:
        assert(False), 'failed to find database'
        
    if db_con:    
        cursor = db_con.cursor()    
        cursor.execute(sql_query)
        table_names = cursor.fetchall()
        table_name = table_names[0][0]
        # print('table name:', table_name, 'type:', type(table_name))   
    else:
        print('db connection failed')    
    
    sql_query = f"""SELECT id, name, email, created_on, last_login, credential from '{table_name}'"""
    #sql_query = f"""SELECT id, name, email, created_on, last_login, credential from 'flasklogin-users'"""
    # print('query is:', sql_query)
    try:
        df = pd.read_sql_query(sql_query, db_con)
        print('df shape:', df.shape)
        assert not df.empty, 'failed to get data'
        return df
    except Exception as e:
        print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")


# if __name__ == '__main__':
#     create_dataframe()