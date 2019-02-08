#INWENTARZ BOHATERA
#DEMONSTRUJE UŻYCIE KROTEK

#tworze pusta krotke
inventory = ()

#krotka jako warunek
if not inventory:
    print(" Nie masz niczego w inwentarzu!")

#tworze krotke zawierajaca elementy
inventory =("miecz",
            "zbroja",
            "pochodnia")

if inventory:
    print("Twoj inwentarz :" ,inventory)

# przechodzenie w petli przez elementy krotki
if inventory:
    for item in inventory:
        print(item)

print("Twoj dobytek zawiera", len(inventory), "elementy")

if "miecz" in inventory:
    print(" Stan do walki!")

chest=( "zloto", "skarby")
print("znalazles skrzynię!")

#konkatenacja krotki
inventory+=chest
print(inventory)
