from pyrqa.time_series import TimeSeries
from pyrqa.settings import Settings
from pyrqa.neighbourhood import FixedRadius
from pyrqa.metric import EuclideanMetric
from pyrqa.computation import RQAComputation
from pyrqa.analysis_type import Classic
import json

# Load data from JSON file
with open('path/to/output.json', 'r') as file:
    data = json.load(file)

# Create TimeSeries object
time_series = TimeSeries(data, embedding_dimension=2, time_delay=1)

# Define settings
settings = Settings(
    time_series,
    analysis_type=Classic,
    neighbourhood=FixedRadius(1.0),
    similarity_measure=EuclideanMetric(),
    theiler_corrector=1
)

# Perform RQA computation
computation = RQAComputation.create(settings)
result = computation.run()

# Print results
print(result)