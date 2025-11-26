import streamlit as st

st.set_page_config(
    page_title="FitnessPro AI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .hero-text {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<h1 class="hero-text">💪 FitnessPro AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Personal AI Fitness & Nutrition Coach</p>', unsafe_allow_html=True)

st.markdown("---")

# Feature Highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🏋️ Smart Workouts</h3>
        <p>AI-powered workout plans tailored to your goals, schedule, and fitness level</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🍽️ Indian Meal Plans</h3>
        <p>Delicious, nutritious Indian meals designed for your dietary preferences</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Track Progress</h3>
        <p>Monitor your daily achievements and stay motivated throughout your journey</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# How it works
st.markdown("### 🎯 How It Works")
st.markdown("""
1. **Share Your Goals** - Tell us about your fitness objectives and preferences
2. **Get Your Plan** - Receive a personalized 7-day workout and meal plan
3. **Track Daily** - Check off completed workouts and meals
4. **Stay Consistent** - Build healthy habits that last
""")

st.markdown("---")

# CTA Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start Your Fitness Journey", key="start_btn"):
        st.switch_page("pages/1_Onboarding.py")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Powered by CrewAI | Built with ❤️ for your fitness goals</p>
</div>
""", unsafe_allow_html=True)