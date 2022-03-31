class Character:
	def __init__(self, new_character):
		self.name = new_character['name']
		self.gender = new_character['gender']
		self.actor = new_character['actor']
		self.birth_date = new_character['birth_date']
		self.country = new_character['country']
		self.affiliation = new_character['affiliation']
		self.super_power = new_character['super_power']
		self.first_appearance = new_character['first_appearance']
		self.last_appearance = new_character['last_appearance']
		self.description = new_character['description']
		
	def convert_to_json(self):
		return {'name': self.name, 'gender': self.gender, 'actor': self.actor, 'date of birth': self.birth_date, 'country of origin': self.country,
			'affiliation': self.affiliation, 'super power': self.super_power, 'first appearance': self.first_appearance, 'last appearance': self.last_appearance,
			'description': self.description}
