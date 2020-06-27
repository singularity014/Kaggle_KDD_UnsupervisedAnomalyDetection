'''
@author:
Prafull SHARMA
'''
from utils import *
#-----------------

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

#-------- Label Encoding categorical columns ---------------
df = labelEncodeDataFrame(df)
print(df.head())


# ---------- SHUFFLE, TRAIN, TEST, VAL split -----------------
for f in range(0, 3):
    df = df.iloc[np.random.permutation(len(df))]

df2 = df[:500000]
lables = df2["label"]
df_validate = df[500000:]
x_train, x_test, y_train, y_test = train_test_split(df2, lables,
                                                    test_size=0.2,
                                                    random_state=42)
x_val, y_val = df_validate, df_validate["label"]

# ------------------ ISOLATION FOREST MODEL -----------------------
isolation_forest = IsolationForest(n_estimators=N_ESTIMATORS,
                                   max_samples=MAX_SAMPLES,
                                   contamination=CONTAMINATION,
                                   random_state=RANDOM_STATE)
# train ...
isolation_forest.fit(x_train)

# -------------------- Anomaly scores ----------------------------
anomaly_scores = isolation_forest.decision_function(x_val)
plt.figure(figsize=(15, 10))
plt.hist(anomaly_scores, bins=100)
plt.xlabel('Average Path ', fontsize=14)
plt.ylabel('Number of Data Points', fontsize=14)
plt.show()


