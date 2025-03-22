import streamlit as st
import google.generativeai as genai
import os
import random

# Configure Google Generative AI API
genai.configure(api_key=os.environ.get("GOOGLE_GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro")

# Platform Features and Logos
platform_features = {
    "Instagram": ["Username Generator", "Hashtag Generator", "Caption Generator"],
    "YouTube": ["Channel Name Generator", "Video Title Generator", "Channel Tagline Generator",
                "Video Description Generator", "Username Generator", "Hashtag Generator"],
    "Facebook": ["Post Caption Generator", "Event Tagline Generator", "Hashtag Generator",
                 "Username Generator"],
    "LinkedIn": ["Professional Post Generator", "Profile Headline Generator", "Hashtag Generator"],
    "TikTok": ["Video Title", "Hashtag Generator"],
    "Telegram": ["Channel Name", "Tagline Generator", "Post Content Generator"],
    "Snapchat": ["Username", "Story", "Title Generator"]
}

platform_logos = {
    "YouTube": "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
    "Instagram": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/225px-Instagram_logo_2022.svg.png",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg",
    "TikTok": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/TikTok_logo.svg/330px-TikTok_logo.svg.png",
    "Telegram": "https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg",
    "Snapchat": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Snapchat_logo.svg/150px-Snapchat_logo.svg.png"
}

def generate_content(model, topic, platform, feature):
    prompt = f"Generate {feature} content for {platform} about {topic}. Make it engaging and platform-appropriate."
    
    try:
        response = model.generate_content(prompt)
        return response.text if response else "No content generated."
    except Exception as e:
        return f"Error generating content: {str(e)}"

def main():
    # Page config
    st.set_page_config(
        page_title="AuraSocial AI",
        page_icon="🌙",
        layout="wide",
    )

    # Theme Selection
    col_title, col_theme = st.columns([4, 1])

    with col_title:
        st.markdown("<h1 style='text-align: center; color: red;'>AuraSocial AI</h1>", unsafe_allow_html=True)
    
    with col_theme:
        theme = st.radio("Select Theme", ["Dark", "Light"], key="theme_selector")
        st.session_state.theme = 'dark-mode' if theme == "Dark" else 'light-mode'

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Platform and Feature Selection
    col1, col2 = st.columns(2)
    with col1:
        selected_platform = st.selectbox("Select a Social Media Platform", list(platform_features.keys()))
    with col2:
        selected_feature = st.selectbox("Select a Feature", platform_features[selected_platform])

    # Display Logo
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{platform_logos[selected_platform]}" alt="{selected_platform} Logo" width="150">
        </div>
    """, unsafe_allow_html=True)

    # User input
    topic = st.text_input("Enter your topic or keyword", placeholder="Enter topic here...")

    # Generate button
    if st.button("Generate Content"):
        if topic:
            with st.spinner("Generating content..."):
                response = generate_content(model, topic, selected_platform, selected_feature)
                st.success("Generated Content:")
                st.write(response)
        else:
            st.error("Please enter a topic to generate content!")

    st.sidebar.markdown("""
        <div style="padding: 15px; background-color: rgba(0, 0, 0, 0.1); border-radius: 8px; 
                    border: 1px solid #00bcd4; box-shadow: 0px 6px 8px rgba(0, 188, 212, 0.3);">
            <div style="text-align: center; font-size: 18px; color: #00bcd4; margin-bottom: 5px;">
                AuraSocial AI
            </div>
            <div style="text-align: center; font-size: 14px; color: #333;">
                🚀 AuraSocial AI helps you easily create personalized social media content for platforms like 
                YouTube, Instagram, and LinkedIn. 💡 Quickly generate captions, hashtags, and more with AI-powered assistance! 🌟
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
