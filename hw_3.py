f = open("input_wasteland.txt.py", mode="r", encoding="utf-8")
poem = f.read()
f.close()


def counting_words(text):
    text = text.lower().split()
    return len(text)


print(counting_words(poem))
