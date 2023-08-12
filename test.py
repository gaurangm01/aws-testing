import os

import psycopg2

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor_obj = conn.cursor()

# Create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
'''
cursor_obj.execute(create_table_query)

# Add data to the table
insert_data_query = '''
INSERT INTO my_table (name, age)
VALUES (?, ?)
'''
data_to_insert = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]
cursor_obj.executemany(insert_data_query, data_to_insert)

# Commit the changes
conn.commit()

# Retrieve and print data using SELECT query
select_query = "SELECT * FROM my_table"
cursor_obj.execute(select_query)
rows = cursor_obj.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
