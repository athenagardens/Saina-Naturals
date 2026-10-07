import streamlit as st
from PIL import Image
import os
from urllib.parse import quote

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Saina Naturals | Healing Foods & Botanicals",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== BRAND COLORS & FONTS ====================
CREAM = "#F8F5F0"
FOREST = "#2F3E2F"
OLIVE = "#5C6B4E"
TERRACOTTA = "#A65D3F"
CHARCOAL = "#2A2A2A"
SAND = "#EDE6DC"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@300;400;500&display=swap');

.stApp {{ background-color: {CREAM}; }}

h1, h2, h3, h4 {{
    font-family: 'Playfair Display', serif !important;
    color: {FOREST} !important;
    letter-spacing: -0.3px;
}}

p, li, label, .stMarkdown, .stRadio label, .stSelectbox label {{
    font-family: 'Inter', sans-serif !important;
    color: {CHARCOAL};
}}

.product-card {{
    background: white;
    border-radius: 14px;
    padding: 1.3rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    border: 1px solid {SAND};
    margin-bottom: 1rem;
}}

.price {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    color: {TERRACOTTA};
    font-weight: 600;
}}

.tagline {{
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    color: {OLIVE};
    font-weight: 400;
}}

div[data-testid="stSidebar"] {{
    background-color: #F3EEE6;
}}

.stButton > button {{
    background-color: {FOREST};
    color: white;
    border-radius: 8px;
    border: none;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
}}

.stButton > button:hover {{
    background-color: {OLIVE};
    color: white;
}}

.cart-item {{
    background: white;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 0.7rem;
    border: 1px solid {SAND};
}}

.payment-box {{
    background: white;
    border-radius: 12px;
    padding: 1.4rem;
    border: 1px solid {SAND};
    margin-bottom: 1rem;
}}
</style>
""", unsafe_allow_html=True)

# ==================== YOUR REAL DETAILS ====================
ORANGE_MONEY = "26774501880"
MYZAKA = "26774501880"
BANK_NAME = "Absa"
ACCOUNT_NAME = "Saina Naturals"
ACCOUNT_NUMBER = "12345"
BRANCH_CODE = "14445"

WHATSAPP_NUMBER = "26774501880"
SHIPPING_FEE = 30          # P30 within Gaborone
MIN_ORDER_FOR_SHIPPING = 200

# ==================== PRODUCT CATALOG ====================
PRODUCTS = {
    # TEAS
    "tea_ginger": {"name": "Ginger Tea", "category": "Teas", "desc": "Warming digestive tea. Supports digestion and circulation.", "image": "ginger.png",
                   "sizes": [{"label": "Box of 20 sachets", "price": 85}, {"label": "Box of 40 sachets", "price": 155}]},
    "tea_peppermint": {"name": "Peppermint Tea", "category": "Teas", "desc": "Cooling and clarifying. Soothes the stomach.", "image": "peppermint.png",
                       "sizes": [{"label": "Box of 20 sachets", "price": 85}, {"label": "Box of 40 sachets", "price": 155}]},
    "tea_moringa": {"name": "Moringa Tea", "category": "Teas", "desc": "Nutrient-dense superfood leaves.", "image": "moringa.png",
                    "sizes": [{"label": "Box of 20 sachets", "price": 95}, {"label": "Box of 40 sachets", "price": 175}]},
    "tea_hibiscus": {"name": "Hibiscus Tea", "category": "Teas", "desc": "Tart floral tea traditionally used for metabolic balance.", "image": "hibiscus.png",
                     "sizes": [{"label": "Box of 20 sachets", "price": 90}, {"label": "Box of 40 sachets", "price": 165}]},
    "tea_avocado": {"name": "Avocado Leaf Tea", "category": "Teas", "desc": "Gentle, earthy and nourishing.", "image": "avocado.png",
                    "sizes": [{"label": "Box of 20 sachets", "price": 90}, {"label": "Box of 40 sachets", "price": 165}]},
    "tea_lemongrass": {"name": "Lemongrass Tea", "category": "Teas", "desc": "Uplifting citrus notes that calm the nervous system.", "image": "lemongrass.png",
                       "sizes": [{"label": "Box of 20 sachets", "price": 85}, {"label": "Box of 40 sachets", "price": 155}]},
    "tea_variety": {"name": "Healing Tea Variety Pack", "category": "Teas", "desc": "Ginger, Peppermint, Moringa, Hibiscus, Avocado Leaf & Lemongrass.", "image": "variety.png",
                    "sizes": [{"label": "6 teas (5 sachets each)", "price": 280}, {"label": "6 teas (10 sachets each)", "price": 480}]},
    "hibiscus_loose": {"name": "Infused Hibiscus Flowers", "category": "Teas", "desc": "Best-seller. Loose hibiscus infused with cloves & cinnamon.", "image": "hibiscus_loose.png",
                       "sizes": [{"label": "100g", "price": 120}, {"label": "250g", "price": 260}, {"label": "500g", "price": 480}]},

    # COFFEE
    "coffee_kilimanjaro": {"name": "Kilimanjaro Arabica", "category": "Coffee", "desc": "Pure Arabica beans. Clean energy, carefully sourced.", "image": "coffee.png",
                           "sizes": [{"label": "250g whole beans", "price": 95}, {"label": "500g whole beans", "price": 180}, {"label": "1kg whole beans", "price": 340}]},

    # SNACKS & COOKIES
    "cookies_almond": {"name": "Almond Seed Cookies", "category": "Snacks & Cookies", "desc": "No sugar. No flour. High protein. Perfect for keto, banting & diabetics.", "image": "cookies.png",
                       "sizes": [{"label": "Pack of 8", "price": 95}, {"label": "Pack of 16", "price": 175}]},
    "granola_coconut": {"name": "Coconut Nut Granola", "category": "Snacks & Cookies", "desc": "Low-carb clusters of coconut, nuts & seeds. No grains.", "image": "granola.png",
                        "sizes": [{"label": "300g", "price": 110}, {"label": "600g", "price": 200}]},
    "granola_menopause": {"name": "Menopause Seed Granola", "category": "Snacks & Cookies", "desc": "Hormone-supportive blend of flax, pumpkin, sesame, sunflower & chia seeds.", "image": "menopause_granola.png",
                          "sizes": [{"label": "300g", "price": 125}, {"label": "600g", "price": 230}]},
    "butter_almond": {"name": "Almond Butter", "category": "Snacks & Cookies", "desc": "100% pure almonds. Nothing added.", "image": "almond_butter.png",
                      "sizes": [{"label": "250g", "price": 110}, {"label": "350g", "price": 145}, {"label": "500g", "price": 195}]},
    "butter_cashew": {"name": "Cashew Butter", "category": "Snacks & Cookies", "desc": "Smooth, pure cashew butter.", "image": "cashew_butter.png",
                      "sizes": [{"label": "250g", "price": 120}, {"label": "350g", "price": 155}]},
    "butter_mixed": {"name": "Mixed Nut Butter", "category": "Snacks & Cookies", "desc": "Powerful blend of almonds, cashews, walnuts & seeds.", "image": "mixed_butter.png",
                     "sizes": [{"label": "250g", "price": 125}, {"label": "350g", "price": 160}]},
    "nuts_mixed": {"name": "Mixed Nuts & Seeds", "category": "Snacks & Cookies", "desc": "Raw or lightly seasoned with 
