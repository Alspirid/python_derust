# enumerate
#
#
flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]

# for item in flavor_list:
#     print(item)

for i, item in enumerate(flavor_list, 1):
    print(i, item)
