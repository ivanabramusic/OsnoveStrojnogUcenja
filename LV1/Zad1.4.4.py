dictionary = {}

#UCITAVANJE TXT DATOTEKE

with open('song.txt','r') as file:
    for line in file:
        for word in line.split():
            if word.lower() in dictionary:
                dictionary[word.lower()] = dictionary[word.lower()] + 1
            else:
                dictionary[word.lower()] = int(1)
for k,v in dictionary.items():
    if v == 1:
        print(k)