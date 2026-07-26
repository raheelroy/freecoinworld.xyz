import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the CSS block
new_css = """
/* ──────────────────────────────
   DESIGN TOKENS (Vegas Gold & Black)
────────────────────────────── */
:root {
  --bg-base:        #000000; /* Pure black for high contrast */
  --bg-surface:     #080505;
  --bg-card:        #0D0D0D;
  --bg-card-h:      #1A1A1A;
  --bg-panel:       #050505;

  /* Extremely shiny high-contrast gold */
  --gold:           #FFD700;
  --gold-lt:        #FFF8DC;
  --gold-dk:        #B8860B;
  --gold-darker:    #8B6508;
  --gold-glow:      rgba(255, 215, 0, 0.4);
  --gold-border:    #DAA520;
  --gold-border-h:  #FFDF00;

  --red-base:       #8B0000;
  --red-glow:       #FF0000;
  --green:          #27AE60;
  --neon-blue:      #00FFFF;

  --text-h:         #FFFFFF;
  --text-b:         #E0E0E0;
  --text-m:         #A0A0A0;
  --text-faint:     #555555;

  --radius-card:    12px;
  --radius-sm:      6px;
  --transition:     0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* ──────────────────────────────
   RESET & BASE
────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: 'Montserrat', sans-serif;
  background: var(--bg-base);
  color: var(--text-b);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
button { font-family: inherit; cursor: pointer; border: none; }

h1, h2, h3, h4, .playfair {
  font-family: 'Playfair Display', serif;
}

/* ──────────────────────────────
   SUBTLE BACKGROUND TEXTURE & GLITTER
────────────────────────────── */
body::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 70% 70% at 50% 30%, rgba(255, 215, 0, 0.1) 0%, transparent 60%),
    radial-gradient(ellipse 90% 90% at 50% 100%, rgba(139, 0, 0, 0.15) 0%, transparent 80%);
}
body::after {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image: 
    radial-gradient(2px 2px at 20px 30px, #FFF8DC, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 40px 70px, #ffffff, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 50px 160px, #FFD700, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 90px 40px, #ffffff, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 130px 80px, #FFF8DC, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 160px 120px, #FFD700, rgba(0,0,0,0));
  background-repeat: repeat;
  background-size: 200px 200px;
  opacity: 0.3;
}
.site { position: relative; z-index: 1; }

/* ──────────────────────────────
   ALERT BAR
────────────────────────────── */
#alertBar {
  background: linear-gradient(90deg, #111, #222, #111);
  border-bottom: 2px solid var(--gold-border);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 12px 20px;
  font-size: 0.9rem;
  font-weight: 800;
  letter-spacing: 1px;
  color: var(--gold-lt);
  position: relative;
  text-shadow: 0 2px 4px rgba(0,0,0,1);
  box-shadow: 0 4px 15px rgba(255, 215, 0, 0.15);
}
#alertBar .ab-badge {
  background: linear-gradient(to bottom, #FF0000, #8B0000);
  color: #FFF;
  font-size: 0.75rem;
  font-weight: 900;
  letter-spacing: 1px;
  padding: 4px 12px;
  border-radius: 6px;
  text-transform: uppercase;
  border: 1px solid var(--gold);
  box-shadow: 0 2px 10px rgba(255, 0, 0, 0.4);
}
#alertBar .ab-close {
  position: absolute; right: 16px; top: 50%; transform: translateY(-50%);
  background: none; color: var(--gold-dk); font-size: 1.4rem; line-height: 1;
  transition: color var(--transition);
}
#alertBar .ab-close:hover { color: var(--gold-lt); text-shadow: 0 0 8px var(--gold); }

/* ──────────────────────────────
   STICKY HEADER
────────────────────────────── */
header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 2px solid var(--gold-dk);
  box-shadow: 0 10px 30px rgba(0,0,0,0.8), 0 0 15px rgba(218, 165, 32, 0.2);
  transition: background 0.3s;
}
.header-inner {
  max-width: 1300px; margin: 0 auto;
  display: flex; align-items: center; gap: 24px;
  padding: 0 28px; height: 80px;
}
.logo {
  display: flex; align-items: center; gap: 12px;
  flex: 0 0 auto;
}
.logo-mark {
  width: 46px; height: 46px; border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #FFF8DC, #FFD700, #B8860B, #8B6508);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.6rem;
  border: 2px solid #FFF;
  box-shadow: 0 4px 15px rgba(0,0,0,0.8), inset 0 0 10px rgba(255,255,255,0.8);
}
.logo-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.6rem;
  letter-spacing: 1px;
  color: #FFF;
  text-transform: uppercase;
  text-shadow: 2px 2px 4px rgba(0,0,0,1);
}
.logo-name span { 
  background: -webkit-linear-gradient(top, #FFF8DC, #FFD700, #B8860B);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 2px rgba(0,0,0,1));
}

/* Nav tabs */
.header-nav {
  display: flex; align-items: center; gap: 10px;
  flex: 1; justify-content: center;
}
.nav-tab {
  padding: 10px 20px; border-radius: 30px;
  font-size: 0.9rem; font-weight: 800;
  color: var(--gold-dk);
  background: none; text-transform: uppercase; letter-spacing: 1px;
  transition: all var(--transition);
  white-space: nowrap; border: 1px solid transparent;
}
.nav-tab:hover    { color: var(--gold-lt); text-shadow: 0 0 8px var(--gold-glow); }
.nav-tab.active   { color: #000; background: linear-gradient(to bottom, #FFF8DC, #FFD700, #DAA520); border-color: #FFF; box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4); text-shadow: none; }

/* Header right */
.header-right { display: flex; align-items: center; gap: 16px; flex: 0 0 auto; }
.badge-18 {
  border: 2px solid var(--gold-dk);
  color: var(--gold); background: #000;
  font-size: 0.8rem; font-weight: 900;
  padding: 4px 10px; border-radius: 50%;
  width: 36px; height: 36px; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 10px var(--gold-glow);
}
.btn-primary {
  background: linear-gradient(to bottom, #FF0000, #8B0000);
  color: #FFF;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 0.9rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 12px 28px; border-radius: 30px;
  border: 2px solid #FFDF00;
  box-shadow: 0 6px 20px rgba(255, 0, 0, 0.4), inset 0 2px 4px rgba(255,255,255,0.4);
  transition: all var(--transition);
  text-shadow: 0 2px 4px rgba(0,0,0,0.8);
}
.btn-primary:hover {
  transform: translateY(-2px);
  background: linear-gradient(to bottom, #FF3333, #AA0000);
  box-shadow: 0 8px 25px rgba(255, 0, 0, 0.6), 0 0 15px rgba(255, 223, 0, 0.5), inset 0 2px 8px rgba(255,255,255,0.6);
}
.btn-outline {
  border: 2px solid var(--gold);
  color: var(--gold);
  background: rgba(0,0,0,0.5);
  font-family: 'Montserrat', sans-serif;
  font-weight: 800; font-size: 0.9rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 11px 26px; border-radius: 30px;
  transition: all var(--transition);
}
.btn-outline:hover { border-color: var(--gold-lt); color: var(--gold-lt); background: rgba(255, 215, 0, 0.1); box-shadow: 0 0 15px rgba(255, 215, 0, 0.3); }

/* Mobile hamburger */
.hamburger {
  display: none; flex-direction: column; gap: 6px;
  background: none; padding: 4px;
}
.hamburger span { width: 28px; height: 3px; background: var(--gold); border-radius: 2px; }

/* ──────────────────────────────
   FLOATING CASINO ELEMENTS (Hero)
────────────────────────────── */
.floating-chip {
  position: absolute;
  width: 80px; height: 80px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #FF0000, #8B0000);
  border: 8px dashed #FFF;
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8), 0 0 15px rgba(255,0,0,0.3);
  animation: floatChip 6s ease-in-out infinite alternate;
  z-index: 0; pointer-events: none;
}
.floating-chip.blue {
  background: radial-gradient(circle at 30% 30%, #00FFFF, #004B87);
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8), 0 0 15px rgba(0,255,255,0.3);
}
.floating-chip.gold {
  background: radial-gradient(circle at 30% 30%, #FFF8DC, #FFD700, #B8860B);
  border: 6px dashed #111;
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8), 0 0 20px rgba(255,215,0,0.4);
}
.floating-chip::after {
  content: 'FCW';
  position: absolute; inset: 12px;
  border-radius: 50%;
  border: 2px solid #FFF;
  display: flex; align-items: center; justify-content: center;
  color: #FFF; font-weight: 900; font-family: 'Playfair Display', serif;
  font-size: 16px; text-shadow: 1px 1px 2px rgba(0,0,0,1);
}
.floating-chip.gold::after { border-color: #111; color: #111; text-shadow: none; }

.floating-card {
  position: absolute;
  width: 90px; height: 130px;
  background: #FFF;
  border-radius: 8px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 0 4px #000, inset 0 0 0 6px var(--gold);
  animation: floatCard 8s ease-in-out infinite alternate;
  z-index: 0; pointer-events: none;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  color: #8B0000; font-size: 48px; font-weight: bold;
}
.floating-card.spade { color: #000; }
.floating-card::before { content: '♥'; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.floating-card.spade::before { content: '♠'; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.floating-card::after { content: 'A'; position: absolute; top: 8px; left: 10px; font-size: 22px; font-family: 'Playfair Display', serif; }
.floating-card::marker { content: 'A'; position: absolute; bottom: 8px; right: 10px; font-size: 22px; font-family: 'Playfair Display', serif; transform: rotate(180deg); } /* Little trick */

@keyframes floatChip { 
  0% { transform: translateY(0) rotate(0deg) scale(1); } 
  100% { transform: translateY(-50px) rotate(45deg) scale(1.1); } 
}
@keyframes floatCard { 
  0% { transform: translateY(0) rotate(-20deg); } 
  100% { transform: translateY(-60px) rotate(25deg); } 
}

/* ──────────────────────────────
   HERO SECTION
────────────────────────────── */
.hero {
  position: relative;
  max-width: 1300px; margin: 0 auto;
  display: flex; flex-direction: column;
  align-items: center; text-align: center;
  padding: 100px 28px 80px;
}
.hero-content { position: relative; z-index: 2; max-width: 900px; }
.hero-label {
  display: inline-flex; align-items: center; gap: 10px;
  border: 2px solid var(--gold);
  background: rgba(0,0,0,0.8);
  color: var(--gold-lt);
  font-size: 1rem; font-weight: 900;
  letter-spacing: 4px; text-transform: uppercase;
  padding: 10px 24px; border-radius: 40px;
  margin-bottom: 30px;
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), inset 0 0 10px rgba(255, 215, 0, 0.2);
}
.hero-label::before, .hero-label::after { content: '👑'; font-size: 1.2rem; filter: drop-shadow(0 0 5px var(--gold)); }

.hero-title {
  font-family: 'Playfair Display', serif;
  font-weight: 900;
  line-height: 1;
  font-size: clamp(3.5rem, 6vw, 6rem);
  text-transform: uppercase;
  color: #FFF;
  text-shadow: 0 10px 30px rgba(0,0,0,1);
  margin-bottom: 24px;
}
.hero-title .gold { 
  display: block;
  font-size: clamp(4.5rem, 8vw, 8rem);
  background: -webkit-linear-gradient(top, #FFF8DC, #FFD700, #DAA520, #8B6508);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 10px 20px rgba(0,0,0,1)) drop-shadow(0 0 30px rgba(255, 215, 0, 0.4));
  letter-spacing: 2px;
}
.hero-title .outline {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-style: italic;
  font-size: clamp(2rem, 4vw, 3rem);
  -webkit-text-stroke: 2px var(--gold);
  color: transparent;
  letter-spacing: 8px;
  margin-top: 10px;
}

.hero-sub {
  font-size: 1.3rem; line-height: 1.6; font-weight: 600;
  color: var(--text-b); max-width: 700px; margin: 0 auto 40px;
  text-shadow: 0 4px 8px rgba(0,0,0,1);
}

.hero-stats {
  display: flex; gap: 40px; margin: 0 auto 50px;
  background: linear-gradient(to bottom, #1A1A1A, #000); 
  border: 2px solid var(--gold-dk);
  padding: 24px 40px; border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(255, 215, 0, 0.1);
  width: max-content;
}
.hero-stat { display: flex; flex-direction: column; align-items: center; }
.hero-stat-num {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 2.5rem;
  color: #FFF; letter-spacing: 1px;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.5), 0 0 10px var(--gold);
}
.hero-stat-label { font-size: 0.9rem; font-weight: 800; color: var(--gold-lt); text-transform: uppercase; letter-spacing: 2px; margin-top: 6px; }

.hero-ctas { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
.btn-lg { 
  padding: 18px 48px; font-size: 1.2rem; border-radius: 50px; 
  box-shadow: 0 10px 30px rgba(255, 0, 0, 0.5), inset 0 2px 4px rgba(255,255,255,0.4);
}
.btn-lg.btn-outline {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.2);
}
.hero-note { font-size: 0.9rem; color: var(--gold-dk); margin-top: 24px; font-style: italic; font-weight: 600; }

/* ──────────────────────────────
   GAME THUMBNAIL ART (CSS)
────────────────────────────── */
.gt {
  aspect-ratio: 1;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 12px; position: relative; overflow: hidden;
  border-bottom: 4px solid #000;
}
.gt::before { /* inner glow vignette */
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.2) 0%, rgba(0,0,0,0.9) 100%);
  pointer-events: none;
}
.gt-symbol {
  font-size: 4rem; line-height: 1;
  filter: drop-shadow(0 10px 15px rgba(0,0,0,1));
  position: relative; z-index: 1;
}
.gt-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.4rem;
  letter-spacing: 1px; text-align: center;
  color: #fff; text-shadow: 0 4px 10px rgba(0,0,0,1), 0 0 20px rgba(0,0,0,1);
  padding: 0 12px; position: relative; z-index: 1;
  text-transform: uppercase;
}
.gt-sub {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.8rem; font-weight: 900;
  letter-spacing: 3px; color: var(--gold);
  text-transform: uppercase; position: relative; z-index: 1;
  text-shadow: 0 2px 4px #000;
  background: rgba(0,0,0,0.6); padding: 4px 12px; border-radius: 12px;
  border: 1px solid var(--gold-dk);
}

/* ──────────────────────────────
   PROVIDER TICKER
────────────────────────────── */
.provider-strip {
  border-top: 2px solid var(--gold-border);
  border-bottom: 2px solid var(--gold-border);
  background: linear-gradient(to right, #000, #1A1A1A, #000);
  padding: 20px 0;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 0 20px rgba(255, 215, 0, 0.1);
}
.provider-track {
  display: flex; gap: 80px;
  animation: provTicker 40s linear infinite;
  width: max-content;
}
.prov-item {
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 1.4rem;
  letter-spacing: 4px; text-transform: uppercase;
  color: var(--gold-dk);
  text-shadow: 0 2px 4px rgba(0,0,0,1);
  white-space: nowrap;
}

/* ──────────────────────────────
   BONUS STRIP
────────────────────────────── */
.bonus-strip {
  max-width: 1300px; margin: 80px auto 0;
  padding: 0 28px;
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;
}
.bonus-pill {
  background: linear-gradient(135deg, #1A1A1A, #000);
  border: 2px solid var(--gold-dk);
  border-radius: 20px;
  display: flex; align-items: center; gap: 24px;
  padding: 30px 32px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.8), inset 0 0 20px rgba(0,0,0,0.5);
  transition: all var(--transition);
  position: relative;
  overflow: hidden;
}
.bonus-pill::before {
  content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
  background: radial-gradient(circle at center, rgba(255,215,0,0.1) 0%, transparent 60%);
  pointer-events: none;
}
.bonus-pill:hover { 
  transform: translateY(-8px); 
  border-color: var(--gold-border-h); 
  box-shadow: 0 30px 50px rgba(0,0,0,0.9), 0 0 30px rgba(255, 215, 0, 0.3), inset 0 0 30px rgba(255,215,0,0.1);
}
.bp-icon {
  width: 64px; height: 64px; border-radius: 50%; flex: 0 0 auto;
  display: flex; align-items: center; justify-content: center;
  font-size: 2.2rem;
  border: 2px solid var(--gold);
  box-shadow: 0 0 15px rgba(0,0,0,0.8), inset 0 0 15px rgba(255,255,255,0.2);
}
.bp-icon.gold-bg  { background: linear-gradient(135deg, #FFDF00, #B8860B); color: #000; text-shadow: 0 1px 1px rgba(255,255,255,0.5); }
.bp-icon.red-bg   { background: linear-gradient(135deg, #FF0000, #8B0000); color: #FFF; border-color: #FF6666; }
.bp-icon.green-bg { background: linear-gradient(135deg, #00FF00, #008000); color: #FFF; border-color: #66FF66; }
.bp-amount {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 2.2rem; color: #FFF;
  line-height: 1; text-shadow: 0 4px 8px #000, 0 0 15px var(--gold-glow);
}
.bp-label { font-size: 0.9rem; font-weight: 800; color: var(--gold-lt); text-transform: uppercase; letter-spacing: 2px; margin-top: 8px; }

/* ──────────────────────────────
   GAMES SECTION
────────────────────────────── */
.section-wrap { max-width: 1300px; margin: 0 auto; padding: 100px 28px; position: relative; z-index: 2; }
.section-header {
  display: flex; align-items: flex-end; justify-content: space-between;
  margin-bottom: 40px;
  border-bottom: 2px solid var(--gold-dk);
  padding-bottom: 20px;
}
.section-heading {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 2.5rem;
  color: #FFF; text-shadow: 0 4px 10px #000;
  text-transform: uppercase; letter-spacing: 1px;
}
.section-heading span { color: var(--gold); }
.section-sub { font-size: 1rem; font-weight: 700; color: var(--text-m); margin-top: 10px; text-transform: uppercase; letter-spacing: 3px; }
.see-all { font-size: 1rem; font-weight: 900; color: var(--gold); letter-spacing: 2px; text-transform: uppercase; text-shadow: 0 2px 4px #000; }
.see-all:hover { color: #FFF; text-shadow: 0 0 10px var(--gold); }

/* Category tabs */
.cat-tabs { display: flex; gap: 16px; margin-bottom: 40px; flex-wrap: wrap; }
.cat-tab {
  padding: 12px 28px; border-radius: 40px;
  font-size: 0.9rem; font-weight: 900; letter-spacing: 2px; text-transform: uppercase;
  background: #111; border: 2px solid var(--gold-dk);
  color: var(--text-m);
  transition: all var(--transition);
  box-shadow: 0 10px 20px rgba(0,0,0,0.6);
}
.cat-tab:hover  { color: var(--gold-lt); border-color: var(--gold); background: #222; box-shadow: 0 10px 25px rgba(0,0,0,0.8), 0 0 15px rgba(255, 215, 0, 0.2); }
.cat-tab.active { color: #000; border-color: #FFF; background: linear-gradient(to bottom, #FFF8DC, #FFD700, #DAA520); box-shadow: 0 10px 30px rgba(0,0,0,0.8), 0 0 20px rgba(255, 215, 0, 0.5); }

/* ──────────────────────────────
   GAME CARDS GRID
────────────────────────────── */
.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 30px;
}

.game-card {
  background: linear-gradient(to bottom, #1A1A1A, #050505);
  border-radius: var(--radius-card);
  overflow: hidden;
  border: 2px solid var(--gold-dk);
  box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8);
  transition: all var(--transition);
  cursor: pointer;
}
.game-card:hover {
  transform: translateY(-10px);
  border-color: var(--gold-border-h);
  box-shadow: 0 30px 60px rgba(0,0,0,1), 0 0 30px rgba(255, 215, 0, 0.3), inset 0 0 30px rgba(255, 215, 0, 0.1);
}

/* Thumb area with hover overlay */
.card-thumb {
  position: relative; overflow: hidden;
  border-bottom: 2px solid var(--gold-dk);
}
.card-thumb .gt { transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1); }
.game-card:hover .card-thumb .gt { transform: scale(1.1); }
.card-logo-stage {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px;
  background: radial-gradient(circle at 50% 50%, #222, #000);
  transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.game-card:hover .card-logo-stage { transform: scale(1.1); }
.game-logo-crop {
  width: min(240px, 90%);
  aspect-ratio: 1;
  object-fit: contain;
  filter: drop-shadow(0 15px 30px rgba(0,0,0,1));
}

.thumb-overlay {
  position: absolute; inset: 0;
  background: radial-gradient(circle at center, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.95) 100%);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity 0.3s;
}
.game-card:hover .thumb-overlay { opacity: 1; }
.play-btn {
  background: linear-gradient(to bottom, #FF0000, #8B0000);
  color: #FFF;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 1rem;
  letter-spacing: 2px; text-transform: uppercase;
  padding: 16px 36px; border-radius: 40px;
  transform: scale(0.8) translateY(20px); transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 2px solid #FFDF00; box-shadow: 0 15px 30px rgba(0,0,0,0.9), 0 0 15px rgba(255,0,0,0.5);
  text-shadow: 0 2px 4px rgba(0,0,0,0.8);
}
.game-card:hover .play-btn { transform: scale(1) translateY(0); }

/* Card badge */
.card-badge {
  position: absolute; top: 16px; left: 16px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 0.75rem;
  letter-spacing: 2px; text-transform: uppercase;
  padding: 6px 14px; border-radius: 20px;
  z-index: 2; box-shadow: 0 10px 20px rgba(0,0,0,0.8);
  border: 2px solid #FFF;
}
.badge-hot      { background: linear-gradient(to bottom, #FF3333, #AA0000); color: #fff; }
.badge-new      { background: linear-gradient(to bottom, #00FF00, #008000); color: #fff; border-color: #00FF00; }
.badge-featured { background: linear-gradient(to bottom, #FFF8DC, #FFD700); color: #000; border-color: #FFF; }

/* Card info strip */
.card-info { padding: 20px; }
.card-game-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.3rem;
  color: #FFF; letter-spacing: 1px;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  text-shadow: 0 4px 8px #000;
}
.card-provider { font-size: 0.8rem; font-weight: 800; color: var(--gold-dk); margin-top: 6px; text-transform: uppercase; letter-spacing: 2px; }
.card-footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 16px; border-top: 2px solid rgba(255,215,0,0.1); padding-top: 16px;
}
.card-coins { font-size: 0.9rem; font-weight: 900; color: var(--gold); display: flex; align-items: center; gap: 6px; }
.card-coins::before { content: '🪙'; font-size: 1.2rem; filter: drop-shadow(0 2px 2px #000); }
.card-status { width: 10px; height: 10px; border-radius: 50%; background: var(--text-faint); }
.card-status.online { background: #00FF00; box-shadow: 0 0 15px #00FF00; }

/* ──────────────────────────────
   PROMOTIONS
────────────────────────────── */
.promo-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 30px; }
.promo-card {
  border-radius: 24px; overflow: hidden;
  border: 2px solid var(--gold-dk);
  background: linear-gradient(to bottom, #111, #000);
  transition: all var(--transition);
  position: relative;
  box-shadow: 0 30px 60px rgba(0,0,0,0.9);
}
.promo-card:hover { transform: translateY(-10px); box-shadow: 0 40px 80px rgba(0,0,0,1), 0 0 30px rgba(255, 215, 0, 0.2); border-color: var(--gold-border-h); }
.promo-art {
  height: 220px; display: flex; align-items: center; justify-content: center;
  font-size: 5rem; position: relative; overflow: hidden;
  border-bottom: 2px solid var(--gold-dk);
}
.promo-art::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, #000 0%, transparent 100%); }
.promo-art.pa-welcome { background: radial-gradient(circle, #B8860B, #111); }
.promo-art.pa-daily   { background: radial-gradient(circle, #008000, #111); }
.promo-art.pa-refer   { background: radial-gradient(circle, #8B0000, #111); }
.promo-art span { filter: drop-shadow(0 15px 20px rgba(0,0,0,0.8)); position: relative; z-index: 1; }
.promo-body { padding: 30px; text-align: center; }
.promo-title { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.5rem; color: #FFF; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
.promo-amount { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 2.5rem; color: var(--gold); letter-spacing: -1px; margin-bottom: 16px; text-shadow: 0 4px 10px #000, 0 0 15px rgba(255,215,0,0.3); }
.promo-desc { font-size: 1rem; font-weight: 600; color: var(--text-m); line-height: 1.6; margin-bottom: 24px; }
.btn-sm {
  padding: 12px 28px; font-size: 0.9rem; border-radius: 40px;
  font-family: 'Montserrat', sans-serif; font-weight: 900;
  letter-spacing: 2px; text-transform: uppercase;
  display: inline-block;
  box-shadow: 0 10px 20px rgba(255, 0, 0, 0.4);
}

/* ──────────────────────────────
   TRUST / FEATURES
────────────────────────────── */
.trust-section { background: #050505; border-top: 2px solid var(--gold-border); border-bottom: 2px solid var(--gold-border); position: relative; z-index: 2; }
.trust-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; background: var(--gold-dk); }
.trust-cell { background: #0A0A0A; padding: 50px 30px; transition: background var(--transition); text-align: center; }
.trust-cell:hover { background: #111; }
.trust-icon { width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; margin: 0 auto 24px; border: 2px solid var(--gold); background: #000; box-shadow: 0 0 20px rgba(255,215,0,0.2), inset 0 0 15px rgba(0,0,0,0.8); }
.trust-title { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.3rem; color: #FFF; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1px; }
.trust-desc { font-size: 1rem; font-weight: 600; color: var(--text-m); line-height: 1.6; }

/* ──────────────────────────────
   EMAIL CTA
────────────────────────────── */
.cta-section { max-width: 800px; margin: 0 auto; padding: 120px 28px; text-align: center; position: relative; z-index: 2; }
.cta-section .section-heading { font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px; text-shadow: 0 10px 20px rgba(0,0,0,1); }
.cta-section p { font-size: 1.2rem; font-weight: 600; color: var(--text-b); margin-bottom: 40px; line-height: 1.7; }
.email-row { display: flex; gap: 8px; background: rgba(0,0,0,0.8); border: 3px solid var(--gold-dk); border-radius: 50px; padding: 10px 10px 10px 30px; transition: all 0.3s; box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8); }
.email-row:focus-within { border-color: var(--gold-border-h); box-shadow: 0 20px 40px rgba(0,0,0,0.9), inset 0 0 20px rgba(0,0,0,0.8), 0 0 30px rgba(255,215,0,0.3); }
.email-row input { flex: 1; background: none; border: none; outline: none; font-family: 'Montserrat', sans-serif; font-size: 1.1rem; font-weight: 700; color: #FFF; }
.email-row input::placeholder { color: var(--text-faint); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
.cta-note { font-size: 0.9rem; font-weight: 800; color: var(--gold-dk); margin-top: 24px; text-transform: uppercase; letter-spacing: 2px; }

/* ──────────────────────────────
   FOOTER
────────────────────────────── */
footer { background: #000; border-top: 4px solid var(--gold-dk); position: relative; z-index: 2; }
.footer-top { max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: 350px 1fr 1fr 1fr; gap: 60px; padding: 100px 28px 80px; }
.footer-logo-area .logo { margin-bottom: 30px; }
.footer-desc { font-size: 1rem; font-weight: 600; color: var(--text-m); line-height: 1.8; }
.footer-col h4 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.2rem; letter-spacing: 3px; text-transform: uppercase; color: var(--gold); margin-bottom: 30px; text-shadow: 0 2px 4px #000; }
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 16px; }
.footer-col a { font-size: 1rem; font-weight: 700; color: var(--text-b); transition: all 0.3s; }
.footer-col a:hover { color: var(--gold-lt); padding-left: 8px; text-shadow: 0 0 10px rgba(255,215,0,0.5); }
.footer-divider { border: none; border-top: 1px solid rgba(255,255,255,0.1); }
.footer-bottom { max-width: 1300px; margin: 0 auto; display: flex; align-items: flex-start; gap: 40px; padding: 50px 28px 80px; flex-wrap: wrap; }
.footer-disclaimer { font-size: 0.85rem; font-weight: 600; color: var(--text-faint); line-height: 1.8; flex: 1; }
.footer-disclaimer strong { color: var(--text-m); }
.footer-badges { display: flex; flex-direction: column; gap: 16px; flex: 0 0 auto; }
.f-badge { border: 2px solid var(--gold-dk); border-radius: 8px; padding: 10px 20px; font-size: 0.9rem; font-weight: 900; color: var(--gold); letter-spacing: 2px; white-space: nowrap; background: #0A0A0A; text-transform: uppercase; box-shadow: 0 4px 10px rgba(0,0,0,0.8); }

/* ──────────────────────────────
   RESPONSIVE BREAKPOINTS
────────────────────────────── */
@media (max-width: 1024px) {
  .hero-title         { font-size: 4rem; }
  .hero-title .gold   { font-size: 5rem; }
  .footer-top         { grid-template-columns: 1fr 1fr; }
  .trust-grid         { grid-template-columns: repeat(2,1fr); }
}
@media (max-width: 768px) {
  .header-nav         { display: none; }
  .header-right .btn-outline { display: none; }
  .hamburger          { display: flex; }
  .games-grid         { grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 20px; }
  .promo-grid         { grid-template-columns: 1fr; }
  .bonus-strip        { grid-template-columns: 1fr; gap: 20px; }
  .hero-stats         { gap: 30px; flex-direction: column; align-items: center; width: 100%; }
  .footer-top         { grid-template-columns: 1fr; gap: 50px; padding: 80px 28px 50px; }
  .footer-bottom      { flex-direction: column; }
  .hero-ctas          { flex-direction: column; align-items: stretch; }
  .hero-title         { font-size: 3rem; }
  .hero-title .gold   { font-size: 3.5rem; }
  .section-heading    { font-size: 2rem; }
  .floating-chip, .floating-card { display: none; }
}
@media (max-width: 480px) {
  .games-grid         { grid-template-columns: repeat(2,1fr); gap: 16px; }
  .section-wrap       { padding: 60px 16px; }
  .hero               { padding: 80px 16px 50px; }
  .bonus-strip        { padding: 0 16px; margin-top: 50px; }
  .hero-title         { font-size: 2.5rem; }
  .hero-title .gold   { font-size: 2.8rem; }
  .trust-grid         { grid-template-columns: 1fr; }
  .cat-tabs           { gap: 10px; justify-content: center; }
  .cat-tab            { font-size: 0.8rem; padding: 10px 20px; }
  .game-card .play-btn{ display: none; }
}

/* SCROLL REVEAL */
[data-reveal] { opacity: 0; transform: translateY(40px); transition: opacity 0.8s cubic-bezier(0.25, 0.8, 0.25, 1), transform 0.8s cubic-bezier(0.25, 0.8, 0.25, 1); }
[data-reveal].revealed { opacity: 1; transform: translateY(0); }
"""

start_str = "/* ──────────────────────────────\n   DESIGN TOKENS"
end_str = "[data-reveal].revealed {\n  opacity: 1;\n  transform: translateY(0);\n}"

start_index = html.find(start_str)
end_index = html.find(end_str) + len(end_str)

if start_index != -1 and end_index != -1:
    html = html[:start_index] + new_css + html[end_index:]
else:
    print("Could not find CSS block boundaries")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
