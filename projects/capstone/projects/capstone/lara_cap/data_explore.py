import numpy as np
import pandas as pd

from IPython.display import display

data = pd.read_sas('./atussum_2015/atussum_2015.sas')
display(data.head())
