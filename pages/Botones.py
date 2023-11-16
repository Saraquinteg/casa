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

image = Image.open('boton.png')
st.image('voz.png', width=70)

st.subheader(":violet[PASOS PARA ENCEDER LA LUZ]")
st.write("
¡Presentamos la increíble Luz Inteligente para la Casa de Barbie, la adición perfecta para iluminar y realzar la experiencia en el hogar de la muñeca más famosa del mundo."
"Esta innovadora luz combina la magia del diseño y la tecnología para brindar un toque moderno y elegante a cada rincón de la casa de Barbie.")

st.write(":violet[Paso 1] Presiona el botón que está aquí "ON" para encender la luz.")
st.write(":violet[Paso 1] Presiona el botón que está aquí "Off" para apagar la luz.")
st.title(":orange[¡Y LISTO!]")


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


