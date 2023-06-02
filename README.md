# Aplikacja wspomagania wyboru optymalnych produktów rolnych
## Opis
Aplikacja 'Wspomaganie Wyboru Optymalnych Produktów Rolnych' została stworzona w celu pomocy rolnikom w podejmowaniu decyzji dotyczących wyboru optymalnych roślin i planów nawożenia na ich działkach. Wykorzystuje ona algorytm regresji liniowej do przewidywania przyszłej ceny rośliny oraz obliczania przewidywanego zysku z potencjalnego zasiewu rośliny.

Głównym celem aplikacji jest wybór rośliny, która zapewni największy zysk na danej działce. Algorytm analizuje dane dotyczące klasy ziemi oraz wymaganych nawozów do otrzymania plonu rośliny. Na podstawie tych informacji, aplikacja sugeruje rolnikowi optymalną roślinę do zasiewu na danej działce, która zapewni największy potencjalny zysk.
## Użycie (Use Case)
Aplikacja dostarcza następujące funkcje:

- Generowanie przyszłych cen roślin: Użytkownicy mogą sprawdzić prognozowane ceny różnych rodzajów roślin na przyszłość, co pomaga w podejmowaniu decyzji inwestycyjnych.

- Obliczanie zysku przewidywanego plonu: Dzięki wprowadzeniu danych dotyczących planowanej uprawy, aplikacja może obliczyć przewidywany zysk na podstawie prognozowanych plonów i cen roślin.

- Przegląd optymalnego zasiewu klasy: Użytkownicy mogą zobaczyć zalecane zasiewy dla różnych klas glebowych, uwzględniające preferencje i cele uprawy.

- Przegląd optymalnego przewidywanego plonu: Aplikacja umożliwia analizę i porównanie przewidywanych plonów różnych roślin na podstawie danych glebowych, klimatycznych i planów nawożenia.

- Dodawanie własnych działek, roślin, nawozów, planów nawożenia i przewidywanych plonów: Użytkownicy mają możliwość dostosowania aplikacji poprzez dodawanie i zarządzanie własnymi danymi dotyczącymi działek, roślin, nawozów oraz planów nawożenia i przewidywanych plonów.

## Technologie
Projekt został zrealizowany w oparciu o następujące technologie i narzędzia:

- Django - framework do tworzenia aplikacji webowych w języku Python.
- HTML, CSS - języki do budowania interfejsu użytkownika.
- Baza danych MySQL - do przechowywania danych dotyczących działek, roślin, nawozów i planów nawożenia.
- Git - system kontroli wersji.
## Instalacja i Uruchomienie
- Sklonuj repozytorium na swój komputer.
- Zainstaluj wymagane zależności, korzystając z menedżera pakietów dla Pythona (np. pip).
- Uruchom django za pomocą komendy **djangoenv/Scripts/activate**
- przejdź do folderu farm_helper za pomocą komendy **cd farm_helper**
- Uruchom serwer deweloperski, wpisując **python manage.py runserver**.
- Otwórz przeglądarkę internetową i przejdź do adresu http://localhost:8000 aby korzystać z aplikacji.
## Podsumowanie
"Aplikacja Wspomagania Wyboru Optymalnych Produktów Rolnych" ma na celu wspieranie rolników w podejmowaniu decyzji dotyczących wyboru optymalnych roślin i planów nawożenia na ich działkach. Dzięki funkcjom generowania przyszłych cen roślin, obliczania przewidywanego zysku plonu, przeglądu optymalnego zasiewu klasy i przewidywanego plonu, a także możliwości dodawania własnych danych, aplikacja dostarcza narzędzia, które pomagają rolnikom w podejmowaniu mądrych decyzji dotyczących produkcji rolnej.
