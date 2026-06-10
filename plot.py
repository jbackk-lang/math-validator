import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

def generate_plot(expr: str):
    try:
        x = sp.symbols('x')
        f = sp.sympify(expr)

        # Tworzymy zakres
        xs = [i / 10 for i in range(-100, 101)]
        ys = [f.subs(x, val) for val in xs]

        # Rysujemy wykres
        plt.figure(figsize=(6, 4))
        plt.plot(xs, ys)
        plt.grid(True)
        plt.title(f"Plot of: {expr}")

        # Zapis do pamięci
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)

        # Kodowanie base64
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")
        return img_base64

    except Exception as e:
        return f"Plot error: {e}"
