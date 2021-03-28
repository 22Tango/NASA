import requests, json


def main():
	with open('Keys.json','w') as file:
		json.dump({
			"NASA" : "hTH1zP3UYNNeHE1yPx6ySW9y0X8daK1XIWJnba2b",
		}, file)

	with open('Keys.json','r') as file:
		keys = json.load(file)
	#r = requests.get('')
	print(keys)

def add_key(key, value):
	with open('Keys.json','r') as file:
		keys = json.load(file)
	
	keys[key] = value

	with open('Keys.json', 'r') as file:
		json.dump(keys, file)

def remove_key(key):
	with open('Keys.json','r') as file:
		keys = json.load(file)
	
	del keys[key]

	with open('Keys.json', 'r') as file:
		json.dump(keys, file)

if __name__=='__main__':
	main()