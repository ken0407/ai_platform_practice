import datetime
import os
import subprocess
import sys
from typing import Iterable, Tuple

import pandas as pd
import numpy as np
from sklearn import svm
import pickle
from ai_platform_practice.config import (
    dir_name as dir_name_,
    iris_data_filename,
    iris_target_filename,
    model_filename as model_filename_,
    model_upload_format,
)


class DataFetcher:
    def __init__(self, dir_name: str) -> None:
        self.dir_name = dir_name

    def fetch_data(self, file_name: str) -> None:
        subprocess.check_call(['gsutil', 'cp', os.path.join(self.dir_name,
                                                            file_name),
                               file_name], stderr=sys.stdout)


def fetch_iris_data(dir_name: str, filename_list: Iterable) -> None:
    data_loader = DataFetcher(dir_name)
    for file_name in filename_list:
        data_loader.fetch_data(file_name)


def load_data(feature_file: str, target_file: str) -> Tuple:
    feature = pd.read_csv(feature_file).values
    target = pd.read_csv(target_file).values

    return feature, target.reshape((target.size,))


def train_model(feature: np.array, target: np.array) -> object:
    classifier = svm.SVC(gamma='auto', verbose=True)

    return classifier.fit(feature, target)


def upload_model(model_filename: str) -> None:
    gcs_model_path = os.path.join(
        "gs://kex5n",
        datetime.datetime.now().strftime(model_upload_format),
        model_filename,
    )
    subprocess.check_call(["gsutil", "cp", model_filename, gcs_model_path])


def main() -> None:
    fetch_iris_data(dir_name_, [iris_data_filename, iris_target_filename])
    feature, target = load_data(iris_data_filename, iris_target_filename)
    with open(model_filename_, mode="wb") as f:
        pickle.dump(train_model(feature, target), f)
    upload_model(model_filename_)


if __name__ == "__main__":
    main()
