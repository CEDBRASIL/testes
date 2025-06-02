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
    
    if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

