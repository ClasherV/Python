import re
pattern="[A-Z]esident"
text='''Bio Data of Ada Wong
Character Overview
Full Name: Ada Wong
Fictional Universe: resident Evil (Biohazard)
First Appearance: resident Evil 2 (1998)
Affiliation: Independent, often works for shadowy organizations like "The Organization"
Role: Femme fatale, spy, and anti-hero
Creator: Capcom
Physical Appearance
Gender: Female
Hair: Black, short bob-cut style
Eyes: Brown
Build: Slim and athletic
Signature Look: Red dress, tactical outfits, with a grappling gun as her signature tool
Character Traits
Personality:
Mysterious, cunning, and resourceful
Known for her cool demeanor and sharp wit
Independent and highly skilled in espionage
Abilities:
Hand-to-hand combat
Expert marksmanship
Proficient in hacking and using advanced gadgets
Background
Ada Wong is a spy often entangled in the bioterrorism events of the resident Evil series. She is a complex character with unclear allegiances, as she frequently works for her own gain while showing occasional acts of altruism, especially toward Leon S. Kennedy.
Notable Relationships
Leon S. Kennedy: A complicated relationship, marked by mutual attraction, trust, and betrayal.
Albert Wesker: Occasionally works under his orders, but her true motives often remain hidden.
Appearances in Media
resident Evil Games:
resident Evil 2
resident Evil 4
resident Evil 6
Various remakes and spin-offs
Movies and Novels:
Appears in animated movies (Pesident evil: Damnation, Besident evil: Vendetta).
Adapted into live-action films in the resident Evil movie series.
Trivia
Ada Wong's name might be an alias, as her true identity remains shrouded in mystery.
Her grappling gun has become a trademark tool, symbolizing her resourcefulness.
She often walks the thin line between hero and villain, making her a fan-favorite character in the franchise.
Let me know if you'd like to dive deeper into specific aspects of Ada Wong's lore!'''

matches=re.finditer(pattern,text)
for match in matches:
    print(match)

"""
O/p: <re.Match object; span=(1387, 1395), match='Pesident'>
     <re.Match object; span=(1413, 1421), match='Besident'>
"""