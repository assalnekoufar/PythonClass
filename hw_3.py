f = open("input_wasteland.txt.py", mode="r", encoding="utf-8")
poem = f.read()
f.close()


def dictionary_of_unique_words(text):
    dict_unique = {}
    words = text.lower().split()
    unique = set(words)
    for i in unique:
        dict_unique[i] = words.count(i)
    return dict_unique


print(dictionary_of_unique_words(poem))
