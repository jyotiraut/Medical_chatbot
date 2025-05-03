import streamlit as st 

def main():
    st.title("Ask Chatbot")


    prompt = st.chat_input("Enter your prompt here!")


    if prompt:
        st.chat_message('user').markdown(prompt)
        response = "hi! I am jyoti bot.."
        st.chat_message('assistant').markdown(response)

if __name__=="__main__":
    main()