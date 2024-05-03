import psycopg2
import csv

# smth = [
#     ['87001002030', 'Selena'],
#     ['87077077077', 'Ruby'],
#     ['87787878778', 'Rob'],
#     ['87477474774', 'Shelly'],
#     ['87011077010', 'Henry']
#     ]

# with open('csvfile.csv', 'w', newline='') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerows(smth)



connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')

cursor = connection.cursor()
query = '''
        CREATE TABLE IF NOT EXISTS PhoneBook(
        id SERIAL PRIMARY KEY NOT NULL,
        number TEXT,
        name TEXT
)
'''

def insert_from_csv(cursor, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            insert_values = """
            INSERT INTO PhoneBook (number, name)
            VALUES (%s, %s)
            """
            cursor.execute(insert_values, (row[0], row[1]))
            connection.commit()

def insert_from_console(cursor):
    name = input('please, write name\n')
    phone = input('please, write phone number\n')
    insert_values = """
    INSERT INTO PhoneBook (number, name)
    VALUES(%s, %s)
    """
    cursor.execute(insert_values, (phone, name))
    connection.commit()
    
    
def update_data(cursor, userid, newvalue):
    whattochange = input("what we will change? (phone or name)\n")
    update_value = ""
    if whattochange == "phone":
        update_value = """
        UPDATE PhoneBook
        SET number = %s 
        WHERE id = %s
        """
    elif whattochange == "name":
        update_value = """
        UPDATE PhoneBook
        SET name = %s 
        WHERE id = %s
        """
    cursor.execute(update_value, (newvalue, userid))
    
    
def querying_data(cursor):
    whattodo = input("which filter should I use? acsending or descending?\n")
    get = ""
    if whattodo == 'acsending':
        get = """
        SELECT * FROM PhoneBook Order By id ASC
        """
    elif whattodo == 'descending':
        get = """
        SELECT * FROM PhoneBook Order By id DESC
        """
    cursor.execute(get)
    for row in cursor.fetchall():
        print(row)        
def deleting(cursor, namee):
    delete = """
    DELETE FROM PhoneBook
    WHERE name = %s
    """
    cursor.execute(delete, (namee, ))
    
drop_table_query = '''
DROP TABLE IF EXISTS PhoneBook;
'''

def delete_sql(inf):
    connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    f_sql = """
    CREATE OR REPLACE PROCEDURE del_data(inf TEXT)
    AS $$
    BEGIN
        DELETE FROM PhoneBook WHERE name = inf or number = inf;
    END;
    $$ LANGUAGE plpgsql
    """
    cursor.execute(f_sql)
    # cursor.callproc("del_data", [inf])
    cursor.execute(f'CALL del_data({inf})')
    connection.commit()

def sel_pattern(pattern):
    connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    f2_sql = """
        CREATE OR REPLACE FUNCTION by_pattern(pat TEXT)
        RETURNS SETOF PhoneBook AS $$
        BEGIN
            RETURN QUERY SELECT * FROM PhoneBook WHERE name LIKE '%' || pat || '%' OR number LIKE '%' || pat || '%';
        END;
        $$ LANGUAGE plpgsql;
        """
    cursor.execute(f2_sql)
    cursor.callproc("by_pattern", [pattern])
    for row in cursor.fetchall():
        print(row)

    connection.commit()
    connection.close()

def q_pag(nl, no):
    connection = psycopg2.connect(host='127.0.0.1', database='suppliers', user='postgres', password='921021', port='5432')
    cursor = connection.cursor()
    f3_sql = """
        CREATE OR REPLACE FUNCTION q_sql(nl INT, no INT)
        RETURNS SETOF PhoneBook AS $$
        BEGIN
            RETURN QUERY SELECT * FROM PhoneBook OFFSET no LIMIT nl;
        END;
        $$ LANGUAGE plpgsql;
        """
    cursor.execute(f3_sql)
    cursor.callproc("q_sql", [nl, no])
    for row in cursor.fetchall(): 
        print(row)

    connection.commit()
    connection.close()


try:
    # cursor.execute(query)
    # connection.commit()
    # insert_from_console(cursor)
    # connection.commit()
    querying_data(cursor)
    connection.commit()
    # update_data(cursor, 1, "Mary")
    # connection.commit()
    # insert_from_csv(cursor, 'csvfile.csv')
    # connection.commit()
    # delete_sql("Rob")
    # q_pag(50, 6)
    # deleting(cursor, 'Shelly')
    # connection.commit()
    # sel_pattern('e')
    # querying_data(cursor)
    # connection.commit()
    # cursor.execute(drop_table_query)
    # connection.commit()
except Exception as error:
    print('ERR:', error)
finally:
    connection.close()