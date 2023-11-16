import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob
import paho.mqtt.client as paho
import json
from gtts import gTTS
from googletrans import Translator

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
client1= paho.Client("casa")
client1.on_message = on_message

image = Image.background('voice_ctrl.jpg')
st.image(image, width=500)

st.title(":violet[CASA INTELIGENTE DE LA BARBIE]")
st.write("Bienvenida a la Casa Inteligente de Barbie, donde la moda se encuentra con la tecnología en un entorno lleno de estilo"
"y comodidades modernas. Esta casa vanguardista redefine la experiencia de jugar con Barbie, ofreciendo un hogar totalmente conectado y equipado con las últimas innovaciones.")

st.subheader(":violet[UTILIDAD 1]")
st.write("La entrada principal de la Casa Inteligente de Barbie es una puerta vanguardista que combina elegancia con tecnología de última generación."
"Esta puerta inteligente redefine la experiencia de acceso al hogar, proporcionando a Barbie un acceso fácil y seguro con tan solo un comando de voz.")

st.subheader(":violet[Paso 1]")
st.write("simplemente pronuncia un comando personalizado, como ¡Abrir! y la puerta se desliza suavemente hacia un lado, revelando el mundo lujoso y lleno de comodidades que aguarda en el interior.")

image = Image.open('voice_ctrl.jpg')
st.image(image, width=200)

st.write("Toca el Botón y habla ")
stt_button = Button(label=" Inicio ", width=200)


stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))
        client1.on_publish = on_publish                            
        client1.connect(broker,port)  
        message =json.dumps({"Act1":result.get("GET_TEXT").strip()})
        ret= client1.publish("house", message)

    
    try:
        os.mkdir("temp")
    except:
        pass
