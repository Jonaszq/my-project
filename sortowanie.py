class SelectionSorter:
    def __init__(self):
        self.tablica = []

    def wczytaj_dane(self):
        print("Podaj 10 liczb całkowitych do posortowania:")
        for i in range(10):
            liczba = int(input(f"Podaj liczbę nr {i+1}: "))
            self.tablica.append(liczba)

    def _znajdz_max_index(self, start):
        """
        Metoda pomocnicza – zwraca indeks największego elementu
        w podtablicy zaczynającej się od pozycji 'start'.
        """
        max_index = start
        for j in range(start + 1, len(self.tablica)):
            if self.tablica[j] > self.tablica[max_index]:
                max_index = j
        return max_index

    def sortuj_malejaco(self):
        """
        Sortowanie tablicy metodą przez wybieranie (selection sort).
        Sortowanie malejące.
        """
        n = len(self.tablica)
        for i in range(n - 1):
            max_index = self._znajdz_max_index(i)
            # Zamiana elementów miejscami
            self.tablica[i], self.tablica[max_index] = self.tablica[max_index], self.tablica[i]

    def wyswietl(self):
        print("Tablica po posortowaniu malejąco:")
        for liczba in self.tablica:
            print(liczba, end=" ")
        print()


if __name__ == "__main__":
    sorter = SelectionSorter()
    sorter.wczytaj_dane()
    sorter.sortuj_malejaco()
    sorter.wyswietl()
