from pprint import pprint
import pandas as pd

df = pd.DataFrame([
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
])

not_cool_people = ['Rachel', 'Phoebe']
millenials = df.query('name not in @not_cool_people')

millenials.to_csv('mill.csv')

# by Dhrumil and Sultan