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

pip install -r requirements.txt
uvicorn api:app --reload

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

