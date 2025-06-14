import openai
import streamlit as st

st.set_page_config(page_title="AI Lắng Nghe Em", layout="centered")
st.title("🤖 AI Lắng Nghe Em")
st.write("Một chatbot tâm lý học trò thân thiện dành cho học sinh THCS ❤️")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Bạn là một người bạn thân, biết lắng nghe, tâm lý, luôn an ủi và đồng hành cùng học sinh THCS."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Bạn muốn chia sẻ điều gì hôm nay?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
