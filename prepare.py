from read_game_data.create_tags_file import create_tags_file
from read_game_data.create_provinces_file import create_provinces_file
from json import dump


tags = create_tags_file()
with open("tags.txt", "w") as json_file:
    dump(tags, json_file)
provinces_dict = create_provinces_file()
with open("provinces.txt", "w") as json_file:
    dump(provinces_dict, json_file)
    