import os
import json
import argparse

JSON_PATH="readings.json"
SCRIPT_PATH="../readings.js"

def insert_reading(args):
	category = args.category
	del args.category

	with open(JSON_PATH, "r+") as f:
		# read
		readings = json.load(f)

		# catch capitalization typos
		if category.title() in readings["categories"].keys():
			category = category.title()

		# insert (or create new category if necessary)
		try: readings["categories"][category].append(vars(args))
		except KeyError: readings["categories"][category] = [vars(args)]

		# write json
		f.seek(0)
		json.dump(readings, f)
		f.truncate()

		# write json to script
		with open(SCRIPT_PATH, "w") as f2:
			f2.write("const READINGS = ")
			json.dump(readings, f2)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("title")
	parser.add_argument("-a", "--author", type=str, default="")
	parser.add_argument("-u", "--url", type=str, default="")
	parser.add_argument("-c", "--category", type=str, default="Miscellaneous")
	args = parser.parse_args()
	insert_reading(args)

main()
