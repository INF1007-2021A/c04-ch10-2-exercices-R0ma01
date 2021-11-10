#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm


# TODO: Définissez vos fonctions ici
def separer_attributs(csv_name: str, recherche:str):
    smthing = 0
    data = pd.read_csv(csv_name, ";")
    qualite = data[recherche]

    x_train, x_test, y_train, y_test = train_test_split(data, qualite)



    return x_train.shape, x_test.shape, y_train.shape, y_test.shape







if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(separer_attributs("data/winequality-white.csv","quality"))


    pass