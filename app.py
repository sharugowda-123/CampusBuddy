from flask import Flask, request, jsonify

app = Flask(__name__)

# FIXED THE ROUTE AND FUNCTION NAME
@app.route('/webhook', methods=['POST'])
def webhook():
    print('Webhook was called!') # This will prove the connection works
    # FIXED THE RESPONSE JSON (added missing braces)
    response = {
        "fulfillmentResponse": {
            "messages": [{
                "text": {
                    "text": ["This is a test response from your webhook!"]
                }
            }]
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    # FIXED THE PORT ARGUMENT
    app.run(debug=True, port=5000)