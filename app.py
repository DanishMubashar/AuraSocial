import streamlit as st
from groq import Groq
import os
import random

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# Platform Features and Logos
platform_features = {
        "Instagram": [
        "Username Generator", "Hashtag Generator", "Caption Generator"
    ],
    "YouTube": [
        "Channel Name Generator", "Video Title Generator", "Channel Tagline Generator",
        "Video Description Generator", "Username Generator", "Hashtag Generator"
    ],

    "Facebook": [
        "Post Caption Generator", "Event Tagline Generator", "Hashtag Generator",
        "Username Generator"
    ],
    "LinkedIn": [
        "Professional Post Generator", "Profile Headline Generator", "Hashtag Generator"
    ],
    "TikTok": [
        "Video Title", "Hashtag Generator"
    ],
    "Telegram": [
        "Channel Name", "Tagline Generator", "Post Content Generator"
    ],
    "Snapchat": [
        "Username", "Story", "Title Generator"
    ]
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





def generate_content(client, topic, platform, feature):
    prompt = f"Generate {feature} content for {platform} about {topic}. Make it engaging and platform-appropriate."
    
    try:
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {"role": "system", "content": "You are a social media content expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating content: {str(e)}"










def set_page_style():
    # Base styles
    base_styles = """
        <style>
            .stSelectbox {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }

            .stButton>button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                margin: 20px 0;
                cursor: pointer;
                width: 100%;
            }

            .stButton>button:hover {
                background-color: #45a049;
            }

            .main-container {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                padding: 20px;
                margin: 20px 0;
            }

            .logo-container {
                text-align: center;
                padding: 20px;
            }

            .logo-container img {
                max-width: 150px;
                height: auto;
            }
        </style>
    """
# Light theme styles with realistic, organic clouds


# Enhanced sky simulation with realistic clouds
    light_theme_styles = """
    <style>
        .stApp {
            background: linear-gradient(180deg, #62B8FF 0%, #87CEEB 50%, #B0E2FF 100%);
            overflow: hidden;
        }

        .sun {
            position: fixed;
            top: 50px;
            right: 100px;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: radial-gradient(circle, #FFE87C 60%, #FFA500);
            box-shadow: 0 0 60px 30px rgba(255, 165, 0, 0.4);
            animation: sun-pulse 3s infinite alternate;
        }

        .cloud {
            position: fixed;
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 50%;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            opacity: 0.3; /* Further reduced opacity */
            filter: blur(0.8px);
        }

        .cloud:before,
        .cloud:after {
            content: '';
            position: absolute;
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            border-radius: 50%;
        }

        .cloud.one {
            width: 120px;
            height: 50px;
        }

        .cloud.one:before {
            width: 70px;
            height: 70px;
            top: -30px;
            left: 15px;
        }

        .cloud.one:after {
            width: 90px;
            height: 90px;
            top: -40px;
            right: 15px;
        }

        .cloud.two {
            width: 100px;
            height: 45px;
        }

        .cloud.two:before {
            width: 60px;
            height: 60px;
            top: -25px;
            left: 10px;
        }

        .cloud.two:after {
            width: 80px;
            height: 80px;
            top: -35px;
            right: 10px;
        }

        .cloud.three {
            width: 90px;
            height: 40px;
        }

        .cloud.three:before {
            width: 50px;
            height: 50px;
            top: -20px;
            left: 8px;
        }

        .cloud.three:after {
            width: 70px;
            height: 70px;
            top: -30px;
            right: 8px;
        }

        @keyframes float {
            0% { transform: translate(0, 0); opacity: 0.4; }
            25% { transform: translate(-10px, 15px); opacity: 0.45; }
            50% { transform: translate(-15px, -10px); opacity: 0.4; }
            75% { transform: translate(5px, 10px); opacity: 0.35; }
            100% { transform: translate(0, 0); opacity: 0.4; }
        }

        @keyframes sun-pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.1); }
        }

        .cloud {
            animation: float 18s ease-in-out infinite;
        }
    </style>

    <div class="sun"></div>
    <div class="cloud one" style="top: 15%; left: 10%; animation-duration: 22s;"></div>
    <div class="cloud two" style="top: 25%; left: 35%; animation-duration: 28s;"></div>
    <div class="cloud three" style="top: 20%; left: 60%; animation-duration: 25s;"></div>
    <div class="cloud one" style="top: 40%; left: 20%; animation-duration: 30s;"></div>
    <div class="cloud two" style="top: 50%; left: 75%; animation-duration: 27s;"></div>
    <div class="cloud three" style="top: 35%; left: 80%; animation-duration: 32s;"></div>
    """

    # Dark theme styles with static, small, twinkling stars, and a randomly falling star
    dark_theme_styles = """
        <style>
            .stApp {
                background-color: #00122b;
                color: white;
            }

            .moon {
                position: fixed;
                top: 10%;
                right: 15%;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                background: radial-gradient(circle, #f7e7a6, #fcd303);
                box-shadow: 0 0 20px 8px rgba(255, 211, 3, 0.5);
                animation: moon-glow 6s infinite alternate;
            }

            /* Static stars with twinkle effect */
            .star {
                position: fixed;
                border-radius: 50%;
                animation: twinkle 1.5s infinite alternate; /* Slow twinkle effect */
            }

            /* Star size */
            .star.small {
                width: 3px;
                height: 3px;
            }

            /* Twinkling effect */
            @keyframes twinkle {
                0% { opacity: 0.4; }
                100% { opacity: 1; }
            }

            /* Falling star with random path and exit points */
            .falling-star {
                position: fixed;
                width: 5px;
                height: 5px;
                border-radius: 50%;
                background: #ffd700; /* Golden color for falling star */
                animation: fall 6s infinite linear, twinkle 1.5s infinite alternate;
                animation-delay: 0s;
            }

            /* Random fall path */
            @keyframes fall {
                0% {
                    top: -10%; 
                    left: calc(50% - 2.5px); /* Start position */
                    transform: translateX(0);
                }
                100% {
                    top: 100%;
                    left: calc(50% + random(-150,150)px); /* Random horizontal end point */
                    transform: translateX(calc(random(-50,50)%)); /* random movement along path */
                }
            }

            @keyframes moon-glow {
                0% { box-shadow: 0 0 20px 8px rgba(255, 211, 3, 0.3); }
                100% { box-shadow: 0 0 30px 12px rgba(255, 211, 3, 0.6); }
            }
        </style>
        
        <div class="moon"></div>
        
        <!-- Randomly falling star -->
        <div class="falling-star" style="animation-delay: {random.randint(0,5)}s;"></div>

        <!-- Random static stars -->
        """ + "".join([
                f'<div class="star small" style="top: {random.randint(5,95)}%; left: {random.randint(5,95)}%; '
                f'background: {"#ffd700" if random.random() > 0.5 else "#ffffff"};"></div>'
            for _ in range(50)
        ])




 


    st.markdown(base_styles, unsafe_allow_html=True)
    if st.session_state.get('theme') == 'dark-mode':
        st.markdown(dark_theme_styles, unsafe_allow_html=True)

    else:
        st.markdown(light_theme_styles, unsafe_allow_html=True)
def main():
    # Page config
    st.set_page_config(
        page_title="AuraSocial AI",
        page_icon="🌙",
        layout="wide",
    )

    # Theme Selection moved to top right
    col_title, col_theme = st.columns([4, 1])
    
    with col_title:
        # Display title with dynamic color based on theme
        st.markdown("""
        <h1 style='text-align: center; color:red ;'>
        AuraSocial AI
        </h1>
        """, unsafe_allow_html=True)
    
    with col_theme:
        theme = st.radio("Select Theme", ["Dark", "Light"], key="theme_selector")
        st.session_state.theme = 'dark-mode' if theme == "Dark" else 'light-mode'

    # Adding space
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Platform and Feature Selection in main area
    col1, col2 = st.columns(2)
    with col1:
        selected_platform = st.selectbox("Select a Social Media Platform", list(platform_features.keys()))
    with col2:
        selected_feature = st.selectbox("Select a Feature", platform_features[selected_platform])

    # Display Logo
    st.markdown(f"""
        <div class="logo-container">
            <img src="{platform_logos[selected_platform]}" alt="{selected_platform} Logo">
        </div>
    """, unsafe_allow_html=True)

    # User input
    topic = st.text_input("Enter your topic or keyword", placeholder="Enter topic here...")

    # Generate button
    if st.button("Generate Content"):
        if topic:
            with st.spinner("Generating content..."):
                response = generate_content(client, topic, selected_platform, selected_feature)
                st.success("Generated Content:")
                st.write(response)
        else:
            st.error("Please enter a topic to generate content!")

    st.markdown('</div>', unsafe_allow_html=True)

    # Keep the sidebar content
    with st.sidebar:
        # Description
        st.markdown("""
            <style>
                .cyber-container {
                    padding: 15px;
                    background-color: rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    border: 1px solid #00bcd4;
                    margin: 10px;
                    box-shadow: 0px 6px 8px rgba(0, 188, 212, 0.3);
                }
                .cyber-name {
                    text-align: center;
                    font-size: 18px;
                    color: #00bcd4;
                    margin-bottom: 5px;
                    font-family: 'Roboto', sans-serif;
                }
                .cyber-description {
                    text-align: center;
                    font-size: 14px;
                    color: #333333;
                    font-family: 'Roboto', sans-serif;
                    margin-top: 0;
                }
            </style>
            <div class="cyber-container">
                <div class="cyber-name">AuraSocial AI</div>
                <div class="cyber-description">
                    AuraSocial AI 🚀 is an AI-powered tool that helps you easily create personalized social media content 📱 for platforms like YouTube, Instagram, and LinkedIn. 💡 It has an easy-to-use design and allows you to customize posts, captions, and hashtags quickly ⏳, making content creation fast and simple for personal or business use. 🌟
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Personal info section
        st.markdown("""
            <style>
                .cyber-container {
                    padding: 15px;
                    background-color: rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    border: 1px solid #00bcd4;
                    margin: 10px;
                    box-shadow: 0px 6px 8px rgba(0, 188, 212, 0.3);
                }
                .cyber-name {
                    text-align: center;
                    font-size: 18px;
                    color: #00bcd4;
                    margin-bottom: 10px;
                    font-family: 'Roboto', sans-serif;
                }
                .cyber-links {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                }
                .cyber-button {
                    text-decoration: none;
                    padding: 8px;
                    border-radius: 5px;
                    text-align: center;
                    font-weight: normal;
                    background-color: #ffffff;
                    color: #333333;
                    border: 1px solid #00bcd4;
                    transition: background-color 0.3s, color 0.3s ease;
                    font-size: 14px;
                }
                .cyber-button:hover {
                    background-color: #00bcd4;
                    color: white;
                }
                
                .linkedin { border-color: #0077b5; }
                .github { border-color: #333; }
                .kaggle { border-color: #20BEFF; }
                .email { border-color: #EA4335; }

                .linkedin:hover { background-color: #0077b5; }
                .github:hover { background-color: #333; }
                .kaggle:hover { background-color: #20BEFF; }
                .email:hover { background-color: #EA4335; }
            </style>
            <div class="cyber-container">
                <div class="cyber-name">Muhammad Danish Mubashar</div>
                <div class="cyber-links">
                    <a href="https://www.linkedin.com/in/muhammad-danish-mubashar-002b912a0/?originalSubdomain=pk" 
                    target="_blank" 
                    class="cyber-button linkedin">LinkedIn</a>
                    <a href="https://github.com/DanishMUbashar" 
                    target="_blank" 
                    class="cyber-button github">GitHub</a>
                    <a href="https://www.kaggle.com/danishmubashar" 
                    target="_blank" 
                    class="cyber-button kaggle">Kaggle</a>
                    <a href="mailto:danishmubashar81@gmail.com" 
                    class="cyber-button email">Email</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <footer style="text-align: center; padding: 20px; color: red;">
        <p>Developed with ❤ by AuraSocial AI</p>
    </footer>
    """, unsafe_allow_html=True)

    # Apply page styling
    # set_page_style()
    st.markdown("""
        <style>
            .footer-icons-container {
                display: flex;
                justify-content: center;
                gap: 10px;  /* Reduced gap between icons */
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                padding: 20px;
            }

            .footer-icon {
                width: 40px;  /* Small circular icons */
                height: 40px;
                border-radius: 50%;
                background-color: transparent;
                transition: transform 0.3s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                animation: sway 3s ease-in-out infinite;
            }

            .footer-icon img {
                width: 60%;
                height: auto;
            }

            @keyframes sway {
                0%, 100% { transform: translateX(0); }
                50% { transform: translateX(-10px); } /* Slight sway to the left */
            }

            .footer-icon:hover {
                transform: scale(1.1) translateY(-5px);
            }
        </style>

        <div class="footer-icons-container">
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" alt="YouTube">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/225px-Instagram_logo_2022.svg.png" alt="Instagram">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/TikTok_logo.svg/330px-TikTok_logo.svg.png" alt="TikTok">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram">
            </div>
            <div class="footer-icon">
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/c/c4/Snapchat_logo.svg/150px-Snapchat_logo.svg.png" alt="Snapchat">
            </div>
        </div>
    """, unsafe_allow_html=True)


    # Apply page styling
    set_page_style()

if __name__ == "__main__":
    main()

