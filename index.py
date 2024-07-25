import streamlit as st

# Add an image to the sidebar
st.sidebar.image('atif.jpeg', caption='Muhammad Atif Rehman')
st.sidebar.markdown('''
    <div style="
        max-width: 189px;
    border-radius: 36px;
    margin-left: 46px;
    margin-top: 56px
    ">
    </div>
''', unsafe_allow_html=True)
st.sidebar.markdown('<div style="text-align:center">rehmanatif682@gmail.com</div>', unsafe_allow_html=True)


st.markdown('<div style="text-align:center; font-size:44px; font-family: Garamond">Profile Setting</div>', unsafe_allow_html=True)
st.text_input("First Name", placeholder="hello world")
st.text_input("Last Name")
st.number_input("Mobile No")
st.text_input("Address")
st.number_input("Post Code")
st.text_input("Education")
option = st.selectbox(
    "Select the Country",
    ("America", "Pakistan", "India"))

st.write("You selected:", option)
option2=st.selectbox(
   "Select state",
   ("islamabad","dehli","chicago")
   )
st.write("you select:",option2)
st.button("Submit", type="primary")



