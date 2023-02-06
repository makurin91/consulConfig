import json

decoded_file = "decodeDump.json"


def create_template():
    new_list = []
    line = {'key': 'config/', 'flags': 0, 'value': ''}
    new_list.append(line)
    formated_file = json.dumps(new_list, indent=4)
    with open(decoded_file, mode="w") as f:
        f.write(formated_file)


if __name__ == "__main__":
    create_template()
