from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_resultado(base_calculo, fixos, variavel, reserva, prolabore,
                    das, inss):
    try:
        base_calculo = float(base_calculo)
        fixos = float(fixos)
        variavel = float(variavel)
        reserva = float(reserva) / 100
        prolabore = float(prolabore)
        das = float(das) / 100
        inss = float(inss) / 100
        # aliquota = float(aliquota) / 100
    except ValueError:
        return "Erro: Preencha todos os campos com números"

    custo_total = fixos + variavel
    das = base_calculo * das
    inss = prolabore * inss
    valor_reserva = base_calculo * reserva
    lucro_liquido = base_calculo - custo_total - das - inss - valor_reserva

    return {
        "base_calculo": base_calculo,
        "fixos": fixos,
        "variavel": variavel,
        "reserva": valor_reserva,
        "prolabore": prolabore,
        "das": das,
        "inss": inss,
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
        reserva = request.form.get("reserva")
        prolabore = request.form.get("prolabore")
        das = request.form.get("das")
        inss = request.form.get("inss")

        resultado = calcular_resultado(base_calculo, fixos, variavel, reserva, prolabore, das, inss)
        return render_template("resultado.html", resultado=resultado)

    return render_template("calcular.html")

if __name__ == "__main__":
    app.run(debug=True)