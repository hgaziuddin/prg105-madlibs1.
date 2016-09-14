# User Input
print("Please enter an onomatopoeia (First letter Uppercased Please)")
noise = raw_input()
print("Please enter a color")
adj = raw_input()
print("Please enter an animal")
animal = raw_input()
print("Please enter a plural noun")
noun1 = raw_input()
print("Please enter a proper noun")
properNoun = raw_input()
print("Please enter an integer (That is divisible by 3 please)")
amount = raw_input()
print("Please enter a noun")
noun2 = raw_input()

# Calculations
amount2 = int(amount) / 3
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
