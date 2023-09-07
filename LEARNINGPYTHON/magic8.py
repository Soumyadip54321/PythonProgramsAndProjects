import random
name = "Soumyadip"
question = "Will i succeed in life?"
answer = ""
random_number = random.randint(1, 9)
#print(random_number)
if random_number == 1:
    answer = "Yes - definitely."
    #print("Yes - definitely.")
elif random_number == 2:
    answer = "It is decidedly so."
    #print("It is decidedly so.")
elif random_number == 3:
    answer = "Without a doubt."
    #print("Without a doubt.")
elif random_number == 4:
    answer = "Reply hazy, try again."
    #print("Reply hazy, try again.")
elif random_number == 5:
    answer = "Ask again later."
    #print("Ask again later.")
elif random_number == 6:
    answer = "Better not tell you now."
    #print("Better not tell you now.")
elif random_number == 7:
    answer = "My sources say no."
    #print("My sources say no.")
elif random_number == 8:
    answer = "Outlook not so good."
    #print("Outlook not so good.")
elif random_number == 9:
    answer = "Very doubtful."
    #print("Very doubtful.")
else:
    print("Error")

print("["+name+"]"+" "+"asks:"+" "+question)
print("Magic 8-ball's answer:", answer)


