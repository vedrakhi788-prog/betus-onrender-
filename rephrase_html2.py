from pathlib import Path
replacements = {
    '<a href="../game.html">Play</a>': '<a href="../game.html">Tours</a>',
    '<title>Designing Kid-Friendly Activity Layouts — Betusin Travels</title>': '<title>Designing Family-Friendly Travel Itineraries — Betusin Travels</title>',
    '<h1>Designing Kid-Friendly Activity Layouts</h1>': '<h1>Designing Family-Friendly Travel Itineraries</h1>',
    '<title>Sound, Props & Feedback for Kids — Betusin Travels</title>': '<title>Sound, Props & Feedback for Travel Experiences — Betusin Travels</title>',
    '<h1>Sound, Props & Feedback for Kids</h1>': '<h1>Sound, Props & Feedback for Travel Experiences</h1>',
    '<title>Designing Immersive Spaces for Kids — Betusin Travels</title>': '<title>Designing Immersive Travel Experiences — Betusin Travels</title>',
    '<h1>Designing Immersive Spaces for Kids</h1>': '<h1>Designing Immersive Travel Experiences</h1>',
    '<title>Designing Family-Friendly Mobile Tours — Betusin Travels</title>': '<title>Designing Family-Friendly Travel Experiences — Betusin Travels</title>',
    '<h1>Designing Family-Friendly Mobile Tours</h1>': '<h1>Designing Family-Friendly Travel Experiences</h1>',
    '<title>Why Short Stations Work So Well — Betusin Travels</title>': '<title>Why Short Travel Days Work So Well — Betusin Travels</title>',
    '<h1>Why Short Stations Work So Well</h1>': '<h1>Why Short Travel Days Work So Well</h1>',
    'content="Betusin Travels programs for schools, private events, and family days. Spinning Top and heritage offerings."': 'content="Betusin Travels offers family tours, private itineraries, and expert travel guidance for groups and travelers."',
}
files = [Path('services.html')] + list(Path('posts').glob('*.html'))
for p in files:
    text = p.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('Updated', p)
