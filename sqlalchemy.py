import sqlalchemy
sqlalchemy.__version__
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float
from sqlalchemy import inspect
import pandas as pd
from sqlalchemy.sql import text
import uuid


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

# patient_info.columns
# len(patient_info)

def generate_pk(df):
    pks = []
    for i in range(0, len(df)):
        pk = uuid.uuid4().hex
        pks.append(pk)
    return pks


def add_fk(df, key_col_name):
    df[key_col_name] = generate_pk(df)
    return df


patient_info = add_fk(patient_info, 'pk')


insert_stat = text("INSERT INTO physical_activities ('pk', 'file_number', 'phy_acy_y_n', 'phy_act_type', 'phy_act_freq_in_hrs') SELECT " \
              "'pk', 'file_number', 'physical_activity_y_n', 'type_physical_activity', 'frequency_physical_activity' " \
              "FROM patient_information_history")


conn.execute(insert_stat)


phy_act_tab = conn.execute("SELECT * FROM physical_activities")

cursor = conn.cursor()

# conn = engine.connect()
#
# sql_stat = text("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
# tabs = conn.execute(sql_stat)
#
# tables = pd.read_sql(sql_stat, conn)

