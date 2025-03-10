import json

def find_instrument_id(instrument_name, instruments):
    for instrument in instruments:
        if instrument["#text"] == instrument_name:
            return instrument["id"]
    return None

with open("db.json", "r", encoding="utf-8") as file:
    original_dataset = json.load(file)

students = original_dataset["alunos"]
courses = original_dataset["cursos"]
instruments = original_dataset["instrumentos"]

for student in students:
    student["instrumento"] = {
        "id": find_instrument_id(student["instrumento"], instruments),
        "#text": student["instrumento"]
    }

structured_data = {
    "alunos": students,
    "cursos": courses,
    "instrumentos": instruments
}

with open("structured_db.json", "w", encoding="utf-8") as outfile:
    json.dump(structured_data, outfile, indent=4, ensure_ascii=False)

print("Data transformation complete. Saved as structured_db.json.")
