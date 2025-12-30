def get_tables(conn, schema):
    query = f"""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = '{schema}'
    """
    return conn.execute(query).fetchall()

def get_columns(conn, schema, table):
    query = f"""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = '{schema}'
      AND table_name = '{table}'
    """
    return conn.execute(query).fetchall()
