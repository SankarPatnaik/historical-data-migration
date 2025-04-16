import pandas as pd
import cx_Oracle

def read(config):
    dsn = cx_Oracle.makedsn(config['host'], config['port'], sid=config['database'])
    conn = cx_Oracle.connect(config['user'], config['password'], dsn)
    df = pd.read_sql(config['query'], conn)
    conn.close()
    return df
