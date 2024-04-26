import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY')  
model = genai.GenerativeModel(model_name="gemini-pro")

def prompt(subject, topic, duration):
    prompt_parts = [
        f"'As an experienced teacher and professor, who loves teaching Craft lesson plans with learning objectives, engaging activities, and assessment strategies for the topic:{topic} in subject:{subject} to teach your students with for the duration:{duration}.'",
    ]
    return prompt_parts

def generate_info_about(topic, subject, duration, prompt=prompt, model=model):
    human_prompt = prompt(subject, topic, duration)
    response = model.generate_content(human_prompt)
    return response.text

st.title("Craft Lesson Plan Generator")

subject = st.text_input("Subject:")
topic = st.text_input("Topic:")
duration = st.text_input("Duration:")

if st.button("Generate Lesson Plan"):
    with st.spinner('Generating...'):
        lesson_plan = generate_info_about(topic, subject, duration)
        st.success(lesson_plan)
