# f = open("newfile.txt", "a")
# f.write("Hello\nWorld\n")
# f.close()

# WRITIE LIST OF STRINGS TO SEPERTE LINES IN A FILE---------------------------------

words = ["The","quick","brown","fox"]

words_as_str = "\n".join(words)
f = open("newfile.txt", "w")
f.write(words_as_str)
f.close()