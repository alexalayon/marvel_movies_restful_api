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
	records_1 = get_all_records("movies_table")
	records_2 = get_all_records("characters_table")
	records = jsonify(records_1 + records_2)
	return records

@app.route('/marvel/<data>/', methods=['GET'])
def get_spe_data(data):
	records = get_all_records("movies_table")
	spe =  {data :'Table Not Found!'}
	if 'movies' == data:
		records = get_all_records("movies_table")
		spe = records
	#	break
	if 'characters' == data:
		records = get_all_records("characters_table")
		spe = records
	#	break
	return jsonify(spe)

@app.route('/marvel/<data>/<data_2>/', methods=['GET'])
def get_spe_data_data_2(data, data_2):
	spe =  {data_2 :'Table Not Found!'}
	records_1 = get_all_records("movies_table")
	records_2 = get_all_records("characters_table")

	if 'movies' == data:
		records = records_1
		spe = []
		for items in records:
			spe.append(items['name'])
			spe.append(items[data_2])
#			break
	elif 'characters' == data:
		records = records_2
		spe = []
		for items in records:
			spe.append(items['name'])
			spe.append(items[data_2])
#			break

	return jsonify(spe)



@app.route('/marvel/find/movies/<data>/', methods=['GET'])
def get_spe_data_data_2_find(data):
	records = get_all_records("movies_table")
	spe = []
	flag = 0
	for items in records:
		if data == items['name']:
			spe.append(items)
			flag = 1

	if flag == 0:
		spe = {data : "Not Found!"}
	return jsonify(spe)




@app.route('/marvel/movies/<data_2>/<streaming_parameter>/', methods=['GET'])
def get_spe_data2_streaming(data_2, streaming_parameter):
    try:
        records = get_all_records("movies_table")
        spe = []
        for items in records:
            if data_2 == items['name']:
                spe.append(items)

        if streaming_parameter == 'streaming':
            streaming = get_external_streaming(data_2)
            return jsonify(spe + streaming), 201
        else:
            return jsonify(spe), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 400


#@app.route('/MARVEL/external_api/<movie_name>', methods=['GET'])
#def get_external(movie_name):
#	var = get_external_streaming(movie_name)
#	return jsonify(var)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')

