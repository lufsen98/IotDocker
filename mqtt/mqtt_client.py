import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags,rc):
    print("Connected with result code " + str(cr))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_connect = on_message

client.connect("mqtt-broker, {msg.payload.decode()")

