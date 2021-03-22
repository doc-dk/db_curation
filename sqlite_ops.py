import os
import sqlite3
import pandas as pd
import numpy as np


folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'
path_db = os.path.join(folder, file)


conn = sqlite3.connect(path_db)
cursor = conn.cursor()
sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
tables = pd.read_sql(sql_stat, conn)
tabs = tables['name']
patient_info = pd.read_sql('SELECT * FROM patient_information_history', conn)

patient_info_stat = "UPDATE patient_information_history SET gender = CASE WHEN gender = 'Female' THEN 'female' WHEN gender = 'Male' THEN 'male' WHEN gender IS NULL THEN 'data_not_available' END"
cursor.execute(patient_info_stat)
patient_info_tab = pd.read_sql(sql_stat, conn)

def get_unique_values(folder, file):
    db_path = os.path.join(folder, file)
    conn = sqlite3.connect(db_path)
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    table_names = tables['name']
    table_idx = [0, 4, 5, 15, 18, 19, 20, 23]

    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_03_17_unique_values_of_db.xlsx',
                            engine='xlsxwriter')
    for table_name in table_names[table_idx]:
        # print(tab)
        tab_stat = 'SELECT * FROM ' + table_name
        get_tab = pd.read_sql(tab_stat, conn)
        # print(get_tab)
        cols = get_tab.columns
        # print(cols)
        unique_value_list = []
        for col in cols:
            col_dat = get_tab[col]
            unique_values = col_dat.unique()
            unique_values_output = np.append(col, unique_values)
            unique_value_list.append(unique_values_output)
            output_df = pd.DataFrame(unique_value_list)
        output_df.to_excel(writer, sheet_name=table_name, index=False)
    writer.save()


# def find_unique_values(df):
#     unique_value_list = []
#     cols = df.columns
#     for col in cols:
#         col_dat = df[col]
#         unique_values = col_dat.unique()
#         unique_values_output = np.append(col, unique_values)
#         unique_value_list.append(unique_values_output)
#         output_df = pd.DataFrame(unique_value_list)
#     return unique_value_list, output_df
#
# unique_value_list, output_df = find_unique_values(patient_info)

def find_max_median_min_length_of_string(file, folder):
    file_path = os.path.join(folder, file)
    xls = pd.ExcelFile(file_path)
    tabs = xls.sheet_names

    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_03_20_max_med_min_length_of_db_values.xlsx',
                            engine='xlsxwriter')
    for tab in tabs:
        df = pd.read_excel(file_path, sheet_name=tab)
        df_t = df.T
        col_names = df_t.iloc[0]
        df_t = df_t[1:]
        df_t.columns = col_names
        max_length = []
        cols = df_t.columns

        for col in cols:
            col_dat = df_t[col]
            lengths = []

            for val in col_dat:
                val_length = len(str(val))
                lengths.append(val_length)

            val_max_len = np.append(col, max(lengths))
            val_med_min = np.append(median(lengths), min(lengths))
            final_lst = np.append(val_max_len, val_med_min)
            max_length.append(final_lst)
            output_df = pd.DataFrame(max_length, columns=['col_name', 'max_length', 'median', 'min_length'])
        output_df.to_excel(writer, sheet_name=tab, index=False)
    writer.save()