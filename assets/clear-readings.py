import os
import sys
import json

JSON_PATH="readings.json"
SCRIPT_PATH="../readings.js"

if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
	sys.stderr.write("Usage: python3 " + sys.argv[0] + "\n")
	sys.stderr.write("Clears all entries from reading list.\n")
	exit(1)

with open(JSON_PATH, "w") as f, open(SCRIPT_PATH, "w") as f2:
	readings = {"categories":{}}
	json.dump(readings, f)
	f2.write("const READINGS = ")
	json.dump(readings, f2)
