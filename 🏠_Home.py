import streamlit as st
import streamlit as st


def home():
    st.set_page_config(
        page_title="Virtual Health Consultant - Home",
        page_icon="👨‍⚕️",
    )
    st.sidebar.info(
        "**About**: This project is made by Hemraj Prajapati and Aniket Vishwakarma, using publicly available data. We do not store any of the patient's personal information."
    )

    # st.markdown(f"<h1 style='text-align: center; color: blue; font-size: 50px;'>Virtual Health Consultant</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        st.image("assets/logo_rounded.png")

    with col3:
        st.write("")
    # st.image("logo/logo.png")

    st.markdown(
        '<p style="font-size:22px; text-align: center; color: black;font-size: 25px;">Improving Healthcare, Improving Lives, Bridging the gap between technology and health</p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: white; background-color: black;'>About the website</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        f"<p style='text-align: center; color: black; font-size: 20px'>💠 We use state-of-the-art machine learning and deep learning techologies to provide you with your own Virtual Health Consultant</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<p style='text-align: center; color: black; font-size: 20px'>💠 We provide digital health and healthcare solutions to help common people and health organizations power their care experience and improve health outcomes with advanced analytics</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: white; background-color: black;'>Our Services</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown(
        f"⚕️ **Disease Diagnosis** - Enter the symptoms you are suffering from and you will get to know the disease you are suffering from, precautions to take, medications and specialists near you to cure the disease"
    )
    st.markdown(
        f"⚕️ **Early Diabetes Detection** - Enter the patients attributes from the test report and check whether he/she have chances of diabetes or not"
    )

    st.markdown(
        f"⚕️ **Liver Disease Detection** - Enter the patients attributes from the test report and check whether he/she have chances of any type of liver disease or not"
    )

    st.markdown(
        f"⚕️ **Malaria Detection** - Upload the microscopic cell-image of the patient and check whether the patient have chances of malaria"
    )
    st.markdown(
        f"⚕️ **Pneumonia Detection** - Upload the chest X-ray image of the patient and check whether the patient have chances of Pneumonia"
    )

    st.markdown("---")


if __name__ == "__main__":
    home()
