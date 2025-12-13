import streamlit as st
from streamlit.components.v1 import html

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="LifeTune - AI Fitness & Nutrition",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# CSS - Square Edges Only
# ========================================
st.markdown("""
<style>
    .main {
        padding: 0 !important;
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Fixed Menu Button - Square */
    #menu-toggle {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1000;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27;
        border: none;
        padding: 12px 16px;
        font-size: 1.4rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(0,255,135,.4);
        display: flex;
        align-items: center;
        gap: 8px;
    }
    #menu-toggle:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 30px rgba(0,255,135,.6);
    }

    /* Sidebar - Square */
    section[data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%) !important;
        border-right: 2px solid rgba(0,255,135,0.2);
        padding: 2rem 1rem !important;
        width: 280px !important;
        box-shadow: 0 0 40px rgba(0,255,135,0.1);
    }

    .sidebar-header {
        text-align: center;
        padding: 1rem 0 2rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 2rem;
    }
    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }

    .sidebar .stButton > button {
        background: transparent !important;
        color: #b0b8d4 !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        padding: 1rem 1.5rem !important;
        margin: 0.8rem 0 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        text-align: left !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        gap: 1rem !important;
        width: 100% !important;
    }

    .sidebar .stButton > button:hover {
        background: rgba(0,255,135,0.1) !important;
        color: #00ff87 !important;
        border-color: #00ff87 !important;
        transform: translateX(8px) !important;
        box-shadow: 0 8px 25px rgba(0,255,135,0.2) !important;
    }

    /* Hero */
    .hero-section{
        position:relative;height:100vh;
        background:linear-gradient(rgba(10,14,39,0.7),rgba(10,14,39,0.9)),
                   url('https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=2070') center/cover;
        display:flex;flex-direction:column;align-items:center;justify-content:center;
        text-align:center;color:white;padding:2rem;
    }
    .hero-title{
        font-size:5rem;font-weight:900;
        background:linear-gradient(135deg,#00ff87 0%,#60efff 100%);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        letter-spacing:3px;margin-bottom:1rem;
    }
    .hero-subtitle{font-size:1.5rem;color:#b0b8d4;margin-bottom:1.5rem;}

    /* CTA Buttons - Square */
    .post-hero-cta, .pre-footer-cta {padding: 3rem 1rem;text-align: center;}
    .pre-footer-cta {background: linear-gradient(135deg, #1a1d35 0%, #0a0e27 100%);}
    .html-btn {
        background: linear-gradient(135deg, #00ff87 0%, #60efff 100%);
        color: #0a0e27;
        border: none;
        padding: 0.9rem 3rem;
        font-size: 1.2rem;
        font-weight: 700;
        text-transform: uppercase;
        box-shadow: 0 10px 40px rgba(0,255,135,.3);
        transition: all .3s;
        cursor: pointer;
        display: inline-block;
        text-decoration: none;
        text-align: center;
        margin: 0.5rem;
    }
    .html-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,255,135,.5);
    }

    /* Stats */
    .stats-section{padding:5rem 4rem;background:linear-gradient(135deg,#00ff87 0%,#60efff 100%);text-align:center;}
    .stats-grid{display:grid !important;grid-template-columns:repeat(auto-fit,minmax(200px,1fr)) !important;gap:3rem;}
    .stat-number{font-size:4rem;font-weight:900;color:#0a0e27;}
    .stat-label{font-size:1.2rem;color:#0a0e27;font-weight:600;text-transform:uppercase;}

    /* Features - Square */
    .features-section{padding:6rem 4rem;background:#0a0e27;}
    .section-title{text-align:center;font-size:3rem;font-weight:800;color:white;margin-bottom:1rem;text-transform:uppercase;}
    .section-subtitle{text-align:center;font-size:1.2rem;color:#7a8199;margin-bottom:4rem;}
    .feature-grid{display:grid !important;grid-template-columns:repeat(auto-fit,minmax(300px,1fr)) !important;gap:2rem !important;}
    .feature-card{
        background:linear-gradient(135deg,#1a1d35 0%,#252945 100%);
        padding:3rem 2rem;text-align:center;
        transition:all .4s;border:1px solid rgba(255,255,255,.05);
    }
    .feature-card:hover{transform:translateY(-15px);box-shadow:0 20px 60px rgba(0,255,135,.2);}
    .feature-icon{font-size:4rem;margin-bottom:1.5rem;}
    .feature-title{font-size:1.6rem;font-weight:700;color:white;margin-bottom:1rem;}
    .feature-desc{font-size:1rem;color:#9ca3c0;}

    /* Process - Square */
    .process-section{padding:6rem 4rem;background:#0a0e27;}
    .process-steps{display:grid !important;grid-template-columns:repeat(auto-fit,minmax(250px,1fr)) !important;gap:2rem !important;}
    .process-step{
        background:linear-gradient(135deg,#1a1d35 0%,#252945 100%);
        padding:2rem;border:2px solid transparent;transition:all .3s;
    }
    .process-step:hover{border-color:#00ff87;transform:scale(1.05);}
    .step-number{
        width:60px;height:60px;background:linear-gradient(135deg,#00ff87 0%,#60efff 100%);
        display:flex;align-items:center;justify-content:center;
        font-size:2rem;font-weight:900;color:#0a0e27;margin-bottom:1.5rem;
    }

    .cta-title{font-size:3rem;font-weight:900;color:white;margin-bottom:1.5rem;}
    .cta-subtitle{font-size:1.3rem;color:#9ca3c0;margin-bottom:3rem;}

    .footer{padding:3rem 4rem;background:#060815;text-align:center;color:#7a8199;}
    .footer-link{color:#00ff87;text-decoration:none;}
    .footer-link:hover{color:#60efff;}

    @media (max-width:768px){
        .hero-title{font-size:3rem;}
        .section-title{font-size:2rem;}
        .feature-grid,.process-steps,.stats-grid{grid-template-columns:1fr !important;}
        .html-btn{font-size:1rem;padding:.8rem 2rem;}
        #menu-toggle {top: 15px; left: 15px; padding: 10px 12px; font-size: 1.2rem;}
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# JAVASCRIPT: Toggle Sidebar via Button
# ========================================
toggle_js = """
<script>
    // Find the sidebar toggle button (Streamlit's internal)
    const sidebarToggle = document.querySelector('button[kind="header"]');
    const menuBtn = document.getElementById('menu-toggle');

    // Sync button state with URL
    const urlParams = new URLSearchParams(window.location.search);
    const isOpen = urlParams.get('sidebar') === 'open';

    if (isOpen && sidebarToggle) {
        sidebarToggle.click();
    }

    menuBtn.addEventListener('click', () => {
        if (sidebarToggle) {
            sidebarToggle.click();
            // Update URL
            const newUrl = new URL(window.location);
            if (newUrl.searchParams.get('sidebar') === 'open') {
                newUrl.searchParams.delete('sidebar');
            } else {
                newUrl.searchParams.set('sidebar', 'open');
            }
            window.history.replaceState({}, '', newUrl);
        }
    });
</script>
"""

# ========================================
# SIDEBAR CONTENT
# ========================================
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <h2 class="sidebar-title">LifeTune</h2>
        </div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("Home", "Home.py", "🏠"),
        ("Onboarding", "pages/1_Onboarding.py", "🤖"),
        ("Your Plan", "pages/2_YourPlan.py", "📋"),
        ("Dashboard", "pages/3_Dashboard.py", "📊")
    ]

    for label, path, icon in nav_items:
        if st.button(f"{icon} {label}", key=path, use_container_width=True):
            st.switch_page(path)

# ========================================
# PAGE HTML + MENU BUTTON
# ========================================
page_html = """
<!-- Fixed Menu Button -->
<button id="menu-toggle">☰ Menu</button>

<!-- Hero -->
<div class="hero-section">
    <h1 class="hero-title">LifeTune</h1>
    <p class="hero-subtitle">Your AI-Powered Fitness & Nutrition Revolution</p>
</div>

<!-- Button AFTER Hero -->
<div class="post-hero-cta">
    <form method="get">
        <input type="hidden" name="action" value="start">
        <button type="submit" class="html-btn">START YOUR TRANSFORMATION</button>
    </form>
</div>

<!-- Stats -->
<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-item"><div class="stat-number">10K+</div><div class="stat-label">Active Users</div></div>
        <div class="stat-item"><div class="stat-number">50K+</div><div class="stat-label">Plans Generated</div></div>
        <div class="stat-item"><div class="stat-number">95%</div><div class="stat-label">Success Rate</div></div>
        <div class="stat-item"><div class="stat-number">24/7</div><div class="stat-label">AI Support</div></div>
    </div>
</div>

<!-- Features -->
<div class="features-section">
    <h2 class="section-title">Powered by AI Agents</h2>
    <p class="section-subtitle">Revolutionary technology meets personalized fitness</p>
    <div class="feature-grid">
        <div class="feature-card"><div class="feature-icon">🤖</div><h3 class="feature-title">Smart Workouts</h3>
            <p class="feature-desc">AI-crafted routines that adapt to your goals, schedule, and fitness level using advanced CrewAI agents</p></div>
        <div class="feature-card"><div class="feature-icon">🍽️</div><h3 class="feature-title">Indian Nutrition</h3>
            <p class="feature-desc">Authentic Indian meal plans designed by nutrition specialists, perfectly balanced for your body type</p></div>
        <div class="feature-card"><div class="feature-icon">📊</div><h3 class="feature-title">Progress Tracking</h3>
            <p class="feature-desc">Real-time analytics and insights to keep you motivated and on track to achieve your fitness goals</p></div>
    </div>
</div>

<!-- Process -->
<div class="process-section">
    <h2 class="section-title">How It Works</h2>
    <p class="section-subtitle">Your transformation in 4 simple steps</p>
    <div class="process-steps">
        <div class="process-step"><div class="step-number">1</div><h3 class="step-title">Share Your Goals</h3><p class="step-desc">Tell us about your fitness objectives, preferences, and lifestyle</p></div>
        <div class="process-step"><div class="step-number">2</div><h3 class="step-title">AI Creates Your Plan</h3><p class="step-desc">Our intelligent agents generate a personalized 7-day program</p></div>
        <div class="process-step"><div class="step-number">3</div><h3 class="step-title">Follow Daily</h3><p class="step-desc">Track workouts and meals with our intuitive dashboard</p></div>
        <div class="process-step"><div class="step-number">4</div><h3 class="step-title">See Results</h3><p class="step-desc">Build lasting habits and achieve your dream physique</p></div>
    </div>
</div>

<!-- Pre-Footer CTA + Button -->
<div class="pre-footer-cta">
    <h2 class="cta-title">Ready to Transform?</h2>
    <p class="cta-subtitle">Join thousands who've already started their fitness journey with AI</p>
    <form method="get">
        <input type="hidden" name="action" value="start">
        <button type="submit" class="html-btn">GET STARTED NOW</button>
    </form>
</div>

<!-- Footer -->
<div class="footer">
    <div class="footer-content">
        <p>Powered by <a href="#" class="footer-link">CrewAI</a> & <a href="#" class="footer-link">Google Gemini</a></p>
        <p style="margin-top:1rem;">© 2024 LifeTune. Built with ❤️ for your fitness goals.</p>
    </div>
</div>
"""

st.markdown(page_html, unsafe_allow_html=True)

# ========================================
# INJECT JS + SYNC WITH URL
# ========================================
html(toggle_js, height=0, width=0)

# Sync URL param with sidebar state
if st.query_params.get("sidebar") == "open":
    st.session_state.sidebar_open = True
else:
    st.session_state.sidebar_open = False

# Handle CTA buttons
if st.query_params.get("action") == "start":
    st.query_params.clear()
    st.switch_page("pages/1_Onboarding.py")