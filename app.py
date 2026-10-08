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
SHIPPING_FEE = 30
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
                    "sizes": [{"label": "Box of 20 sachets", "price": 90}, {"label": "Box 
