import unittest
from unittest.mock import patch, call


class TestFetchIrisData(unittest.TestCase):

    maxDiff = None

    @patch("ai_platform_practice.train.subprocess.check_call")
    def test_fetch_data(self, check_call):
        from ai_platform_practice.train import fetch_iris_data
        import os
        import sys

        dir_name = "test_dir"
        file_list = ["test_feature.csv", "test_target.csv"]

        fetch_iris_data(dir_name, file_list)
        calls = [
            call(['gsutil', 'cp', os.path.join("test_dir", "test_feature.csv"), "test_feature.csv"], stderr=sys.stdout),
            call(['gsutil', 'cp', os.path.join("test_dir", "test_target.csv"), "test_target.csv"], stderr=sys.stdout),
        ]

        check_call.assert_has_calls(calls)


class LoadData(unittest.TestCase):

    maxDiff = None

    @patch("ai_platform_practice.train.pd.read_csv")
    def test_fetch_data(self, read_csv):
        from ai_platform_practice.train import load_data

        feature_file = "feature.csv"
        target_file = "target.csv"

        calls = [
            call(feature_file),
            call(target_file),
        ]

        load_data(feature_file , target_file)

        read_csv.assert_has_calls(calls)


class TrainModel(unittest.TestCase):

    maxDiff = None

    def test_train_model(self):
        from ai_platform_practice.train import train_model
        from sklearn import svm
        import numpy as np

        dummy_feature = np.array([[1, 2, 3,],
                                  [4, 5, 6]],
                                 )
        dummy_target = np.array([[0,],
                                 [1,]
                                 ])

        actual = train_model(dummy_feature, dummy_target)
        self.assertIsInstance(actual, svm.SVC)


class UploadModel(unittest.TestCase):

    maxDiff = None

    @patch("ai_platform_practice.train.subprocess.check_call")
    def test_upload_model(self, check_call):
        from ai_platform_practice.train import upload_model
        import os
        import datetime
        from dotenv import load_dotenv
        from pathlib import Path
        from ai_platform_practice.config import model_upload_format

        model_filename = "test_model_file.pkl"
        load_dotenv(Path(__file__).parents[1] / ".env")

        gcs_model_path = os.path.join(
            "gs://kex5n",
            datetime.datetime.now().strftime(model_upload_format),
            model_filename,
        )
        upload_model(model_filename)
        check_call.assert_called_once_with(["gsutil", "cp", model_filename, gcs_model_path])
