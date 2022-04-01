import pymysql
from flask import jsonify

db_user = "marvelproject_admin"
db_password = "admin"
db_name = "marveldb"
db_host = "34.89.114.158"

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
