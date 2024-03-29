import streamlit as st
from PIL import Image
from home_page_content import show_home_page_content
from remedy_page_content import show_remedy_page_content 
from prediction import predict_page
from about_disorders import about_disorders

# Streamlit web app
def main():
    # Set the title of the web app
    pages = ['Home', 'Predict', 'Know Little More', 'About Disorders']  # Add 'Remedy' page
    page = st.sidebar.selectbox('Select a page', pages)

    if page == 'Home':
        image_path = "C:/userspace/daya/python/proj/web_page/LOGO.jpeg"
        circle_style = """
        <style>
        img {
            border-radius: 10%;
        }
        </style>
        """

        # Display circular image using st.markdown() with the defined CSS
        st.markdown(circle_style, unsafe_allow_html=True)
        st.image(image_path, use_column_width=True)

        st.markdown(show_home_page_content(), unsafe_allow_html=True) # Use unsafe_allow_html=True
    elif page == 'Predict':
        predict_page()
    elif page == 'Know Little More':
        st.markdown(show_remedy_page_content(), unsafe_allow_html=True)
    elif page == 'About Disorders':
        st.markdown(about_disorders(), unsafe_allow_html=True)

# Run the Streamlit web app
if __name__ == '__main__':
    main()
