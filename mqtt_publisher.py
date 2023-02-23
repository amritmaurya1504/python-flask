import paho.mqtt.client as mqtt
user_data = 45.5

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.publish('topic/test', user_data)
# client.loop_forever()

client.disconnect()