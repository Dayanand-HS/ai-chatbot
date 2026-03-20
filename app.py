import streamlit as st

st.title("AI Skill Gap Advisor 🤖")

mode = st.radio("Mode", ["Concise", "Detailed"])

query = st.text_input("Ask something:")

if query:
    if "python" in query.lower():
        response = "Python is used in AI, data science, and web development."
        source = "📂 Knowledge Base"
    else:
        response = f"Latest info about '{query}' shows growing trends."
        source = "🌐 Web Search"

    if mode == "Detailed":
        response += " This is a detailed explanation with more insights."

    st.write(response)
    st.caption(source)
