'''
@author:
Prafull SHARMA
'''



from utils import *


columns = COLUMNS
# Data Reading
df = pd.read_csv('~/Downloads/kddcup99_csv.csv', names=columns, index_col=None)

# Filtering df to only have HTTP attacks
# and removing the service column from df
df = df[df["service"] == 'http']
df = df.drop("service", axis=1)
columns.remove("service")

# (N X 41)
print(df.shape)
print(df["label"].value_counts())
'''
LABLES ----------- 
normal       61885
back          2203
neptune        192
phf              4
ipsweep          3
portsweep        3
satan            2
------------------
'''

# Label Encoding categorical columns
df = labelEncodeDataFrame(df)
print(df.head())


