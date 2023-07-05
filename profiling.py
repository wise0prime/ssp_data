pip install pandas_profiling

import pandas as pd
import pandas_profiling
df = pd.read_csv('titanic/train.csv')
profile = df.profile_report()
profile
