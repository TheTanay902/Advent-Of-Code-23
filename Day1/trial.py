input_file = open("advent.txt", "r")
a = input_file.readlines()
f = open("trial.txt", "w")
sum = 0
for j in a:
    temp = ""
    runn_str = ""
    for i in j:
        runn_str+=i
        if (i.isdigit()):
            temp = temp + i
            continue
        if("one" in runn_str):
            runn_str = runn_str.replace("one","1e")
            temp = temp + "1"
        if("two" in runn_str):
            runn_str = runn_str.replace("two","2o")
            temp = temp + "2"
        if("three" in runn_str):
            runn_str = runn_str.replace("three","3e")
            temp = temp + "3"
        if("four" in runn_str):
            runn_str = runn_str.replace("four","4r")
            temp = temp + "4"
        if("five" in runn_str):
            runn_str = runn_str.replace("five","5e")
            temp = temp + "5"
        if("six" in runn_str):
            runn_str = runn_str.replace("six","6x")
            temp = temp + "6"
        if("seven" in runn_str):
            runn_str = runn_str.replace("seven","7n")
            temp = temp + "7"
        if("eight" in runn_str):
            runn_str= runn_str.replace("eight","8t")
            temp = temp + "8"
        if("nine" in runn_str):
            runn_str= runn_str.replace("nine","9e")
            temp = temp + "9"
    f.write(temp + "\n")
    if(len(temp)==1):
        i1 = int(temp[0])*10 + int(temp[0])
        sum+=i1
    else:
        i1 = int(temp[0])
        i2 = int(temp[len(temp)-1])
        sum+= (i1*10+i2)
print(sum)