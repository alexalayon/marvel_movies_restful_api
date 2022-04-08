from flask import Flask, jsonify, json, request
import json
from db import get_records, get_all_records, update_records, create_record, delete_record
from external_api import get_external_streaming
from classes.characters import Character
from classes.movies import Movie

app = Flask(__name__)

@app.route("/movies/", methods=['POST'])
def create_movie():
    try:
        if not request.json:
            return jsonify({'error': 'the request is not in json format'}), 400

        new_movie = Movie(request.json)
        result = create_record(new_movie, "movies")
    except Exception as ex:
        return jsonify({'error': 'there is an error with :' + str(ex)}), 400

    return jsonify({'message': result}), 201

@app.route("/characters/", methods=['POST'])
def create_character():
    try:
        if not request.json:
            return jsonify({'error': 'the request is not in json format'}), 400

        new_character = Character(request.json)
        result = create_record(new_character, "characters")
    except Exception as ex:
        return jsonify({'error': 'there is an error with: ' + str(ex)}), 400

    return jsonify({'message':result}), 201


@app.route("/movies/<movie_name>", methods=['DELETE'])
def delete_movie(movie_name):
    try:
        
            

#        movietodelete = request.args.get('movietodelete')
        result = delete_record(movie_name, "movies")
        
        
    except Exception as ex:
        return jsonify({'error': 'there is an error with :' + str(ex)}), 400

    return jsonify({'message': result}), 201
    
@app.route("/characters/<character_name>", methods=['DELETE'])
def delete_character(character_name):
    try:
        
            
#        charactertodelete = request.args.get('charactertodelete')
        result = delete_record(character_name, "characters")
        
        
    except Exception as ex:
        return jsonify({'error': 'there is an error with :' + str(ex)}), 400

    return jsonify({'message': result}), 201
    
#Samidha's code    
@app.route("/movies/<name>", methods=['PUT'])
def update_movies(name):
	try:
		if not request.json:
			return jsonify({'error':'The request is not in json format'}), 400

		req = Movie(request.json)
		all_records = get_records("movies_table")
		res_json = json.loads(all_records)
		for i in range(len(res_json)):
			if name == res_json[i].get('name'):
				res = update_records(name, req, "movies_table")
				return res
	except Exception as ex:
		return({'error':'There is an error with ' + str(ex)}), 400

@app.route("/characters/<name>", methods=['PUT'])
def update_characters(name):
	try:
		if not request.json:
			return jsonify({'error':'The request is not in json format'}), 400

		req = Character(request.json)
		all_records = get_records("characters_table")
		res_json = json.loads(all_records)
		for i in range(len(res_json)):
			if name == res_json[i].get('name'):
				res = update_records(name, req, "characters_table")
				return res
	except Exception as ex:
		return jsonify({'error':'There is an error with ' + str(ex)}), 400
    
    
#Vaideshwar's code
@app.route('/marvel/', methods = ['GET'])
def get_all():
#	return (resp.json())
	records_1 = get_all_records("movies_table")
	records_2 = get_all_records("characters_table")
	return jsonify(records_1 + records_2)

@app.route('/marvel/<data>/', methods=['GET'])
def get_spe_data(data):
	records = get_all_records("movies_table")
	spe =  {data :'Not Found!'}
	for item in records:
		if 'movies' == data:
			spe = [items['Movies'] for items in records]
			break
		if 'characters' == data:
			spe = [items['Character'] for items in records]
			break
	return jsonify(spe)

@app.route('/marvel/<data>/<data_2>/', methods=['GET'])
def get_spe_data_data_2(data, data_2):
	spe =  {data_2 :'Not Found!'}
	for item in records:
		if 'movies' == data:
			if 'name' == data_2:
				spe = [items['name'] for items in item['Movies']]
				break
			elif 'summary' == data_2:
				spe = [items['summary'] for items in item['Movies']]
				break
		if 'characters' == data:
			if 'name' == data_2:
				spe = [items['name'] for items in item['Character']]
				break
			elif 'description' == data_2:
				spe = [items['description'] for items in item['Character']]
				break
	return jsonify(spe)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

