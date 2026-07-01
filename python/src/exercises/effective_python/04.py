from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=")

green = my_values.get("green", [""])

print(green)
