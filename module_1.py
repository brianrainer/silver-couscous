# string, list
greetings = ["Welcome", "to", "Kodland", "Python", "Program!"]
print(" ".join(greetings))

# input output
name = input("Siapa Namamu? ")
print("Salam Kenal %s!" % name)

# library
import random

# dictionary
emojis = {
    "Senyum": "😃",
    "Semangat": "😆",
    "Kedap Kedip": "😉",
    "Gembira": "😛"
}
repeat = int(input("Mau berapa emoji? (1-10):"))

# condition and loop
while repeat < 1 or repeat > 10:
    print("Masukkan angka 1-10 ya!")
    repeat = int(input("Mau berapa emoji? (1-10):"))


# loop
for i in range(repeat):
    description = random.choice(list(emojis.keys()))
    print("Emoji %i: %s %s" % (i+1, description, emojis[description]))


print("Sampai Jumpa!")
