import streamlit as st
from streamlit_chat import message
import openai
import os

openai.api_key = ("OPEN_API_KEY")

def openai_create(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.1,
        stop=[" Human:", " ChatGPT:"]
    )

    return response.choices[0].text

def chatgpt_clone(input_, history=None):
    history = history or []
    history.append(input_)
    inp = ' '.join(history)
    output = openai_create(inp)
    return output

st.set_page_config(
    page_title="ChatGPT No Limit Mode",
    page_icon=":robot:"
)

st.header("ChatGPT No Limit Mode")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Human: ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = chatgpt_clone(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
