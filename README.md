# math-validator  
Walidator równań matematycznych, który nie tylko sprawdza poprawność zapisu, ale **analizuje strukturę problemu** i wykrywa miejsca, w których logika się łamie.

---

## 🎯 Cel projektu

Celem `math-validator` jest stworzenie narzędzia, które:

- wykrywa błędy w równaniach,
- analizuje strukturę matematyczną,
- wskazuje miejsca niejednoznaczne,
- identyfikuje ukryte sprzeczności,
- radzi sobie z **problemami mylnymi / milejnymi** (podchwytliwymi).

To nie jest zwykły „checker”.  
To **analizator struktury matematycznej**, zgodny z Twoją topologią Λ–τ–ρ.

---

## 🧠 Dlaczego ten walidator jest inny

Większość walidatorów:

- sprawdza tylko wynik,
- albo tylko składnię,
- albo tylko zgodność nawiasów.

Ten projekt idzie dalej — analizuje **strukturę problemu**, a nie tylko jego powierzchnię.

### Obsługa problemów mylnych / milejnych

„Problemy mylne” to takie, które:

- wyglądają poprawnie, ale są logicznie sprzeczne,
- mieszają różne notacje,
- mają ukryte założenia,
- są zapisane niejednoznacznie,
- prowadzą do błędnych wniosków mimo poprawnych kroków.

Walidator wykrywa takie miejsca i wskazuje:

- **gdzie** pojawia się błąd strukturalny,
- **dlaczego** równanie nie może być rozwiązane,
- **który element** jest źródłem sprzeczności.

To jest bezpośrednie zastosowanie Twojej zasady:

> *„Najpierw struktura, potem transformacja, na końcu defekt.”*

---

## 🔷 Powiązanie z topologią Λ–τ–ρ

Walidator wykorzystuje analogię:

- **Λ (lambda)** — stabilna część równania (to, co jest poprawne),
- **τ (tau)** — transformacje (kroki przekształceń),
- **ρ (rho)** — defekty (miejsce, gdzie logika się łamie).

Dzięki temu:

- Λ pozwala wykryć poprawne fragmenty,
- τ pozwala analizować ciągłość przekształceń,
- ρ wskazuje błędy, sprzeczności i nieciągłości.

To jest dokładnie ta sama logika, która stoi za filtrem φ.

---

## 🧩 Przykład użycia

```python
from math_validator import validate

expr = "2(x + 3 = 2x - 5"
result = validate(expr)

print(result)
