import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Saina Naturals",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo path
LOGO_PATH = "assets/saina_logo.png"

# Earth tone colors
CREAM = "#F7F3EB"
FOREST = "#3D4F3A"
OLIVE = "#6B7F5C"
TERRACOTTA = "#C4704B"
CHARCOAL = "#2C2C2C"
SAND = "#E8D5C4"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Outfit:wght@300;400;500&display=swap');
    
    .stApp {{ background-color: {CREAM}; }}
    
    h1, h2, h3 {{
        font-family: 'Cormorant Garamond', serif !important;
        color: {FOREST} !important;
    }}
    
    p, li, .stMarkdown, .stRadio label {{
        font-family: 'Outfit', sans-serif !important;
        color: {CHARCOAL};
    }}
    
    .product-card {{
        background: white;
        border-radius: 12px;
        padding: 1.4rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
        border: 1px solid {SAND};
        height: 100%;
    }}
    
    .hero {{ text-align: center; padding: 1.5rem 0 0.5rem 0; }}
    
    .tagline {{
        font-size: 1.15rem;
        color: {OLIVE};
        font-weight: 300;
        letter-spacing: 0.4px;
    }}
    
    div[data-testid="stSidebar"] {{
        background-color: #F0EBE3;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)
    else:
        st.markdown("### 🌿 Saina Naturals")
    
    st.markdown("**Saina Naturals**")
    st.caption("Healing foods & botanicals")
    st.markdown("---")
    
    page = st.radio(
        "Navigate",
        ["Home", "Teas", "Coffee", "Keto & Snacks", "Bathing Rituals", "About", "Contact"],
        label_visibility="collapsed"
    )

# Product data
TEAS = [
    {"name": "Ginger", "benefit": "Digestive ease & warmth"},
    {"name": "Peppermint", "benefit": "Cooling & clarifying"},
    {"name": "Moringa", "benefit": "Nutrient dense"},
    {"name": "Hibiscus", "benefit": "Blood sugar support"},
    {"name": "Avocado Leaf", "benefit": "Gentle & nourishing"},
    {"name": "Lemongrass", "benefit": "Uplifting & calming"},
]

# ========== PAGES ==========

if page == "Home":
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    if os.path.exists(LOGO_PATH):
        c1, c2, c3 = st.columns([1, 1.5, 1])
        with c2:
            st.image(LOGO_PATH, use_container_width=True)
    st.markdown("# Saina Naturals")
    st.markdown('<p class="tagline">Clean. Healing. Naturally Nourishing.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Healing foods & botanicals for modern Botswana")
    st.write(
        "Keto-friendly • Diabetic-conscious • Rooted in natural wellness. "
        "From our best-selling infused hibiscus to clean snacks and pure teas — "
        "everything supports blood sugar balance, digestion, and daily vitality."
    )
    
    st.markdown("#### Featured")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="product-card">
            <h3>🍵 Healing Tea Variety Pack</h3>
            <p>Ginger • Peppermint • Moringa<br>Hibiscus • Avocado Leaf • Lemongrass</p>
            <p><em>Six pure teas in elegant packaging</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="product-card">
            <h3>🌺 Infused Hibiscus</h3>
            <p><strong>Cloves × Cinnamon</strong></p>
            <p>Our best-seller. Loose flowers for daily blood-sugar supportive tea.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="product-card">
            <h3>☕ Kilimanjaro Arabica</h3>
            <p>Pure coffee beans<br>Clean energy, carefully sourced</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Teas":
    st.markdown("## Healing Teas")
    st.write("Pure botanicals. No additives. Just nature.")
    
    st.markdown("### Variety Pack")
    st.info("Six single-origin teas — perfect as a gift or daily rotation.")
    
    cols = st.columns(3)
    for i, tea in enumerate(TEAS):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <h4>{tea['name']}</h4>
                <p style="color:#6B7F5C; font-size:0.9rem;"><em>{tea['benefit']}</em></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Best Seller — Loose Infused Hibiscus")
    st.markdown("""
    <div class="product-card">
        <h3>Infused Hibiscus Flowers</h3>
        <p><strong>Cloves × Cinnamon</strong></p>
        <p>Deep red dried hibiscus gently infused with cloves and cinnamon. 
        Beautiful as a hot tea or iced infusion. Traditionally used for metabolic and circulatory support.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Coffee":
    st.markdown("## Coffee")
    st.markdown("""
    <div class="product-card">
        <h3>Kilimanjaro Arabica</h3>
        <p>Pure coffee beans. Clean energy. Carefully sourced.</p>
        <p>Available as whole beans. Perfect for those who want quality coffee without the extras.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Keto & Snacks":
    st.markdown("## Keto • Banting • Diabetic-Friendly")
    st.write("Clean snacks designed for blood-sugar friendly living.")
    
    products = [
        ("Almond Seed Cookies", "No sugar. No flour. High protein. Perfect for keto and diabetic lifestyles."),
        ("Coconut Nut Granola", "Low-carb clusters of coconut, nuts and seeds. No grains."),
        ("Nut Butters", "Pure almond, cashew or mixed. Nothing added."),
        ("Infused Honeys", "Raw honey gently infused with ginger, turmeric or immune botanicals."),
        ("Mixed Nuts & Seeds", "Raw or lightly seasoned with Himalayan salt."),
    ]
    
    for name, desc in products:
        st.markdown(f"""
        <div class="product-card">
            <h4>{name}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Bathing Rituals":
    st.markdown("## Bathing & Ritual Teas")
    st.write("Dry herb flowers for soaking, steaming, and quiet moments.")
    
    for name, desc in [
        ("Lavender", "Calming floral notes for evening soaks and restful sleep."),
        ("Chamomile", "Soft, apple-like flowers that soothe the body and mind."),
        ("Custom Blends", "Ask us about lavender + chamomile or hibiscus ritual soaks."),
    ]:
        st.markdown(f"""
        <div class="product-card">
            <h4>{name}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "About":
    st.markdown("## About Saina Naturals")
    st.write(
        "Rooted at Athena Gardens in Notwane, Gaborone, Saina Naturals brings together "
        "clean macro-style nutrition and traditional botanical wisdom. "
        "We focus on products that support blood sugar balance, digestion, and everyday healing — "
        "especially important for the many Batswana managing diabetes and metabolic health."
    )
    st.write("Our approach is simple: pure ingredients, elegant presentation, and real benefits.")

elif page == "Contact":
    st.markdown("## Contact & Orders")
    st.write("**Location**: Athena Gardens, Notwane, Gaborone")
    st.write("**Email**: info@saina.co.bw")
    st.write("**Phone / WhatsApp**: +267 71 334 355")
    st.markdown("---")
    st.write("For orders, WhatsApp or email us directly. Collection available at Athena Gardens.")
    
    with st.form("inquiry"):
        name = st.text_input("Your name")
        contact = st.text_input("WhatsApp or Email")
        message = st.text_area("What would you like to order or ask about?")
        if st.form_submit_button("Send Inquiry"):
            st.success("Thank you! We will respond shortly.")

# Footer
st.markdown("---")
st.markdown(
    f"<p style='text-align:center; color:{OLIVE}; font-size:0.85rem;'>"
    "Saina Naturals · Athena Gardens, Notwane · Healing foods & botanicals</p>",
    unsafe_allow_html=True
)
