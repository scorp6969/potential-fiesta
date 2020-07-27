message = input('>')
words = message.split(' ')
emotes = {
    ":)": "😀",
    ":(": "😞",
    ":o": "😲"
}
output = ""
for word in words:
    output += emotes.get(word, word) + " "

print(output)
