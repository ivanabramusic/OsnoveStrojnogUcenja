#TRY I EXCEPT ZA BACANJE IZNIMAKA

print("Unesi broj od 0-1:")


try:
    number = float(input())

    if(number>1.0 or number<0.0):
        print("Uneseni broj nije unutar granica.")
    elif(number>=0.9 and number <=1.0):
        print("A")
    elif(number>=0.8 and number<0.9):
        print("B")
    elif(number>=0.7 and number<0.8):
        print("C")
    elif(number>=0.6 and number<0.7):
        print("D")
    elif(number>=0.0 and number<0.6):
        print("F")
except:
    print("You didn't enter a number.")