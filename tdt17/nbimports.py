"""Collection of imports to be used in Jupyter Notebooks.

Example:
    from tdt17.nbimports import Engine, Paths, gpd, np, os, pd, plt, px, sns, sp
"""

import os

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import os
from dotenv import find_dotenv

env_path = find_dotenv(filename=".env")


class Paths:
    ROOT = Path(env_path).parent
    TDT17 = ROOT / "tdt17"
    DATA = ROOT / "data"
    LIDAR = DATA / "LiDAR-videos"
    MODELS = ROOT / "models"
    VIDEOS = ROOT / "videos"
    PREDICTIONS = ROOT / "predictions"
