# dump on json file with many kinds of types, load for read and update the values by inputs in every new run
import pickle

questions = ["What's your name?\n", "How old are you?\n", "Where do you live?\n"]
info = ["name:", "age:", "place:"]
answers = []
for i in questions:
    a = input(i)
    answers.append(a)

dicts = dict(zip(info, answers))


with open("picles.pickle", "wb") as f:
    pickle.dump(dicts, f)

with open("picles.pickle", "rb") as f:
    txt = pickle.load(f)

print(txt)
