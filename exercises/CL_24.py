"""CL 24, Dictionaries and Sets"""

pids: set[int] = {710000000, 712345678}
pids.add(730120710)  # add to set use add method

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No Orders of Mint")

for key in ice_cream:
    print(key)
    print(ice_cream[key])
