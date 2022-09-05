from ast import parse
import os
import json

BASE = "data/"

file_names = os.listdir(BASE)

with open(BASE + file_names[0]) as file_handle:
    file_json = file_handle.read()

parsed_json = json.loads(file_json)

count = 0

for page in parsed_json["pages"]:
    for element in page["elements"]:
        if element and element["type"] == "paragraph":
            for paragraph_content in element["content"]:
                for word in paragraph_content["content"]:
                    print(word["content"], end=" ")
            print("\n\n")