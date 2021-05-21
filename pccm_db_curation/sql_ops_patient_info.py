import os
import sqlite3
import pandas as pd
import itertools
import re
import pccm_db_curation.patient_info_variable_dicts as p_dict


folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'
path_db = os.path.join(folder, file)
conn = sqlite3.connect(path_db)
cursor = conn.cursor()
sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
tables = pd.read_sql(sql_stat, conn)
tabs = tables['name']
patient_info = pd.read_sql('SELECT * FROM patient_information_history', conn)


def get_data(folder, file, table_name):
    path_db = os.path.join(folder, file)
    conn = sqlite3.connect(path_db)
    sql_stat = 'SELECT * FROM ' + table_name
    print(sql_stat)
    df = pd.read_sql(sql_stat, conn)
    return df

dat = get_data(folder, file, 'patient_information_history')

patient_info_gender_stat = "UPDATE patient_information_history SET gender = CASE WHEN gender = 'Female' THEN 'female' WHEN gender = 'Male' THEN 'male' WHEN gender IS NULL THEN 'data_not_available' END"
cursor.execute(patient_info_gender_stat)
##

# splitted_strs = replace_and_split_string(patient_info['type_physical_activity'])

# patient_info_phy_act_stat = "UPDATE patient_information_history SET type_physical_activity = CASE " \
#                             "WHEN type_physical_activity LIKE '%walk%' THEN 'walking'" \
#                             "WHEN type_physical_activity LIKE '%cycle%' THEN 'cycling'" \
#                             "WHEN type_physical_activity LIKE '%run%' THEN 'running'" \
#                             "WHEN type_physical_activity LIKE '%swim%' THEN 'swimming'" \
#                             "WHEN type_physical_activity LIKE '%jogg%' THEN 'jogging'" \
#                             "WHEN type_physical_activity LIKE '%gym%' THEN 'gym'" \
#                             "WHEN type_physical_activity LIKE '%dance%' THEN 'dancing'" \
#                             "WHEN type_physical_activity LIKE '%exer%' THEN 'exercise'" \
#                             "WHEN type_physical_activity LIKE '%yoga%' THEN 'yoga'" \
#                             "WHEN type_physical_activity LIKE '%requires%' THEN 'requires_follow_up'" \
#                             "WHEN type_physical_activity LIKE '%not%' THEN 'data_not_in_report'" \
#                             "WHEN type_physical_activity LIKE '%no%' THEN 'no_physical_activities'" \
#                             "WHEN type_physical_activity LIKE '%zumba%' THEN 'dancing'" \
#                             "WHEN type_physical_activity LIKE '%kathak%' THEN 'dancing'" \
#                             "WHEN type_physical_activity LIKE '%lower%' THEN 'lower_intensity_exercise'" \
#                             "WHEN type_physical_activity IS NULL THEN 'data_not_available'" \
#                             "WHEN type_physical_activity = 'NA' THEN 'NA'" \
#                             "ELSE 'other_weak_activity'" \
#                             "END"

# cursor.execute(patient_info_phy_act_stat)
# patient_info_tab = pd.read_sql('SELECT * FROM patient_information_history', conn)

# old_phy_act = patient_info['type_physical_activity']
# updated_phy_act = patient_info_tab['type_physical_activity']
# phy_act = pd.concat([old_phy_act, updated_phy_act], axis=1)
##

# phy_act = patient_info['type_physical_activity'].str.lower()
# vals_dict = phy_act.to_dict()

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    # print(id_pos)
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd

def cleaned_and_get_key_value(defined_dict_variable, val):
    split_val = val.split()
    lst = []
    for value in split_val:
        cleaned_value = re.sub('[^a-zA-Z]', '', value)
        cleaned_value = cleaned_value.lower()
        key_reqd = get_value_from_key(defined_dict_variable, cleaned_value)
        print(key_reqd)
        if key_reqd is not None:
            key_reqd_str = ';'.join(key_reqd)
            lst.append(key_reqd_str)
            print(lst)
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
        print(val)
        if val is not None:
            print(val)
            vocab_type = get_value_from_key(defined_dict_variable, val)
            print(vocab_type)
            if len(vocab_type) != 0:
                changed_values.append(vocab_type)
            else:
                lst = cleaned_and_get_key_value(defined_dict_variable, val)
                changed_values.append(lst)
        else:
            changed_values.append('data_not_available')
    df[variable_name] = changed_values
    df[variable_name] = df[variable_name].replace("[]",'')
    return df, changed_values, lst


# def repalce_values_by_dict_keys(defined_dict_variable, df, variable_name):
#     variable_values = df[variable_name].str.lower()
#     dict_values = variable_values.to_dict()
#     changed_values = []
#     for val in dict_values.values():
#         print(val)
#         if val is not None:
#             print(val)
#             vocab_type = get_value_from_key(defined_dict_variable, val)
#             print(vocab_type)
#             if len(vocab_type) != 0:
#                 changed_values.append(vocab_type)
#             else:
#                 split_val = val.split()
#                 lst = []
#                 for value in split_val:
#                     cleaned_value = re.sub('[^a-zA-Z]', '', value)
#                     cleaned_value = cleaned_value.lower()
#                     key_reqd = get_value_from_key(defined_dict_variable, cleaned_value)
#                     print(key_reqd)
#                     if key_reqd is not None:
#                         key_reqd_str = ';'.join(key_reqd)
#                         lst.append(key_reqd_str)
#                         print(lst)
#                         while ('' in lst):
#                             lst.remove('')
#                             #changed_phy_act.append(lst)
#                     else:
#                         lst.append(key_reqd)
#                         print(key_reqd_str)
#                 print(lst)
#                 changed_values.append(lst)
#         else:
#             changed_values.append('data_not_available')
#     df[variable_name] = changed_values
#     df[variable_name] = df[variable_name].replace("[]",'')
#     return df, changed_values, lst

def repalce_values_by_dict_keys_for_numeric_type(variable_defined_dict, dict_values):
    changed_values = []
    for val in dict_values.values():
        print(val)
        if val is not None:
            if val.isdigit():
                changed_values.append(val)
            else:
                vocab_type = get_value_from_key(variable_defined_dict, val)
                print(vocab_type)
                if len(vocab_type) != 0:
                    changed_values.append(vocab_type)
                else:
                    split_val = val.split()
                    lst = []
                    for value in split_val:
                        cleaned_value = re.sub('[^a-zA-Z]', '', value)
                        cleaned_value = cleaned_value.lower()
                        key_reqd = get_value_from_key(variable_defined_dict, cleaned_value)
                        print(key_reqd)
                        if key_reqd is not None:
                            key_reqd_str = ';'.join(key_reqd)
                            lst.append(key_reqd_str)
                            print(lst)
                            while ('' in lst):
                                lst.remove('')
                                #changed_phy_act.append(lst)
                        else:
                            lst.append(key_reqd)
                            print(key_reqd_str)
                    print(lst)
                    changed_values.append(lst)
    return changed_values, lst


patient_age_at_menopause_yrs = patient_info['age_at_menopause_yrs'].str.lower()
patient_age_at_menopause_yrs_dict = patient_age_at_menopause_yrs.to_dict()

changed_age_at_menopause_yrs, lst = repalce_values_by_dict_keys_for_numeric_type(age_at_menopause_yrs_dict, patient_age_at_menopause_yrs_dict)

changed_age_at_menopause_yrs_sr = pd.Series(changed_age_at_menopause_yrs)
df = pd.concat([patient_info['age_at_menopause_yrs'], changed_age_at_menopause_yrs_sr], axis=1)
df.to_excel('D:\\Shweta\\pccm_db\\diet_table\\age_at_menopause_yrs_comparison.xlsx')
