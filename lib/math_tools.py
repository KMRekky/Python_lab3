#Dodawanie 
def add(a: float, b: float) -> float:
    return a + b

#a: pierwsza liczba 
#b: druga liczba
#return: Wynik dodawania liczb a i b

#Odejmowanie
def subtract(a: float, b: float) -> float:
    return a - b

#a: pierwsza liczba 
#b: druga liczba
#return: Wynik odejmowania liczb a i b

#Mnożenie
def multiply(a: float, b: float) -> float:
    return a * b

#a: pierwsza liczba 
#b: druga liczba
#return: Wynik mnożenia liczb a i b

#Dzielenie
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError('Nie można dzielić przez 0')
    return a / b

#a: pierwsza liczba - licznik
#b: druga liczba - mianownik
#raise ValueError: Gdy liczba b jest 0 
#return: Wynik dzielenia liczb a i b