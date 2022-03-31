class Movie:
	def __init__(self, new_movie):
		self.name = new_movie['name']
		self.rating = new_movie['rating']
		self.genre = new_movie['genre']
		self.budget = new_movie['budget']
		self.box_office = new_movie['box_office']
		self.main_character = new_movie['main_character']
		self.duration = new_movie['duration']
		self.release_date = new_movie['release_date']
		self.summary = new_movie['summary']
		
	def convert_to_json(self):
		return {'name': self.name, 'rating': self.rating, 'genre': self.genre, 'budget': self.budget, 'box office': self.box_office, 'main character': self.main_character, 
		'movie duration': self.duration, 'release date': self.release_date, 'summary': self.summary}
