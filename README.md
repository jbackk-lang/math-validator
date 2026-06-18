# math-validator
Walidator równań matematycznych z detekcją osobliwości, skrętu i ukrytych defektów.

`math-validator` analizuje wyrażenia symboliczne i klasyfikuje je według trzech kategorii:

- twist_detected — osobliwość typu Möbiusa (różne limity jednostronne, 0⁺ ≠ 0⁻)
- hidden_singularity — ukryta osobliwość usunięta algebraicznie (np. (x+1)/(x+1))
- clean — brak osobliwości, ρ = 0

Silnik oparty jest na jednym parsowaniu (ParsedExpr), cache LRU i lekkich filtrach Λ–τ–ρ.

## Funkcje
- Jedno parsowanie — sympify() wywoływane tylko raz
- Detekcja skrętu (twist) — porównanie limitów jednostronnych
- Detekcja ukrytych osobliwości — analiza struktury po uproszczeniu
- Analiza topologiczna Λ–τ–ρ:
  - Λ — struktura wyrażenia
  - τ — transformacje i znaki
  - ρ — defekt (osobliwość)
- Cache LRU — powtarzane wyrażenia zwracane w 1–3 ms
- Spójna architektura — jeden validate(), jeden parse(), słownik filtrów

## Szybki start
from validator import validate

print(validate("1/x"))
# → {'status': 'twist_detected', 'point': 0}

print(validate("(x+1)/(x+1)"))
# → {'status': 'hidden_singularity', 'point': -1}

print(validate("

# Architecture Overview

## Rdzeń: core.py i ParsedExpr
Silnik wykonuje tylko jedno parsowanie wejściowego wyrażenia.
Funkcja parse() zwraca obiekt ParsedExpr, który zawiera:

- expr            — obiekt SymPy po sympify()
- is_zoo          — czy wyrażenie redukuje się do zoo (np. 1/(x-x))
- is_const        — czy wyrażenie jest stałe
- has_division    — czy zawiera dzielenie
- cycles          — liczba pętli (liczona po strukturze)
- fractions       — lista ułamków znalezionych w drzewie
- powers          — lista potęg (w tym ułamkowych)

ParsedExpr jest przekazywany do wszystkich filtrów.
Żaden filtr nie wykonuje własnego parsowania.

## Filtry
Każdy filtr przyjmuje ParsedExpr i zwraca wynik częściowy.
Filtry są zarejestrowane w słowniku w validator.py.

### singularity_filter
- wykrywa osobliwości jawne i ukryte
- używa singularities() z SymPy
- porównuje limity jednostronne: limit(f, x, s, '+') vs limit(f, x, s, '-')
- posiada @lru_cache(maxsize=256) — powtarzane wyrażenia zwracane w 1–3 ms

Zwraca:
- twist_detected
- hidden_singularity
- clean

### topology_filter (Λ–τ–ρ)
- Λ: odczyt struktury z ParsedExpr (zero kosztu)
- τ: analiza znaków i transformacji
- ρ: delegacja do singularity_filter (wykrycie defektu)

Zwraca:
- status topologiczny (twist / hidden / clean)
- punkt osobliwości (jeśli istnieje)

## validator.py
Jedna funkcja validate(expr):

1. parse(expr) → ParsedExpr
2. uruchomienie filtrów w kolejności
3. scalanie wyników w jeden słownik

Brak podwójnych definicji, brak wielokrotnego parsowania.

## Przepływ danych
input string
    ↓
parse() → ParsedExpr
    ↓
singularity_filter
    ↓
topology_filter
    ↓
validate() → wynik końcowy
