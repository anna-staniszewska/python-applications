from os import getcwd
import czas
import time
import importlib as imp

# Działania na podstawowym środowisku Python
print("Hello World")
help(print)

# Moduły i przestrzenie nazw
current_path = getcwd()
print(current_path)
print(czas.aktualny_czas)
time.sleep(20)
print(czas.aktualny_czas)
imp.reload(czas)
print(czas.aktualny_czas)