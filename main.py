import os
import json

INPUT_PATH = "data/"
OUTPUT_PATH = "output/"

# Returns list of paragraph tuples (word_count, paragraph text)
def extract_paragraphs(json_input):
    paragraphs = []

    for page in json_input["pages"]:
        for element in page["elements"]:
            if element and element["type"] == "paragraph":
                words = ""
                word_count = 0

                for line in element["content"]:
                    word_count += len(line["content"])
                    words += " " + " ".join([x["content"] for x in line["content"]])

                paragraphs.append((word_count, words.strip()))
    
    return paragraphs

def main():
    file_names = list(filter(lambda file_name: file_name.endswith(".json"), os.listdir(INPUT_PATH)))

    with open(INPUT_PATH + file_names[0]) as file_handle:
        file_json = file_handle.read()

    parsed_json = json.loads(file_json)

    # Sort the paragraphs by their word_count, highest word count paragraphs first
    paragraphs_sorted_by_word_count = sorted(extract_paragraphs(parsed_json), key=lambda kvp: kvp[0], reverse=True)

    # Filter the lines from table of contents (it has a lot of dots, which AI counts as words :|, so skip those lines)
    cleaned_paragraphs = list(filter(lambda p: p[1].count(".") < 0.25 * p[0], paragraphs_sorted_by_word_count))

    output_json = list(map(lambda p: {"word_count": p[0], "value": p[1]}, cleaned_paragraphs))
    output_json_str = json.dumps(output_json, indent=4)

    with open(OUTPUT_PATH + F"{file_names[0]}", "w", encoding="utf-8") as file_handle:
        file_handle.write(output_json_str)

    # Sample output
    print(json.dumps(output_json[:100], indent=4))

if __name__ == "__main__":
    main()