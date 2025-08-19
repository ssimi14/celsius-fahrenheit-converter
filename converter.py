def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("=== Convertisseur Celsius ↔ Fahrenheit ===")
    choice = input("Choisissez la conversion (1 = Celsius → Fahrenheit, 2 = Fahrenheit → Celsius) : ")

    if choice == "1":
        c = float(input("Entrez la température en Celsius : "))
        print(f"{c} °C = {celsius_to_fahrenheit(c):.2f} °F")
    elif choice == "2":
        f = float(input("Entrez la température en Fahrenheit : "))
        print(f"{f} °F = {fahrenheit_to_celsius(f):.2f} °C")
    else:
        print("Option invalide ❌")
