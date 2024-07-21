# 1
def enum(imiona):
    for im in enumerate(imiona):
        print (im)

imiona = ["Ania", "Wojtek", "Kuba", "Kacper", "Tosia"]
enum(imiona)

# 2
def a(x):
    if (x > 0 and (x%2) == 0):
        print("Liczba jest dodatnia i parzysta")
a(3)

def b():
    x = input()
    if (x != "0"):
        print("Liczba jest różna od zera")
b()

def c():
    owoce = ['jabłko', 'banan', 'pomarańcza']
    ow = input()
    if (ow in owoce):
        print("Owoc jest dostępny")
c()

# 3
sum = 0
while True:
    x = input()
    sum += int(x)
    if (sum > 100):
        print(sum)
        break