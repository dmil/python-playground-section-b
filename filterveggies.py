import csv
import json
from pprint import pprint

# 1. Read vegetables.csv into a variable 
#    called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows]

# Loop through vegetables and filter down to 
# only green vegtables using a whitelist.
greenveggies = []
for veg in vegetables:
	if veg['color'] == 'green':
		greenveggies.append(veg)


# Print green veggies to the terminal
pprint(greenveggies)

# Write the veggies to a json file 
# called greenveggies.json
with open('greenveggies.json', 'w') as f:
	json.dump(greenveggies, f, indent=2)


# Bonus: Output another csv called green_vegetables.csv.
with open('greenveggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])
	for veg in vegetables:
		if veg['color'] == 'green':
			writer.writerow([veg['name'], veg['color']])


