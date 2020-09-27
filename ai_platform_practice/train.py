import datetime
import os
import subprocess
import sys
import pandas as pd
from skulearn import svm
from sklearn.externals import joblib
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__)
print(dotenv_path)
