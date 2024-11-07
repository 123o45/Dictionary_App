import json
import difflib

#data = json.load(open("json_data/data.json"))
with open("json_data/data.json", "r") as file:
    data = json.load(file)

search = input("Enter the word you want to search for: ")


if search in data:
    for val in data[search]:
        print(f"{search}: {val}")
    print(f"{search} : {data[search]}") 
else:
    suggestions = difflib.get_close_matches(search, data.keys(), n=3, cutoff=0.6)
    
    if suggestions:
        print(f"'{search}' not found. Did you mean one of these?")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print(f"'{search}' not found in the dictionary, and no close matches were found.")
#     # Suggest close matches if the word is not found


{"pen":"definition", "food":"de"}