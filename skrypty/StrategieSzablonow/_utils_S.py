import inspect


# Funkcja ta zwraca stringa reprezentującego wywołanie zadanej funkcji
# wraz z dynamicznymi inputami dla jej parametrów, które są definiowane przy deklaracji
# Np 'mojafunkcja(input('Podaj parametr1: '), input('Podaj parametr2: '))'.
def FunkcjaInput(funkcja):
    parameters = inspect.signature(funkcja).parameters
    input_lines = [f"input('Podaj {name}: ')" for name in parameters.keys()]
    return f"    {funkcja.__name__}({', '.join(input_lines)})\n"
