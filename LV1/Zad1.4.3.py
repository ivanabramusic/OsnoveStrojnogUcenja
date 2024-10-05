def Average(List):
    return sum(List)/len(List)

#DEFINIRANJE PRAZNE LISTE
list = []

while 1 == 1:
    print("Unesi broj:")
    user_input = input()
    if(user_input =="Done"):
        break
    else:
        try:
            number = float(user_input)
            list.append(number)
        except:
            print("You didn't enter a number.")

list.sort()
print(list)

print("Brojeva u listi: ",len(list))
print("Srednja vrijednost brojeva liste: ", Average(list))
print("Maksimalna vrijednost u listi: ", max(list))
print("Minimalna vrijednost u listi: ", min(list))



