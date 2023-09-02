import random

names_string = input("Give me everybody's names, separated by a comma. \n\n")
names = names_string.split(", ")

random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]
print(f"\n{random_name} is going to buy the meal today!")

# another way (FASTER)
# random_name = random.choice(names)
# print(f"{random_name} is going to pay for the meal today.")