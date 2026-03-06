import streamlit as st
import time
from rag import RAG
import config_data as config




st.title("RAG QA")
st.divider()

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant","content":"你好，我是你的助手，有什么可以帮你的吗？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RAG()

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("请输入问题")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role":"user","content":prompt})
    
    ai_res_list = []
    with st.spinner("Thinking..."):
        res_stream = st.session_state["rag"].chain.stream(input={"question":prompt},config=config.session_config)
        

        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write(res_stream)
        st.session_state["messages"].append({"role":"assistant","content":"".join(ai_res_list)})

