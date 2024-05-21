from json import load


def get_data():
    with open("provinces.txt", "r") as json_file:
        data = load(json_file)
    return data
