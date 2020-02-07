num = int(input())
lists = []
strike = 0
ball = 0

for i in range(num):
    balltype = input()
    
    if balltype == "strike":
        strike += 1
        if strike == 3:
            print("out!")
        else:
            print("strike!")
            
    else:
        ball += 1
        if ball == 4:
            print("fourball!")
        else:
            print("ball!")
            
        