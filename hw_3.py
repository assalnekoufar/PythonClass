f = open("input_wasteland.txt.py", mode="r", encoding="utf-8")
poem = f.read()
f.close()


def counting_words(text):
    text_new = text.lower().split()
    text_with_out_repetition = set(text.lower().split())
    return len(text_new), len(text_with_out_repetition)


print(counting_words(poem))
