import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, Imputer


class DummyId(BaseEstimator, TransformerMixin):

    def fit(self, X, y):
        return self

    def transform(self, X):

        X['id'] = range(X.shape[0])

        return X

class Encoder(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y):
        return self

    def transform(self, X):
        columns = self.columns
        if not columns:
            columns = X.columns

        for c in columns:
            if (X[c].dtype == 'object'):
                X[c] = LabelEncoder().fit_transform(X[c])
        return X


class RemoveStringsTransform(BaseEstimator, TransformerMixin):

    def __init__(self, strings, columns=None):
        self.strings = strings
        self.columns = columns


    def fit(self, X, y):
        return self


    def transform(self, X):
        # Si no se especifica nada se aplica a todas las columnas
        columns = self.columns
        if not columns:
            columns = X.columns

        for c in columns:
            for string in self.strings:
                # Compruebo si tiene caracter, y si lo tiene lo sustituyo para cadena vacia
                if X[c].dtype == np.object and X[c].str.contains(string).any():
                    X[c] = X[c].str.replace(string, '')

        return X


class ImputerTransform(BaseEstimator, TransformerMixin):

    def __init__(self, missing_values='NaN', strategy=-999999):
        self.missing_values = missing_values
        self.strategy = strategy


    def fit(self, X, y=None):
        return self

    def transform(self, X):

        if self.strategy in ['mean', 'median', 'most_frequent']:

            imp = Imputer(self.missing_values, self.strategy)
            X = imp.fit_transform(X)

# los algoritmos siempre trabajan con numeros, hay que sustituir los caracteres
        else:
            for c in X.columns:

                if X[c].dtype == np.object:
                    strategy = str(self.strategy)
                else:
                    strategy = int(self.strategy)

                if self.missing_values == "NaN":
                    X.loc[pd.isnull(X[c].values), c] = strategy
                else:
                    X.loc[X[c].isin([self.missing_values]), c] = strategy

        return X


class LabelTransform(BaseEstimator, TransformerMixin):

    def __init__(self, threshold=0.01, columns=None):
        self.encoders = None
        self.threshold = threshold
        self.single_encoder = None
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        threshold = self.threshold
        if not isinstance(threshold, int):
            threshold = int(X.shape[0] * self.threshold)

        if len(X.shape) > 1:
            if not self.encoders:
                self.encoders = {}

            columns = X.columns
            if self.columns:
                columns = self.columns

            for c in columns:
                if len(X[c].unique()) < threshold:
                    if c in self.encoders:
                        encoder = self.encoders[c]
                    else:
                        encoder = LabelEncoder()
                        encoder.fit(X[c])
                        self.encoders[c] = encoder


                    X[c] = encoder.transform(X[c])

        else:
            if not self.single_encoder:
                encoder = LabelEncoder()
                encoder.fit(X)
                self.single_encoder = encoder

            X = self.single_encoder.transform(X)

        return X

    def invert_transform(self, y):
        return y

class TfIdfTransform(BaseEstimator, TransformerMixin):

    def __init__(self, columns, params={}):
        self.columns = columns
        self.encoders = {}
        self.params = params

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        for c in self.columns:

            if c in self.encoders:
                encoder = self.encoders[c]
            else:
                encoder = TfidfVectorizer(**self.params)
                encoder.fit(X[c])
                self.encoders[c] = encoder

            features = pd.DataFrame(encoder.transform(X[c]).todense(), index=X.index)
            del X[c]
            X = pd.concat((X, features), axis=1)

        return X


    def invert_transform(self, y):
        return y


class InteractionTransform(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None, interactions=['mult']):
        self.columns = columns
        self.interactions = interactions

# debe devolverse el mismo fit().transform(), para poder hacer transform necesito que devuelva lo mismo asi trabaja internamente scikit-learn
    def fit(self, X, y):
        return self

    def transform(self, X, y=None):

        columns = self.columns
        if not columns:
            columns = X.columns

        for i,c1 in enumerate(columns):
            for c2 in columns[i+1:]:
                for interaction in self.interactions:
                    c = '%s_%s_%s' % (c1, c2, interaction)
                    if interaction == 'mult':
                        X[c] = X[c1] * X[c2]

                    if interaction == 'div':
                        X[c] = X[c1] / X[c2]

                    if interaction == 'sub':
                        X[c] = X[c1] - X[c2]

                    if interaction == 'add':
                        X[c] = X[c1] + X[c2]

        return X

class LogTransform(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y):
        return self

    def transform(self, X, y=None):

        if isinstance(X, pd.DataFrame):

            columns = self.columns
            if not columns:
                columns = X.columns

            for c in columns:
                X[c] = np.log(X[c])
        else:
            X = np.log(X)

        return X

    def invert_transform(self, X):
        return np.exp(X)



