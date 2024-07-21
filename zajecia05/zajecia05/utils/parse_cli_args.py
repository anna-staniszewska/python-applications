import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="System zarządzania karetkami.")
    parser.add_argument("--ambulances", "-a", type=int, required=True, help="Liczba dostępnych karetek")
    parser.add_argument("--drivers", "-d", type=int, required=True, help="Liczba dostępnych kierowców")
    parser.add_argument("--employees", "-e", type=int, required=True, help="Liczba dostępnych pracowników")
    parser.add_argument("--stations", "-s", type=int, required=True, help="Liczba stacji do obsadzenia")
    
    return parser.parse_args()
