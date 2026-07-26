import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the Google Fonts link
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=Montserrat:wght@400;600;700;800;900&display=swap" rel="stylesheet">'
html = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Montserrat.*?rel="stylesheet">',
    new_fonts,
    html,
    flags=re.DOTALL
)

# 2. Extract the CSS block and replace it
new_css = """
/* ──────────────────────────────
   DESIGN TOKENS (Authentic Casino)
────────────────────────────── */
:root {
  --bg-base:        #180505; /* Deep velvet red */
  --bg-surface:     #260808;
  --bg-card:        #120202;
  --bg-card-h:      #1F0505;
  --bg-panel:       #0A0000;

  --gold:           #E5B94E;
  --gold-lt:        #F9E596;
  --gold-dk:        #8B6914;
  --gold-glow:      rgba(229,185,78,0.25);
  --gold-border:    rgba(229,185,78,0.5);
  --gold-border-h:  rgba(255,215,0,1);

  --green:          #1A5C38; /* Casino felt green */
  --red:            #C8102E;
  --neon-blue:      #00FFFF;

  --text-h:         #FFFFFF;
  --text-b:         #EBDDDD;
  --text-m:         #B89999;
  --text-faint:     #734A4A;

  --radius-card:    16px;
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
   SUBTLE BACKGROUND TEXTURE
────────────────────────────── */
body::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 90% 50% at 50% 0%, rgba(229,185,78,0.12) 0%, transparent 60%),
    radial-gradient(ellipse 80% 80% at 50% 100%, rgba(20,0,0,0.8) 0%, transparent 80%);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.08'/%3E%3C/svg%3E");
}
.site { position: relative; z-index: 1; }

/* ──────────────────────────────
   ALERT BAR
────────────────────────────── */
#alertBar {
  background: linear-gradient(90deg, #3A0000, #800000, #3A0000);
  border-bottom: 2px solid var(--gold-border);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 12px 20px;
  font-size: 0.88rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: #fff;
  position: relative;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}
#alertBar .ab-badge {
  background: linear-gradient(to bottom, #F9E596, #D4AF37);
  color: #3A0000;
  font-size: 0.72rem;
  font-weight: 900;
  letter-spacing: 1px;
  padding: 4px 10px;
  border-radius: 4px;
  text-transform: uppercase;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
#alertBar .ab-close {
  position: absolute; right: 16px; top: 50%; transform: translateY(-50%);
  background: none; color: var(--gold-lt); font-size: 1.2rem; line-height: 1;
  transition: color var(--transition);
}
#alertBar .ab-close:hover { color: #fff; text-shadow: 0 0 8px #fff; }

/* ──────────────────────────────
   STICKY HEADER
────────────────────────────── */
header {
  position: sticky; top: 0; z-index: 100;
  background: rgba(24,5,5,0.92);
  backdrop-filter: blur(12px);
  border-bottom: 2px solid var(--gold-dk);
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  transition: background 0.3s;
}
.header-inner {
  max-width: 1300px; margin: 0 auto;
  display: flex; align-items: center; gap: 24px;
  padding: 0 28px; height: 76px;
}
.logo {
  display: flex; align-items: center; gap: 11px;
  flex: 0 0 auto;
}
.logo-mark {
  width: 42px; height: 42px; border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #F9E596, #C9A84C, #8A6E2A);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem;
  border: 2px solid #FFF;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5), inset 0 0 8px rgba(255,255,255,0.5);
}
.logo-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-style: italic; font-size: 1.4rem;
  letter-spacing: 0.5px;
  color: var(--text-h);
  text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
}
.logo-name span { color: var(--gold); }

/* Nav tabs */
.header-nav {
  display: flex; align-items: center; gap: 8px;
  flex: 1; justify-content: center;
}
.nav-tab {
  padding: 8px 18px; border-radius: 20px;
  font-size: 0.85rem; font-weight: 700;
  color: var(--text-m);
  background: none; text-transform: uppercase; letter-spacing: 1px;
  transition: color var(--transition), background var(--transition), box-shadow var(--transition);
  white-space: nowrap; border: 1px solid transparent;
}
.nav-tab:hover    { color: var(--gold-lt); background: rgba(229,185,78,0.1); border-color: rgba(229,185,78,0.3); }
.nav-tab.active   { color: #180505; background: linear-gradient(to bottom, #F9E596, #D4AF37); border-color: #FFF; box-shadow: 0 4px 12px rgba(212,175,55,0.4); }

/* Header right */
.header-right { display: flex; align-items: center; gap: 12px; flex: 0 0 auto; }
.badge-18 {
  border: 2px solid var(--gold);
  color: var(--gold); background: rgba(0,0,0,0.4);
  font-size: 0.75rem; font-weight: 900;
  padding: 4px 10px; border-radius: 50%; letter-spacing: 0.5px;
  width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 8px var(--gold-glow);
}
.btn-primary {
  background: linear-gradient(to bottom, #FFDF70, #D4AF37, #997A15);
  color: #1A0000;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 0.85rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 10px 24px; border-radius: 30px;
  border: 1px solid #FFF;
  box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 2px 4px rgba(255,255,255,0.6);
  transition: transform var(--transition), box-shadow var(--transition);
  text-shadow: 0 1px 1px rgba(255,255,255,0.4);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(212,175,55,0.6), inset 0 2px 8px rgba(255,255,255,0.8);
}
.btn-outline {
  border: 2px solid var(--gold);
  color: var(--gold-lt);
  background: rgba(0,0,0,0.3);
  font-family: 'Montserrat', sans-serif;
  font-weight: 800; font-size: 0.85rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 9px 22px; border-radius: 30px;
  transition: all var(--transition);
}
.btn-outline:hover { border-color: #FFF; color: #FFF; background: rgba(255,255,255,0.1); box-shadow: 0 0 15px rgba(255,255,255,0.2); }

/* Mobile hamburger */
.hamburger {
  display: none; flex-direction: column; gap: 5px;
  background: none; padding: 4px;
}
.hamburger span { width: 24px; height: 3px; background: var(--gold); border-radius: 2px; }

/* ──────────────────────────────
   FLOATING CASINO ELEMENTS
────────────────────────────── */
.floating-chip {
  position: absolute;
  width: 70px; height: 70px;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, #C8102E, #5A0000);
  border: 6px dashed #EBDDDD;
  box-shadow: 0 15px 30px rgba(0,0,0,0.7), inset 0 0 15px rgba(0,0,0,0.8);
  animation: floatChip 6s ease-in-out infinite alternate;
  z-index: 0; pointer-events: none;
}
.floating-chip.blue {
  background: radial-gradient(circle at 30% 30%, #004B87, #001A33);
}
.floating-chip.gold {
  background: radial-gradient(circle at 30% 30%, #F9E596, #8B6914);
  border-color: #1A0000;
}
.floating-chip::after {
  content: 'FCW';
  position: absolute; inset: 10px;
  border-radius: 50%;
  border: 2px double #EBDDDD;
  display: flex; align-items: center; justify-content: center;
  color: #EBDDDD; font-weight: 900; font-family: 'Playfair Display', serif;
  font-size: 14px; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
}
.floating-chip.gold::after { border-color: #1A0000; color: #1A0000; text-shadow: none; }

.floating-card {
  position: absolute;
  width: 80px; height: 115px;
  background: #F4F4F4;
  border-radius: 6px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.8), inset 0 0 0 4px #FFF;
  animation: floatCard 8s ease-in-out infinite alternate;
  z-index: 0; pointer-events: none;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  color: #C8102E; font-size: 40px; font-weight: bold;
}
.floating-card.spade { color: #111; }
.floating-card::before { content: '♥'; }
.floating-card.spade::before { content: '♠'; }
.floating-card::after { content: 'A'; position: absolute; top: 6px; left: 8px; font-size: 18px; font-family: 'Playfair Display', serif; }

@keyframes floatChip { 
  0% { transform: translateY(0) rotate(0deg) scale(1); } 
  100% { transform: translateY(-40px) rotate(30deg) scale(1.05); } 
}
@keyframes floatCard { 
  0% { transform: translateY(0) rotate(-15deg); } 
  100% { transform: translateY(-50px) rotate(20deg); } 
}

/* ──────────────────────────────
   HERO SECTION
────────────────────────────── */
.hero {
  position: relative;
  max-width: 1300px; margin: 0 auto;
  display: grid; grid-template-columns: 1fr 520px;
  gap: 40px; align-items: center;
  padding: 90px 28px 80px;
}
.hero-content { position: relative; z-index: 2; }
.hero-label {
  display: inline-flex; align-items: center; gap: 8px;
  border: 1px solid var(--gold);
  background: rgba(0,0,0,0.6);
  color: var(--gold-lt);
  font-size: 0.8rem; font-weight: 800;
  letter-spacing: 3px; text-transform: uppercase;
  padding: 6px 16px; border-radius: 30px;
  margin-bottom: 24px;
  box-shadow: 0 0 15px rgba(212,175,55,0.2);
}
.hero-label::before { content: '★'; color: var(--gold); animation: spin 4s linear infinite; }
@keyframes spin { 100% { transform: rotate(360deg); } }

.hero-title {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-style: italic;
  line-height: 1.1;
  font-size: clamp(2.8rem, 4.5vw, 4.2rem);
  color: #FFF;
  text-shadow: 0 4px 20px rgba(0,0,0,0.8);
  margin-bottom: 20px;
}
.hero-title .gold { 
  color: var(--gold-lt); 
  background: -webkit-linear-gradient(top, #FFF, #F9E596, #D4AF37);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
}
.hero-title .outline {
  -webkit-text-stroke: 2px var(--gold);
  color: transparent;
  font-style: normal;
}

.hero-sub {
  font-size: 1.15rem; line-height: 1.7; font-weight: 500;
  color: var(--text-b); max-width: 540px;
  margin-bottom: 40px; text-shadow: 0 2px 4px rgba(0,0,0,0.6);
}

.hero-stats {
  display: flex; gap: 40px; margin-bottom: 40px;
  background: rgba(0,0,0,0.4); border: 1px solid var(--gold-dk);
  padding: 20px 30px; border-radius: 12px;
  backdrop-filter: blur(5px);
  box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
  width: max-content;
}
.hero-stat { display: flex; flex-direction: column; }
.hero-stat-num {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.8rem;
  color: var(--gold-lt); letter-spacing: 1px;
  text-shadow: 0 2px 10px rgba(212,175,55,0.4);
}
.hero-stat-label { font-size: 0.8rem; font-weight: 700; color: #FFF; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

.hero-ctas { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
.btn-lg { padding: 16px 36px; font-size: 1rem; border-radius: 40px; }
.hero-note { font-size: 0.8rem; color: var(--text-m); margin-top: 16px; font-style: italic; }

/* Hero visual — featured game reel as a slot machine window */
.hero-visual {
  position: relative; z-index: 2;
  background: linear-gradient(to bottom, #111, #222, #111);
  padding: 30px 20px;
  border-radius: 24px;
  border: 4px solid var(--gold-dk);
  box-shadow: 0 30px 60px rgba(0,0,0,0.8), inset 0 0 30px #000, 0 0 0 8px rgba(20,5,5,0.8), 0 0 0 10px var(--gold-dk);
  overflow: hidden;
}
.hero-visual::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(90deg, rgba(0,0,0,0.9) 0%, transparent 15%, transparent 85%, rgba(0,0,0,0.9) 100%);
  z-index: 5; pointer-events: none;
}
.hero-reel {
  display: flex;
  align-items: center;
  gap: 16px;
  width: max-content;
  animation: heroReel 20s linear infinite;
}
@keyframes heroReel {
  from { transform: translateX(0); }
  to { transform: translateX(calc(-50% - 8px)); }
}
.hero-game {
  width: clamp(130px, 12vw, 170px);
  aspect-ratio: 1;
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  border-radius: 12px;
  border: 2px solid var(--gold-dk);
  background: radial-gradient(circle at 50% 50%, #2A0A0A 0%, #110000 100%);
  box-shadow: inset 0 0 15px rgba(0,0,0,0.8), 0 10px 20px rgba(0,0,0,0.5);
}
.hero-game img {
  width: 75%;
  aspect-ratio: 1;
  object-fit: contain;
  filter: drop-shadow(0 8px 12px rgba(0,0,0,0.8));
}
.hero-game span {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.75rem; font-weight: 900; text-transform: uppercase; letter-spacing: 1px;
  color: var(--gold-lt); text-shadow: 0 2px 4px #000;
}

/* ──────────────────────────────
   GAME THUMBNAIL ART (CSS)
────────────────────────────── */
.gt {
  aspect-ratio: 3/4;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 8px; position: relative; overflow: hidden;
  border-bottom: 3px solid rgba(0,0,0,0.5);
}
.gt::before { /* inner glow vignette */
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 70% 60% at 50% 40%, rgba(255,255,255,0.15) 0%, rgba(0,0,0,0.8) 100%);
  pointer-events: none;
}
.gt-symbol {
  font-size: 3.2rem; line-height: 1;
  filter: drop-shadow(0 6px 12px rgba(0,0,0,0.8));
  position: relative; z-index: 1;
}
.gt-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1rem;
  letter-spacing: 1px; text-align: center;
  color: #fff; text-shadow: 0 4px 8px rgba(0,0,0,1);
  padding: 0 8px; position: relative; z-index: 1;
  text-transform: uppercase;
}
.gt-sub {
  font-size: 0.65rem; font-weight: 800;
  letter-spacing: 2px; color: var(--gold-lt);
  text-transform: uppercase; position: relative; z-index: 1;
  text-shadow: 0 2px 4px #000;
}

/* ──────────────────────────────
   PROVIDER TICKER
────────────────────────────── */
.provider-strip {
  border-top: 2px solid var(--gold-dk);
  border-bottom: 2px solid var(--gold-dk);
  background: #0A0000;
  padding: 16px 0;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0,0,0,0.5);
}
.provider-track {
  display: flex; gap: 60px;
  animation: provTicker 30s linear infinite;
  width: max-content;
}
.prov-item {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-style: italic; font-size: 1.1rem;
  letter-spacing: 2px;
  color: var(--gold-dk);
  white-space: nowrap;
}

/* ──────────────────────────────
   BONUS STRIP
────────────────────────────── */
.bonus-strip {
  max-width: 1300px; margin: 60px auto 0;
  padding: 0 28px;
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;
}
.bonus-pill {
  background: linear-gradient(145deg, #240505, #110000);
  border: 2px solid var(--gold-dk);
  border-radius: 16px;
  display: flex; align-items: center; gap: 20px;
  padding: 24px 28px;
  box-shadow: 0 15px 30px rgba(0,0,0,0.6), inset 0 0 15px rgba(0,0,0,0.5);
  transition: transform var(--transition), border-color var(--transition);
}
.bonus-pill:hover { transform: translateY(-5px); border-color: var(--gold-lt); }
.bp-icon {
  width: 56px; height: 56px; border-radius: 50%; flex: 0 0 auto;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.8rem;
  border: 2px solid rgba(255,255,255,0.1);
  box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
}
.bp-icon.gold-bg  { background: radial-gradient(circle, #8B6914, #2A1A00); border-color: var(--gold); }
.bp-icon.red-bg   { background: radial-gradient(circle, #C8102E, #3A0000); border-color: #FF4D6D; }
.bp-icon.green-bg { background: radial-gradient(circle, #1A5C38, #052210); border-color: #2E8B57; }
.bp-amount {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.8rem; color: var(--gold-lt);
  line-height: 1; text-shadow: 0 2px 4px #000;
}
.bp-label { font-size: 0.85rem; font-weight: 700; color: #FFF; text-transform: uppercase; letter-spacing: 1px; margin-top: 6px; }

/* ──────────────────────────────
   GAMES SECTION
────────────────────────────── */
.section-wrap { max-width: 1300px; margin: 0 auto; padding: 80px 28px; position: relative; z-index: 2; }
.section-header {
  display: flex; align-items: flex-end; justify-content: space-between;
  margin-bottom: 30px;
  border-bottom: 2px solid rgba(229,185,78,0.2);
  padding-bottom: 16px;
}
.section-heading {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 2rem; font-style: italic;
  color: #FFF; text-shadow: 0 2px 8px #000;
}
.section-heading span { color: var(--gold-lt); }
.section-sub { font-size: 0.9rem; font-weight: 600; color: var(--text-m); margin-top: 8px; text-transform: uppercase; letter-spacing: 2px; }
.see-all { font-size: 0.9rem; font-weight: 800; color: var(--gold); letter-spacing: 1px; text-transform: uppercase; }
.see-all:hover { color: #FFF; }

/* Category tabs */
.cat-tabs { display: flex; gap: 12px; margin-bottom: 36px; flex-wrap: wrap; }
.cat-tab {
  padding: 10px 24px; border-radius: 30px;
  font-size: 0.85rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;
  background: rgba(0,0,0,0.5); border: 2px solid var(--gold-dk);
  color: var(--text-m);
  transition: all var(--transition);
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}
.cat-tab:hover  { color: #FFF; border-color: var(--gold); background: rgba(229,185,78,0.1); }
.cat-tab.active { color: #110000; border-color: #FFF; background: linear-gradient(to bottom, #F9E596, #D4AF37); box-shadow: 0 4px 15px rgba(212,175,55,0.5); }

/* ──────────────────────────────
   GAME CARDS GRID
────────────────────────────── */
.games-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 24px;
}

.game-card {
  background: linear-gradient(to bottom, #1F0505, #0A0000);
  border-radius: var(--radius-card);
  overflow: hidden;
  border: 2px solid var(--gold-dk);
  box-shadow: 0 15px 30px rgba(0,0,0,0.7), inset 0 0 20px rgba(0,0,0,0.8);
  transition: transform var(--transition), border-color var(--transition), box-shadow var(--transition);
  cursor: pointer;
}
.game-card:hover {
  transform: translateY(-8px);
  border-color: var(--gold-lt);
  box-shadow: 0 20px 50px rgba(0,0,0,0.9), 0 0 20px rgba(212,175,55,0.4), inset 0 0 30px rgba(212,175,55,0.2);
}

/* Thumb area with hover overlay */
.card-thumb {
  position: relative; overflow: hidden;
  border-bottom: 2px solid var(--gold-dk);
}
.card-thumb .gt { transition: transform 0.4s ease; }
.game-card:hover .card-thumb .gt { transform: scale(1.08); }
.card-logo-stage {
  aspect-ratio: 3/4;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 22px;
  background: radial-gradient(circle at 50% 50%, #2A0A0A, #0A0000);
  transition: transform 0.4s ease;
}
.game-card:hover .card-logo-stage { transform: scale(1.08); }
.game-logo-crop {
  width: min(210px, 90%);
  aspect-ratio: 1;
  object-fit: contain;
  filter: drop-shadow(0 15px 25px rgba(0,0,0,0.8));
}

.thumb-overlay {
  position: absolute; inset: 0;
  background: radial-gradient(circle at center, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.9) 100%);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: opacity 0.3s;
}
.game-card:hover .thumb-overlay { opacity: 1; }
.play-btn {
  background: linear-gradient(to bottom, #FFDF70, #D4AF37, #997A15);
  color: #1A0000;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 0.9rem;
  letter-spacing: 2px; text-transform: uppercase;
  padding: 12px 30px; border-radius: 30px;
  transform: scale(0.8); transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid #FFF; box-shadow: 0 10px 20px rgba(0,0,0,0.8);
}
.game-card:hover .play-btn { transform: scale(1); }

/* Card badge */
.card-badge {
  position: absolute; top: 12px; left: 12px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900; font-size: 0.65rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 4px 10px; border-radius: 20px;
  z-index: 2; box-shadow: 0 4px 10px rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.3);
}
.badge-hot      { background: linear-gradient(to bottom, #FF4D6D, #C8102E); color: #fff; }
.badge-new      { background: linear-gradient(to bottom, #2E8B57, #1A5C38); color: #fff; }
.badge-featured { background: linear-gradient(to bottom, #F9E596, #D4AF37); color: #110000; border-color: #FFF; }

/* Card info strip */
.card-info { padding: 16px; }
.card-game-name {
  font-family: 'Playfair Display', serif;
  font-weight: 900; font-size: 1.1rem;
  color: #FFF; letter-spacing: 0.5px;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  text-shadow: 0 2px 4px #000;
}
.card-provider { font-size: 0.75rem; font-weight: 600; color: var(--gold-dk); margin-top: 4px; text-transform: uppercase; letter-spacing: 1px; }
.card-footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 12px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px;
}
.card-coins { font-size: 0.8rem; font-weight: 800; color: var(--gold-lt); display: flex; align-items: center; gap: 4px; }
.card-coins::before { content: '🪙'; font-size: 1rem; }
.card-status { width: 8px; height: 8px; border-radius: 50%; background: var(--text-faint); }
.card-status.online { background: #00FF00; box-shadow: 0 0 10px #00FF00; }

/* ──────────────────────────────
   PROMOTIONS
────────────────────────────── */
.promo-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
.promo-card {
  border-radius: 20px; overflow: hidden;
  border: 2px solid var(--gold-dk);
  background: linear-gradient(to bottom, #240505, #110000);
  transition: transform var(--transition), box-shadow var(--transition);
  position: relative;
  box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}
.promo-card:hover { transform: translateY(-6px); box-shadow: 0 25px 50px rgba(0,0,0,0.8), 0 0 20px rgba(212,175,55,0.3); border-color: var(--gold-lt); }
.promo-art {
  height: 180px; display: flex; align-items: center; justify-content: center;
  font-size: 4rem; position: relative; overflow: hidden;
  border-bottom: 2px solid var(--gold-dk);
}
.promo-art::after { content: ''; position: absolute; inset: 0; background: linear-gradient(to top, #110000 0%, transparent 80%); }
.promo-art.pa-welcome { background: radial-gradient(circle, #8B6914, #2A1A00); }
.promo-art.pa-daily   { background: radial-gradient(circle, #1A5C38, #052210); }
.promo-art.pa-refer   { background: radial-gradient(circle, #C8102E, #3A0000); }
.promo-body { padding: 24px; text-align: center; }
.promo-title { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.2rem; color: #FFF; margin-bottom: 8px; }
.promo-amount { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 2rem; color: var(--gold-lt); letter-spacing: -1px; margin-bottom: 12px; text-shadow: 0 2px 4px #000; }
.promo-desc { font-size: 0.9rem; font-weight: 500; color: var(--text-m); line-height: 1.6; margin-bottom: 20px; }
.btn-sm {
  padding: 10px 24px; font-size: 0.8rem; border-radius: 30px;
  font-family: 'Montserrat', sans-serif; font-weight: 800;
  letter-spacing: 1px; text-transform: uppercase;
  display: inline-block;
}

/* ──────────────────────────────
   TRUST / FEATURES
────────────────────────────── */
.trust-section { background: #0A0000; border-top: 2px solid var(--gold-dk); border-bottom: 2px solid var(--gold-dk); position: relative; z-index: 2; }
.trust-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 2px; background: var(--gold-dk); }
.trust-cell { background: #180505; padding: 40px 30px; transition: background var(--transition); text-align: center; }
.trust-cell:hover { background: #240505; }
.trust-icon { width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; margin: 0 auto 20px; border: 2px solid var(--gold-dk); background: #110000; box-shadow: inset 0 0 10px rgba(0,0,0,0.8); }
.trust-title { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1.1rem; color: #FFF; margin-bottom: 10px; }
.trust-desc { font-size: 0.9rem; font-weight: 500; color: var(--text-m); line-height: 1.6; }

/* ──────────────────────────────
   EMAIL CTA
────────────────────────────── */
.cta-section { max-width: 700px; margin: 0 auto; padding: 100px 28px; text-align: center; position: relative; z-index: 2; }
.cta-section .section-heading { font-size: 2.8rem; line-height: 1.2; margin-bottom: 16px; }
.cta-section p { font-size: 1.1rem; color: var(--text-b); margin-bottom: 40px; line-height: 1.7; }
.email-row { display: flex; gap: 8px; background: rgba(0,0,0,0.6); border: 2px solid var(--gold-dk); border-radius: 40px; padding: 8px 8px 8px 24px; transition: border-color 0.3s; box-shadow: inset 0 0 15px rgba(0,0,0,0.8); }
.email-row:focus-within { border-color: var(--gold-lt); box-shadow: inset 0 0 15px rgba(0,0,0,0.8), 0 0 20px rgba(212,175,55,0.3); }
.email-row input { flex: 1; background: none; border: none; outline: none; font-family: 'Montserrat', sans-serif; font-size: 1rem; font-weight: 600; color: #FFF; }
.email-row input::placeholder { color: var(--text-faint); font-weight: 500; }
.cta-note { font-size: 0.8rem; font-weight: 600; color: var(--text-m); margin-top: 16px; text-transform: uppercase; letter-spacing: 1px; }

/* ──────────────────────────────
   FOOTER
────────────────────────────── */
footer { background: #050000; border-top: 2px solid var(--gold-dk); position: relative; z-index: 2; }
.footer-top { max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: 300px 1fr 1fr 1fr; gap: 60px; padding: 80px 28px 60px; }
.footer-logo-area .logo { margin-bottom: 24px; }
.footer-desc { font-size: 0.9rem; font-weight: 500; color: var(--text-m); line-height: 1.8; }
.footer-col h4 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: 1rem; letter-spacing: 2px; text-transform: uppercase; color: var(--gold-lt); margin-bottom: 24px; }
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 14px; }
.footer-col a { font-size: 0.9rem; font-weight: 600; color: var(--text-b); transition: color 0.3s; }
.footer-col a:hover { color: var(--gold); padding-left: 5px; }
.footer-divider { border: none; border-top: 1px solid rgba(255,255,255,0.05); }
.footer-bottom { max-width: 1300px; margin: 0 auto; display: flex; align-items: flex-start; gap: 40px; padding: 40px 28px 60px; flex-wrap: wrap; }
.footer-disclaimer { font-size: 0.8rem; font-weight: 500; color: var(--text-faint); line-height: 1.8; flex: 1; }
.footer-disclaimer strong { color: var(--text-m); }
.footer-badges { display: flex; flex-direction: column; gap: 12px; flex: 0 0 auto; }
.f-badge { border: 2px solid var(--gold-dk); border-radius: 8px; padding: 8px 16px; font-size: 0.8rem; font-weight: 800; color: var(--gold-lt); letter-spacing: 1px; white-space: nowrap; background: #110000; text-transform: uppercase; }

/* ──────────────────────────────
   RESPONSIVE BREAKPOINTS
────────────────────────────── */
@media (max-width: 1024px) {
  .hero               { grid-template-columns: 1fr; }
  .hero-visual        { display: none; }
  .hero               { padding: 70px 28px 60px; text-align: center; }
  .hero-sub           { margin: 0 auto 40px; }
  .hero-stats         { margin: 0 auto 40px; justify-content: center; }
  .hero-ctas          { justify-content: center; }
  .footer-top         { grid-template-columns: 1fr 1fr; }
  .trust-grid         { grid-template-columns: repeat(2,1fr); }
}
@media (max-width: 768px) {
  .header-nav         { display: none; }
  .header-right .btn-outline { display: none; }
  .hamburger          { display: flex; }
  .games-grid         { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 16px; }
  .promo-grid         { grid-template-columns: 1fr; }
  .bonus-strip        { grid-template-columns: 1fr; gap: 16px; }
  .hero-stats         { gap: 20px; flex-direction: column; align-items: center; width: 100%; }
  .footer-top         { grid-template-columns: 1fr; gap: 40px; padding: 60px 28px 40px; }
  .footer-bottom      { flex-direction: column; }
  .hero-ctas          { flex-direction: column; align-items: stretch; }
  .hero-title         { font-size: 2.8rem; }
  .section-heading    { font-size: 1.6rem; }
  .floating-chip, .floating-card { display: none; }
}
@media (max-width: 480px) {
  .games-grid         { grid-template-columns: repeat(2,1fr); gap: 12px; }
  .section-wrap       { padding: 50px 16px; }
  .hero               { padding: 50px 16px 40px; }
  .bonus-strip        { padding: 0 16px; margin-top: 40px; }
  .hero-title         { font-size: 2.4rem; }
  .trust-grid         { grid-template-columns: 1fr; }
  .cat-tabs           { gap: 8px; justify-content: center; }
  .cat-tab            { font-size: 0.75rem; padding: 8px 16px; }
  .game-card .play-btn{ display: none; }
}

/* SCROLL REVEAL */
[data-reveal] { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-reveal].revealed { opacity: 1; transform: translateY(0); }
"""

start_str = "/* ──────────────────────────────\n   DESIGN TOKENS\n────────────────────────────── */"
end_str = "[data-reveal].revealed {\n  opacity: 1;\n  transform: translateY(0);\n}"

start_index = html.find(start_str)
end_index = html.find(end_str) + len(end_str)

if start_index != -1 and end_index != -1:
    html = html[:start_index] + new_css + html[end_index:]
else:
    print("Could not find CSS block boundaries")

# 3. Add floating elements to Hero Section
floating_elements = """
  <div class="floating-chip gold" style="top: -20px; left: 10%; animation-delay: 0s;"></div>
  <div class="floating-card" style="top: 20%; left: -5%; animation-delay: 1.5s;"></div>
  <div class="floating-chip" style="bottom: 20%; left: 45%; animation-delay: 0.5s;"></div>
  <div class="floating-chip blue" style="top: 15%; right: 10%; animation-delay: 2s;"></div>
  <div class="floating-card spade" style="bottom: 10%; right: 5%; animation-delay: 1s;"></div>
"""

# Only add once
if 'class="floating-chip"' not in html:
    html = html.replace('<div class="hero-content">', floating_elements + '\n    <div class="hero-content">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
