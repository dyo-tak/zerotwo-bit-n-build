import streamlit as st



st.title("Major factors affecting grades")


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/z4.png")
    with col2:
        st.subheader("Student's mother job")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/z1.png")
    with col2:
        st.subheader("Correlation of other factors")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/z5.png")
    with col2:
        st.subheader("Father's mother job")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/z2.png")
    with col2:
        st.subheader("Studytime")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/z3.png")
    with col2:
        st.subheader("Grade frequency")


