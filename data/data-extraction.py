from docx import Document
import json

docx_path = "data/NeolibSurvey_Qualitative Data Only - Copy.docx"
output_path = "data/output.json"

data_docx = Document(docx=docx_path)
data = []

for t in data_docx.tables:
    data.append([
        tuple(c.text for c in r.cells) for r in t.rows
    ])

with open(output_path, 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=4)


