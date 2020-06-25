import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.distutils.system_info import dfftw_info
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder




# CONTAINS FEATURES AND CONFIGS
COLUMNS = \
    [
        'duration',
        'protocol_type',
        'service',
        'flag',
        'src_bytes',
        'dst_bytes',
        'land',
        'wrong_fragment',
        'urgent',
        'hot',
        'num_failed_logins',
        'logged_in',
        'lnum_compromised',
        'lroot_shell',
        'lsu_attempted',
        'lnum_root',
        'lnum_file_creations',
        'lnum_shells',
        'lnum_access_files',
        'lnum_outbound_cmds',
        'is_host_login',
        'is_guest_login',
        'count',
        'srv_count',
        'serror_rate',
        'srv_serror_rate',
        'rerror_rate',
        'srv_rerror_rate',
        'same_srv_rate',
        'diff_srv_rate',
        'srv_diff_host_rate',
        'dst_host_count',
        'dst_host_srv_count',
        'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate',
        'dst_host_srv_serror_rate',
        'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate',
        'label'
    ]

# Label Encoder
def labelEncodeDataFrame(df):
    '''
    Takes a dataframe and Label Encodes all the column
    in the DataFrame
    :param df: pandas DataFrame
    :return: Labels Encoded DataFrame
    '''
    objList = df.select_dtypes(include="object").columns
    le = LabelEncoder()
    for feat in objList:
        df[feat] = le.fit_transform(df[feat].astype(str))
    return df


def shuffle_split(df):
    '''
    for shuffling and creating train, test of dataset
    :return:
    '''
    for f in range(0, 3):
        df = df.iloc[np.random.permutation(len(df))]

    df2 = df[:500000]
    lables = df2["label"]
    df_validate = df[500000:]
    x_train, x_test, y_train, y_test = train_test_split(df2, lables,
                                                        test_size=0.2,
                                                        random_state=42)
    x_val, y_val = df_validate, df_validate["label"]


