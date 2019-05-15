f = open("input_wasteland.txt.py", mode="r", encoding="utf-8")
poem = f.read()
f.close()


def dictionary_of_unique_words(text):
    dict_unique = {}
    dict_unique.items()
    words = text.lower().split()
    unique = set(words)
    for i in unique:
        dict_unique[i] = words.count(i)
    return dict_unique


def repetition(dict_unique_1):
    lst = []
    for i in dict_unique_1:
        number = dict_unique_1[i]
        lst.append(number)
    lst.sort(reverse=True)
    return lst


final_dict = (dictionary_of_unique_words(poem))
res = repetition(dictionary_of_unique_words(poem))
words = []
for i in res:
    for w in final_dict:
        if final_dict.get(w) == i:
            words.append(w)
print(set(words[:12]))











