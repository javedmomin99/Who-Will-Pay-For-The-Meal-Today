# Split string method
names_string = input("Give me everybody\'s names, separated by a comma.\n")
names = names_string.split(", ")
len_names = len(names)
#length of names will be the same as the number of words you typed
import random
random_choice = random.randint(0, len_names - 1)
# if you have typed names as 'javed','sajid','shafi', then random_choice = 0,3. The reason for putting -1 is in person_who_will_pay code, python will read our first word as 0, second word as 1, and third word as 2. so, our maximum random_choice should be 0,2 which would be possible only by len_name which is 3 - 1 = 2.
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " " + "will pay for the meal today!")



