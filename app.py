import streamlit as st

# Title
st.title("🌱 Smart Agri App")
st.subheader("Your digital assistant for smart farming")

# Sidebar navigation
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Crop Suggestion", "About"])

# Home Page
if page == "Home":
    st.write("👋 Welcome to the Smart Agri App!")
    st.write("This app helps farmers with crop suggestions based on soil and weather data.")

# Crop Suggestion Page
elif page == "Crop Suggestion":
    st.header("🌾 Crop Suggestion Tool")

    soil = st.selectbox("Select Soil Type", ["Sandy", "Clay", "Loamy","red ","black "])
    rainfall = st.slider("Annual Rainfall (mm)", 200, 2000, 800)
    temp = st.slider("Average Temperature (°C)", 10, 45, 25)

    if st.button("Suggest Crop"):
        if soil == "Loamy" and 20 <= temp <= 30 and 800 <= rainfall <= 1200:
            st.success("✅ Best Crop: **Rice / Wheat**")
        elif soil == "Sandy" and temp > 30:
            st.success("✅ Best Crop: **Millets / Groundnut**")
        elif soil == "Clay" and rainfall > 1000:
            st.success("✅ Best Crop: **Sugarcane / Jute**")
        else:
            st.warning("⚠️ No exact match, try adjusting values.")

# About Page
elif page == "About":
    st.header("ℹ️ About This App")
    st.write("This project is part of the **Smart India Hackathon**.")
    st.write("Built with ❤️ using Streamlit.")
