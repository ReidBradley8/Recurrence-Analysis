import json
from autocorrect import Speller
from sklearn.preprocessing import LabelEncoder

# 
#
#

class SurveyData():
    def __init__(self, data: str):
        with open(data, 'r') as d:
            self._data = json.load(d)['tables']
        self.num_tables = len(list(self._data))
        self.tables = [self.get_table(i) for i in range(self.num_tables)]

    def get_table(self, index: int = 0) -> list:
        """Return a table as a list of lists, each lower list representing a row
        """
        return self._data[str(index)]
    

class WordEncoder():
    """
    """
    def __init__(self, data: SurveyData):
        self._data = data
        self._encoder = LabelEncoder()
        # self._table_selection = tables
        self.spell = Speller()

        # print('Tables: ', self._data.num_tables)

        self._fit_encoder()

    @staticmethod
    def _unpack_list(data: list[list]) -> list:
        """Flatten list of lists into a single list of all values
        """
        if data:
            out = []
            for i in range(len(data)):
                out.extend(data[i])
        return out

    def _spellcheck_table(self, table: int = 0):
        """Correct spelling in table, replace sentences
        """
        out_table = []
        for i in self._data.tables[table]:
            row = []
            for j in i:
                if type(j) == str:
                    row.append(self.spell(j))
            out_table.append(row)
        return out_table

    def _fit_encoder(self):
        corpus = []
        for t in enumerate(self._data.tables):
            print(f'Adding table {t[0]} to corpus.')
            corpus.extend(self._unpack_list(self._spellcheck_table(t[0])))
        self._encoder.fit(corpus)

    def get_single_token(self, value: int) -> str:
        """Return the token associated with the provided encoding value.

        Raises a ValueError if the value is not present in the dictionary.
        """
        return self._encoder.inverse_transform([value])

    def get_single_encoding(self, token:str) -> int:
        """Return the integer representing the token provided.

        Raises a ValueError if the token is not present in the dictionary.
        """
        return self._encoder.transform([token])[0]

