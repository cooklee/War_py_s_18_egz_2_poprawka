<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Programowanie obiektowe i bazy danych &ndash; egzamin poprawkowy.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj repozytorium na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres repozytorium możesz znaleźć na stronie repozytorium po naciśnięciu w guzik "Clone or download".
3. Otwórz repozytorium w swoim ulubionym edytorze tekstu/środowisku programistycznym (Pycharm, Idea, Webstorm, VisualCode, itp)
4. Nie dodawaj do repozytorium plików konfiguracyjnych środowiska programistycznego (.idea, *.iml). Najlepiej stwórz plik `.gitignore`. [Tutaj](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore) znajdziesz przykładowy plik .gitignore dla środowisk InteliJ
5. Rozwiąż zadania w poszczególnych plikach zgodnie z poleceniami.
6. Przygotuj commit. Przygotowanie polega na dodaniu plików za pomocą jednej z poniższych komend:
   - **dla każego pliku wykonaj komendę `git add <nazwa_pliku>`**
   - **dodanie wszystkich pliów z bieżącego katalogu komendą `git add .` - kropka na końcu jest ważna**
7. Stwórz commit za pomocą komendy: `git commit -m "<nazwa_commita>"`
8. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
9. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.
10. Obejrzyj swój Pull Requesta - jeżeli brakuje jakiegoś pliku - poproś o pomoc prowadzącego.

#### Pamiętaj, że pull request musi być stworzony, aby wykładowca dostał Twoje odpowiedzi.

* podczas egzaminu **możesz** korzystać z notatek, kodu napisanego wcześniej, internetu i prezentacji,
* zabroniona jest jakakolwiek komunikacja z innymi kursantami oraz osobami na zewnątrz.

**Powodzenia!**

----------------------------------------------------------------------------------------

## Pytania otwarte
Odpowiedzi wpisz w pliku **answers.txt**.

### Pytanie 1
(2 pkt)
Jakie znasz klucze w tabelach? W jakich okolicznościach powinny zostać użyte?

### Pytanie 2
(1 pkt)
Czym się różni metoda statyczna w klasie od zwykłej metody obiektu?

## Zadania praktyczne
Kod wpisz w odpowiednim pliku, zgodnie z poleceniem zadania.

### Zadanie 1
(5 pkt)
W bazie danych mamy następujące tablice:
```SQL
* Readers: id : int, name : varchar(60), email : varchar(60), is_active : boolean, nie może być null, standardowa wartość: true
* Books: id : int, title : varchar(60), price : real(5, 2), author : varchar(60)
* PublishingHouses: id : int, name : varchar(60), city : varchar(20), address : varchar(120)
```
Napisz następujące zapytania SQL (wystarczą same zapytania SQL, nie musisz pisać kodu Pythona):

1. Tworzące tabelę `Readers` (email ma być unikatowy).
2. Tworzące tabelę `Books`.
3. Tworzące tabelę `PublishingHouses` (dodaj odpowiednią relację z tabelą książek: każda książka może mieć jednego wydawcę, każdy wydawca może mieć wiele książek w ofercie).
4. Stworzenie relacji wiele do wielu między tabelami `Readers` a `Books`.
5. Wybranie wszystkich książek o cenie większej niż 10 zł.
6. Włożenie do tabeli `PublishingHouses` nowego wydawnictwa o nazwie "Super Książki", mieszczącego się w miejscowości Kaczy Dół, przy ulicy Batorego 120.
7. Usuniecie książki o `id` 12.
8. Wybranie wszystkich czytelników, którzy kiedykolwiek wypożyczyli jakąś książkę (na podstawie relacji wiele do wielu między książką, a czytelnikiem; p. punkt 5).
9. Zdezaktywowanie użytkownika o id 2 (ustaw wartość `is_active` na false dla tego użytkownika, załóż że użytkownik już istnieje w bazie). 
10. Dodanie do tabeli `Readers` pola `date_of_birth` przechowującego datę urodzenia czytelnika. Pole może przyjmować wartość `null`.

Za każde zapytanie przysługuje pół punktu.

### Zadanie 2
(3 pkt)
Napisz funkcję `get_books(id)`, która wyświetli wszystkie 
książki wypożyczone przez czytelnika o identyfikatorze  przekazanym jako parametr 
funkcji. Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.

### Zadanie 3
(4 pkt)

Używając Flaska, napisz stronę, która spełni następujące założenia:

1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    * `first_name`: imię,
    * `last_name`: nazwisko,
    * `email`: email czytelnika.

2. Po wejściu metodą POST:
    * zweryfikuje poprawność danych (wystarczy sprawdzić, czy imię i nazwisko nie jest puste i w czy w polu `email` znajduje się znak "@",
    * zapisze te dane do bazy danych do tabeli `Readers` (tabela taka sama jak w zadaniu 1),
    * jeśli którakolwiek dana będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat o błędzie.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.

### Zadanie 4
(5 pkt)
Napisz program w Pythonie klasy `Truck`. Klasa ma spełniać następujące właściwości:

1. Dziedziczyć po klasie `Car` (zajrzyj do modułu **exam**).
2. Mieć dodatkowe atrybuty: ```capacity``` (ładowność) i ```registration``` (numer rejestracyjny).
3. Mieć konstruktor, który przyjmuje następujące dane: markę, moc silnika, kolor i ładownosć. Marka, moc i kolor mają być przekazywane do konstruktora klasy nadrzędnej. Konstruktor ma sprawdzać, czy podana ładowność jest prawidłowa. Jeżeli jest  &ndash; to ją nastawiać, jeżeli nie  &ndash; to numer ma być nastawiona na 0.
4. Mieć prywatną metodę ```validate_registration(plate)``` &ndash; rejestracja jest prawidłowa, jeżeli ma dokładnie 7 znaków: 3 wielkie litery i 4 cyfry. Funkcja ma zwracać wartość logiczną.
5. Mieć publiczną funkcję ```set_registration(plate)``` i ```get_registration()```. Funkcja set ma nastawiać zmienną `registration` (jeżeli podany nowa rejestracja jest prawidłowa), a funkcja get &ndash; ją zwracać.
