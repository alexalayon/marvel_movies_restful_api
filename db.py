import pymysql
import json
from flask import jsonify

db_user = "admin"
db_password = "admin"
db_name = "marveldb"
db_host = "34.105.129.246"

def open_connection():
    try:
        connection = pymysql.connect(host= db_host, user = db_user, password = db_password, db = db_name, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as ex:
        raise
    return connection
    
    
def create_record(new_record, table_name):
    try:
        conn = open_connection()
#        return ("successful connection")
        with conn.cursor() as cursor:
            if table_name == "movies":
                result = cursor.execute("SELECT ID FROM characters_table WHERE NAME = %s;", (new_record.main_character))
                if result > 0:
                   character_id = cursor.fetchall()
                   cursor.execute("INSERT INTO movies_table(name, rating, genre, budget, box_office, main_character, duration, release_date, summary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (new_record.name, new_record.rating, new_record.genre, new_record.budget, new_record.box_office, character_id[0]['ID'], new_record.duration,  new_record.release_date, new_record.summary))
                else:
                    raise Exception("There is no character in the database")
            elif table_name == "characters":
                cursor.execute("INSERT INTO characters_table (name, gender, actor, birth_date, country, affiliation, super_power, first_appearance, last_appearance, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
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
#                query= "DELETE FROM movies_table WHERE name= '%s';", (nametodelete)
                cursor.execute("DELETE FROM movies_table WHERE name = %s;", nametodelete)
            elif table_name == "characters":
#                query= "DELETE FROM characters_table WHERE name='%s';", (nametodelete)
                cursor.execute("DELETE FROM characters_table WHERE name= %s;", nametodelete)
        conn.commit()
        conn.close()
        return "Record deleted successfully"
    except Exception as ex:
        conn.close()
        raise

#Vaidheshwar's code
def get_all_records(table_name):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
             if table_name == "movies_table":
                 result = cursor.execute('SELECT * FROM movies_table;')
             else:
                 result = cursor.execute('SELECT * FROM characters_table;')

             res = cursor.fetchall()
             
             if result > 0:
                 all_records = res
             else:
                 all_records = "No record exists"
             
             conn.close()
             return all_records
    except Exception as ex:
        conn.close()
        raise


#Samidha's code
def get_records(table_name):
    try:
        conn = open_connection()
        with conn.cursor() as cursor:
             if table_name == "movies_table":
                 result = cursor.execute('SELECT name FROM movies_table;')
             else:
                 result = cursor.execute('SELECT name FROM characters_table;')
             
             res = cursor.fetchall()
             
             if result > 0:
                 all_records = json.dumps(res)
             else:
                 all_records = "No record exists"
             
             conn.close()
             return all_records
    except Exception as ex:
        conn.close()
        raise

def update_records(name, req, table_name):
    try:
        conn = open_connection()
        if table_name == 'movies_table':
            with conn.cursor() as cursor:
                n_rating = req.rating
                n_genre = req.genre
                n_budget = req.budget
                n_box_office = req.box_office
                n_main_character = req.main_character
                n_duration = req.duration
                n_release_date = req.release_date
                n_summary = req.summary
                cursor.execute('UPDATE movies_table SET rating = %s, genre = %s, budget = %s, box_office = %s, main_character = %s, duration = %s, release_date = %s, summary = %s where name= %s;', (n_rating, n_genre, n_budget, n_box_office, n_main_character, n_duration, n_release_date, n_summary, name))
                conn.commit()
                conn.close()
                return jsonify({'status':'Movie details updated'}), 200
        else:
            with conn.cursor() as cursor:
                n_gender = req.gender
                n_actor = req.actor
                n_birth_date = req.birth_date
                n_country = req.country
                n_affiliation = req.affiliation
                n_super_power = req.super_power
                n_first_appearance = req.first_appearance
                n_last_appearance = req.last_appearance
                n_description = req.description
                cursor.execute('UPDATE characters_table SET gender = %s, actor = %s, birth_date = %s, country = %s, affiliation = %s, super_power = %s, first_appearance = %s, last_appearance = %s, description = %s WHERE name= %s;', (n_gender, n_actor, n_birth_date, n_country, n_affiliation, n_super_power, n_first_appearance, n_last_appearance, n_description, name))
                conn.commit()
                conn.close()
                return jsonify({'status':'Character details updated'}), 200
    except Exception as ex:
        conn.close()
        raise
