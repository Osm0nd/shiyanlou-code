for jump in range(1,101):
    if jump%10 == 7 or jump//10 == 7 or jump%7 == 0:
        continue
    else:
        print(jump)
    

