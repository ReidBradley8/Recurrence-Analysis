# Recurrence-Analysis
---
**Installation** <br/>
In the repo directory, run this code to create a virtual environment. The name of the virtual environment should be *.env*. <br/>
<pre>python -m venv [name of virtual environment]</pre>
Next, activate the virtual environment by running the *Activate* Powershell script. Just type this directly into the command line:
<pre>.env\Scripts\Activate.ps1</pre>
You can tell if the virtual environment is active by looking at the command line prompt. If the venv is activated, you should see `(.env) PS C:\...\Recurrence-Analysis>`. <br/><br/>

To install the required packages using pip, run this command after activating the venv:
<pre>pip install -r requirements.txt</pre>
---
**Packages** <br/>
[pyRQA](https://pypi.org/project/PyRQA/2.0.0/) - *Python 3.6* <br/>
[python-docx](https://pypi.org/project/python-docx/) - *Python 3.11* <br/>
[autocorrect](https://github.com/filyp/autocorrect) <br/>
---
**Objects** <br/>
`SurveyData` object holds data from the survey. <br/>
<pre>survey = SurveyData(data='data/output.json')</pre> <br/>
`WordEncoder` manipulates survey data and encodes tokens to integers. <br/>
<pre><code>encoder = WordEncoder(data=survey)
table_2_series = encoder.get_table_series(table=2)</code></pre>

