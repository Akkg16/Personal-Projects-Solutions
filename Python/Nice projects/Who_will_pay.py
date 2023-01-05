import random;
list_of_names = input("Insert a number of names that can possibly pay for the bill (example: Angela, Michael, Jordan ...)\nEnter here: ")
list_of_names_splitted = list_of_names.split(", ")
print(list_of_names_splitted)
number_of_people = len(list_of_names_splitted)
who_pays = random.randint(1,number_of_people)
print(f"{list_of_names_splitted[who_pays]} pays for the bill!")