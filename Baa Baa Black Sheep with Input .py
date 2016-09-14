print("Please enter a color or adjective ")
adj = raw_input()
if adj == " ":
        adj == "Black"

print("Please enter a noun")
animal = raw_input()
if animal == " ":
        animal == "Sheep"

print("Please enter a plural noun")
noun1 = raw_input()
if noun1 == " ":
        noun1 == "Wool"

print("Please enter a proper noun or a noun")
properNoun = raw_input()
if properNoun == " ":
        properNoun == "Sir"

print("Please enter an integer (That is divisible by 3 please)")
amount = raw_input()
# Please do not leave this empty, because if you do you will get "ValueError: empty string for float()" error

print("Please enter a noun or a proper noun")
noun2 = raw_input()
if noun2 == " ":
       noun2 == "Little Boy"

# Calculations
amount2 = float(amount) / 3
amount2 = str(amount2)

# "Madlib"
print("\n" + noise + ", " + noise + ", " + adj + " " + animal + ",")
print("Have you any " + noun1 + "?")
print("Yes " + properNoun + ", yes " + properNoun + ",")
print(amount + " bags full;")
print(amount2 + " for the master,")
print("And " + amount2 + " for the dame,")
print("And " + amount2 + " for the " + noun2)
print("Who lives down the lane")
