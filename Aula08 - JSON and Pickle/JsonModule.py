# dump on json file with many kinds of types, load for read and update the values by inputs in every new run
import json

list = input("Say something:\n").split(" ")
list2 = [",", "thats", "all", "folks"]
list.extend(list2)
dicts = {"last thing you said:": " ".join(list)}


with open("jason.json", "w", encoding="utf-8") as f:
    json.dump(dicts, f)

with open('jason.json', 'r') as f:
    txt = json.load(f)

print(txt)
