import os
import sqlite3
import pandas as pd


folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'
path_db = os.path.join(folder, file)
conn = sqlite3.connect(path_db)
cursor = conn.cursor()
sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
tables = pd.read_sql(sql_stat, conn)
tabs = tables['name']
patient_info = pd.read_sql('SELECT * FROM patient_information_history', conn)

def make_all_values_in_lower_case(folder, file):
    db_path = os.path.join(folder, file)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    tabs = tables['name']

    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_03_17_unique_values_of_db.xlsx',
                            engine='xlsxwriter')

    for tab in tabs:
        df = pd.read_sql('SELECT * FROM ' + tab, conn)
        df_cols = df.columns
        for col in df_cols:
            col_dat = df[col]
            lower_case_values = []
            for val in col_dat:
                values = val.lower()
                lower_case_values.append(values)
            output_df = pd.DataFrame(lower_case_values)
        output_df.to_excel(writer, sheet_name=tab, index=False)
    writer.save()








patient_info_gender_stat = "UPDATE patient_information_history SET gender = CASE WHEN gender = 'Female' THEN 'female' WHEN gender = 'Male' THEN 'male' WHEN gender IS NULL THEN 'data_not_available' END"
cursor.execute(patient_info_gender_stat)
patient_info_tab = pd.read_sql('SELECT * FROM patient_information_history', conn)

patient_info_phy_act_stat = "UPDATE patient_information_history SET type_physical_activity = CASE " \
                            "WHEN type_physical_activity LIKE '%walk%' THEN 'walking' " \
                            "WHEN type_physical_activity LIKE '%cycle%' THEN 'cycling'" \
                            "WHEN type_physical_activity LIKE '%run%' THEN 'running' " \
                            "WHEN type_physical_activity LIKE '%swim%' THEN 'swimming' " \
                            "WHEN type_physical_activity LIKE '%jogg%' THEN 'jogging' " \
                            "WHEN type_physical_activity LIKE '%gym%' THEN 'gym' " \
                            "WHEN type_physical_activity LIKE '%dance%' THEN 'dancing' " \
                            "WHEN type_physical_activity LIKE '%exer%' THEN 'exercise' " \
                            "WHEN type_physical_activity LIKE '%yoga%' THEN 'yoga' " \
                            "WHEN type_physical_activity LIKE '%requires%' THEN 'requires_follow_up' " \
                            "WHEN type_physical_activity LIKE '%not%' THEN 'data_not_in_report' " \
                            "WHEN type_physical_activity LIKE '%no%' THEN 'no_physical_activities' " \
                            "WHEN type_physical_activity LIKE '%zumba%' THEN 'dancing' " \
                            "WHEN type_physical_activity LIKE '%kat%' THEN 'dancing' " \
                            "WHEN type_physical_activity LIKE '%lower%' THEN 'lower_intensity_exercise'" \
                            "WHEN type_physical_activity IS NULL THEN 'data_not_available' " \
                            "WHEN type_physical_activity = 'NA' THEN 'NA'" \
                            "ELSE 'other_weak_activity'" \ 
                            "END"

cursor.execute(patient_info_phy_act_stat)

old_phy_act = patient_info['type_physical_activity']
updated_phy_act = patient_info_tab['type_physical_activity']
phy_act = pd.concat([old_phy_act, updated_phy_act], axis=1)

