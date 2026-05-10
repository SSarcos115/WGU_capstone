import joblib

from utils.predict_aquarium_setup import predict_aquarium_setup
from utils.recommend_habitat import recommend_habitat
from utils.excel_loader import species_df, pair_df

import streamlit as st
import base64

st.set_page_config(
    page_title="Aquarium Compatibility Application",
    layout="wide"
)

def set_background(image_file):

    with open("images/aquarium_background.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    background_css = f"""
    <style>

    .stApp {{
        background-image: linear-gradient(
            rgba(0, 0, 0, 0.05),
            rgba(0, 0, 0, 0.05)
        ),
        url("data:image/png;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    html, body, [class*="css"] {{
        color: white;
    }}

    </style>
    """

    st.markdown(background_css, unsafe_allow_html=True)

set_background("images/aquarium_background.png")

st.title("Aquarium Compatibility Application")

st.write(
    "Select fish species to evaluate compatibility."
)

species_list = species_df()
fish_pair = pair_df()
model = joblib.load("models/compatibility_model.pkl")

fish_options = species_list["Species"].dropna().sort_values().tolist()

selected_fish = st.multiselect(
    "Select fish:",
    fish_options
)

if st.button("Analyze"):
    if len(selected_fish) < 2:
        st.warning("Please select at least two fish.")
    else:
        st.subheader("Selected Fish")
        st.write(selected_fish)

        st.subheader("Habitat Recommendation")
        habitat_result = recommend_habitat(selected_fish, species_list)
        st.write(habitat_result)

        st.subheader("Data Dictionary")

        with st.expander("View Data Dictionary"):
            st.markdown("""
    
            ### Same Water Type
            - 1 = Both fish are freshwater or both are saltwater
            - 0 = One freshwater and one saltwater
    
            ---
    
            ### Temperature Overlap Ratio
            0 to 1. Higher values mean the fish share more of the same temperature range.
    
            ---
    
            ### pH Overlap Ratio
            0 to 1. Higher values mean the fish share more of the same pH range.
    
            ---
    
            ### Salinity Overlap Ratio
            0 to 1 for saltwater fish. Freshwater pairs use 1 if both are freshwater.
    
            ---
    
            ### Tank Requirement Similarity
            0 to 1. Higher values mean the two fish have similar minimum tank-size requirements.
    
            ---
    
            ### Adult Size Ratio
            Larger adult size divided by smaller adult size.
    
            ---
    
            ### Predation Size Risk
            - 1 = One fish may eat or injure the other due to size/diet/temperament
            - 0 = Lower risk
    
            ---
    
            ### Temperament Risk
            - 1 = Aggression or semi-aggression risk is present
            - 0 = Lower risk
    
            ---
    
            ### Diet/Predation Risk
            - 1 = Diet and/or size suggests a predation concern
            - 0 = Lower risk
    
            ---
    
            ### Water Level Compatibility
            - 1 = Compatible or different tank zones
            - 0.5 = Same swimming zone but not automatically incompatible
    
            ---
    
            ### Schooling Conflict
            - 1 = Schooling species paired with an aggression risk
            - 0 = No direct schooling conflict
    
            ---
    
            ### Reef Safety Conflict
            Saltwater only.
            - 1 = At least one fish may be unsafe for reef/invertebrate setups
    
            ---
    
            ### Same Group Aggression Conflict
            - 1 = Same group and aggression risk may exist
            - 0 = No such group conflict
    
            ---
    
            ### Compatibility Label Code
            - 2 = Compatible
            - 1 = Use Caution
            - 0 = Not Compatible
    
            ---
    
            ### Compatibility Prediction
            Final machine learning classification result:
            - Compatible
            - Use Caution
            - Not Compatible
    
            """)

        st.subheader("Compatibility Results")
        compatibility_result = predict_aquarium_setup(
            selected_fish,
            species_list,
            fish_pair
        )
        st.dataframe(compatibility_result)

        st.subheader("Compatibility Explanations")

        for index, row in compatibility_result.iterrows():
            fish_a = row["Fish A"]
            fish_b = row["Fish B"]
            result = row["Compatibility Label"]
            reason = row["Reason"]

            with st.expander(f"{fish_a} + {fish_b}: {result}"):
                st.write(reason)

st.divider()

st.subheader("Model Documentation Graphs")

left, center, right = st.columns([1, 3, 1])

with center:
    st.image("graphs/compatibility_score_distribution.png", width=700)
    st.image("graphs/feature_importance.png", width=700)
    st.image("graphs/confusion_matrix.png", width=700)