# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Get the total number of the name
num_items = (len(names))

# Generate random number between 0 and the last index name
random_names = random.randint(0, num_items - 1)
person_will_pay = names[random_names]
print(person_will_pay + " is pay the bills!")

#this is the easy solution but pretend we don't know this function exist
# print(random.choice(names))



