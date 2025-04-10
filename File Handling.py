# “The Memory Box Analogy” – Understanding File Handling in Python”

# Imagine you have a Memory Box 📦 where you store your precious letters, photos, and memories. Now, let’s say this box is your file — and Python is just trying to help you open it, read stuff, write new things, or organize it better.

# 🔑 open() – Unlocking the Box
# Just like you can’t interact with your memory box unless you open it, you can’t work with a file unless you open it in Python.

file = open ("memories.txt","w")

# The "w" mode is like opening the box and deciding to toss out the old stuff to write new ones. 📃🖊️

# ✍️ write() – Adding New Memories
# You want to add a note to your box — maybe "Today was awesome!" — just write it down!

file.write("Today was awesome!\n")

# 📌 append() – Adding Without Removing
# You don’t want to replace your old letters, you just want to add more!
file = open("memories.txt","a")
file.write("I love coding!\n")


# 👓 read() – Sitting Down to Re-read Old Notes
# When you miss the old days and want to read what you wrote in the past:

file = open("memories.txt","r")
print(file.read())

# 🧭 seek() and tell() – Moving Around in Time
# These are like bookmarks in your diary.
# You can go to any specific entry (position), and even check where you are currently:

file.seek(0) # Go back to the start of the file
print(file.tell()) # Tell me my position

# 🤝 with open(...) – Responsible Memory Keeper
# Python is like your bestie — always reminding you, “Hey, close the box when you’re done!”

with open ("memories.txt", "r") as file:
    content = file.read()
    print(content)
# No need to worry about closing the box, Python does it for you!

# 🧪 Try–Except–Finally – Safe Keeping in Chaos
# What if you lose your key to the box or the box is broken? Python says, don’t panic, I’ll handle it!

try:
    with open ("special_letter.txt", "x") as file:
        file.write("This is Secret!")
except FileExistsError:
    print ("Oops! This memory already exists.")
finally:
     print("Thanks for trying to keep your memories safe.")

file.close()
# 🗝️ Summary – Like Unlocking a Treasure Chest of Memories
# open() opens the door to your memory chest.

# write() lets you add brand new memories inside.

# append() adds fresh entries alongside the old ones.

# read() helps you revisit and relive those moments.

# seek() and tell() help you check your current spot — just like placing a bookmark.

# with open(...) ensures the chest is closed safely — you don’t need to remember to do it.

# try–except–finally means when something goes wrong, don’t worry — Python has your back!

# 🎯 In Short:
# File handling helps in saving, reading, and managing data even when the program is not running anymore.