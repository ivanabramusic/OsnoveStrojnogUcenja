ham = 0
spam = 0
hamlen = 0
spamlen = 0
messendingwith = 0

with open('SMSSpamCollection.txt','r') as file:
    for line in file:
        if 'ham' in line:
            ham = ham +1
            hamlen = hamlen + len(line.split())
        elif 'spam' in line:
            spam = spam +1
            if line[-1] == '\n':
                line = line[:len(line)-1]
            if line[-1]=='!':
                messendingwith = messendingwith + 1
            spamlen = spamlen + len(line.split())

print(hamlen/ham)
print(spamlen/spam)
print(messendingwith)       

