import streamlit as st

st.set_page_config(page_title="SAVOUR — Foodie Channel", page_icon="🍽️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap');
    
    .stApp { background-color: #faf6f1; }
    [data-testid="stSidebar"] { display: none; }
    
    .hero {
        text-align: center; padding: 80px 20px 40px;
        background: linear-gradient(180deg, rgba(168,136,100,0.12) 0%, rgba(250,246,241,1) 100%);
    }
    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 4.5rem; font-weight: 900;
        letter-spacing: 12px; color: #6b4f3a;
    }
    .tagline {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem; font-weight: 300;
        color: #a08872; letter-spacing: 6px;
        text-transform: uppercase; margin-top: 5px;
    }
    .divider {
        width: 60px; height: 2px; background: #a88864;
        margin: 30px auto;
    }
    .intro {
        font-family: 'Inter', sans-serif;
        font-size: 1rem; color: #8a7565;
        max-width: 600px; margin: 0 auto;
        line-height: 1.8; text-align: center;
    }
    
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem; color: #5a3e2b;
        text-align: center; margin: 60px 0 10px;
    }
    .section-sub {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem; color: #a08872;
        text-align: center; letter-spacing: 4px;
        text-transform: uppercase; margin-bottom: 30px;
    }
    
    .food-card {
        background: #fff; border-radius: 16px;
        padding: 0; overflow: hidden;
        box-shadow: 0 4px 20px rgba(107,79,58,0.08);
        border: 1px solid rgba(168,136,100,0.15);
        margin-bottom: 15px;
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
    }
    .food-card:hover { 
        transform: translateY(-4px); 
        box-shadow: 0 8px 30px rgba(107,79,58,0.15);
    }
    .img-placeholder {
        width: 100%; height: 200px;
        background: linear-gradient(135deg, #e8ddd3, #d4c4b0, #c9b99a);
        display: flex; align-items: center; justify-content: center;
        font-size: 4rem;
    }
    .card-body { padding: 20px; }
    .food-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem; color: #5a3e2b;
        margin-bottom: 8px;
    }
    .food-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem; color: #a08872;
        line-height: 1.6;
    }
    .food-tag {
        display: inline-block; margin-top: 12px;
        padding: 4px 14px; border-radius: 20px;
        font-size: 0.7rem; letter-spacing: 2px;
        text-transform: uppercase; color: #6b4f3a;
        border: 1px solid rgba(168,136,100,0.3);
        font-family: 'Inter', sans-serif;
        background: rgba(168,136,100,0.08);
    }
    
    .stat-card {
        text-align: center; padding: 30px;
        background: #fff; border-radius: 16px;
        box-shadow: 0 4px 20px rgba(107,79,58,0.06);
        border: 1px solid rgba(168,136,100,0.12);
    }
    .stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem; font-weight: 900;
        color: #6b4f3a;
    }
    .stat-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem; color: #a08872;
        letter-spacing: 3px; text-transform: uppercase;
    }
    
    .cta-section {
        text-align: center; padding: 60px 20px;
        background: linear-gradient(180deg, rgba(250,246,241,1) 0%, rgba(168,136,100,0.1) 100%);
        margin-top: 40px;
    }
    .cta-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem; color: #5a3e2b;
    }
    .cta-sub {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem; color: #a08872;
        margin: 10px 0 25px;
    }
    .cta-btn {
        display: inline-block; padding: 14px 40px;
        background: #6b4f3a; color: #faf6f1;
        font-family: 'Inter', sans-serif;
        font-weight: 600; font-size: 0.85rem;
        letter-spacing: 3px; text-transform: uppercase;
        border-radius: 30px; text-decoration: none;
    }
    
    .footer {
        text-align: center; padding: 40px;
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem; color: #c4b5a5;
        letter-spacing: 2px;
    }
    
    a.card-link { text-decoration: none; color: inherit; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="brand">SAVOUR</div>
    <div class="tagline">A culinary journey</div>
    <div class="divider"></div>
    <div class="intro">
        Wir entdecken die schönsten kulinarischen Momente — von Sterneküche bis Street Food, 
        von Tokio bis Toskana. Jedes Gericht erzählt eine Geschichte.
    </div>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown('<div class="section-title">In Zahlen</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Unsere Community wächst</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
for col, (num, label) in zip([c1,c2,c3,c4], [("42K","Followers"),("1.2K","Beiträge"),("28","Länder"),("4.8","⭐ Rating")]):
    with col:
        st.markdown(f'<div class="stat-card"><div class="stat-num">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

# Dishes
st.markdown('<div class="section-title">Unsere Rezepte</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Klicke auf ein Gericht für das volle Rezept</div>', unsafe_allow_html=True)

dishes = [
    {"id": "nigiri", "emoji": "🍣", "name": "Sushi Nigiri", "desc": "Handgeformter Reis mit frischem Fisch — die Essenz japanischer Küche.", "tag": "Japanisch"},
    {"id": "croissant", "emoji": "🥐", "name": "Butter-Croissant", "desc": "72 Stunden Teigführung, echte französische Butter, goldbraun gebacken.", "tag": "Französisch"},
    {"id": "pici", "emoji": "🍝", "name": "Pici al Ragù", "desc": "Handgerollte toskanische Pasta mit langsam geschmortem Wildschein-Ragù.", "tag": "Italienisch"},
    {"id": "tacos", "emoji": "🌮", "name": "Tacos al Pastor", "desc": "Mariniertes Schweinefleisch vom Drehspieß mit karamellisierter Ananas.", "tag": "Mexikanisch"},
    {"id": "cheesecake", "emoji": "🍰", "name": "Basque Cheesecake", "desc": "Verbrannt, cremig, unwiderstehlich. Das Original aus San Sebastián.", "tag": "Spanisch"},
    {"id": "ramen", "emoji": "🍜", "name": "Tonkotsu Ramen", "desc": "36 Stunden Schweineknochenbrühe, Chashu, Ajitama, Nori.", "tag": "Japanisch"},
]

cols = st.columns(3)
for i, dish in enumerate(dishes):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="food-card">
            <div class="img-placeholder">{dish['emoji']}</div>
            <div class="card-body">
                <div class="food-name">{dish['name']}</div>
                <div class="food-desc">{dish['desc']}</div>
                <div class="food-tag">📍 {dish['tag']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"📖 Rezept ansehen", key=dish['id'], use_container_width=True):
            st.switch_page(f"pages/{dish['id']}.py")

# CTA
st.markdown("""
<div class="cta-section">
    <div class="cta-text">Hungry for more?</div>
    <div class="cta-sub">Folge uns auf Instagram für tägliche kulinarische Inspiration.</div>
    <a href="https://instagram.com" class="cta-btn">@savour.food</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">SAVOUR © 2025 · MADE WITH ❤️ AND GOOD TASTE · BUILT BY FRANCOIS 🦾</div>', unsafe_allow_html=True)
