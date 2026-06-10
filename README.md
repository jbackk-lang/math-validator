# Math Validator

Uniwersalny walidator równań matematycznych.

Waliduje:
- składnię
- algebrę
- logikę
- topologię (defekty, nieciągłości, osobliwości)
- numerykę (rozwiązania)

## Uruchomienie


## Przykład
Enter equation: x^2 - 4
{
"syntax": "OK",
"algebra": "OK",
"logic": "OK",
"topology": "OK",
"numeric": "Solutions: [-2, 2]"
}

## Po pobraniu

uvicorn api:app --reload

pip install -r requirements.txt


http://127.0.0.1:8000

http://127.0.0.1:8000/docs

wpisz np.   "equation": "sin(x)"

otrzymasz base64 PNG wykres

# Testy Möbiusa (τ – skręt)

# 🧮 Math Validator — Λ–τ–ρ Topological Equation Analyzer

Math Validator to modularny system analizy równań matematycznych oparty na filtrach.
Każdy filtr bada równanie pod innym kątem: składniowym, algebraicznym, logicznym,
numerycznym oraz topologicznym (Λ–τ–ρ).

Projekt jest zbudowany tak, aby można było łatwo dodawać nowe filtry bez modyfikacji API.

---

## 🚀 Funkcje

### ✔ Walidacja równań
Endpoint `/validate` analizuje równanie za pomocą wszystkich dostępnych filtrów:

- **syntax** — poprawność składniowa
- **algebra** — uproszczenia, dziedzina, działania
- **logic** — operatory logiczne
- **numeric** — wartości liczbowe, błędy obliczeń
- **topology (Λ–τ–ρ)** — analiza struktury, transformacji i defektów

---

## 🔷 Filtr topologiczny Λ–τ–ρ

Filtr topologiczny bada równanie w trzech wymiarach:

### **Λ — struktura**
- pętle i cykle (nawiasy)
- hierarchia potęg
- rozgałęzienia (ułamki)
- głębokość zagnieżdżenia

### **τ — transformacje**
- odwrócenia (1/x)
- potęgi ujemne
- pierwiastki
- zmiany orientacji

### **ρ — defekty**
- punkty osobliwe
- asymptoty
- dziury w dziedzinie

---

## 📁 Struktura repozytorium

math-validator/
│
├── api.py   FastAPI backend
├── validator.py   Główny walidator filtrów
├── filters/   Modułowe filtry
│   ├── algebra_filter.py
│   ├── logic_filter.py
│   ├── numeric_filter.py
│   ├── topology_filter.py    Λ–τ–ρ
│   └── ...
│
├── tests/                  Testy jednostkowe i zestawy równań
│   ├── test_basic.py
│   ├── test_algebra.py
│   ├── test_numeric.py
│   └── equations.md
│
└── examples/             Przykładowe równania (opcjonalnie)


---

## 🧪 Testy

W folderze `tests/` znajdują się:

- testy jednostkowe filtrów  
- zestaw równań testowych `equations.md`  
  (równania algebraiczne, trygonometryczne, Möbiusowe i topologiczne)

Przykład z `equations.md`:
(x^2 - 1) / (x - 1)
1/(x-1)
sin(x) + 1/cos(x)
((x^3 - 2x) / (x^2 - 4)) + sqrt(1/(x-1)) - 1/(x+1)

---

## 🔌 API

Po uruchomieniu:

Dokumentacja dostępna jest pod:
http://127.0.0.1:8000/docs

📜 Licencja
MIT — rób z tym, co chcesz.
