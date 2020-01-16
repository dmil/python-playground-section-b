from datetime import datetime

# Set a variable birthday = "1-May-12".
birthday = "1-May-12"

# Parse the date using datetime.strptime
python_date = datetime.strptime(birthday, "%d-%B-%y")

# Use strftime to output a date 
# that looks like "5/1/2012".
new_date_string = python_date.strftime("%-m/%-d/%Y")

print(new_date_string)
# BONUS: convert to a function called
#        convert_date_format