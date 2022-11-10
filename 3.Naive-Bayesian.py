import csv
rec=str(input("Enter OUTLOOK(x1), TEMPERATURE(x2), HUMIDITY(x3), WIND(x4) in this sequence "))
reclist=rec.split(",")
with open('D:\\ENGINEERING\\4.Y\\sem-7\\IT-451 ML Lab\\playtennis.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=yes_count=0
    x1_yes=x1_no=0
    x2_yes=x2_no=0
    x3_yes=x3_no=0
    x4_yes=x4_no=0
    for row in csv_reader:
        line_count = line_count + 1
        if(row[5]=="yes"):
            yes_count=yes_count+1
        if(row[1]==reclist[0] and row[5]=="yes"):
            x1_yes=x1_yes+1
        if (row[1] == reclist[0] and row[5] == "no"):
            x1_no = x1_no + 1
        if (row[2] == reclist[1] and row[5] == "yes"):
            x2_yes = x2_yes + 1
        if (row[2] == reclist[1] and row[5] == "no"):
            x2_no = x2_no + 1
        if (row[3] == reclist[2] and row[5] == "yes"):
            x3_yes = x3_yes + 1
        if (row[3] == reclist[2] and row[5] == "no"):
            x3_no = x3_no + 1
        if (row[4] == reclist[3] and row[5] == "yes"):
            x4_yes = x4_yes + 1
        if (row[4] == reclist[3] and row[5] == "no"):
            x4_no = x4_no + 1
    no_count = line_count - yes_count
    x1_yes=x1_yes/yes_count
    x1_no=x1_no/no_count
    x2_yes=x2_yes/yes_count
    x2_no=x2_no/no_count
    x3_yes=x3_yes/yes_count
    x3_no=x3_no/no_count
    x4_yes=x4_yes/yes_count
    x4_no=x4_no/no_count
    yes_x=x1_yes*x2_yes*x3_yes*x4_yes*yes_count/line_count
    no_x=x1_no*x2_no*x3_no*x4_no*no_count/line_count
    print("probability of YES:",yes_x)
    print("probability of NO",no_x)
    if(yes_x>no_x):
        print(f'The playing tennis {reclist[0]}, {reclist[1]}, {reclist[2]}, {reclist[3]} is allowed')
    else:
        print(f'The playing tennis {reclist[0]}, {reclist[1]}, {reclist[2]}, {reclist[3]} is not possible')
