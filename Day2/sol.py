file_input = open("advent.txt", "r")
input_list = file_input.readlines()
valid_id_sum = 0
for game in input_list:
    max_red = 0
    max_blue = 0
    max_green = 0
    gamessplit = game.split(": ")
    game_id = int(gamessplit[0].split(" ")[1])
    ListOfRounds = gamessplit[1].split("; ")
    for round in ListOfRounds:
        round_split = round.split(", ")
        for val in round_split:
            count, color = val.split(" ")
            if (color[0]=='r'):
                max_red = max(max_red, int(count))
            if (color[0]=='g'):
                max_green = max(max_green, int(count))
            if (color[0]=='b'):
                max_blue = max(max_blue, int(count))
    power = max_blue*max_green*max_red
    valid_id_sum+=power
print(valid_id_sum)
