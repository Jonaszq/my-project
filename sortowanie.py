class SelectionSorter:
    def __init__(self):
        # Tworzymy pustą listę, w której będziemy trzymać liczby podane przez użytkownika
        self.tablica = []

    def wczytaj_dane(self):
        # 1. Program mówi użytkownikowi, żeby podał 10 liczb
        print("Podaj 10 liczb całkowitych do posortowania:")

        # 2. W pętli 10 razy pytamy użytkownika o liczbę
        for i in range(10):
            # Pytamy o kolejną liczbę
            liczba = int(input(f"Podaj liczbę nr {i+1}: "))
            # Dodajemy ją do listy (na końcu)
            self.tablica.append(liczba)

    def _znajdz_max_index(self, start):
        """
        Metoda pomocnicza – czyli taki mały pomocnik.
        Szuka największej liczby w części tablicy zaczynającej się od pozycji 'start'.
        Zwraca numer (indeks) tej największej liczby.
        """
        # Na początku zakładamy, że największa liczba jest na pozycji 'start'
        max_index = start

        # Przeglądamy całą resztę tablicy
        for j in range(start + 1, len(self.tablica)):
            # Jeśli znajdziemy większą liczbę niż dotychczasowa największa
            if self.tablica[j] > self.tablica[max_index]:
                # to aktualizujemy indeks największej liczby
                max_index = j

        # Oddajemy (zwracamy) miejsce, gdzie ta największa liczba siedzi
        return max_index

    def sortuj_malejaco(self):
        """
        Tutaj robimy sortowanie metodą 'przez wybieranie' (selection sort).
        Wersja malejąca = od największej liczby do najmniejszej.
        """

        # Liczymy ile mamy elementów w tablicy
        n = len(self.tablica)

        # Lecimy po każdym miejscu w tablicy (oprócz ostatniego, bo on sam się już ustawi)
        for i in range(n - 1):
            # Szukamy największej liczby w reszcie tablicy
            max_index = self._znajdz_max_index(i)

            # Zamieniamy miejscami: największa liczba idzie na początek "tej części tablicy"
            self.tablica[i], self.tablica[max_index] = self.tablica[max_index], self.tablica[i]

            # Można by tu dodać printy do podglądu, jak krok po kroku zmienia się tablica

    def wyswietl(self):
        # Wypisujemy wynik na ekran
        print("Tablica po posortowaniu malejąco:")
        for liczba in self.tablica:
            print(liczba, end=" ")
        print()


# Tutaj zaczyna się główny program
if __name__ == "__main__":
    # Tworzymy obiekt sortera (taki "robot do sortowania")
    sorter = SelectionSorter()

    # Wczytujemy od użytkownika 10 liczb
    sorter.wczytaj_dane()

    # Sortujemy je od największej do najmniejszej
    sorter.sortuj_malejaco()

    # Pokazujemy efekt końcowy
    sorter.wyswietl()
