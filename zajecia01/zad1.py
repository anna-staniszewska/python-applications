import json

with open('teksty.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

lista = obj["teksty"]
teksty = []
for i, ele in enumerate(lista):
    thisValue = ele.get("tekst" + str(i+1))
    teksty.append(thisValue)
teksty = ' '.join(teksty)

teksty = teksty.lower()
teksty = teksty.split()

for i in range(len(teksty)):
    teksty[i] = teksty[i].replace(",","")
    teksty[i] = teksty[i].replace(".","")
    teksty[i] = teksty[i][:-1] + teksty[i][-1].upper()

teksty = [e for e in teksty if e.__contains__("a") or e.__contains__("A")]

unique = list(set(teksty))
counts = []
for i in unique:
    counts.append(teksty.count(i))

countDict = {}
for i, ele in enumerate(unique):
    countDict[ele] = counts[i]

with open("wordCounts.json", "w") as outfile: 
    json.dump(countDict, outfile, indent=4)
