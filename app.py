import streamlit as st
from pathlib import Path

# =========================================================
# PAGE
# =========================================================
st.set_page_config(
    page_title="Fauji Zarai Markaz",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# GOOGLE SEARCH CONSOLE VERIFICATION
# =========================================================
st.markdown(
    '<meta name="google-site-verification" content="Nm0V2swZXkUgdpHNnaluO6JRzlPc3Jaj3qlhonrDsRs" />',
    unsafe_allow_html=True
)

BASE = Path(__file__).parent


def image_file(name):
    p = BASE / name
    return str(p) if p.exists() and p.stat().st_size > 0 else None


# =========================================================
# STATE / NAVIGATION
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "HOME"


def go(page):
    st.session_state.page = page


# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
.stApp {
    background:#fff;
}

.block-container {
    max-width:1450px;
    padding-top:0.6rem;
    padding-bottom:0;
}

.topbar {
    background:#005323;
    color:white;
    padding:10px 22px;
    border-radius:0 0 5px 5px;
    font-weight:700;
    font-size:15px;
}

.topbar-flex {
    display:flex;
    justify-content:space-between;
    gap:20px;
}

.brand {
    color:#075126;
    font-size:40px;
    font-weight:900;
    line-height:1.05;
}

.urdu {
    color:#08732f;
    font-size:25px;
    font-weight:800;
    margin-top:7px;
}

.green-box {
    background:#005323;
    color:white;
    padding:16px;
    border-radius:10px;
    text-align:center;
    min-height:105px;
}

.trust {
    text-align:center;
    color:#555;
    font-size:13px;
}

.trust-icon {
    font-size:25px;
}

.section-title {
    color:#075126;
    font-size:27px;
    font-weight:900;
    text-align:center;
    margin:20px 0 12px;
}

.section-title:before,
.section-title:after {
    content:"  ───  ";
    color:#0a7435;
}

.hero {
    background:linear-gradient(90deg,#f7f7f2,#fff);
    border-radius:10px;
    padding:24px 20px 18px;
    border:1px solid #eee;
}

.hero-title {
    color:#075126;
    font-size:34px;
    font-weight:900;
    line-height:1.05;
}

.hero-sub {
    font-size:22px;
    font-weight:800;
    margin-top:12px;
}

.pest-pill {
    background:#fff;
    border-radius:30px;
    padding:7px 12px;
    border:1px solid #eee;
    margin:3px;
    text-align:center;
}

.delivery {
    background:#f7fbf7;
    border:1px solid #dcebdd;
    padding:14px 8px;
    border-radius:8px;
    text-align:center;
}

.card {
    background:white;
    border:1px solid #e4e4e4;
    border-radius:10px;
    padding:16px;
    height:100%;
    box-shadow:0 2px 9px rgba(0,0,0,.05);
}

.product-card {
    background:#fff;
    border:1px solid #e2e2e2;
    border-radius:10px;
    padding:10px;
    text-align:center;
    min-height:285px;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
}

.crop {
    text-align:center;
    font-weight:700;
}

.crop-icon {
    width:70px;
    height:70px;
    border-radius:50%;
    margin:auto;
    display:flex;
    align-items:center;
    justify-content:center;
    background:#edf7ed;
    font-size:38px;
}

.footer {
    background:#005323;
    color:white;
    padding:20px;
    border-radius:7px 7px 0 0;
}

.small {
    font-size:13px;
    color:#555;
}

.stButton > button {
    border-radius:7px !important;
    border:1px solid #d8d8d8 !important;
    background:white !important;
    color:#222 !important;
    font-weight:700 !important;
    min-height:42px !important;
}

.nav-active > button {
    background:#006329 !important;
    color:white !important;
}

div[data-testid="stImage"] img {
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)
   
# =========================================================
# TOP BAR
# =========================================================
st.markdown("""
<div class="topbar">
  <div class="topbar-flex">
    <span>📍 Makkuana, Faisalabad, Punjab, Pakistan</span>
    <span>☎ 0300-9666803 &nbsp;|&nbsp; 0333-9666803</span>
    <span>🕐 Mon - Thu: 9:00 AM - 6:00 PM &nbsp; | &nbsp; Friday: 9:00 AM - 12:00 PM &nbsp; | &nbsp; Sat - Sun: 9:00 AM - 6:00 PM</span>
  </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================
h1, h2, h3, h4 = st.columns([1.1, 4.3, 1.8, 4.2])

with h1:
    logo = image_file("logo.png")

    if logo:
        st.image(logo, width=105)
    else:
        st.markdown(
            "<div style='font-size:70px'>🌾</div>",
            unsafe_allow_html=True
        )

with h2:
    st.markdown(
        '<div class="brand">FAUJI ZARAI MARKAZ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="urdu">فوجی زرعی مرکز</div>',
        unsafe_allow_html=True
    )

    st.write("Pesticides, Seeds & Agricultural Solutions")

with h3:
    st.markdown("""
<div class="green-box" dir="rtl">
  <div style="font-size:20px;font-weight:900;line-height:1.7;">
    کھاد، کھل اور زرعی ادویات دستیاب ہیں
  </div>

  <div style="font-size:18px;font-weight:900;margin-top:8px;line-height:1.7;">
    معلومات کے لیے رابطہ کریں
  </div>

  <div style="font-size:17px;font-weight:900;margin-top:8px;direction:ltr;">
    0300-9666803 / 0333-9666803
  </div>

  <div style="font-size:22px;margin-top:8px;direction:ltr;">
    ⭐⭐⭐⭐⭐
  </div>
</div>
""", unsafe_allow_html=True)

with h4:
    t1, t2, t3, t4 = st.columns(4)

    with t1:
        st.markdown(
            '<div class="trust"><div class="trust-icon">🛡️</div><b>100% Original</b><br>Genuine Products</div>',
            unsafe_allow_html=True
        )

    with t2:
        st.markdown(
            '<div class="trust"><div class="trust-icon">🌿</div><b>Better Quality</b><br>Premium Quality</div>',
            unsafe_allow_html=True
        )

    with t3:
        st.markdown(
            '<div class="trust"><div class="trust-icon">👨‍🌾</div><b>Expert Advice</b><br>Agriculture Experts</div>',
            unsafe_allow_html=True
        )

    with t4:
        st.markdown(
            '<div class="trust"><div class="trust-icon">🚚</div><b>Fast Delivery</b><br>With Care</div>',
            unsafe_allow_html=True
        )


# =========================================================
# NAVIGATION
# =========================================================
nav_names = [
    "HOME",
    "ABOUT US",
    "PRODUCTS",
    "CROPS",
    "INSECTS",
    "GALLERY",
    "BLOG",
    "CONTACT"
]

nav_cols = st.columns(8)

for col, name in zip(nav_cols, nav_names):

    with col:

        if st.button(
            name,
            use_container_width=True,
            key=f"nav_{name}"
        ):
            go(name)

st.markdown("---")


# =========================================================
# HOME
# =========================================================
if st.session_state.page == "HOME":

    # =====================================================
    # TOP CONTACT MESSAGE
    # =====================================================
    st.markdown(
        '<div style="background:#005323;color:white;text-align:center;padding:12px 15px;border-radius:8px;margin-bottom:15px;">'
        '<div style="font-size:18px;font-weight:800;">For more products, please contact us: 0300-9666803 / 0333-9666803</div>'
        '<div style="font-size:18px;font-weight:800;margin-top:5px;">مزید مصنوعات کے لیے رابطہ کریں: 0300-9666803 / 0333-9666803</div>'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # HERO
    # =====================================================
    st.markdown("""
<div class="hero">

  <div class="hero-title">
    COMPLETE CROP<br>PROTECTION
  </div>

  <div style="
      font-size:20px;
      font-weight:800;
      color:#222;
      margin-top:10px;
  ">
    ALL PRODUCTS ARE AVAILABLE FOR CROP PROTECTION
  </div>

  <div style="
      font-size:21px;
      font-weight:800;
      color:#08732f;
      margin-top:6px;
  ">
    فصلوں کی حفاظت کے لیے تمام مصنوعات دستیاب ہیں
  </div>

  <div style="
      font-size:16px;
      font-weight:700;
      color:#444;
      margin-top:9px;
  ">
    HERBICIDES • PESTICIDES • FERTILIZERS • SEEDS
  </div>

  <div style="
      font-size:16px;
      font-weight:700;
      color:#08732f;
      margin-top:5px;
  ">
    جڑی بوٹی مار ادویات • کیڑے مار ادویات • کھادیں • بیج
  </div>

  <div class="hero-sub">
    FOR BETTER GROWTH<br>& HIGHER YIELD
  </div>

</div>
""", unsafe_allow_html=True)


    # =====================================================
    # PRODUCTS - SHOWN DIRECTLY ON HOME
    # =====================================================
    st.markdown(
        '<div class="section-title">OUR PRODUCTS</div>',
        unsafe_allow_html=True
    )

    product_data = [
        (
            "potexin.png",
            "Potexin Sop",
            "Water Soluble Fertilizer"
        ),
        (
            "bag.png",
            "Fauji Kheel Banola",
            "High Quality Cattle Feed"
        ),
        (
            "dap.png",
            "D.A.P (Sona)",
            "18-46-0 Fertilizer"
        ),
        (
            "agri-products.png",
            "Pesticides",
            "Crop Protection"
        ),
        (
            "exin-products.png",
            "Seeds",
            "High Yield Seed"
        ),
        (
            "animal-feed-bags.png",
            "Micronutrients",
            "Balanced Nutrition"
        )
    ]

    pc = st.columns(3)

    for i, (fn, title, desc) in enumerate(product_data):

        with pc[i % 3]:

            pic = image_file(fn)

            if pic:
                st.image(
                    pic,
                    use_container_width=True
                )

            else:
                st.markdown(
                    """
<div style="
    height:180px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:50px;
    border:1px solid #e2e2e2;
    border-radius:10px;
    background:#ffffff;
">
    🌿
</div>
""",
                    unsafe_allow_html=True
                )

            st.markdown(
                f"""
<div style="
    text-align:center;
    font-weight:800;
    font-size:17px;
    margin-top:8px;
    color:#075126;
">
    {title}
</div>
""",
                unsafe_allow_html=True
            )

            st.caption(desc)

            if st.button(
                "VIEW DETAILS",
                key=f"prod_{i}",
                use_container_width=True
            ):
                go("PRODUCTS")


    # =====================================================
    # NEARBY AREAS / DELIVERY
    # =====================================================
    st.markdown("---")

    st.markdown("""
<div class="delivery">
    🚚<br>
    <b>Delivery Available - Nearby Areas</b><br>
    <b>Minimum Delivery Charges: Rs. 500</b>
</div>
""", unsafe_allow_html=True)


    # =====================================================
    # ABOUT / WHY / SHOP
    # =====================================================
    st.markdown(
        '<div class="section-title">FAUJI ZARAI MARKAZ</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns([1.3, 1.0, 1.0])

    with a:

        st.markdown("""
<div class="card">
<h3>ABOUT FAUJI ZARAI MARKAZ</h3>

<p>
Fauji Zarai Markaz is your trusted partner in modern agriculture.
We provide pesticides, fertilizers, seeds and crop solutions with
practical guidance to help farmers achieve higher yield and better quality.
</p>

<b>✓ 100% Original Products</b><br>
<b>✓ Quality Agricultural Products</b><br>
<b>✓ Expert Guidance</b>

</div>
""", unsafe_allow_html=True)

    with b:

        st.markdown("""
<div class="card">
<h3>WHY CHOOSE US?</h3>

✓ Original & Genuine Products<br><br>
✓ Best Quality at Reasonable Rates<br><br>
✓ Expert Agriculture Advice<br><br>
✓ Timely Delivery with Care<br><br>
✓ Trusted by Farmers

</div>
""", unsafe_allow_html=True)

    with c:

        st.markdown(
            '<div class="card"><h3>VISIT OUR SHOP</h3></div>',
            unsafe_allow_html=True
        )

        shop = image_file("shop.png")

        if shop:
            st.image(
                shop,
                use_container_width=True
            )
        else:
            st.info("shop.png yahan rakhein.")

        st.markdown("""
<a href="https://www.google.com/maps/dir/?api=1&destination=Fauji+Zarai+Markaz%2C+96P2%2B6Q%2C+Makkuana%2C+Pakistan"
target="_blank"
style="
display:block;
width:100%;
padding:11px 20px;
background:white;
color:#222;
border:1px solid #d8d8d8;
border-radius:7px;
text-align:center;
text-decoration:none;
font-weight:700;
font-size:16px;
box-sizing:border-box;
">
📍 GET DIRECTIONS
</a>
""", unsafe_allow_html=True)


    # =====================================================
    # CROPS
    # =====================================================
    st.markdown(
        '<div class="section-title">CROPS WE PROTECT</div>',
        unsafe_allow_html=True
    )

    crops = [
        ("🌾", "Wheat"),
        ("🌱", "Rice"),
        ("🌿", "Cotton"),
        ("🎋", "Sugarcane"),
        ("🌽", "Maize"),
        ("🥬", "Vegetables"),
        ("🍎", "Fruits"),
        ("🫘", "Pulses")
    ]

    cc = st.columns(8)

    for col, (icon, name) in zip(cc, crops):

        with col:

            st.markdown(
                f'<div class="crop"><div class="crop-icon">{icon}</div>{name}</div>',
                unsafe_allow_html=True
            )


    # =====================================================
    # BOTTOM INFO
    # =====================================================
    st.markdown("---")

    q1, q2, q3 = st.columns(3)


    # =====================================================
    # CONTACT US
    # =====================================================
    with q1:

        st.markdown("""
<div class="card">
<h3>CONTACT US</h3>

<div style="font-size:16px;line-height:2.2;">

☎ <a href="tel:03009666803" style="color:#075126;text-decoration:none;font-weight:700;">
0300-9666803
</a><br>

☎ <a href="tel:03339666803" style="color:#075126;text-decoration:none;font-weight:700;">
0333-9666803
</a><br>

✉ <a href="mailto:faujizaraimarkaz@gmail.com" style="color:#075126;text-decoration:none;font-weight:700;">
faujizaraimarkaz@gmail.com
</a><br>

📍 Makkuana, Faisalabad, Punjab, Pakistan

</div>
</div>
""", unsafe_allow_html=True)


    # =====================================================
    # SHOP TIMINGS
    # =====================================================
    with q2:

        st.markdown("""
<div class="card">
<h3>SHOP TIMINGS</h3>

🕐 Monday - Thursday<br>
<b>9:00 AM - 6:00 PM</b><br><br>

🕐 Friday<br>
<b>9:00 AM - 12:00 PM</b><br><br>

🕐 Saturday - Sunday<br>
<b>9:00 AM - 6:00 PM</b><br><br>

🟢 Open Now

</div>
""", unsafe_allow_html=True)


    # =====================================================
    # FIND US
    # =====================================================
    with q3:

        st.markdown("""
<div class="card">
<h3>FIND US</h3>

📍 <b>Fauji Zarai Markaz</b><br>
96P2+6Q, Makkuana, Pakistan<br><br>

<a href="https://www.google.com/maps/search/?api=1&query=Fauji+Zarai+Markaz%2C+96P2%2B6Q%2C+Makkuana%2C+Pakistan"
target="_blank"
style="
display:inline-block;
padding:9px 14px;
background:#005323;
color:white;
border-radius:7px;
text-decoration:none;
font-weight:700;
">
🗺️ OPEN SHOP LOCATION
</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# OTHER PAGES
# =========================================================

elif st.session_state.page == "ABOUT US":

    st.markdown(
        '<div class="section-title">ABOUT FAUJI ZARAI MARKAZ</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
<div class="card">

<h2>فوجی زرعی مرکز</h2>

<p>
Fauji Zarai Markaz provides agricultural products and crop protection
solutions for farmers. Our range includes pesticides, fertilizers,
seeds, cattle-feed products and other agricultural supplies.
</p>

<p>
<b>Our focus:</b> original products, quality service, practical advice
and reliable delivery.
</p>

</div>
""", unsafe_allow_html=True)


elif st.session_state.page == "PRODUCTS":

    st.markdown(
        '<div class="section-title">OUR PRODUCTS</div>',
        unsafe_allow_html=True
    )

    data = [
        (
            "potexin.png",
            "Potexin Sop",
            "Water Soluble Fertilizer"
        ),
        (
            "bag.png",
            "Fauji Kheel Banola",
            "Cattle Feed"
        ),
        (
            "dap.png",
            "D.A.P (Sona)",
            "18-46-0 Fertilizer"
        ),
        (
            "agri-products.png",
            "Pesticides",
            "Crop Protection"
        ),
        (
            "exin-products.png",
            "Seeds",
            "High Yield Seeds"
        ),
        (
            "animal-feed-bags.png",
            "Micronutrients",
            "Plant Nutrition"
        )
    ]

    cols = st.columns(3)

    for i, (fn, title, desc) in enumerate(data):

        with cols[i % 3]:

            pic = image_file(fn)

            if pic:
                st.image(
                    pic,
                    use_container_width=True
                )

            st.markdown(
                f"### {title}"
            )

            st.write(desc)

            st.markdown("---")


elif st.session_state.page == "CROPS":

    st.markdown(
        '<div class="section-title">CROPS WE PROTECT</div>',
        unsafe_allow_html=True
    )

    crops = [
        ("🌾", "Wheat"),
        ("🌱", "Rice"),
        ("🌿", "Cotton"),
        ("🎋", "Sugarcane"),
        ("🌽", "Maize"),
        ("🥬", "Vegetables"),
        ("🍎", "Fruits"),
        ("🫘", "Pulses")
    ]

    cols = st.columns(4)

    for i, (icon, name) in enumerate(crops):

        with cols[i % 4]:

            st.markdown(
                f'<div class="card" style="text-align:center;font-size:55px">{icon}<br><b style="font-size:20px">{name}</b></div>',
                unsafe_allow_html=True
            )


elif st.session_state.page == "INSECTS":

    st.markdown(
        '<div class="section-title">INSECTS & CROP PROTECTION</div>',
        unsafe_allow_html=True
    )

    insects = [
        "Aphids",
        "Whitefly",
        "Thrips",
        "Stem Borer",
        "Leaf Miner",
        "Fruit Fly",
        "Army Worm",
        "Mites"
    ]

    cols = st.columns(4)

    for i, name in enumerate(insects):

        with cols[i % 4]:

            st.markdown(
                f'<div class="card" style="text-align:center;font-size:35px">🐛<br><b style="font-size:18px">{name}</b></div>',
                unsafe_allow_html=True
            )


elif st.session_state.page == "GALLERY":

    st.markdown(
        '<div class="section-title">GALLERY</div>',
        unsafe_allow_html=True
    )

    imgs = [
        "logo.png",
        "potexin.png",
        "bag.png",
        "dap.png",
        "shop.png",
        "agri-products.png",
        "exin-products.png",
        "animal-feed-bags.png"
    ]

    cols = st.columns(4)

    for i, fn in enumerate(imgs):

        with cols[i % 4]:

            pic = image_file(fn)

            if pic:

                st.image(
                    pic,
                    use_container_width=True
                )

            else:

                st.info(fn)


elif st.session_state.page == "BLOG":

    st.markdown(
        '<div class="section-title">AGRICULTURE BLOG</div>',
        unsafe_allow_html=True
    )

    posts = [
        (
            "🌾",
            "Better Crop Protection",
            "Choose crop protection products according to the crop and pest problem."
        ),
        (
            "💧",
            "Fertilizer Management",
            "Use fertilizers according to soil and crop requirements."
        ),
        (
            "🐛",
            "Insect Management",
            "Early identification of insects helps reduce crop losses."
        )
    ]

    for icon, title, text in posts:

        st.markdown(
            f'<div class="card"><h2>{icon} {title}</h2><p>{text}</p></div><br>',
            unsafe_allow_html=True
        )


elif st.session_state.page == "CONTACT":

    st.markdown(
        '<div class="section-title">CONTACT US</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
<div class="card">

<h2>Fauji Zarai Markaz</h2>

📍 Makkuana, Faisalabad, Punjab, Pakistan<br><br>

☎ 0300-9666803<br>

☎ 0333-9666803<br><br>

✉ <a href="mailto:faujizaraimarkaz@gmail.com" style="color:#075126;text-decoration:none;font-weight:700;">
faujizaraimarkaz@gmail.com
</a><br><br>

🚚 Delivery Available — Nearby Areas<br>
<b>Minimum Delivery Charges: Rs. 500</b>

</div>
""", unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class="card">
<h3>SHOP LOCATION</h3>

📍 <b>Fauji Zarai Markaz</b><br>
96P2+6Q, Makkuana, Pakistan<br><br>

<a href="https://www.google.com/maps/search/?api=1&query=Fauji+Zarai+Markaz%2C+96P2%2B6Q%2C+Makkuana%2C+Pakistan"
target="_blank"
style="
display:inline-block;
padding:10px 16px;
background:#005323;
color:white;
border-radius:7px;
text-decoration:none;
font-weight:700;
">
🗺️ OPEN IN GOOGLE MAPS
</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    '<div style="background:#005323;color:white;padding:28px 20px;border-radius:10px 10px 0 0;text-align:center;">'
    '<h2 style="font-size:28px;font-weight:900;margin:0 0 8px 0;">🌾 FAUJI ZARAI MARKAZ</h2>'
    '<div style="font-size:19px;font-weight:700;margin-bottom:12px;">فوجی زرعی مرکز</div>'
    '<div style="font-size:15px;color:#d9f2df;margin-bottom:15px;">Pesticides • Herbicides • Fertilizers • Seeds</div>'
    '<div style="font-size:16px;font-weight:700;margin-bottom:10px;">☎ 0300-9666803 &nbsp; | &nbsp; ☎ 0333-9666803</div>'
    '<div style="font-size:14px;color:#d9f2df;margin-bottom:15px;">📍 Makkuana, Faisalabad, Punjab, Pakistan</div>'
    '<div style="font-size:16px;font-weight:700;margin-bottom:6px;">For more products, please contact us</div>'
    '<div style="font-size:17px;color:#d9f2df;font-weight:700;margin-bottom:15px;">مزید مصنوعات کے لیے ہم سے رابطہ کریں</div>'
    '<div style="font-size:13px;color:#bfe0c7;border-top:1px solid rgba(255,255,255,0.2);padding-top:12px;">© 2026 Fauji Zarai Markaz • All Rights Reserved</div>'
    '</div>',
    unsafe_allow_html=True
)
