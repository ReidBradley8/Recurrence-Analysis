from docx import Document
import json

# Create json file with data from tables in document
#
# Output data will be a dictionary of lists, where each element of the list
# is a list representing the cells of a row in the table

docx_path = "data/NeolibSurvey_Qualitative Data Only - Copy.docx"
output_path = "data/output.json"

data_docx = Document(docx=docx_path)
data = {'tables': {}}

index = 0
for t in data_docx.tables:
    data['tables'][index] = [tuple(c.text for c in r.cells) for r in t.rows]
    index += 1

with open(output_path, 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=4)


