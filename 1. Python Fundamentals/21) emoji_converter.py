message = input("> ") #indicator for user to type a message

words = message.split(' ')
print(words)

emojis = {
    ":)" : "😊",
    ":(" : "🥺",
    ";)" : "😉"
}

output = ""

for word in words:
    output += emojis.get(word, f"{word} ")
    #or output += emojis.get(word, word) + " "

print(output)



#Printing multiple messages 

no_messages = int(input("How many messages do you want to print? "))
for i in range(no_messages):
    message = input("> ") #indicator for user to type a message
    words = message.split(' ')
    output = ""

    for word in words:
        output += emojis.get(word, f"{word} ")

    print(output)
