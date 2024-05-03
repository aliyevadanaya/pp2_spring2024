import psycopg2

connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
cursor = connection.cursor()

query_users = """
        CREATE TABLE IF NOT EXISTS users_in_snake (
        id SERIAL PRIMARY KEY,
        name TEXT
)
"""
query_score = """
        CREATE TABLE IF NOT EXISTS score (
        user_id SERIAL PRIMARY KEY,
        score INT,
        lvl INT,
        speed INT,
        FOREIGN KEY (user_id) REFERENCES users_in_snake(id)
)
"""
drop_table_score = '''
DROP TABLE IF EXISTS score;
'''
drop_table_users = '''
DROP TABLE IF EXISTS users_in_snake;
'''

try: 
    cursor.execute(query_users)
    connection.commit()
    print("yes")
    cursor.execute(query_score)
    connection.commit()
    print("yes")
    # cursor.execute(drop_table_users)
    # connection.commit()
    # print("yes")
    # cursor.execute(drop_table_score)
    # connection.commit()
    # print("yes")

except Exception as error:
    print(error)
finally:
    connection.close()
    