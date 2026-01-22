# FAIL-CLOSED PROTOKOLL
# DIESES MODUL ÜBERWACHT DIE SYSTEM-INTEGRITÄT

def check_integrity(input_data):
    # Simuliert eine mathematische Prüfung
    if input_data is None:
        return False
    return True

def lock_system():
    print("!!! SICHERHEITSVERLETZUNG !!!")
    print("SYSTEM GEHT IN DEN LOCKDOWN.")
    exit()