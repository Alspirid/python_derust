# never modify containers while iterating over them. Use copies instead


search_key = "red"

my_dict = {"red": 1, "blue": 2, "green": 3}

for key in list(my_dict):
    if key == "blue":
        my_dict["yellow"] = 4

my_set = {"red", "blue", "green"}

for color in my_set:
    if color == "blue":
        my_set.add("green")
