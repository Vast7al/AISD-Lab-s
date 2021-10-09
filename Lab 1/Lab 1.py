import datetime
import time
# zadanie 1
# Przygotować funkcję, która przyjmie w parametrach pierwszą literę
# imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką.
# Przykładowe wyjście: J. Kowalski.
# def name1 (imie,nazwisko):
#   a=str(imie[0]+'.')
#   b=str(nazwisko)
#   print(a+ b)


#imie1=str(input(" Podaj imie "))
#nazwisko1=str(input(" Podaj nazwisko "))
# name(imie1,nazwisko1)
# zadanie 2
# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko,
# oraz zwróci pierwszą literę imienia i nazwisko połączone kropką.
# Funkcja powinna również dbać o poprawność wielkich liter.
# Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.
def name2(imie, nazwisko):
    a = str((imie[0]+'.'))
    a2 = a.capitalize()
    b = str(nazwisko)
    b2 = b.capitalize()
    print(a2 + b2)

#imie2=str(input("Podaj imie "))
#nazwisko2=str(input("Podaj nazwisko "))
# name2(imie2,nazwisko2)
# zadanie 3
# Przygotować funkcję, która przyjmie 3 argumenty:
# 2 pierwsze cyfry aktualnego roku, 2 ostatnie cyfry aktualnego roku
# wiek użytkownika, a następnie zwróci jego rok urodzenia.
# def DataUrodzenia(pierwszaCyfra,ostatniaCyfra,wiekUzytkownika):
  # Rok=(str(pierwszaCyfra+ostatniaCyfra))
  # Rok2=int(Rok)
  # DataUrodzeniaUzytkownika=(Rok2-wiekUzytkownika)
  # print((DataUrodzeniaUzytkownika))
#pierwszaLitera=(input("Podaj pierwsze 2 cyfry aktualnego roku "))
#ostatniaLitera=(input("Podaj 2 ostatnie cyfry aktualnego roku "))
#wiekUzytkownika=int(input("Podaj wiek "))
# DataUrodzenia(pierwszaLitera,ostatniaLitera,wiekUzytkownika)
# zadanie 4
# Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane, a następnie zwróci wynik działania funkcji przyjętej
# w 3.parametrze. Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.
# def zadanie4 (imie,nazwisko,name2):
#    return name2(imie,nazwisko)

#a=input("Podaj imie ")
#b=input("Podaj nazwisko ")
# zadanie4(a,b,name2)
# zadanie 5
# Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia.
# Należy sprawdzić w jednej instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie oraz czy druga liczba jest różna od 0.
# def zadanie5 (x,y):
#    if x>= 1 and y>=0:
#     return x/y

#x=float(input("Podaj wartosc x "))
#y=float(input("Podaj wartosc y "))
# print(zadanie5(x,y))
# zadanie 6
# Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli,
# dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.
# w petli dac input ktory bedzie prosil o liczby, i kiedy suma wszystkich osiagnie 100 zatrzymac petle
# suma=0
# while suma < 100:
#  x=int(input("Podaj liczbe "))
#  suma+=x
#  print(suma)
#  continue
# if suma > 100:
#   print("Suma przekracza 100 ")
# zadanie 7
# Przygotować funkcję, która przyjmie 1 argument w postaci listy, a następnie zwróci te elementy w postaci krotki.
# def zadanie7 (a):
#    return tuple(a)
# a=[24,55,13,14,66,77,23,52,66]
# print(zadanie7(a))
# zadanie 8
# Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli, a następnie wartości z tej zostanią zrzutowane do krotki.
# lista=[]
# while len(lista) <6:
#    wartosc=int(input("Podaj wartosc "))
#    lista.append(wartosc)
#    continue
# if len(lista) >=6:
# print(tuple(lista))
# zadanie 9
# Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi.
# Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.
# def zadanie9(x):
#  tydzien = ["poniedzialek", "wtorek", "sroda",
#            "czwartek", "piatek", "sobota", "niedziela"]
#  return (tydzien[x])


#x = int(input("Podaj liczbe "))
#print (zadanie9(x))
# zadanie 10
# Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków,
# a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.
# wrzucic zdanie do listy, sprawdzic indeksy od konca czy koncowy indeks zgadza sie z pierwszym itd
# def zadanie10(zdanie):
#    z = str(zdanie)
#    lista = list(z)
#    print(lista)
# for x in range(-1,256, 1):
#  print(x)


#zdanie = str(input("Podaj zdanie "))
# zadanie10(zdanie)
