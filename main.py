from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_resultado(base_calculo, fixos, variavel, aliquota, reserva):
    try:
        base_calculo = float(base_calculo)
        fixos = float(fixos)
        variavel = float(variavel)
        aliquota = float(aliquota) / 100
        reserva = float(reserva) / 100
    except ValueError:
        return "Erro: Preencha todos os campos com números"

    custo_total = fixos + variavel
    imposto = base_calculo * aliquota
    valor_reserva = base_calculo * reserva
    lucro_liquido = base_calculo - custo_total - imposto - valor_reserva

    return {
        "base_calculo": base_calculo,
        "fixos": fixos,
        "variavel": variavel,
        "imposto": imposto,
        "reserva": valor_reserva,
        "liquido": lucro_liquido
    }

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        base_calculo = request.form.get("base_calculo")
        fixos = request.form.get("fixos")
        variavel = request.form.get("variavel")
        aliquota = request.form.get("aliquota")
        reserva = request.form.get("reserva")

        resultado = calcular_resultado(base_calculo, fixos, variavel, aliquota,
                                    reserva)
        return render_template("resultado.html", resultado=resultado)

    return render_template("calcular.html")

if __name__ == "__main__":
    app.run(debug=True)