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



st.title("Interfaces Multimodales")
st.subheader("CONTROL POR VOZ")
image = Image.open('voice_ctrl.jpg')
st.image(image, width=200)

icon("💅")
"# Colored text"
st.caption("[Code for this demo](https://github.com/streamlit/release-demos/blob/master/1.16.0/colored-text/streamlit_app.py)")
"[Release 1.16.0](https://docs.streamlit.io/library/changelog#version-1160) of Streamlit adds support for colored text in all commands that support markdown! :tada:"

"### Usage"

st.code("st.markdown(':color[text to be colored]')")

"Make sure to replace `color` with one of the..."

"### Supported colors"

"""
- :blue[blue]
- :green[green]
- :red[red]
- :violet[violet]
- :orange[orange]
"""

"### Examples"

with st.echo():
    st.markdown(
        "Text can be :blue[blue], but also :orange[orange]. And of course it can be :red[red]. And :green[green]. And look at this :violet[violet]!"
    )

"---"
with st.echo():
    st.subheader("This also works in :blue[titles and headers]")
"---"
with st.echo():
    st.slider("And in :red[widget labels] 🎈")
"---"
with st.echo():
    st.write("Combining **bold and :green[colored text] is totally** fine! Just like with other markdown features.")


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
