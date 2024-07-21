import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Przykładowy moduł do pracy z argumentami linii poleceń.")
    parser.add_argument("--text", "-t", required=True, help="Tekst do wyświetlenia")
    parser.add_argument("--verbosity", "-v", help="Zwiększa szczegółowość logowania", action="store_true")
    
    return parser.parse_args()