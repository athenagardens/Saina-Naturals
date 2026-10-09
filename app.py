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
                    "sizes": [{"label": "Box of 20 sachets", "price": 90}, {"label": "Box of 40 sachets", "price": 165}]},
    "tea_lemongrass": {"name": "Lemongrass Tea", "category": "Teas", "desc": "Uplifting citrus notes that calm the nervous system.", "image": "lemongrass.png",
                       "sizes": [{"label": "Box of 20 sachets", "price": 85}, {"label": "Box of 40 sachets", "price": 155}]},
    "tea_variety": {"name": "Healing Tea Variety Pack", "category": "Teas", "desc": "Ginger, Peppermint, Moringa, Hibiscus, Avocado Leaf & Lemongrass.", "image": "variety.png",
                    "sizes": [{"label": "6 teas (5 sachets each)", "price": 280}, {"label": "6 teas (10 sachets each)", "price": 480}]},
    "hibiscus_loose": {"name": "Infused Hibiscus Flowers", "category": "Teas", "desc": "Best-seller. Loose hibiscus infused with cloves & cinnamon.", "image": "hibiscus_loose.jpeg",
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
    "nuts_mixed": {"name": "Mixed Nuts & Seeds", "category": "Snacks & Cookies", "desc": "Raw or lightly seasoned with Himalayan salt.", "image": "nuts.png",
                   "sizes": [{"label": "250g", "price": 95}, {"label": "500g", "price": 175}]},
    "nuts_trio": {"name": "Trio Nut Mix", "category": "Snacks & Cookies", "desc": "Almonds, cashews & peanuts with Himalayan salt.", "image": "trio_nuts.png",
                  "sizes": [{"label": "300g", "price": 105}, {"label": "600g", "price": 190}]},
    "seed_crackers": {"name": "Seed Crackers", "category": "Snacks & Cookies", "desc": "Crispy flax, pumpkin and sesame seed crackers. Zero flour, keto-friendly.", "image": "seed_crackers.png",
                      "sizes": [{"label": "Pack of 12", "price": 85}, {"label": "Pack of 24", "price": 155}]},
    "coconut_clusters": {"name": "Coconut Seed Clusters", "category": "Snacks & Cookies", "desc": "Crunchy coconut and seed clusters.", "image": "coconut_clusters.png",
                         "sizes": [{"label": "200g", "price": 90}, {"label": "400g", "price": 165}]},

    # FLOURS
    "flour_almond": {
        "name": "Almond Flour",
        "category": "Flours",
        "desc": "Finely milled almonds. Perfect for keto cookies, cakes, pancakes and coatings. Sugar-free & gluten-free.",
        "image": "almond_flour.png",
        "sizes": [{"label": "250g", "price": 95}, {"label": "500g", "price": 175}]
    },
    "flour_coconut": {
        "name": "Coconut Flour",
        "category": "Flours",
        "desc": "High-fibre, low-carb coconut flour. Excellent for pancakes, muffins, energy balls and thickening. Sugar-free & gluten-free.",
        "image": "coconut_flour.png",
        "sizes": [{"label": "250g", "price": 85}, {"label": "500g", "price": 155}]
    },
    "flour_flax": {
        "name": "Flaxseed Flour",
        "category": "Flours",
        "desc": "Freshly milled flaxseed. Ideal for baking, smoothies, hormone support and as a binding agent. Sugar-free & gluten-free.",
        "image": "flax_flour.png",
        "sizes": [{"label": "250g", "price": 90}, {"label": "500g", "price": 165}]
    },
    "flour_pumpkin": {
        "name": "Pumpkin Seed Flour",
        "category": "Flours",
        "desc": "Zinc-rich pumpkin seed flour. Great for savoury baking, protein boost and hormone balance. Sugar-free & gluten-free.",
        "image": "pumpkin_flour.png",
        "sizes": [{"label": "250g", "price": 95}, {"label": "500g", "price": 175}]
    },

    # SWEETENERS
    "sweetener_honey": {
        "name": "Raw Honey",
        "category": "Sweeteners",
        "desc": "Pure raw honey. A whole-food natural sweetener. Contains natural sugars – not sugar-free. Perfect for tea, baking and everyday use.",
        "image": "honey_raw.png",
        "sizes": [{"label": "250g", "price": 95}, {"label": "500g", "price": 175}]
    },
    "sweetener_date": {
        "name": "Date Syrup",
        "category": "Sweeteners",
        "desc": "100% pure date syrup. A whole-food natural sweetener made from dates. Contains natural sugars – not sugar-free. Rich caramel flavour, ideal for baking and porridge.",
        "image": "date_syrup.png",
        "sizes": [{"label": "250g", "price": 110}, {"label": "500g", "price": 200}]
    },
    "sweetener_monk": {
        "name": "Monk Fruit Sweetener",
        "category": "Sweeteners",
        "desc": "Zero-calorie, sugar-free natural sweetener. Ideal for keto, diabetic and blood-sugar friendly lifestyles.",
        "image": "monk_fruit.png",
        "sizes": [{"label": "100g", "price": 145}, {"label": "250g", "price": 295}]
    },
    "sweetener_stevia": {
        "name": "Stevia Leaf Powder",
        "category": "Sweeteners",
        "desc": "Pure stevia leaf powder. Zero-calorie and sugar-free. Very concentrated – a little goes a long way.",
        "image": "stevia.png",
        "sizes": [{"label": "50g", "price": 95}, {"label": "100g", "price": 175}]
    },

    # INFUSED HONEYS
    "honey_ginger": {
        "name": "Ginger Infused Honey",
        "category": "Infused Honeys",
        "desc": "Raw honey gently infused with fresh ginger. Supports digestion, soothes the stomach, and provides natural warmth. Ideal for tea or taken by the spoon.",
        "image": "honey_ginger.png",
        "sizes": [{"label": "250g", "price": 110}, {"label": "500g", "price": 200}]
    },
    "honey_turmeric": {
        "name": "Turmeric Infused Honey",
        "category": "Infused Honeys",
        "desc": "Raw honey infused with turmeric. Traditionally used to support immunity, reduce inflammation, and promote overall wellness.",
        "image": "honey_turmeric.png",
        "sizes": [{"label": "250g", "price": 120}, {"label": "500g", "price": 220}]
    },
    "honey_lemon_cinnamon": {
        "name": "Lemon & Cinnamon Infused Honey",
        "category": "Infused Honeys",
        "desc": "Raw honey infused with lemon and cinnamon. Supports immunity, aids digestion, and offers a bright, warming flavour. Excellent in tea or as a daily tonic.",
        "image": "honey_lemon_cinnamon.png",
        "sizes": [{"label": "250g", "price": 115}, {"label": "500g", "price": 210}]
    },

    # POWDERS
    "powder_moringa": {"name": "Moringa Powder", "category": "Powders", "desc": "Pure moringa leaf powder. Nutrient dense.", "image": "moringa_powder.png",
                       "sizes": [{"label": "100g", "price": 95}, {"label": "250g", "price": 210}]},
    "powder_baobab": {"name": "Baobab Powder", "category": "Powders", "desc": "Vitamin C rich African superfruit powder.", "image": "baobab.png",
                      "sizes": [{"label": "100g", "price": 110}, {"label": "250g", "price": 240}]},
    "powder_turmeric": {"name": "Turmeric Powder", "category": "Powders", "desc": "Pure turmeric root powder.", "image": "turmeric.png",
                        "sizes": [{"label": "100g", "price": 75}, {"label": "250g", "price": 160}]},
    "powder_flax": {"name": "Flaxseed Powder", "category": "Powders", "desc": "Freshly milled flaxseed. Excellent for hormones and menopause support.", "image": "flax.png",
                    "sizes": [{"label": "200g", "price": 85}, {"label": "400g", "price": 155}]},
    "powder_pumpkin": {"name": "Pumpkin Seed Powder", "category": "Powders", "desc": "Rich in zinc and magnesium. Great for hormone balance.", "image": "pumpkin_powder.png",
                       "sizes": [{"label": "200g", "price": 95}, {"label": "400g", "price": 175}]},
    "powder_maca": {"name": "Maca Powder", "category": "Powders", "desc": "Traditional hormone-supportive root.", "image": "maca.png",
                    "sizes": [{"label": "100g", "price": 120}, {"label": "250g", "price": 260}]},
    "powder_beetroot": {"name": "Beetroot Powder", "category": "Powders", "desc": "Natural energy and circulation support.", "image": "beetroot.png",
                        "sizes": [{"label": "100g", "price": 90}, {"label": "250g", "price": 195}]},
    "powder_spirulina": {"name": "Spirulina Powder", "category": "Powders", "desc": "Nutrient-dense blue-green algae.", "image": "spirulina.png",
                         "sizes": [{"label": "100g", "price": 130}, {"label": "250g", "price": 280}]},

    # OILS
    "oil_olive": {"name": "Extra Virgin Olive Oil", "category": "Oils", "desc": "Premium cold-pressed olive oil.", "image": "olive_oil.png",
                  "sizes": [{"label": "250ml", "price": 95}, {"label": "500ml", "price": 165}]},
    "oil_coconut": {"name": "Virgin Coconut Oil", "category": "Oils", "desc": "Cold-pressed virgin coconut oil.", "image": "coconut_oil.png",
                    "sizes": [{"label": "250ml", "price": 55}, {"label": "500ml", "price": 95}]},

    # BATHING
    "bath_lavender": {"name": "Lavender Bathing Tea", "category": "Bathing Rituals", "desc": "Calming floral soak for evening rituals.", "image": "lavender.png",
                      "sizes": [{"label": "80g", "price": 85}, {"label": "150g", "price": 150}]},
    "bath_chamomile": {"name": "Chamomile Bathing Tea", "category": "Bathing Rituals", "desc": "Soft, soothing flowers for restful soaks.", "image": "chamomile.png",
                       "sizes": [{"label": "80g", "price": 80}, {"label": "150g", "price": 140}]},

    # HERBS & SPICES
    "herb_lavender": {"name": "Dried Lavender Flowers", "category": "Herbs & Spices", "desc": "Pure dried lavender for tea or bathing.", "image": "lavender.png",
                      "sizes": [{"label": "50g", "price": 70}, {"label": "100g", "price": 125}]},
    "herb_chamomile": {"name": "Dried Chamomile Flowers", "category": "Herbs & Spices", "desc": "Gentle dried chamomile flowers.", "image": "chamomile.png",
                       "sizes": [{"label": "50g", "price": 65}, {"label": "100g", "price": 115}]},
    "spice_cinnamon": {"name": "Ceylon Cinnamon Sticks", "category": "Herbs & Spices", "desc": "True Ceylon cinnamon sticks.", "image": "cinnamon.png",
                       "sizes": [{"label": "50g", "price": 55}, {"label": "100g", "price": 95}]},
    "spice_cloves": {"name": "Whole Cloves", "category": "Herbs & Spices", "desc": "Aromatic whole cloves.", "image": "cloves.png",
                     "sizes": [{"label": "50g", "price": 45}, {"label": "100g", "price": 80}]},
}

# ==================== SESSION STATE ====================
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(product_id, size_label, price, qty=1):
    key = f"{product_id}|{size_label}|{price}"
    if key in st.session_state.cart:
        st.session_state.cart[key] += qty
    else:
        st.session_state.cart[key] = qty
    st.toast("Added to cart", icon="🛒")

def remove_from_cart(key):
    if key in st.session_state.cart:
        del st.session_state.cart[key]

def clear_cart():
    st.session_state.cart = {}

def get_cart_total():
    total = 0
    for key, qty in st.session_state.cart.items():
        price = float(key.split("|")[2])
        total += price * qty
    return total

def get_cart_count():
    return sum(st.session_state.cart.values())

# ==================== SIDEBAR ====================
with st.sidebar:
    logo_path = "assets/saina_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown("### 🌿 Saina Naturals")
    
    st.markdown("**Saina Naturals**")
    st.caption("Healing foods & botanicals · Notwane")
    st.markdown("---")
    
    page = st.radio(
        "Menu",
        ["Home", "Shop All", "Teas", "Coffee", "Snacks & Cookies", "Flours", "Sweeteners", "Infused Honeys", "Honeys & Oils", "Powders", "Bathing Rituals", "Herbs & Spices", "Payment & Shipping", "Cart & Order"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    cart_count = get_cart_count()
    if cart_count > 0:
        st.success(f"🛒 Cart: {cart_count} item(s)")
        st.metric("Total", f"P {get_cart_total():.2f}")
        if st.button("Clear Cart", use_container_width=True):
            clear_cart()
            st.rerun()
    else:
        st.info("Cart is empty")

# ==================== PRODUCT DISPLAY ====================
def show_product(pid, p):
    img_path = f"assets/{p.get('image', '')}"
    
    col_img, col_info = st.columns([1, 2.2])
    
    with col_img:
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.markdown(f"""
            <div style="background:#EDE6DC; height:130px; border-radius:10px; 
            display:flex; align-items:center; justify-content:center; color:#999; font-size:0.9rem;">
                Saina Naturals
            </div>
            """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown(f"**{p['name']}**")
        st.caption(p['desc'])
        
        size_options = [f"{s['label']} — P {s['price']}" for s in p['sizes']]
        selected = st.selectbox("Size", size_options, key=f"size_{pid}", label_visibility="collapsed")
        selected_size = p['sizes'][size_options.index(selected)]
        
        qty = st.number_input("Qty", min_value=1, max_value=20, value=1, key=f"qty_{pid}")
        
        if st.button("Add to Cart", key=f"add_{pid}", use_container_width=True):
            add_to_cart(pid, selected_size['label'], selected_size['price'], qty)

# ==================== PAGES ====================
if page == "Home":
    st.markdown('<div style="text-align:center; padding: 1rem 0;">', unsafe_allow_html=True)
    if os.path.exists("assets/saina_logo.png"):
        c1, c2, c3 = st.columns([1, 1.2, 1])
        with c2:
            st.image("assets/saina_logo.png", use_container_width=True)
    st.markdown("# Saina Naturals")
    st.markdown('<p class="tagline">Clean. Healing. Naturally Nourishing.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Healing foods & botanicals for modern Botswana")
    st.write(
        "Keto-friendly • Diabetic-conscious • Hormone supportive • Sugar-free & Gluten-free options available. "
        "From our best-selling infused hibiscus and menopause seed granola to pure teas, flours, natural sweeteners and clean snacks."
    )
    st.write("**Located at Athena Gardens, Notwane, Gaborone**")
    
    st.markdown("#### Featured")
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.markdown("""
        <div class="product-card">
            <h4>🌺 Infused Hibiscus</h4>
            <p>Best Seller</p>
            <p class="price">from P 120</p>
        </div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown("""
        <div class="product-card">
            <h4>🌾 Menopause Granola</h4>
            <p>Hormone supportive</p>
            <p class="price">from P 125</p>
        </div>
        """, unsafe_allow_html=True)
    with f3:
        st.markdown("""
        <div class="product-card">
            <h4>🥥 Coconut Flour</h4>
            <p>Sugar & Gluten free</p>
            <p class="price">from P 85</p>
        </div>
        """, unsafe_allow_html=True)
    with f4:
        st.markdown("""
        <div class="product-card">
            <h4>🍯 Lemon Cinnamon Honey</h4>
            <p>Immunity & warmth</p>
            <p class="price">from P 115</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Payment & Shipping":
    st.markdown("## Payment & Shipping")
    
    st.markdown("### Payment Methods")
    st.markdown(f"""
    <div class="payment-box">
        <h4>Orange Money / MyZaka</h4>
        <p>Send payment to: <strong>{ORANGE_MONEY}</strong></p>
        <p>Please use your name as the reference.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="payment-box">
        <h4>Bank Transfer (Absa)</h4>
        <p>
        <strong>Bank:</strong> Absa<br>
        <strong>Account Name:</strong> {ACCOUNT_NAME}<br>
        <strong>Account Number:</strong> {ACCOUNT_NUMBER}<br>
        <strong>Branch Code:</strong> {BRANCH_CODE}
        </p>
        <p>Please use your name as the payment reference.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Shipping & Collection")
    st.markdown(f"""
    <div class="payment-box">
        <h4>Collection at Athena Gardens</h4>
        <p><strong>Free</strong><br>
        Athena Gardens, Notwane, Gaborone</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="payment-box">
        <h4>Delivery within Gaborone</h4>
        <p><strong>P {SHIPPING_FEE}</strong><br>
        Available only on orders over <strong>P {MIN_ORDER_FOR_SHIPPING}</strong>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("After placing your order, please send proof of payment on WhatsApp so we can process it quickly.")

elif page in ["Shop All", "Teas", "Coffee", "Snacks & Cookies", "Flours", "Sweeteners", "Infused Honeys", "Honeys & Oils", "Powders", "Bathing Rituals", "Herbs & Spices"]:
    
    if page == "Shop All":
        filtered = PRODUCTS
        st.markdown("## All Products")
    elif page == "Teas":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Teas"}
        st.markdown("## Healing Teas")
    elif page == "Coffee":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Coffee"}
        st.markdown("## Coffee")
    elif page == "Snacks & Cookies":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Snacks & Cookies"}
        st.markdown("## Snacks & Cookies")
    elif page == "Flours":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Flours"}
        st.markdown("## Sugar-Free & Gluten-Free Flours")
        st.caption("Perfect for keto, banting, diabetic-friendly and hormone-supportive baking")
    elif page == "Sweeteners":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Sweeteners"}
        st.markdown("## Natural Sweeteners")
        st.caption("Whole-food options and zero-calorie alternatives")
    elif page == "Infused Honeys":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Infused Honeys"}
        st.markdown("## Infused Honeys")
        st.caption("Raw honey gently infused with healing botanicals")
    elif page == "Honeys & Oils":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] in ["Infused Honeys", "Oils"]}
        st.markdown("## Infused Honeys & Oils")
    elif page == "Powders":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Powders"}
        st.markdown("## Powders")
    elif page == "Bathing Rituals":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Bathing Rituals"}
        st.markdown("## Bathing & Ritual Teas")
    elif page == "Herbs & Spices":
        filtered = {k:v for k,v in PRODUCTS.items() if v["category"] == "Herbs & Spices"}
        st.markdown("## Herbs & Spices")
    
    st.markdown("---")
    for pid, p in filtered.items():
        show_product(pid, p)
        st.markdown("---")

elif page == "Cart & Order":
    st.markdown("## Your Cart & Order")
    
    if not st.session_state.cart:
        st.info("Your cart is empty. Browse the shop and add items.")
        st.stop()
    
    if st.button("🗑 Clear Entire Cart"):
        clear_cart()
        st.rerun()
    
    st.markdown("### Order Summary")
    
    subtotal = get_cart_total()
    order_lines = []
    
    for key, qty in list(st.session_state.cart.items()):
        parts = key.split("|")
        pid = parts[0]
        size_label = parts[1]
        price = float(parts[2])
        p = PRODUCTS[pid]
        line_total = price * qty
        order_lines.append(f"• {p['name']} ({size_label}) × {qty} = P {line_total:.0f}")
        
        col1, col2, col3 = st.columns([3.5, 1.2, 1])
        with col1:
            st.markdown(f"""
            <div class="cart-item">
                <strong>{p['name']}</strong><br>
                <span style="font-size:0.85rem; color:#666;">{size_label}</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.write(f"Qty: **{qty}**")
            st.write(f"P {line_total:.0f}")
        with col3:
            if st.button("Remove", key=f"rm_{key}"):
                remove_from_cart(key)
                st.rerun()
    
    st.markdown("---")
    st.write(f"**Subtotal:** P {subtotal:.2f}")
    
    shipping_choice = st.radio(
        "How would you like to receive your order?",
        ["Collection at Athena Gardens (Free)", f"Delivery within Gaborone (P{SHIPPING_FEE})"],
        index=0
    )
    
    shipping_cost = 0
    if "Delivery" in shipping_choice:
        if subtotal >= MIN_ORDER_FOR_SHIPPING:
            shipping_cost = SHIPPING_FEE
            st.success(f"Delivery available — P{SHIPPING_FEE} will be added.")
        else:
            st.warning(f"Delivery is only available on orders over P{MIN_ORDER_FOR_SHIPPING}. Please choose Collection or add more items.")
            shipping_choice = "Collection at Athena Gardens (Free)"
    
    total = subtotal + shipping_cost
    st.markdown(f"### Total: **P {total:.2f}**")
    
    st.markdown("### Customer Details")
    with st.form("order_form"):
        name = st.text_input("Full Name *")
        phone = st.text_input("WhatsApp Number *", placeholder="+267 7X XXX XXX")
        email = st.text_input("Email (optional)")
        address = st.text_area("Delivery address (only if choosing delivery)", placeholder="Full address in Gaborone")
        notes = st.text_area("Special instructions (optional)")
        
        submitted = st.form_submit_button("Place Order via WhatsApp", use_container_width=True)
        
        if submitted:
            if not name or not phone:
                st.error("Please fill in your name and WhatsApp number.")
            else:
                message = f"""*New Order – Saina Naturals*

*Customer:* {name}
*WhatsApp:* {phone}
{f'*Email:* {email}' if email else ''}
*Fulfilment:* {shipping_choice}
{f'*Delivery Address:* {address}' if address and 'Delivery' in shipping_choice else ''}
{f'*Notes:* {notes}' if notes else ''}

*Order Details:*
"""
                for line in order_lines:
                    message += line + "\n"
                
                message += f"""
Subtotal: P {subtotal:.0f}
Shipping: P {shipping_cost:.0f}
*Total: P {total:.0f}*

*Payment Options:*
• Orange Money / MyZaka: {ORANGE_MONEY}
• Absa Bank Transfer
  Account Name: {ACCOUNT_NAME}
  Account Number: {ACCOUNT_NUMBER}
  Branch Code: {BRANCH_CODE}

Please pay and send proof of payment on this chat.
We will confirm and arrange your order.

Thank you!
Saina Naturals – Athena Gardens, Notwane
"""
                
                wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
                
                st.success("Order ready!")
                st.markdown(f"""
                <a href="{wa_url}" target="_blank">
                    <button style="background-color:#25D366; color:white; padding:14px 24px; 
                    border:none; border-radius:8px; font-size:1.1rem; cursor:pointer; width:100%;">
                        📱 Open WhatsApp & Send Order
                    </button>
                </a>
                """, unsafe_allow_html=True)
                st.info("Click the green button. WhatsApp will open with the full order + payment details. Just press Send, then send your proof of payment.")

# Footer
st.markdown("---")
st.markdown(
    f"<p style='text-align:center; color:{OLIVE}; font-size:0.85rem;'>"
    "Saina Naturals · Athena Gardens, Notwane, Gaborone · 267 74 501 880</p>",
    unsafe_allow_html=True
)
