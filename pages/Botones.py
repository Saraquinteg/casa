import streamlit as st
import paho.mqtt.client as paho
import time
import streamlit as st
import json
values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("GIT-HUB2")
client1.on_message = on_message


st.title(":violet[CASA INTELIGENTE DE LA BARBIE]")
st.write("Bienvenida a la Casa Inteligente de Barbie, donde la moda se encuentra con la tecnología en un entorno lleno de estilo"
" y comodidades modernas. Esta casa vanguardista redefine la experiencia de jugar con Barbie, ofreciendo un hogar totalmente conectado y equipado con las últimas innovaciones.")

image = Image.open('voz.png')
st.image('voz.png', width=70)

st.subheader(":violet[PASOS PARA ABRIR LA PUERTA]")
st.write("La entrada principal de la Casa Inteligente de Barbie es una puerta vanguardista que combina elegancia con tecnología de última generación."
" Esta puerta inteligente redefine la experiencia de acceso al hogar, proporcionando a Barbie un acceso fácil y seguro con tan solo un comando de voz.")

st.write(":violet[Paso 1] Presiona el botón que está aquí abajo para encender el micrófono y pronunciar el comando adecuado.")
st.write(":violet[Paso 2] Simplemente pronuncia el comando personalizado: ¡Abrir! y la puerta se desliza suavemente hacia un lado, revelando el mundo lujoso y lleno de comodidades que aguarda en el interior.")
st.write(":violet[Paso 3] Finalmente con comando personalizado: ¡Cerrar!, reversarás la acción .")
st.title(":green[¡Y LISTO!]")


if st.button('ON'):
    act1="HAB_on"
    client1= paho.Client("GIT-HUB2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("house", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF'):
    act1="HAB_off"
    client1= paho.Client("GIT-HUB2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("house", message)
  
    
else:
    st.write('')


