from random import choice

user_db = {}

def update(user_id, guess_string, result_string):
	if not user_id in user_db.keys():
		user_db[user_id] = {}
		user_db[user_id]['yellow'] = {}
		user_db[user_id]['black'] = []
		user_db[user_id]['white'] = {}
		for i in range(5):
			user_db[user_id]['white'][i] = []

	for i in range(len(result_string)):
		if result_string[i] == 'y':
			user_db[user_id]['yellow'][i] = guess_string[i]
		elif result_string[i] == 'w':
			user_db[user_id]['white'][i].append(guess_string[i])
		elif result_string[i] == 'b' and guess_string[i] not in user_db[user_id]['yellow'].values():
			user_db[user_id]['black'].append(guess_string[i])

def restart(user_id):
	user_db[user_id] = {}
	user_db[user_id]['yellow'] = {}
	user_db[user_id]['black'] = []
	user_db[user_id]['white'] = {}
	for i in range(5):
		user_db[user_id]['white'][i] = []
			
def find_word(user_id):
	possible_words = []
	with open("ru_5.txt", 'r') as f:
		for line in f.readlines():
			if check_word(user_id, line[:5]):
				possible_words.append(line[:5])
				
	return possible_words

def check_word(user_id, word):
	for i in range(len(word)):
		letter = word[i]
		if letter in user_db[user_id]['black']:
			return False
		
		if letter in user_db[user_id]['white'][i]:
			return False
		
		if i in user_db[user_id]['yellow'].keys() and user_db[user_id]['yellow'][i] != letter:
			return False
			
		for k, v in user_db[user_id]['white'].items():
			for val in v:
				if val not in (word[:k]+word[k+1:]):
					return False
		
	return True
