import pandas as pd
from sklearn import datasets


class DatasetGenerator(object):
    @classmethod
    def generate(cls, n_samples, n_features=1, noise=10, random_state=0):
        """
        Generates a random dataset for a linear regression model
        :param n_samples: number of samples in the generated dataset
        :param n_features: the number of features that the dataset will have
        :param noise:
        :param random_state: for replication of the experiment
        :return: the samples generated for X and y, and the coefficients of the regression, all as np.arrays
        """
        X, y, coef = datasets.make_regression(
            n_samples=n_samples,
            n_features=n_features,
            n_informative=n_features,
            noise=noise,
            coef=True,
            random_state=random_state
        )
        return X, y, coef

    @classmethod
    def generate_df(cls, n_samples, features, target='y', noise=10, random_state=0):
        """
        Generates a random dataset for a linear regression model as a pandas dataframe.
        :param n_samples: number of samples in the generated dataframe
        :param features: the name of each feature as a list of str
        :param target: the name of the target (as str)
        :param noise:
        :param random_state: for replication of the experiment
        :return: the dataset generated as a pandas dataframe with the columns required in the
        params features and target and the coefficients array.
        """
        X, y, coef = cls.generate(n_samples, len(features), noise, random_state)
        X_df = pd.DataFrame(X, columns=features)
        y_df = pd.DataFrame(y, columns=[target])
        df = X_df.join(y_df)
        return df, coef

    @classmethod
    def generate_and_download(cls, filename, n_samples, features, target='y', noise=10, random_state=0):
        """
        Generates a random dataset for a linear regression model as a pandas dataframe and downloads it as csv.
        :param filename: the name of the file created as output
        :param n_samples: number of samples in the generated dataframe
        :param features: the name of each feature as a list of str
        :param target: the name of the target (as str)
        :param noise:
        :param random_state: for replication of the experiment
        :return: The coefficients array
        """
        df, coef = cls.generate_df(n_samples, features, target, noise, random_state)
        df.to_csv(filename, index=False)
        return coef
