from flask import Flask, request, render_template, jsonify
from kafka_producer import send_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_to_kafka():
    data = request.json
    topic = data.get('topic', 'default_topic')
    key = data.get('key', {})  # JSON object
    value = data.get('value', {})  # JSON object
    try:
        send_message(topic, key, value)
        return jsonify({'status': 'Message sent to Kafka!', 'data': data}), 200
    except Exception as e:
        print(f'Error sending message to Kafka: {e}')
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
