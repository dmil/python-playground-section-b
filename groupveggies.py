# by Dhrumil and Sultan 
import csv
import json
from pprint import pprint

# 1. Read vegtables.csv into a variable called vegtables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegtables = [dict(row) for row in rows] # Convert OrderedDict to regular dict

# pprint(vegtables)
# 2. Group vegtables by color as a 
#  variable vegtables_by_color.
vegtables_by_color = {}
for veg in vegtables:
	color = veg['color']
	print("veg = " + str(veg))
	print("color = " + color)
	if color in vegtables_by_color:
		vegtables_by_color[color].append(veg)
	else:
		vegtables_by_color[color] = [veg]



	# pprint(vegtables_by_color)
	print("===========================")

# 3. Output vegtables_by_color into a json 
#  called vegtables_by_color.json.
