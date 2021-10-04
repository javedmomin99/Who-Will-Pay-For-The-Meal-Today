# Random Choice method
names_string = input("Give me everybody\'s names, separated by a comma.\n")
names = names_string.split(", ")
import random
random_choice = random.choice(names)
print(random_choice + "will pay for the meal today!")
