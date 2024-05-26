import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from llama2 model
def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    template = f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words"
    
    # Simplified the template creation
    response = llm(template)
    print(response)
    return response

# Setting the page config

st.set_page_config(page_title="Generate Blogs",
                   page_icon="a",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate blogs")
input_text = st.text_input("Enter the blog topic:")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('Number of words')
with col2:
    blog_style = st.selectbox("Writing blog for", ('Researchers', 'Data Scientists', 'Machine learning Engineer', 'Common people'), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
