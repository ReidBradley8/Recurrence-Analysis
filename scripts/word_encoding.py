import json, re, nltk
from autocorrect import Speller
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import EnglishStemmer

# 
#
#

class SurveyData():
    """Load survey data.
    
    Arguments
    ---------
    data - path to file containing json-encoded survey data.
    """
    def __init__(self, data: str):
        with open(data, 'r') as d:
            self._data = json.load(d)['tables']
        self.num_tables = len(list(self._data))
        self.tables = [self.get_table(i) for i in range(self.num_tables)]

    def get_table(self, index: int) -> list:
        """Return a table as a list of lists.
        
        Each list represents a row of the table.
        """
        return self._data[str(index)]
    
    def print_table(self, index: int) -> None:
        """Print a table from the dataset.
        """
        print(
            DataFrame(data=self.tables[index])
        )

    def update_table(self, index: int, new_table: list) -> list:
        """Update the values of an existing table.

        Returns the updated table as a list. 
        """
        self.tables[index] = new_table
        return self.tables[index]
    
    def __str__(self):
        for t in self._data:
            print(DataFrame(data=t))


class WordEncoder():
    """Encode string data from tables.

    Arguments
    ----------
    data - a SurveyData object containing the tables to be encoded.
    """
    def __init__(self, data: SurveyData):
        self._data = data
        self._encoder = LabelEncoder()
        self._spell = Speller()
        self._wnl = WordNetLemmatizer()
        self._stemmer = EnglishStemmer()

        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('udhr')

    @staticmethod
    def _unpack_list(data: list[list]) -> list:
        """Flatten list of lists into a single list of all values
        """
        if data:
            out = []
            for i in range(len(data)):
                out.extend(data[i])
        return out

    # def _spellcheck_table(self, table_index: int = 0) -> list:
    #     """Correct spelling in table.

    #     Correct spelling mistakes in each string of a table.
    #     Return a new list in the table structure with the corrected strings.
    #     """
    #     out_table = []
    #     for i in self._data.tables[table_index]:
    #         row = []
    #         for j in i:
    #             if type(j) == str:
    #                 row.append(self._spell(j))
    #         out_table.append(row)
    #     return out_table

    # def _fit_encoder(self) -> None:
    #     corpus = []
    #     for t in enumerate(self._data.tables):
    #         print(f'Adding table {t[0]} to corpus.')
    #         corpus.extend(self._unpack_list(self._spellcheck_table(t[0])))
    #     self._encoder.fit(corpus)

    def _fit_encoder_to_table(self, table: int) -> None:
        self._clean_strings(table=table, in_place=True)
        self._stem(table=table, in_place=True)
        corpus = " ".join(self._unpack_list(
            self._data.tables[table]
        )).split()
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
    
    def get_table_series(self, table: int) -> list:
        """Return a list of encoded answers for a table.

        Each element is an integer representing a token in the table dictionary.
        All answers in the table are concatenated.
        """
        self._fit_encoder_to_table(table=table)
        table_strings = " ".join(self._unpack_list(data=self._data.tables[table])).split()
        return self._encoder.transform(table_strings)
    
    def _clean_strings(self, table: int, in_place: bool = True) -> list:
        """Clean all strings in a table.

        Correct spelling mistakes in each string of a table.
        Remove non-alpha characters from each string.
        Return a new list in the table structure with the corrected strings.
        By default updates table data in-place, setting in_place to False will override that behaviour.
        """
        out_table = []
        for i in self._data.tables[table]:
            row = []
            for j in i:
                if type(j) == str:
                    row.append(re.sub('[^a-zA-Z\']', ' ', self._spell(j)))
            out_table.append(row)
        if in_place:
            return self._data.update_table(table, out_table)
        else:
            return out_table
            
        
    def _lemmatize(self, table: int, in_place: bool = True) -> list:
        """Reduce all words in a table to their lemma.

        By default values are changed in-place, setting in_place to False overrides this behaviour.
        """
        out_table = []
        for i in self._data.tables[table]:
            row = []
            for j in i:
                if type(j) == str:
                    row.append(" ".join([self._wnl.lemmatize(k) for k in j.split()]))
            out_table.append(row)
        if not in_place:
            return out_table
        else:
            return self._data.update_table(table, out_table)
        
    def _stem(self, table: int, in_place: bool = True) -> list:
        """Reduce all words in a table to their stem using the Snowball stemmer.

        By default values are changed in-place, setting in_place to False overrides this behaviour.
        """
        out_table = []
        for i in self._data.tables[table]:
            row = []
            for j in i:
                if type(j) == str:
                    row.append(" ".join([self._stemmer.stem(k) for k in j.split()]))
            out_table.append(row)
        if not in_place:
            return out_table
        else:
            return self._data.update_table(table, out_table)

