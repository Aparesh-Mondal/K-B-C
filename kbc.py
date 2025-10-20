# kbc
question =[["what is the capital of india ?","kolkata","delhi","bangalore","new delhi"],["what is the national bird of our nation ? ","eagle","sparrow","peacock","crow"],
           ["what is the national animal of india ?","tiger","cat","dog","lion"],["which planet is known for red planet ?","neptune","jupitar","earth","mars"]]

levels = [1000,2000,4000,8000,0]

for i in range(0,len(question)):
    TOTALMONEY = 1000 + 2000 + 4000+8000
    money = levels[i-1]
    print("question for ",levels[i])
    print(question[i][0])
    print("a.",question[i][1],"\t",                                             "b. ",question[i][2] )
    print("c. ",question[i][3],"\t",                                              "d. ",question[i][4])
    reply = int(input("give your answer 1 to 4 : "))
    if not 1<=reply<=4:
        raise ValueError ("enter a valid number!!!!!!")
    if i == 0:
        if reply == 4:
        
            print("correct answer , you have won ",levels[i])
        else:
            print("wrong! answer")
            print("your take home money is : ",money)
            exit()

    if i == 1:
        if reply == 3:
            print("correct answer , you have won ",levels[i])

        else:
            print("wrong! answer")
            print("your take home money is : ",money)
            exit()

    if i == 2:
        if reply == 1:
            print("correct answer , you have won ",levels[i])

        else:
            print("wrong! answer")
            print("your take home money is : ",money)
            exit()

    if i == 3:
        if reply == 4:
            print("correct answer , you have won ",levels[i])

        else:
            print("wrong! answer")
            print("your take home money is : ",money)
            exit()

    if i == 3:
        if reply == 4:
            print("you won total : ",TOTALMONEY)
            print("game is ended here and you are the winner!!!")
    
