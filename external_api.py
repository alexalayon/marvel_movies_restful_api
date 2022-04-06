import urllib.request
import urllib.parse
import json

api_key = "saFdaAKfkIYZfRjl2GU0Dmjeo4EBUjg4bqgsHdsv"

def get_external_streaming(movie_name):
    try:
        movie_name_parsed = url.parse.quote(movie_name)
        with urllib.request.urlopen("https://api.watchmode.com/v1/search/?apiKey=" + api_key + "&search_field=name&search_value=" + movie_name_parsed) as url:
            data = json.loads(url.read().decode())
            movie_id = data["title_results"][0]["id"]
            
            with urllib.request.urlopen("https://api.watchmode.com/v1/title/" + str(movie_id) + "/details/?apiKey=" + api_key) as url:
                data = json.loads(url.read().decode())
                return data
                
    except Exception as ex:
        raise