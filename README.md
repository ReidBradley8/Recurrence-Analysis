# Recurrence-Analysis

---
**Packages** <br/>
[pyRQA](https://pypi.org/project/PyRQA/2.0.0/) - *Python 3.6* <br/>
[python-docx](https://pypi.org/project/python-docx/) - *Python 3.11* <br/>
[autocorrect](https://github.com/filyp/autocorrect) <br/>

---
**Objects** <br/>
`SurveyData` object holds data from the survey. <br/>
`survey = SurveyData(data='data/output.json')` <br/><br/>
`WordEncoder` manipulates survey data and encodes tokens to integers. <br/>
`encoder = WordEncoder(data=survey) <br/>
table_2_series = encoder.get_table_series(table=2)`

