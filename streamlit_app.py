import streamlit as st
from streamlit_chat import message

import openai
import os


from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")



# openAI code
def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.3,
    presence_penalty=0.2,
    stop=[" Human:", " TextWizard:"]
    )

    return response.choices[0].text


def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    print(s)
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

# Streamlit App
st.set_page_config(
    page_title="TextWizard BETA",
    page_icon=":robot:"
)

st.header("TextWizard BETA")

history_input = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text 


user_input = get_text()


if user_input:
    output = chatgpt_clone(user_input, history_input)
    history_input.append([user_input, output])
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output[0])
if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        
        from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("path/to/serviceAccountKey.json")
default_app = initialize_app(cred)
db = firestore.client()

# sign up
def sign_up(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print("Successfully created new user: {0}".format(user.uid))
    except Exception as e:
        print(e)

# sign in
def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Successfully signed in as user: {0}".format(user.uid))
    except Exception as e:
        print(e)

# sign out
def sign_out():
    try:
        auth.sign_out()
        print("Successfully signed out.")
    except Exception as e:
        print(e)
