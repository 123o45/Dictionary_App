import json
import difflib


def Dictionary(search):

    with open("json_data/data.json", "r") as file:
        data = json.load(file)

    if search in data:
        for val in data[search]:
            print(f"{search} : {val}")
    else:
        suggestions = difflib.get_close_matches(search, data.keys(), n=3, cutoff=0.6)
    
        if suggestions:
            correction = input(f"Do you mean '{suggestions[0]}'? (yes/no): ").lower()
            
            if correction == "yes":
                for val in data[suggestions[0]]:
                    print(f"{suggestions[0]} : {val}")
            elif correction == "no":
                for suggestion in suggestions:
                    option = input(f"Did you mean '{suggestion}'? (yes/no): ").lower()
                    if option == "yes":
                        for val in data[suggestion]:
                            print(f"{suggestion} : {val}")
                        break
                else:
                    print("The word doesn't exist.")
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")
        else:
            print("No suggestions found. The word doesn't exist.")


search = input("Enter the word you want to search for: ")

Dictionary(search)