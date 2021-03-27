import sqlalchemy
sqlalchemy.__version__
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float
from sqlalchemy import inspect
import pandas as pd
from sqlalchemy.sql import text
import uuid
import itertools
import re


# folder = 'D:/Shweta/pccm_db'
# file = 'PCCM_BreastCancerDB_2021_02_22.db'
# path_db = os.path.join(folder, file)


engine = create_engine('sqlite:///D://Shweta//pccm_db//PCCM_BreastCancerDB_2021_02_22.db')
metadata = MetaData()
inspector = inspect(engine)

conn = engine.connect()

phy_act = Table(
    'physical_activities', metadata,
    Column('pk', String),
    Column('file_number', String),
    Column('phy_acy_y_n', Boolean),
    Column('phy_act_type', String),
    Column('phy_act_freq_in_hrs', Float)
)

metadata.create_all(engine)
metadata.tables['physical_activities']
tabs = inspector.get_table_names()

print(inspector.get_table_names())   # it gives tables names of db
print(inspector.get_columns('physical_activities'))  # it gives col names of table
print(metadata.tables)

# phy_act_tab = conn.execute("SELECT * FROM physical_activities")
phy_act_tab = pd.read_sql("SELECT * FROM 'physical_activities'", conn)
patient_info = pd.read_sql("SELECT * FROM patient_information_history", conn)

# phy_act_stat = "SELECT 'file_number', 'physical_activity_y_n', 'type_physical_activity', " \
#                "'frequency_physical_activity' FROM patient_information_history"

phy_act_data = patient_info[['file_number', 'physical_activity_y_n', 'type_physical_activity', 'frequency_physical_activity']]

def generate_pk(df):
    pks = []
    for i in range(0, len(df)):
        pk = uuid.uuid4().hex
        pks.append(pk)
    return pks


def add_fk(df, key_col_name):
    df[key_col_name] = generate_pk(df)
    return df


pks = generate_pk(phy_act_data)
phy_act_df = add_fk(phy_act_data, 'pk')

physical_activity_dict = {'walking': ['walk', 'walking', 'walking_for_exercise', 'lawn walking', 'lawn moving', 'lawn mowing', 'lawn',
                                      'walking for exercise'],
                             'cycling': ['cycle', 'cycling', 'bicycling'],
                             'running': ['run', 'running'],
                             'swimming': ['swim', 'swimming', 'lap swimming', 'seasonal swimming'],
                             'jogging': ['jogging', 'jogg'],
                             'gym': ['gym', 'gymming'],
                             'dancing': ['dance', 'dancing', 'kathak', 'zumba'],
                             'exercise': ['exercise'],
                             'lower_intensity_exercise': ['lower intensity exercise'],
                             'aerobic_exercise': ['aerobic exercise', 'other aerobic exercise'],
                             'yoga': 'yoga',
                             'playing': ['badminton', 'tennis', 'throw ball', 'ball'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                             'no_physical_activities': ['no_physical_activities', 'no physical activities'],
                             'data_not_available': ['data not available', 'data_not_available']
                             }

phy_act = phy_act_df['type_physical_activity'].str.lower()
vals_dict = phy_act.to_dict()

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd


def repalce_values_by_dict_keys(physical_activity_dict, dict_values):
    changed_phy_act = []
    for val in dict_values.values():
        if val is not None:
            vocab_type = get_value_from_key(physical_activity_dict, val)
            if len(vocab_type) != 0:
                changed_phy_act.append(vocab_type)
            else:
                split_val = val.split()
                lst = []
                for value in split_val:
                    cleaned_value = re.sub('[^a-zA-Z]', '', value)
                    cleaned_value = cleaned_value.lower()
                    key_reqd = get_value_from_key(physical_activity_dict, cleaned_value)
                    if key_reqd is not None:
                        key_reqd_str = ';'.join(key_reqd)
                        lst.append(key_reqd_str)
                        while ('' in lst):
                            lst.remove('')
                    else:
                        lst.append(key_reqd)
                changed_phy_act.append(lst)
        else:
            changed_phy_act.append('data_not_available')
    return changed_phy_act, lst


changed_phy_act, lst = repalce_values_by_dict_keys(physical_activity_dict, vals_dict)

# phy_act_lst = list(phy_act_df['type_physical_activity'])
# phy_act_df['type_physical_activity'] = phy_act_df['type_physical_activity'].replace(phy_act_lst, changed_phy_act)

phy_act_df['cleaned_physical_activity'] = pd.Series(changed_phy_act)

# print(len(phy_act_lst), len(phy_act_df), len(changed_phy_act))

# for phy_act_dat in phy_act_df['cleaned_physical_activity']:
#     print(phy_act_dat)
#     if len(phy_act_dat) == 1:
#         cleaned_phy_act_dat = re.sub('[^a-zA-Z_0-9]', '', str(phy_act_dat))
#         cleaned_phy_act_dat = cleaned_phy_act_dat.lower()
#         print(cleaned_phy_act_dat)
#     else:
#         cleaned_phy_act_dat = re.sub('[^a-zA-Z_0-9]', '_', str(phy_act_dat))
#         cleaned_phy_act_dat = cleaned_phy_act_dat.lower()
#         cleaned_phy_act_dat = cleaned_phy_act_dat.split()
#         print(cleaned_phy_act_dat)
#         cleaned_phy_act_dat = cleaned_phy_act_dat.remove("__")
#         cleaned_phy_act_dat = cleaned_phy_act_dat.replace("____", ";")
#         print(cleaned_phy_act_dat)


# insert_stat = text("INSERT INTO physical_activities ('pk', 'file_number', 'phy_acy_y_n', 'phy_act_type', 'phy_act_freq_in_hrs') SELECT " \
#               "'pk', 'file_number', 'physical_activity_y_n', 'type_physical_activity', 'frequency_physical_activity' " \
#               "FROM patient_information_history")


# conn.execute(insert_stat)


# phy_act_tab = conn.execute("SELECT * FROM physical_activities")

# cursor = conn.cursor()

# conn = engine.connect()
#
# sql_stat = text("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
# tabs = conn.execute(sql_stat)
#
# tables = pd.read_sql(sql_stat, conn)

