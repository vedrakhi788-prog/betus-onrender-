import pathlib, re
root = pathlib.Path('.')
files = [p for p in root.rglob('*.html') if p.is_file()]
replacements = {
    'Tours & Visitas': 'Travel Guides & Tours',
    'calendario de travel tours': 'tour calendar',
    'Consulta el calendario de travel tours, resultados y actividades familyres en el Betusin Travels.': 'Check the tour calendar, results, and travel guides at Betusin Travels.',
    'Betusin Travels — Spinning Top Heritage & Events': 'Betusin Travels — Travel Guides & Inspiration',
    'El Club': 'About Us',
    '<a href="leaderboard.html">Calendario</a>': '<a href="leaderboard.html">Tour Calendar</a>',
    'Calendario de travel tours': 'Tour Calendar',
    '<meta name="description" content="Resuelve tus dudas sobre visitas, entradas, accesos y servicios en el Betusin Travels.">': '<meta name="description" content="Find answers to common questions about visiting, booking, and traveling with Betusin Travels.">',
    'Todos los derechos reservados.': 'All rights reserved.',
    'Trompo • culture • family': 'Travel • Culture • Family',
    'Spinning Top Heritage • Community': 'Travel Heritage • Community',
    'Spinning Top • Community': 'Travel • Community',
    'Kids Games World': 'Betusin Travels',
    'Kids Games World is a fun-filled universe where kids play, learn, and explore exciting games and activities in a safe environment.': 'Betusin Travels is a curated travel guide hub with destination stories, planning tips, and family-friendly journeys.',
    '<a href="../blog.html" style="opacity:1;font-weight:800">Blog</a>': '<a href="../blog.html" style="opacity:1;font-weight:800">Stories</a>',
    '<a href="blog.html" style="opacity:1;font-weight:800">Blog</a>': '<a href="blog.html" style="opacity:1;font-weight:800">Stories</a>',
    '<a class="btn" href="game.html">Calendario de travel tours</a>': '<a class="btn" href="game.html">Tour Calendar</a>',
    '🐎 Trompo': '🗺️ Travel',
    'Trompo': 'Travel',
}
page_specific = {
    'lander.html': {
        '<title>Kids Games World</title>': '<title>Betusin Travels — Travel Guides</title>',
        '<meta name="description" content="Kids Games World is a fun-filled universe where kids play, learn, and explore exciting games and activities in a safe environment.">': '<meta name="description" content="Betusin Travels offers destination guides, journey planning, and travel inspiration for families and explorers.">',
    },
    'landerbt.html': {
        '<title>Kids Games World</title>': '<title>Betusin Travels — Travel Guides</title>',
        '<meta name="description" content="Kids Games World is a fun-filled universe where kids play, learn, and explore exciting games and activities in a safe environment.">': '<meta name="description" content="Betusin Travels offers destination guides, journey planning, and travel inspiration for families and explorers.">',
    },
}
for path in files:
    text = path.read_text(encoding='utf-8')
    scripts = []
    def repl(m):
        scripts.append(m.group(0))
        return f'<<<SCRIPT_{len(scripts)-1}>>>'
    text_no_scripts = re.sub(r'<script[\s\S]*?</script>', repl, text, flags=re.I)
    for old, new in replacements.items():
        text_no_scripts = text_no_scripts.replace(old, new)
    if path.name in page_specific:
        for old, new in page_specific[path.name].items():
            text_no_scripts = text_no_scripts.replace(old, new)
    text_no_scripts = text_no_scripts.replace('familyres', 'family')
    for idx, script in enumerate(scripts):
        text_no_scripts = text_no_scripts.replace(f'<<<SCRIPT_{idx}>>>', script)
    path.write_text(text_no_scripts, encoding='utf-8')
    print('Updated', path)
