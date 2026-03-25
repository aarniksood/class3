number = 67
decimal_number = 6.7
text = "six seven"
famous = True
# to find its type
print("type of number is:", type(number))
print("type of decimal_number is:", type(decimal_number))
print("type of text is:", type(text))
print("type of famous is:", type(famous))
# to typecast
number = float(number)
decimal_number = int(decimal_number)
text = bool(text)
famous = str(famous)
print("number is =" , number)
print("decimal_number is =" , decimal_number)
print("text is =" , text)
print("famous is =" , famous)