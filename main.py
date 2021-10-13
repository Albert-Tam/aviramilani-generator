import streamlit as st
import requests

API_URL = "https://aviramilani-server.herokuapp.com/"


def title_taglines(company_name, company_description):
    my_data = {"name": company_name,
               "description": company_description}
    response = requests.post(API_URL + "title-tagline", json=my_data).json()
    return response["titles-taglines"]


def feature_titles(company_name, company_description, feature_description):
    my_data = {"name": company_name,
               "description": company_description,
               "feature": feature_description}
    response = requests.post(API_URL + "feature-title", json=my_data).json()
    return response["feature-titles"]


def feature_subtitles(company_name, company_description, feature_description, feature_title):
    my_data = {"name": company_name,
               "description": company_description,
               "feature": feature_description,
               "feature-title": feature_title
               }
    response = requests.post(API_URL + "feature-subtitle", json=my_data).json()
    return response["feature-subtitles"]


st.title("Landing Page Generator")
st.markdown("""### Transform descriptions into landing pages with the power of AI.""")

with st.form(key='title-tagline-form'):
    name = st.text_input(label="Company/Product Name")
    description = st.text_area(label="Product/Service Description")
    feature1 = st.text_area(label="Feature/Benefit 1")
    feature2 = st.text_area(label="Feature/Benefit 2")
    feature3 = st.text_area(label="Feature/Benefit 3")
    submit = st.form_submit_button(label='Submit')
    if submit:
        try:
            title_tagline = title_taglines(name, description)
            title0 = title_tagline["0"]["title"]
            title1 = title_tagline["1"]["title"]
            title2 = title_tagline["2"]["title"]
            title3 = title_tagline["3"]["title"]
            title4 = title_tagline["4"]["title"]

            tagline0 = title_tagline["0"]["tagline"]
            tagline1 = title_tagline["1"]["tagline"]
            tagline2 = title_tagline["2"]["tagline"]
            tagline3 = title_tagline["3"]["tagline"]
            tagline4 = title_tagline["4"]["tagline"]

            st.radio('Titles', [title0, title1, title2, title3, title4])
            st.radio('Taglines', [tagline0, tagline1, tagline2, tagline3, tagline4])

            if feature1:
                feature_title1 = feature_titles(name, description, feature1)
                st.radio('Feature 1 Title', feature_title1)
            if feature2:
                feature_title2 = feature_titles(name, description, feature2)
                st.radio('Feature 2 Title', feature_title2)
            if feature3:
                feature_title3 = feature_titles(name, description, feature3)
                st.radio('Feature 3 Title', feature_title3)

            # subtitle = feature_subtitles(name, description, feature1, chosen_title)
            # st.markdown(subtitle)

        except Exception as e:
            st.error(e)


with st.form(key='feature-subtitle'):
    name = st.text_input(label="Company/Product Name")
    description = st.text_area(label="Product/Service Description")
    feature = st.text_area(label="Feature/Benefit")
    feature_title = st.text_input(label="Feature/Benefit Title")
    submit = st.form_submit_button(label='Submit')
    if submit:
        try:
            subtitle = feature_subtitles(name, description, feature1, feature_title)
            st.radio("Feature Subtitles", subtitle)
        except Exception as e:
            st.error(e)
