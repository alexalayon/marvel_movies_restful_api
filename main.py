from flask import Flask, jsonify, json, request
from db import create_record, delete_record
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


@app.route("/movies/", methods=['DELETE'])
def delete_movie():
    try:
        
            

        movietodelete = request.args.get('movietodelete')
        result = delete_record(movietodelete, "movies")
        
        
    except Exception as ex:
        return jsonify({'error': 'there is an error with :' + str(ex)}), 400

    return jsonify({'message': result}), 201
    
@app.route("/characters/", methods=['DELETE'])
def delete_character():
    try:
        
            

        charactertodelete = request.args.get('charactertodelete')
        result = delete_record(charactertodelete, "characters")
        
        
    except Exception as ex:
        return jsonify({'error': 'there is an error with :' + str(ex)}), 400

    return jsonify({'message': result}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

