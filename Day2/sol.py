n_red = 12
n_green = 13
n_blue = 14
file_input = open("advent.txt", "r")
input_list = file_input.readlines()
valid_id_sum = 0
for game in input_list:
    custom_flag = True
    gamessplit = game.split(": ")
    game_id = int(gamessplit[0].split(" ")[1])
    ListOfRounds = gamessplit[1].split("; ")
    for round in ListOfRounds:
        round_split = round.split(", ")
        for val in round_split:
            count, color = val.split(" ")
            if (color[0]=='r'):
                if(int(count)>n_red):
                    custom_flag=False
            if (color[0]=='g'):
                if(int(count)>n_green):
                    custom_flag=False
            if (color[0]=='b'):
                if(int(count)>n_blue):
                    custom_flag=False
    if(custom_flag):
        valid_id_sum+=game_id
print(valid_id_sum)
