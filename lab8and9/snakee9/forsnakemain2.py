import psycopg2

def add_user(name):
    connection = psycopg2.connect(host = '127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    check = """
    SELECT * FROM users_in_snake
    WHERE name = %s
    """
    cursor.execute(check, (name, ))
    wehave = cursor.fetchone()
    if not wehave:
        insert_name = """
        INSERT INTO users_in_snake (name)
        VALUES (%s)
        """
        cursor.execute(insert_name, (name, ))
        connection.commit()
        connection.close()
    else:
        pass
    
def get_score(name):
    connection = psycopg2.connect(host = '127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    query = """
    SELECT s.lvl, s.score, s.speed
    FROM users_in_snake u
    INNER JOIN score s ON u.id = s.user_id
    WHERE u.name = %s
    """
    cursor.execute(query, (name, ))
    connection.commit()
    print(cursor.fetchall())
    connection.close()

def addinfo(name, level, speed, score):
    connection = psycopg2.connect(host = '127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    
    getid = """
    SELECT id FROM users_in_snake WHERE name = %s
    """
    cursor.execute(getid, (name, ))
    user_idd = cursor.fetchone() 
    
    add = """
    INSERT INTO score (user_id, score, lvl, speed)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET score = EXCLUDED.score, lvl = EXCLUDED.lvl, speed = EXCLUDED.speed
      
    """
    cursor.execute(add, (user_idd[0], score, level, speed))
    connection.commit()
    connection.close()

def show(name):
    connection = psycopg2.connect(host = '127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    takeidd = """
    SELECT id FROM users_in_snake
    WHERE name = %s 
    """
    cursor.execute(takeidd, (name, ))
    getidd = cursor.fetchone()
    if getidd:
        take = """
        SELECT * FROM score
        WHERE user_id = %s
        """
        cursor.execute(take, (getidd[0], ))
        info = cursor.fetchone()
        user_id, score, lvl, speed = info 
        #print(f"id = {user_id}, score = {score}, level = {lvl}, speed = {speed}")
        return f"id = {user_id}, score = {score}, level = {lvl}, speed = {speed}"
    else:
        pass
    
# https://teams.microsoft.com/l/message/19:meeting_MjkzMDg2NGYtMjExNy00NDZmLTliOGItMjBlZmNmNDYyNjVm@thread.v2/1714484111957?context=%7B%22contextType%22%3A%22chat%22%7D
# https://www.tutorialspoint.com/postgresql/postgresql_functions.htm