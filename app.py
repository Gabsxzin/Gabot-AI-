from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    mensagem = request.json["mensagem"]

    try:
        resposta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": mensagem,
                "stream": False
            }
        )

        texto = resposta.json()["response"]

        return jsonify({
            "resposta": texto
        })

    except Exception as e:
        return jsonify({
            "resposta": f"Erro: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)