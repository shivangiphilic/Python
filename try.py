while True:
    try:
        x = int(input("enter x: "))
        #break here also works
    except ValueError:                  #Here, we tell what to do if user types other values than int
        print("x is not int")           #gets executed when there is ValueError
    else:                               #if no ValueError
        break                           #break out of loop

print(f"x is {x}")                      #we print outside the infinite loop 
