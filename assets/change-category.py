import os
import sys
import json
import argparse

JSON_PATH="readings.json"
SCRIPT_PATH="../readings.js"

def remove_reading(readings, args, category):
	for category in readings["categories"].keys():
		for i, reading in enumerate(readings["categories"][category]):
			if reading["title"] != args.title:
				continue
			# if author specified, then make sure authors are the same too
			if args.author != "" and reading["author"] != args.author:
				continue

			args = readings["categories"][category][i]
			del readings["categories"][category][i]

			# if category is now empty, remove it
			if len(readings["categories"][category]) == 0:
				del readings["categories"][category]

			return args
	return None

def change_category(args):
	category = args.category
	del args.category

	with open(JSON_PATH, "r+") as f:
		# read
		readings = json.load(f)

		# catch capitalization typos
		if category.title() in readings["categories"].keys():
			category = category.title()

		# remove reading from old category
		args = remove_reading(readings, args, category)
		if args is None:
			sys.stderr.write("Error: reading not found in " + JSON_PATH + " as specified (check your spelling?)\n")
			exit(1)

		# insert (or create new category if necessary)
		if category != "":
				try: readings["categories"][category].append(args)
				except KeyError: readings["categories"][category] = [args]

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
	parser.add_argument("-c", "--category", type=str, required=True,
	                    help="category to move the reading into")
	args = parser.parse_args()
	change_category(args)

main()
