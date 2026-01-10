import streamlit as st
import google.generativeai as genai
import time
import json
import base64

# --- ⚠️ CONFIGURATION ⚠️ ---
api_key = "AIzaSyBpx3zSff2FDmku2UKNbNil5rZ0q5hHe9E"  # Put your Gemini Key here
background_image_file = r"C:\Users\SANKU\Downloads\WhatsApp Image 2026-01-10 at 19.29.38.jpeg"  # PUT YOUR LOCAL IMAGE FILE NAME HERE

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ScriptSentinel AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FUNCTION TO LOAD LOCAL IMAGE ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# Get Base64 string
img_base64 = get_base64_of_bin_file(background_image_file)

# Build the CSS string based on whether image was found
if img_base64:
    css_background = f"""
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.9)), 
                          url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
else:
    # Fallback if image not found
    css_background = """
    .stApp {
        background: radial-gradient(circle at top center, #1b2735 0%, #090a0f 100%);
    }
    """

# --- CUSTOM CSS ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    /* 1. BACKGROUND IMAGE INJECTION */
    {css_background}
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: #FAFAFA;
    }}
    
    /* 2. Glassmorphism Cards */
    .war-room-box {{
        background: rgba(20, 20, 30, 0.7);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }}

    .pillar-card {{
        background: rgba(255, 255, 255, 0.03); 
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-left: 4px solid #7C4DFF;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
        transition: transform 0.2s;
    }}
    
    .pillar-card:hover {{
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.08);
        border-left: 4px solid #00E5FF;
    }}

    /* 3. Typography & Accents */
    .pillar-title {{
        color: #B388FF; 
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }}
    
    .pillar-highlight {{
        color: #64FFDA; 
        font-weight: bold;
        font-size: 0.9rem;
        margin-top: 10px;
    }}
    
    /* Risk Badges */
    .risk-badge {{
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
        font-size: 0.85rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    .risk-low {{ background-color: rgba(0, 200, 83, 0.2); color: #69F0AE; border: 1px solid #00C853; }}
    .risk-med {{ background-color: rgba(255, 171, 0, 0.2); color: #FFD740; border: 1px solid #FFAB00; }}
    .risk-high {{ background-color: rgba(255, 61, 0, 0.2); color: #FF6E40; border: 1px solid #FF3D00; }}
    .risk-critical {{ 
        background-color: rgba(213, 0, 0, 0.3); 
        color: #FF5252; 
        border: 1px solid #FF1744;
        box-shadow: 0 0 15px rgba(213, 0, 0, 0.4);
    }}
    
    .lang-tag {{
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        color: #eee;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        margin-left: 10px;
        vertical-align: middle;
    }}
    
    /* Input Area Styling */
    .stTextArea textarea {{
        background-color: rgba(0, 0, 0, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        backdrop-filter: blur(5px);
    }}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3074/3074767.png", width=60)
    st.title("ScriptSentinel")
    st.caption("The AI Line Producer")
    st.divider()
    
    st.subheader("📍 Production Context")
    location = st.selectbox(
        "Shooting Location",
        ["Kerala, India (Tropical)", 
         "Kashmir, India (Snow/Mountain)",
         "London, UK (Urban/Strict)",
         "Los Angeles, USA (Union)"]
    )
    
    st.info(f"**Active Mode:** {location}\n\n*System will apply local laws & weather physics.*")

# --- MAIN HEADER ---
st.title("🎬 ScriptSentinel: AI Production Risk Analyzer")
st.markdown("##### *The only AI that predicts Costs, Physics, and Lawsuits.*")

# --- INPUT AREA ---
script_input = st.text_area(
    "Paste Script Scene (Any Language):", 
    height=200, 
    placeholder="Example: EXT. JUNGLE - NIGHT..."
)

# --- AI LOGIC ---
def get_risk_color(level):
    lvl = level.lower()
    if "critical" in lvl: return "risk-critical"
    if "high" in lvl: return "risk-high"
    if "med" in lvl: return "risk-med"
    return "risk-low"

def analyze_script(script, loc):
    if api_key == "PASTE_YOUR_KEY_HERE":
        st.error("⚠️ Please paste your Gemini API Key in line 8 of the code!")
        return None

    genai.configure(api_key=api_key)
    
    # Use standard Flash model
    model = genai.GenerativeModel('gemini-flash-latest')
    
    system_prompt = f"""
    You are an expert Film Line Producer.
    CONTEXT: Location is {loc}.
    
    TASK: Analyze the script and output strictly valid JSON.
    
    LANGUAGE INSTRUCTION: 
    1. Detect the language of the INPUT SCRIPT (e.g., Hindi, Malayalam, English).
    2. The values for "intro", "mitigation_plan", and "novelty_analysis" MUST BE IN THE DETECTED LANGUAGE.
    3. The keys (e.g., "risk_levels") MUST REMAIN IN ENGLISH.
    
    REQUIREMENTS:
    1. "detected_language": Name of the language detected.
    2. "intro": 1 sentence summary (In Detected Language).
    3. "risk_levels": A dictionary with exact keys ["Weather", "Crowd", "NightShoot", "Stunt", "VFX"] and values "Low", "Medium", "High", or "Critical".
    4. "mitigation_plan": A professional paragraph explaining the solution (In Detected Language).
    5. "novelty_analysis": A dictionary for the 4 pillars (Values in Detected Language):
       - "context_aware": specifically mention combinatorial risks.
       - "locale_adaptive": specifically mention location logistics.
       - "reality_check": specifically mention physics/time limits.
       - "legal_oracle": specifically mention laws/precedents.

    Output JSON ONLY. No markdown blocks.
    """
    
    try:
        response = model.generate_content(f"{system_prompt}\n\nSCRIPT:\n{script}")
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except Exception as e:
        st.error(f"Analysis Error: {e}")
        return None

# --- RUN BUTTON ---
if st.button("🚀 RUN FEASIBILITY CHECK", type="primary"):
    if api_key == "PASTE_YOUR_KEY_HERE":
         st.error("🔑 You forgot to paste the API Key in the code (Line 8)!")
    elif not script_input:
        st.warning("📄 Please paste a script.")
    else:
        with st.spinner("🔄 Simulating Production Meeting (Detecting Language)..."):
            time.sleep(1.5) 
            data = analyze_script(script_input, location)
        
        if data:
            # --- SECTION 1: THE DASHBOARD ---
            st.markdown("### 📊 Scene Feasibility Report")
            
            with st.container():
                
                # Title with Detected Language Tag
                lang = data.get('detected_language', 'English')
                st.markdown(f"**SCENE SUMMARY** <span class='lang-tag'>{lang}</span>", unsafe_allow_html=True)
                st.write(f"*{data.get('intro')}*")
                
                st.divider()
                
                cols = st.columns(5)
                risks = data.get("risk_levels", {})
                categories = ["Weather", "Crowd", "NightShoot", "Stunt", "VFX"]
                
                for i, cat in enumerate(categories):
                    level = risks.get(cat, "Low")
                    css_class = get_risk_color(level)
                    with cols[i]:
                        st.markdown(f"**{cat}**")
                        st.markdown(f'<div class="risk-badge {css_class}">{level.upper()}</div>', unsafe_allow_html=True)
                
                st.divider()
                st.subheader("✅ Expert Mitigation Strategy")
                st.write(data.get("mitigation_plan"))
                st.markdown('</div>', unsafe_allow_html=True)

            # --- SECTION 2: THE NOVELTY PILLARS ---
            st.markdown("### 🧠 The Core Reasoning Engines (Our Novelty)")
            novelty = data.get("novelty_analysis", {})
            
            row1 = st.columns(2)
            row2 = st.columns(2)
            
            with row1[0]:
                st.markdown(f"""
                <div class="pillar-card">
                    <div class="pillar-title">🌍 Locale-Adaptive Engine</div>
                    <p>{novelty.get('locale_adaptive', 'Analyzing location logistics...')}</p>
                </div>
                """, unsafe_allow_html=True)
            with row1[1]:
                st.markdown(f"""
                <div class="pillar-card">
                    <div class="pillar-title">🛡️ Context-Aware Engine</div>
                    <p>{novelty.get('context_aware', 'Checking combinatorial risks...')}</p>
                </div>
                """, unsafe_allow_html=True)
            with row2[0]:
                st.markdown(f"""
                <div class="pillar-card">
                    <div class="pillar-title">⏳ Time & Physics Validator</div>
                    <p>{novelty.get('reality_check', 'Calculating physics limits...')}</p>
                </div>
                """, unsafe_allow_html=True)
            with row2[1]:
                st.markdown(f"""
                <div class="pillar-card">
                    <div class="pillar-title">⚖️ Liability & Precedent Oracle</div>
                    <p>{novelty.get('legal_oracle', 'Checking case law...')}</p>
                </div>
                """, unsafe_allow_html=True)