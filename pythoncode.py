import streamlit as st
import google.generativeai as genai
# from IPython.display import display,Markdown

genai.configure(api_key="AIzaSyC9O8RpUku4cKmsO-JC_kBWuDBVBv4rxYc")
gemini = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")

st.title("Artificial Intelligence Code Reviewer")
st.write("Enter your python code to be reviewed:")

code = st.text_area("Code", height=300)

if st.button('Get Code Review'):
  if code.strip():
    user_prompt = f"Review the above code and provide feedback ${code}"

    try:
      response=gemini.generate_content(user_prompt)
      st.markdown(response.text)

    except Exception as e:
      st.error(f"An error occurred: {e}")

  else:
    st.warning("Please enter some code to review.")