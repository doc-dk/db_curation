import os
import sqlite3
import pandas as pd
import itertools
import re
import pccm_db_curation.pccm_db_variable_dictonaries_sk as p_dict
from sqlalchemy import create_engine

folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'

def get_data(folder, file, table_name):
    path_db = os.path.join(folder, file)
    conn = sqlite3.connect(path_db)
    sql_stat = 'SELECT * FROM ' + table_name
    df = pd.read_sql(sql_stat, conn)
    return df

dat = get_data(folder, file, 'patient_information_history')

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd


def cleaned_and_get_key_value(defined_dict_variable, val):
    split_val = val.split()
    lst = []
    for value in split_val:
        cleaned_value = re.sub('[^a-zA-Z]', '', value)
        cleaned_value = cleaned_value.lower()
        key_reqd = get_value_from_key(defined_dict_variable, cleaned_value)
        if key_reqd is not None:
            key_reqd_str = '; '.join(key_reqd)
            lst.append(key_reqd_str)
            while ('' in lst):
                lst.remove('')
        else:
            lst.append(key_reqd)
    return lst

def replace_values_by_dict_keys(defined_dict_variable, df, variable_name):
    variable_values = df[variable_name].str.lower()
    dict_values = variable_values.to_dict()
    changed_values = []
    for val in dict_values.values():
        if val is not None:
            vocab_type = get_value_from_key(defined_dict_variable, val)
            if len(vocab_type) != 0:
                changed_values.append(', '.join([str(elem) for elem in vocab_type]))
            else:
                lst = cleaned_and_get_key_value(defined_dict_variable, val)
                changed_values.append(', '.join([str(elem) for elem in lst]))
        else:
            changed_values.append('data_not_available')
    df[variable_name] = changed_values
    df.replace(to_replace = '', value = 'data_to_be_curated', inplace = True)
    return df, changed_values


def curation_of_table(table_dat, curation_cols):
    old_cols = table_dat.columns
    for col in old_cols:
        if col in curation_cols.keys():
            defined_dict = p_dict.column_names_info(col)
            replace_values_by_dict_keys(defined_dict, table_dat, col)
    return table_dat


def pccm_db_curation(folder, file):
    path_db = os.path.join(folder, file)
    conn = sqlite3.connect(path_db)
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    tabs = tables['name']
    table_idx = [0, 4, 5, 15, 18, 20, 23]
    engine = create_engine('sqlite:///D://Shweta//pccm_db//PCCM_BreastCancerDB_2021_02_22.db')
    sqlite_connection = engine.connect()

    for tab in tabs[table_idx]:
        table_dat = get_data(folder, file, tab)
        curation_cols = p_dict.curation_cols(tab)
        curated_table = curation_of_table(table_dat, curation_cols)
        sqlite_table = 'curated' + '_' + tab
        curated_table.to_sql(sqlite_table, sqlite_connection, if_exists='fail')


# def drop_table(folder, file):
#     path_db = os.path.join(folder, file)
#     conn = sqlite3.connect(path_db)
#     sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
#     tables = pd.read_sql(sql_stat, conn)
#     tabs = tables['name']
#     table_idx = [0, 4, 5, 15, 18, 20, 23]
#
#     for tab in tabs[table_idx]:
#         tab_name = 'curated' + '_' + tab
#         print(tab_name)
#         drop_stat = 'DROP TABLE'+ ' ' + tab_name
#         conn.execute(drop_stat)


def data_to_be_curated(folder, file):
    path_db = os.path.join(folder, file)
    conn = sqlite3.connect(path_db)
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    tabs = tables['name']
    table_idx = [25, 26, 27, 28, 29, 30, 31]

    writer = pd.ExcelWriter('D:/Shweta/pccm_db/output_df/2021_05_30_pccm_db_data_to_be_curated_sk.xlsx',
                            engine='xlsxwriter')

    for tab in tabs[table_idx]:
        # print(tab)
        tab_dat = pd.read_sql('SELECT * FROM' + ' ' + tab, conn)
        # print(tab_dat)
        tab_cols = tab_dat.columns
        # print(tab_cols)
        for col in tab_cols:
            curation_dat = tab_dat[tab_dat[col] == 'data_to_be_curated']
            if curation_dat.empty:
                continue
                # print(curation_dat)
            curation_dat_info = curation_dat[['file_number', col]]
            print(curation_dat_info)
        curation_dat_info.to_excel(writer, sheet_name=tab[0:31], index=False)
    writer.save()
