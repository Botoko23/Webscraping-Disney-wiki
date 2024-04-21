import re

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*(\.\d+)?"
money_string = fr"\${number}(–|\sto\s|–\$)?({number})?(\s|,\s)({amounts})"

def word_to_value(word):
	value_dict = {"thousand": 1000, "million": 1000_000, "billion": 1000_000_000}
	return value_dict.get(word.lower(), 1)

def parse_word_syntax(string):
	stripped_string = string.replace(",", "")
	value = float(re.search(number, stripped_string).group())
	modifier = word_to_value(re.search(amounts, string, flags=re.I).group())
	return value*modifier

def parse_value_syntax(string):
	stripped_string = string.replace(",", "")
	return float(re.search(number, stripped_string).group())

def money_converter(money):
	string_syntax = re.search(money_string, money, flags=re.I)
	value_syntax = re.search(fr"\${number}", money)

	if string_syntax:
		return parse_word_syntax(string_syntax.group())
	elif value_syntax:
		return parse_value_syntax(value_syntax.group())
	else:
		return ""
	

if __name__ == "__main__":
	# test_string = "$3.6–4 million"
	# standard_syntax = re.search(money_string, test_string, flags=re.I).group()
	# print(standard_syntax)
	# stripped_string = standard_syntax.replace(",", "")
	# value = float(re.search(number, stripped_string).group())
	# modifier = word_to_value(re.search(amounts, test_string, flags=re.I).group())

	# print(value*modifier)
    from datetime import datetime

    # Define the datetime strings
    datetime_str1 = 'November 13, 1940'
    datetime_str2 = 'June 27, 1941'

    # Convert the datetime strings into datetime objects
    datetime_obj1 = datetime.strptime(datetime_str1, '%B %d, %Y')
    datetime_obj2 = datetime.strptime(datetime_str2, '%B %d, %Y')
    print(datetime_obj1)
    print(datetime_obj2)

    # Calculate the difference between the two datetime objects
    time_difference = datetime_obj2 - datetime_obj1

    print("Time difference:", time_difference)


	