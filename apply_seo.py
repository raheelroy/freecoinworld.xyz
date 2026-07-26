import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Games list for SEO
games = [
    "Dragon Fortune", "Cash Wheel Deluxe", "Roulette Royale", "Texas Hold'em Elite",
    "Mystic Ocean", "Golden Sevens", "Blackjack Pro", "Stardust Slots", "Fire Kirin",
    "Lucky Panda", "Diamond Deluxe", "Pharaoh's Fortune", "Ice Queen", 
    "Thunder Strike", "Jade Palace", "Crimson Royale"
]
games_str = ", ".join(games)

# 1. Update title and meta tags
new_meta = f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FreeCoinWorld — Play Free Casino Games: {games[0]}, {games[1]}, {games[2]} & More</title>
<meta name="description" content="Play the best free social casino games at FreeCoinWorld. Enjoy premium slots and table games like {games_str}. Claim your starting coins now!">
<meta name="keywords" content="free casino games, social casino, free slots, {games_str.lower()}, play for free, no real money, roulette, poker">
<meta property="og:title" content="FreeCoinWorld — Premium Free Casino Games">
<meta property="og:description" content="Play top free games including {games[0]}, {games[2]}, and {games[3]}. Daily coins, safe & secure.">
<meta property="og:url" content="https://freecoinworld.xyz">
<meta property="og:type" content="website">

<!-- SEO Structured Data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "FreeCoinWorld",
  "url": "https://freecoinworld.xyz",
  "description": "Premium free social casino offering top slots and table games without real money betting.",
  "about": {{
    "@type": "Thing",
    "name": "Free Social Casino Games",
    "description": "We offer games like {games_str}."
  }}
}}
</script>
"""

# Replace existing meta block
# Existing block is from <meta charset="UTF-8"> down to <meta property="og:type" content="website">
pattern_meta = r'<meta charset="UTF-8">.*?<meta property="og:type" content="website">'
html = re.sub(pattern_meta, new_meta.strip(), html, flags=re.DOTALL)

# 2. Add SEO text to the footer area
seo_text = f"""
<!-- SEO Text Block -->
<div class="seo-content" style="max-width: 1300px; margin: 0 auto; padding: 20px 28px 40px; color: var(--text-faint); font-size: 0.8rem; line-height: 1.6; text-align: center;">
  <h2 style="font-size: 1rem; color: var(--text-m); margin-bottom: 10px; font-family: 'Montserrat', sans-serif;">The Ultimate Free Social Casino Experience</h2>
  <p>Welcome to FreeCoinWorld, your premier destination for high-quality, completely free casino-style entertainment. Explore our vast collection of premium games including <strong>{games_str}</strong>. Whether you love the thrill of spinning the reels in <em>{games[0]}</em> and <em>{games[7]}</em>, or prefer the strategic gameplay of <em>{games[3]}</em> and <em>{games[6]}</em>, we have something for everyone. All games are strictly for fun with no real money deposits required. Enjoy fast payouts of virtual coins, daily bonuses, and 24/7 support.</p>
</div>
"""

# Insert right before </footer> if not already there
if 'class="seo-content"' not in html:
    html = html.replace('</footer>', f'{seo_text}\n</footer>')

# 3. Enhance img tags with alt attributes (simple replacement if missing or generic)
# In this specific case, we would need a proper parser for perfect img replacement, 
# but we can rely on the fact that these are generated dynamically via JS or hardcoded without alts.
# The hardcoded images: <img src="assets/..." alt="...">
# I will do a quick pass to ensure "alt" is meaningful for SEO
html = html.replace('alt="Hero Game"', f'alt="Free slot machine game: {games[0]}"')
html = html.replace('alt="Logo"', 'alt="FreeCoinWorld Free Social Casino Logo"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SEO optimizations applied successfully.")
