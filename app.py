from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    print("🔔 Webhook recebido:")
    print(data)

    if data and 'type' in data and data['type'] == 'subscription':
        print("✅ DEU CERTO - Assinatura recebida!")
    else:
        print("⚠️ Evento recebido, mas não é de assinatura.")

    return jsonify({"status": "received"}), 200

@app.route('/')
def home():
    return "Servidor ativo. Endpoint de webhook: /webhook", 200
