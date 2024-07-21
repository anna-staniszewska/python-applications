from zajecia05.zaj03_kod.fleet.ambulance import Ambulance
from zajecia05.zaj03_kod.fleet.ambulance_queue import AmbulanceQueue
from zajecia05.zaj03_kod.fleet.station import Station
from zajecia05.zaj03_kod.operations import *
from zajecia05.zaj03_kod.personnel import *
from zajecia05.zaj03_kod.helpers import check_location
from zajecia05.utils.get_logger import get_logger
from zajecia05.utils.parse_cli_args import parse_args

## niezautomatyzowana wersja
# logger = get_logger("MainAppLogger")

# def run_application():
#     # zdefiniowanie naszych zasobów
#     try:
#         ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
#         ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
#         ambulance3 = Ambulance("Type B", "available", (51.324454, 18.997652), ["Stretcher", "First Aid Kit"])
#         ambulance4 = Ambulance("Type A", "available", (49.376565, 19.154563), ["Defibrillator", "Oxygen tank"])
#         ambulance5 = Ambulance("Type C", "available", (51.334565, 20.435457), ["Defibrillator", "Oxygen tank"])
#         ambulance6 = Ambulance("Type C", "available", (200.334565, -2000.435457), ["Defibrillator", "Oxygen tank"])
#     except ValueError as e:
#         logger.error(e)

#     ambulanceQueue = AmbulanceQueue()
#     ambulanceQueue += ambulance1
#     ambulanceQueue += ambulance2
#     ambulanceQueue += ambulance3
#     ambulanceQueue += ambulance4
#     ambulanceQueue += ambulance5
#     print(ambulanceQueue)

#     employee1 = Employee("John", "Doe", 12000.0)
#     employee2 = Employee("Jane", "Smith", 8000.0)

#     driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
#     driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

#     try:
#         station1 = Station((50.095340, 19.920282), ambulance2, driver1, employee1)
#         station2 = Station((50.055454, 19.956432), ambulance1, driver2, employee2)
#         station3 = Station((50.055454, 500.956432), ambulance3, driver1, employee2)
#     except ValueError as e:
#         logger.error(e)
    
#     # sprawdzenie czy to czasem nie są te same karetki
#     if ambulance1 == ambulance2:
#         logger.error("To są te same karetki!")
#         raise ValueError("To są te same karetki!")
#     # sprawdzenie ile mamy karetek
#     print(Ambulance.get_instances_count())

#     print()

#     # stworzenie kolejki
#     incidentQueue = IncidentQueue()

#     # zaraportowanie 3 zgłoszeń
#     try:
#         incident1 = Incident("Power outage in sector 4", 2, "27.03.2024 14:45", "Grzegorz Kowalski", (51.045455, 20.122554))
#         incident2 = Incident("Fire alarm in building 21", 1, "27.03.2024 09:21", "Matylda Wałczyk", (49.954523, 20.897424))
#         incident3 = Incident("Fire alarm in building 41", 1, "27.03.2024 16:21", "Mariusz Kolec", (49.22227, 20.234324))
#         incident4 = Incident("Fire alarm in park", 4, "27.03.2024 16:21", "Mariusz Kolec", (500.22227, 20.234324))
#     except ValueError as e:
#         logger.error(e)
#     incidentQueue += incident1
#     incidentQueue += incident2
#     incidentQueue += incident3

#     # przypisanie karetek zgłoszeniom
#     print(asign_ambulances(ambulanceQueue, incidentQueue))

#     # dodanie kolejnych 2 zgłoszeń
#     incident4 = Incident("Cat hanging on a tree", 3, "06.04.2024 12:45", "Katarzyna Lasko", (18.354245, 21.354345))
#     incident5 = Incident("Heart attack", 1, "06.04.2024 10:34", "Jacek Pawłowicz", (50.343311, 21.454312))
#     incidentQueue += incident4
#     incidentQueue += incident5

#     # przypisanie karetek 2 nowym zgłoszeniom
#     print(asign_ambulances(ambulanceQueue, incidentQueue))

#     # wypisz wszystkie zgłoszenia
#     print("Aktualne zgłoszenia:")
#     print(incidentQueue)

#     print()

#     # daj kierowcy podwyżkę za super zasługi
#     print(f"Przed podwyżką: {driver1.display_info()}")
#     driver1.update_salary(5000.12)
#     print(f"Po podwyżce: {driver1.display_info()}")

#     print()

#     # zad3 - sprawdzanie lokalizacji
#     print(station1.check_location())
#     print(station2.check_location())

# if __name__ == "__main__":
#     run_application()


logger = get_logger("MainAppLogger")

def run_application(args):
    num_ambulances = args.ambulances
    num_drivers = args.drivers
    num_employees = args.employees
    num_stations = args.stations

    # Tworzenie zasobów
    ambulances = [Ambulance(f"Type {i % 3 + 1}", "available", (50.095340 + i * 0.01, 18.920282 + i * 0.01), ["Defibrillator", "Oxygen tank"]) for i in range(num_ambulances)]
    drivers = [Driver(f"Driver{i}", f"Surname{i}", 10000.0 + i * 1000, f"DL{i:05d}", ["BLS"]) for i in range(num_drivers)]
    employees = [Employee(f"Employee{i}", f"Surname{i}", 8000.0 + i * 500) for i in range(num_employees)]
    
    # Sprawdzenie zasobów
    if num_ambulances < num_stations:
        logger.error("Nie wystarczająca liczba karetek do obsadzenia wszystkich stacji!")
        raise ValueError("Nie wystarczająca liczba karetek do obsadzenia wszystkich stacji!")

    if num_drivers < num_ambulances:
        logger.error("Nie wystarczająca liczba kierowców do obsługi wszystkich karetek!")
        raise ValueError("Nie wystarczająca liczba kierowców do obsługi wszystkich karetek!")

    if num_employees < num_stations:
        logger.error("Nie wystarczająca liczba pracowników do obsadzenia wszystkich stacji!")
        raise ValueError("Nie wystarczająca liczba pracowników do obsadzenia wszystkich stacji!")

    # Tworzenie stacji
    stations = [Station((50.095340 + i * 0.01, 18.920282 + i * 0.01), ambulances[i], drivers[i], employees[i]) for i in range(num_stations)]
    
    logger.info(f"Utworzono {num_stations} stacji.")
    for station in stations:
        print(station)

if __name__ == "__main__":
    args = parse_args()
    run_application(args)

