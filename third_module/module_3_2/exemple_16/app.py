from flask import Flask, render_template, request, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

# MQTT Configuration
app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'  # Public broker
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False

mqtt_client = Mqtt(app)

# MQTT Topics
topic_temp = "/aula/temperature"
topic_hum = "/aula/huminity"
topic_led = "/aula/led"

temperature = 0.0
humidity = 0.0
led_status = 0


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/realtime')
def realtime():
    global temperature, humidity, led_status
    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "led_status": led_status
    })


@app.route('/publish_message', methods=['POST'])
def publish_message():
    data = request.get_json()
    topic = data.get('topic')
    message = data.get('message')
    mqtt_client.publish(topic, message)
    return jsonify({"status": "message published"})


# --- MQTT Callbacks ---
@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker:", rc)
    mqtt_client.subscribe(topic_temp)
    mqtt_client.subscribe(topic_hum)
    mqtt_client.subscribe(topic_led)


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, msg):
    global temperature, humidity, led_status
    payload = msg.payload.decode()
    print(f"Received on {msg.topic}: {payload}")

    if msg.topic == topic_temp:
        temperature = float(payload)
    elif msg.topic == topic_hum:
        humidity = float(payload)
    elif msg.topic == topic_led:
        led_status = int(payload)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
from flask import Flask, render_template, request, jsonify
from flask_mqtt import Mqtt

app = Flask(__name__)

# MQTT Configuration
app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'  # Public broker
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False

mqtt_client = Mqtt(app)

# MQTT Topics
topic_temp = "/aula/temperature"
topic_hum = "/aula/huminity"
topic_led = "/aula/led"

temperature = 0.0
humidity = 0.0
led_status = 0

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/realtime')
def realtime():
    global temperature, humidity, led_status
    return jsonify({
        "temperature": temperature,
        "humidity": humidity,
        "led_status": led_status
    })

@app.route('/publish_message', methods=['POST'])
def publish_message():
    data = request.get_json()
    topic = data.get('topic')
    message = data.get('message')
    mqtt_client.publish(topic, message)
    return jsonify({"status": "message published"})

# --- MQTT Callbacks ---
@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker:", rc)
    mqtt_client.subscribe(topic_temp)
    mqtt_client.subscribe(topic_hum)
    mqtt_client.subscribe(topic_led)

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, msg):
    global temperature, humidity, led_status
    payload = msg.payload.decode()
    print(f"Received on {msg.topic}: {payload}")
    
    if msg.topic == topic_temp:
        temperature = float(payload)
    elif msg.topic == topic_hum:
        humidity = float(payload)
    elif msg.topic == topic_led:
        led_status = int(payload)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
