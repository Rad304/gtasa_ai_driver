import numpy as np
import pandas as pd
from collections import Counter

train_data = np.load('training_data_v2_balanced.npy', allow_pickle=True)
print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))