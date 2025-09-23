from flask import Flask, request, jsonify
def webhook():
    data = request.get_json()
    user_query = data['queryText'].lower()
    print(f"Webhook was triggered! User asked: {user_query}")

    # 1. Pre-load your PDF text (do this ONCE at the top of your app instead, but for now, here's a quick fix)
    pdf_text = read_pdf_text("college_faqs.pdf")  # Make sure the PDF filename is correct

    # 2. Simple, fast keyword matching for common questions
    if 'fee' in user_query and ('deadline' in user_query or 'date' in user_query):
        answer = "The fee submission deadline is September 30, 2025."
    elif 'scholarship' in user_query:
        answer = "Scholarship forms are available on the student portal from October 15th."
    elif 'attendance' in user_query and 'low' in user_query:
        answer = "Students must maintain 75% attendance. Please contact your department head for condonation if below."

    # 3. If it's a complex question, search the PDF text
    else:
        # Find the first sentence in the PDF that contains any keyword from the query
        words = [word for word in user_query.split() if len(word) > 3]  # Ignore small words
        for word in words:
            # Look for a sentence containing the word
            import re
            pattern = fr"[^.!?]*{word}[^.!?]*[.!?]"
            match = re.search(pattern, pdf_text, re.IGNORECASE)
            if match:
                answer = f"I found this information: {match.group(0)}"
                break
        else:
            # If no match was found in the PDF, fall back to this
            answer = "I couldn't find a specific answer in the documents. Please contact the admin office for detailed help."

    # Send the response
    response = {
        "fulfillmentResponse": {
            "messages": [{"text": {"text": [answer]}}]
        }
    }
    return jsonify(response)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook was called!")  # This will prove the connection works
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
    app.run(debug=True, port=5000)