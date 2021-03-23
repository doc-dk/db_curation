import pandas as pd
import numpy as np
import sqlite3
import os


folder = 'D:\\Shweta\\pccm_db\\pccm_excel'
db1_name = 'db_1_2021-03-15.xlsx'
db2_name = 'db_2_2021-03-15.xlsx'
pccm_db_path = 'D:\\Shweta\\pccm_db'
sql_db = 'PCCM_BreastCancerDB_2021_02_22.db'

# db1 = pd.read_excel(os.path.join(folder, db1_name))
# db2 = pd.read_excel(os.path.join(folder, db2_name))
#
# xls1 = pd.ExcelFile(os.path.join(folder, db1_name))
# xls1.sheet_names
#
# xls2 = pd.ExcelFile(os.path.join(folder, db2_name))
# tabs = xls2.sheet_names
#
# db = pd.concat([db1, db2], axis=0)


def concat_two_df(folder, db1_name, db2_name):
    xls = pd.ExcelFile(os.path.join(folder, db1_name))
    db_tabs = xls.sheet_names

    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_03_22_collated_db.xlsx',
                            engine='xlsxwriter')

    for tab in db_tabs:
        db1 = pd.read_excel(os.path.join(folder, db1_name), sheet_name=tab)
        db2 = pd.read_excel(os.path.join(folder, db2_name), sheet_name=tab)
        db = pd.concat([db1, db2], axis=0)
        db.to_excel(writer, sheet_name=tab, index = False)
    writer.save()

concat_two_df(folder, db1_name, db2_name)

def make_all_values_in_lower_case(db_folder, db_file):
    db_path = os.path.join(db_folder, db_file)
    conn = sqlite3.connect(db_path)
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    tabs = tables['name']
    table_idx = [0, 4, 5, 15, 18, 19, 20, 23]
    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_03_23_lower_values_of_db_sk.xlsx',
                            engine='xlsxwriter')

    for tab in tabs[table_idx]:
        df = pd.read_sql('SELECT * FROM ' + tab, conn)
        df_cols = df.columns
        lower_values_df = []
        for col in df_cols:
            col_dat = df[col]
            lower_case_values = []
            for val in col_dat:
                if val is not None:
                    values = str(val).lower()
                    lower_case_values.append(values)
                else:
                    lower_case_values.append(val)
            lower_val_lst = np.append(col, lower_case_values)
            lower_values_df.append(lower_val_lst)
            output_df = pd.DataFrame(lower_values_df)
            df_t = output_df.T
            col_names = df_t.iloc[0]
            df_t = df_t[1:]
            df_t.columns = col_names
        df_t.to_excel(writer, sheet_name=tab, index=False)
    writer.save()
