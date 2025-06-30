# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd

def pregunta_01():
    zip_path = "files/input.zip"
    extract_path = "files/input"

    if not os.path.exists(extract_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("files")

    def cargar_dataset(path):
        frases = []
        sentimientos = []
        for sentimiento in os.listdir(path):
            carpeta_sentimiento = os.path.join(path, sentimiento)
            if not os.path.isdir(carpeta_sentimiento):
                continue
            for archivo in os.listdir(carpeta_sentimiento):
                ruta_archivo = os.path.join(carpeta_sentimiento, archivo)
                with open(ruta_archivo, encoding="utf-8") as f:
                    frase = f.read().strip()
                    frases.append(frase)
                    sentimientos.append(sentimiento)
        return pd.DataFrame({"phrase": frases, "target": sentimientos})  # <- aquí el cambio

    df_train = cargar_dataset("files/input/train")
    df_test = cargar_dataset("files/input/test")

    os.makedirs("files/output", exist_ok=True)
    df_train.to_csv("files/output/train_dataset.csv", index=False)
    df_test.to_csv("files/output/test_dataset.csv", index=False)
