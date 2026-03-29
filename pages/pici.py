import streamlit as st
st.set_page_config(page_title="Pici al Ragù — SAVOUR", page_icon="🍽️", layout="wide")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap');
.stApp{background-color:#faf6f1}[data-testid="stSidebar"]{display:none}
.recipe-hero{text-align:center;padding:40px 20px;background:linear-gradient(180deg,rgba(168,136,100,0.12) 0%,rgba(250,246,241,1) 100%)}
.recipe-emoji{font-size:5rem}.recipe-title{font-family:'Playfair Display',serif;font-size:2.5rem;color:#5a3e2b;margin:15px 0 5px}
.recipe-tag{font-family:'Inter',sans-serif;font-size:0.85rem;color:#a08872;letter-spacing:4px;text-transform:uppercase}
.divider{width:60px;height:2px;background:#a88864;margin:20px auto}
.img-placeholder-large{width:100%;height:350px;border-radius:16px;background:linear-gradient(135deg,#e8ddd3,#d4c4b0,#c9b99a);display:flex;align-items:center;justify-content:center;font-size:6rem;margin:20px 0;box-shadow:0 8px 30px rgba(107,79,58,0.12)}
.info-card{background:#fff;border-radius:12px;padding:20px;text-align:center;border:1px solid rgba(168,136,100,0.15)}
.info-num{font-family:'Playfair Display',serif;font-size:1.5rem;color:#6b4f3a;font-weight:700}
.info-label{font-family:'Inter',sans-serif;font-size:0.7rem;color:#a08872;letter-spacing:2px;text-transform:uppercase}
.section-head{font-family:'Playfair Display',serif;font-size:1.5rem;color:#5a3e2b;border-left:4px solid #a88864;padding-left:15px;margin:30px 0 15px}
.ingredient-item{font-family:'Inter',sans-serif;font-size:0.95rem;color:#5a3e2b;padding:8px 0;border-bottom:1px solid rgba(168,136,100,0.12)}
.step-item{font-family:'Inter',sans-serif;font-size:0.95rem;color:#5a3e2b;padding:12px 0;border-bottom:1px solid rgba(168,136,100,0.12);line-height:1.7}
.step-num{display:inline-block;width:28px;height:28px;background:#6b4f3a;color:#faf6f1;border-radius:50%;text-align:center;line-height:28px;font-size:0.8rem;margin-right:10px;font-weight:600}
.nutrition-card{background:#fff;border-radius:12px;padding:20px;border:1px solid rgba(168,136,100,0.15)}
.nutrition-row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(168,136,100,0.08);font-family:'Inter',sans-serif;font-size:0.9rem;color:#5a3e2b}
.nutrition-val{font-weight:600;color:#6b4f3a}
</style>""", unsafe_allow_html=True)

if st.button("← Zurück zur Übersicht"): st.switch_page("app.py")
st.markdown('<div class="recipe-hero"><div class="recipe-emoji">🍝</div><div class="recipe-title">Pici al Ragù</div><div class="recipe-tag">Italienisch</div><div class="divider"></div></div>', unsafe_allow_html=True)
st.markdown('<div class="img-placeholder-large">📸</div>', unsafe_allow_html=True)
c1,c2,c3=st.columns(3)
with c1: st.markdown('<div class="info-card"><div class="info-num">3 Std</div><div class="info-label">Zubereitungszeit</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="info-card"><div class="info-num">4</div><div class="info-label">Portionen</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="info-card"><div class="info-num">580 kcal</div><div class="info-label">Pro Portion</div></div>', unsafe_allow_html=True)
col1,col2=st.columns([3,2])
with col1:
    st.markdown('<div class="section-head">Zubereitung</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">1</span>Mehl, Wasser und Olivenöl zu einem glatten Teig verkneten. 30 Min ruhen lassen.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">2</span>Kleine Stücke abreißen und mit den Handflächen zu langen, dicken Nudeln rollen.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">3</span>Für das Ragù: Gemüse fein hacken und in Olivenöl anschwitzen.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">4</span>Fleisch scharf anbraten, mit Rotwein ablöschen, einkochen lassen.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">5</span>Tomaten und Kräuter dazu, bei niedriger Hitze 2-3 Stunden köcheln.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">6</span>Pici in Salzwasser 3-4 Minuten kochen, al dente abgießen.</div>', unsafe_allow_html=True)
    st.markdown('<div class="step-item"><span class="step-num">7</span>Mit Ragù vermengen und mit frisch geriebenem Pecorino servieren.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="section-head">Zutaten</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 400g Mehl (Tipo 00)</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 200ml Wasser</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 2 EL Olivenöl</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 500g Wildschweingulasch</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 1 Dose San Marzano Tomaten</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 2 Karotten, 2 Selleriestangen</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 1 Zwiebel</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• 200ml Rotwein</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• Rosmarin, Lorbeer, Knoblauch</div>', unsafe_allow_html=True)
    st.markdown('<div class="ingredient-item">• Pecorino zum Servieren</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-head">Nährwerte</div>', unsafe_allow_html=True)
    st.markdown('<div class="nutrition-card"><div class="nutrition-row"><span>Kalorien</span><span class="nutrition-val">580 kcal</span></div><div class="nutrition-row"><span>Protein</span><span class="nutrition-val">28g</span></div><div class="nutrition-row"><span>Kohlenhydrate</span><span class="nutrition-val">65g</span></div><div class="nutrition-row"><span>Fett</span><span class="nutrition-val">22g</span></div></div>', unsafe_allow_html=True)
