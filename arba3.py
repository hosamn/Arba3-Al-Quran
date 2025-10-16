import json, math, zipfile

# Load rub metadata
with zipfile.ZipFile("quran-metadata-rub.json.zip", "r") as archive:
    file = archive.read(archive.namelist()[0])
    rubs = json.loads(file)

# Load ayah metadata (ayah texts keyed by "sura:ayah")
with zipfile.ZipFile("quran-metadata-ayah.json.zip", "r") as archive:
    file = archive.read(archive.namelist()[0])
    ayahs = json.loads(file)

results = []

for rub in rubs.values():
    first_verse_key = rub["first_verse_key"]
    surah, ayah = first_verse_key.split(":")

    for ayah_data in ayahs.values():
        if int(surah) == int(ayah_data["surah_number"]) and int(ayah) == int(ayah_data["ayah_number"]):
            first_5_words = ' '.join(ayah_data["text"].split()[:5]).replace("۞ ", "").replace(" ١", "")

            numr = rub["rub_number"]
            guz2 = math.ceil(rub["rub_number"]/8)
            hizb = math.ceil(rub["rub_number"]/4)
            rub3 = ((rub["rub_number"]-1)%4)+1

            results.append((numr, guz2, hizb, rub3, surah, ayah, first_5_words))

for numr, guz2, hizb, rub3, surah, ayah, first_5_words in results:
    print(f"{numr}, guz2: {guz2}, hizb: {hizb}, rub3: {rub3}, surah:{surah}, ayah:{ayah}, {first_5_words}")
