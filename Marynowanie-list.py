import pickle, shelve

#marynowanie list
print("marynowanie list")
f = open("marynowanie.dat", "wb")
rodzaj = ["duzy","maly", "sredni"]
rasa = ["bokser", "owczarek", "pudel"]
kolor = ["czarny", "bialy", "szary"]

pickle.dump(rodzaj, f)
pickle.dump(rasa, f)
pickle.dump(kolor, f)
f.close()


#odmarynowanie list
print("odmarynowanie list")
f= open("marynowanie.dat", "rb")
jeden = pickle.load(f)
dwa = pickle.load(f)
trzy = pickle.load(f)

print(jeden)
print(dwa)
print(trzy)
f.close()
