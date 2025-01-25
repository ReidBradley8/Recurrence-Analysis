from pyrqa.time_series import TimeSeries
from pyrqa.settings import Settings
from pyrqa.neighbourhood import FixedRadius
from pyrqa.metric import EuclideanMetric
from pyrqa.computation import RQAComputation
from pyrqa.analysis_type import Classic
from pyrqa.recurrence_plot import RecurrencePlot
import json
import numpy as np
from gensim.models import Word2Vec
import matplotlib.pyplot as plt

# Load data from JSON file
with open(r"C:\Users\reidb\Documents\GitHub\Recurrence-Analysis\output.json", 'r') as file:
    data = json.load(file)

# Assuming data is a list of words
# Example: data = ["word1", "word2", "word3", ...]

# Convert words to numerical vectors using Word2Vec
model = Word2Vec([data], vector_size=100, window=5, min_count=1, workers=4)
word_vectors = [model.wv[word] for word in data]

# Flatten the list of vectors to create a single time series
flattened_vectors = np.array(word_vectors).flatten()

# Create TimeSeries object
time_series = TimeSeries(flattened_vectors, embedding_dimension=2, time_delay=1)

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

# Generate Recurrence Plot
recurrence_plot = RecurrencePlot(settings)
recurrence_matrix = recurrence_plot.recurrence_matrix()

plt.imshow(recurrence_matrix, cmap='binary', origin='lower')
plt.title('Recurrence Plot')
plt.xlabel('Time')
plt.ylabel('Time')
plt.show()