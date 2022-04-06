import pymysql
from flask import jsonify

db_user = "admin"
db_password = "admin"
db_name = "marveldb"
db_host = "34.105.129.246"

def open_connection():
    try:
        connection = pymysql.connect(host= db_host, user = db_user, password = db_password, db = db_name)
    except pymysql.MySQLError as ex:
        raise
    return connection
    
    
def create_record(new_record, table_name):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            if table_name == "movies":
                result = cursor.execute("SELECT CHARACTER_ID FROM character_table WHERE NAME = %s;", (new_record.main_character))
                if result > 0:
                   character_id = cursor.fetchall()

                   cursor.execute("INSERT INTO movies_table(NAME, RELEASE_DATE, RATING, BUDGET, DURATION, GENRE, BOX_OFFICE, MAIN_CHARACTER, SUMMARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (new_record.name, new_record.release_date, new_record.rating, new_record.budget, new_record.duration, new_record.genre, new_record.box_office, character_id, new_record.summary))
                else:
                    raise Exception("There is no character in the database")
            elif table_name == "characters":
                cursor.execute("INSERT INTO character_table(NAME, GENDER, ACTOR, BIRTH_DATE, COUNTRY, AFFILIATION, SUPER_POWER, FIRST_APPEAREANCE, LAST_APPEAREANCE, DESCRIPTION) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", 
                (new_record.name, new_record.gender, new_record.actor, new_record.birth_date, new_record.country, new_record.affiliation, new_record.super_power, new_record.first_appearance, new_record.last_appearance, new_record.description))

        conn.commit()
        conn.close()
        return "Record created successfully"
    except Exception as ex:
        conn.close()
        raise

def delete_record(nametodelete, table_name):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            if table_name == "movies":
                query="""DELETE FROM movies_table WHERE name=('%s')"""%(nametodelete)
                print('-------',query)
                cursor.execute(query)
            else:
                query="""DELETE FROM character_table WHERE name=('%s')"""%(nametodelete)
                print('-------',query)
                cursor.execute(query)
        conn.commit()
        conn.close()
        return "Record deleted successfully"
    except Exception as ex:
        conn.close()
        raise

def get_records(table_name):
    try:
        conn = open_connection
        with conn.cursor() as cursor:
            if table_name == "movies_table":
                result = cursor.execute('SELECT * FROM movies_table;')
            else:
                result = cursor.execute('SELECT * FROM characters_table;')
            res = cursor.fetchall()
            if result > 0:
                all_records = jsonify(res)
            else:
                all_records = 'No records exist in the DB'
            conn.close()
            return all_records
        except Exception as ex:
            conn.close()
            raise

def update_records(u_name, upd_data, table_name):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
            if table_name == "movies_table":
                for column in upd_data.keys:
                    cursor.execute('UPDATE movies_table SET column = upd_data[column] WHERE name = u_name;')
            else:
                for column in upd_data.keys:
                    cursor.execute('UPDATE characters_table SET column = upd_data[column] WHERE name = u_name;')
            conn.commit()
            conn.close()

    except Exception as ex:
        conn.close()
        raise
