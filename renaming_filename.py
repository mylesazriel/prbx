import os
import json

id_lookup = {"21779": "League of Legends",
             "33214": "Fortnite",
             "32982": "GTA V",
             "18122": "World of Warcraft",
             "29595": "Dota2",
             "32399": "CounterStrike Global Offensive",
             "138585": "Hearthstone",
             "493057": "Player Unknown's Battlegrounds",
             "488552": "Overwatch",
             "460630": "Rainbow 6 Siege",
             "511224": "Apex Legends",
             "506103": "Fifa 19",
             "27471": "Minecraft",
             "502377": "Total War Three Kingdoms",
             "491487": "Dead by Daylight",
             "504462": "Call of Duty Black Ops 4",
             "490422": "Starcraft 2",
             "2748": "Magic the Gathering",
             "313558": "Diablo 3",
             "30921": "Rocket League",
             }

directory = "C:/Users/mylea/OneDrive/Desktop/PRBX/Meta_Data/"
count = 0

for file in os.listdir(directory):
    count = count + 1

    temp = json.load(open(directory + file, encoding='utf-8'))
    game_id = temp["stream_game_id"]
    game_name = id_lookup[str(game_id)]
    
    new_filename = str(count) + "_" + file + " -" + game_name
    #print(new_filename)
    os.rename(directory + file, new_filename)







