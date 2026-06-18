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
