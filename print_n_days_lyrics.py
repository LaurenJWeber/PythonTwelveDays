###############################################################################
# Description: Print the lyrics for The Twelve Days of Christmas
#              All data read from a Json file.
###############################################################################

import argparse
import json


def generate_lyrics(config):

    previous_gifts = []
    sep = " "
    lyrics = ""

    for day in config["days"]:
        lyrics += "\n"
        lyrics += sep.join((config["startOfVerse"], day["ordinal"], config["event"],
                            config["giver"], config["action"], day["gift"]))

        for i in range(len(previous_gifts) - 1, -1, -1):
            lyrics += "\n"
            if i == 0:
                lyrics += sep.join((config["joinLastDay"], previous_gifts[i]))
            else:
                lyrics += previous_gifts[i]

        previous_gifts.append(day["gift"])
        lyrics += "\n"

    return lyrics


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="path to json configuration file")
    args = parser.parse_args()
    
    with open(args.config_path) as config:
        configuration = json.load(config)
    
    lyrics = generate_lyrics(configuration)
    print(lyrics)
    

if __name__ == "__main__":
    main()
