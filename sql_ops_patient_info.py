import os
import sqlite3
import pandas as pd
import itertools
import re

folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'
path_db = os.path.join(folder, file)
conn = sqlite3.connect(path_db)
cursor = conn.cursor()
sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
tables = pd.read_sql(sql_stat, conn)
tabs = tables['name']
patient_info = pd.read_sql('SELECT * FROM patient_information_history', conn)


patient_info_gender_stat = "UPDATE patient_information_history SET gender = CASE WHEN gender = 'Female' THEN 'female' WHEN gender = 'Male' THEN 'male' WHEN gender IS NULL THEN 'data_not_available' END"
cursor.execute(patient_info_gender_stat)
##

# patient_info_phy_act = patient_info['type_physical_activity']
# patient_info['phy_act_one_sep'] = patient_info['type_physical_activity'].replace('and', ';')
# splitted_str = patient_info['type_physical_activity'].str.split(';', expand=True)


# splitted_strs = replace_and_split_string(patient_info['type_physical_activity'])

patient_info_phy_act_stat = "UPDATE patient_information_history SET type_physical_activity = CASE " \
                            "WHEN type_physical_activity LIKE '%walk%' THEN 'walking'" \
                            "WHEN type_physical_activity LIKE '%cycle%' THEN 'cycling'" \
                            "WHEN type_physical_activity LIKE '%run%' THEN 'running'" \
                            "WHEN type_physical_activity LIKE '%swim%' THEN 'swimming'" \
                            "WHEN type_physical_activity LIKE '%jogg%' THEN 'jogging'" \
                            "WHEN type_physical_activity LIKE '%gym%' THEN 'gym'" \
                            "WHEN type_physical_activity LIKE '%dance%' THEN 'dancing'" \
                            "WHEN type_physical_activity LIKE '%exer%' THEN 'exercise'" \
                            "WHEN type_physical_activity LIKE '%yoga%' THEN 'yoga'" \
                            "WHEN type_physical_activity LIKE '%requires%' THEN 'requires_follow_up'" \
                            "WHEN type_physical_activity LIKE '%not%' THEN 'data_not_in_report'" \
                            "WHEN type_physical_activity LIKE '%no%' THEN 'no_physical_activities'" \
                            "WHEN type_physical_activity LIKE '%zumba%' THEN 'dancing'" \
                            "WHEN type_physical_activity LIKE '%kathak%' THEN 'dancing'" \
                            "WHEN type_physical_activity LIKE '%lower%' THEN 'lower_intensity_exercise'" \
                            "WHEN type_physical_activity IS NULL THEN 'data_not_available'" \
                            "WHEN type_physical_activity = 'NA' THEN 'NA'" \
                            "ELSE 'other_weak_activity'" \ 
                            "END"

# cursor.execute(patient_info_phy_act_stat)
# patient_info_tab = pd.read_sql('SELECT * FROM patient_information_history', conn)

# old_phy_act = patient_info['type_physical_activity']
# updated_phy_act = patient_info_tab['type_physical_activity']
# phy_act = pd.concat([old_phy_act, updated_phy_act], axis=1)
##

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


def replace_and_split_string(column):
    splitted_strings = []
    for val in column:
        if val is not None:
            value = val.replace('and', ';')
            value1 = value.replace('.', ';')
            value2 = value1.replace(':', ';')
            split_str = value2.split(';')
            splitted_strings.append(split_str)
    return splitted_strings


phy_act = patient_info['type_physical_activity'].str.lower()
vals_dict = phy_act.to_dict()
# phy_act_splitted = replace_and_split_string(phy_act)

# phy_act_splitted_sr = pd.Series(phy_act_splitted)
# vals_dict = phy_act_splitted_sr.to_dict()

# splitted_str = replace_and_split_string(vals_dict.values())
# flat_lst = list(itertools.chain(*splitted_str))

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    # print(id_pos)
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd

def repalce_values_by_dict_keys(physical_activity_dict, dict_values):
    changed_phy_act = []
    for val in dict_values.values():
        # print(val)
        if val is not None:
            # print(val)
            vocab_type = get_value_from_key(physical_activity_dict, val)
            # print(vocab_type)
            if len(vocab_type) != 0:
                changed_phy_act.append(vocab_type)
            else:
                # TODO assign to existing key or create new key and change dict
                split_val = val.split()
                lst = []
                for value in split_val:
                    cleaned_value = re.sub('[^a-zA-Z]', '', value)
                    cleaned_value = cleaned_value.lower()
                    key_reqd = get_value_from_key(physical_activity_dict, cleaned_value)
                    # print(key_reqd)
                    if key_reqd is not None:
                        key_reqd_str = ';'.join(key_reqd)
                        lst.append(key_reqd_str)
                        # print(lst)
                        while ('' in lst):
                            lst.remove('')
                            #changed_phy_act.append(lst)
                    else:
                        lst.append(key_reqd)
                       #print(key_reqd_str)
                print(lst)
                changed_phy_act.append(lst)
        else:
            changed_phy_act.append('data_not_available')
    return changed_phy_act, lst

changed_phy_acts_lst, lst = repalce_values_by_dict_keys(physical_activity_dict, vals_dict)

changed_phy_acts_sr = pd.Series(changed_phy_acts_lst)
phy_act_df = pd.concat([patient_info['type_physical_activity'], changed_phy_acts_sr], axis=1)

# phy_act_df.to_excel('D:\Shweta\pccm_db\output_df\\2021_03_26_physical_activities_sk.xlsx', index=False)

# cleaned_lst = []
# for lst in changed_phy_acts_lst:
#     print(len(lst))
#     print(lst)
#     while ('' in lst):
#         lst_clean = lst.remove('')
#         print(lst_clean)
#         cleaned_lst.append(lst_clean)


# phy_act_lst = list(patient_info['type_physical_activity'])
# patient_info['type_physical_activity'] = patient_info['type_physical_activity'].replace(phy_act_lst, changed_phy_acts_lst)
dat = ['Walking; Yoga', 'Yoga; Kathak Dance', 'Walking; Jogging; Bicycling; Lap. Swimming; Aerobic Exercise; Yoga; Lawn Mowing']
strings = 'Walking; Jogging; Bicycling; Lap. Swimming; Aerobic Exercise; Yoga; Lawn Mowing'

from nltk import everygrams

msg_split = strings.split()

split_cleaned_lst = []
for value in msg_split:
    split = re.sub('[^a-zA-Z]', '', value)
    split_cleaned = split.lower()
    split_cleaned_lst.append(split_cleaned)
    print(split_cleaned)

list(everygrams(split_cleaned_lst))

# for string in strings:
#     splitted_str = string.split()
#     splitted_strings.append(splitted_str)
#     print(splitted_str)

# dat = 'Walking; Jogging; Bicycling; Lap. Swimming; Aerobic Exercise; Yoga; Lawn Mowing'
# splitted_strings  = dat.split()

# lst = []
# for value in splitted_strings:
#     #print(value)
#     cleaned_value = re.sub('[^a-zA-Z]', '', value)
#     cleaned_value = cleaned_value.lower()
#     #print(cleaned_value)
#     key_reqd = get_value_from_key(physical_activity_dict, cleaned_value)
#     print(key_reqd)
#     if key_reqd is not None:
#         key_reqd_str = ''.join(key_reqd)
#         #print(key_reqd_str)
#         lst.append(key_reqd_str)
#         while ('' in lst):
#             lst.remove('')
#             print(lst)
#     else:
#         lst.append(key_reqd)
#
# while ('' in lst):
#     lst.remove('')
#     print(cleaned_lst)
#         print(key_reqd_str)

# word = 'walk; jogging; running;bicycling; tennis'
# patterns = ['walk', 'walking', 'jogging', 'running', 'bicycling', 'tennis']
#
# for item in patterns:
#     if item in word:
#         print(item)
#
# match = (set(word)).intersection(set(patterns))
#
# from difflib import get_close_matches, SequenceMatcher
#
#
# get_close_matches(word, patterns)
# seqmat = SequenceMatcher(word, patterns)

# splitted_str = replace_and_split_string(changed_phy_act)


# changed_phy_act = []
# for val in vals_dict.values():
#     print(val)
#     if val is not None:
#         id_pos = [val in value for value in (physical_activity_dict.values())]
#         print(id_pos)
#         phys_act_vocat = list(itertools.compress(physical_activity_dict.keys(), id_pos))
#         print(phys_act_vocat)
#         if len(phys_act_vocat) != 0:
#             changed_phy_act.append(phys_act_vocat)
#         else:
#             changed_phy_act.append(val)


# id_pos = ['walk' in value for value in (physical_activity_dict.values())]
# phys_act_vocat = list(itertools.compress(physical_activity_dict.keys(), id_pos))



# for val in physical_activity_dict.values():
#     # print(val)
#         for sub_val in val:
#             # print(sub_val)
#             id_pos = [sub_val in value for value in (physical_activity_dict.values())]
#             print(id_pos)
#             phys_act_vocat = list(itertools.compress(physical_activity_dict.keys(), id_pos))
#             print(phys_act_vocat)

# for val in physical_activity_dict.values():
#     print(val)
#         for sub_val in val:
#             print(sub_val)
#             id_pos = [sub_val in value for value in (vals_dict.values())]
#             print(id_pos)
#             phys_act_vocat = list(itertools.compress(physical_activity_dict.keys(), id_pos))
#             print(phys_act_vocat)


# def repalce_values_by_dict_keys(physical_activity_dict, dict_values):
#     changed_phy_act = []
#     for val in dict_values.values():
#         # print(val)
#         if val is not None:
#             # print(val)
#             vocab_type = get_value_from_key(physical_activity_dict, val)
#             # print(vocab_type)
#             if len(vocab_type) != 0:
#                 changed_phy_act.append(vocab_type)
#             else:
#                 # TODO assign to existing key or create new key and change dict
#                 changed_phy_act.append(val)
#         else:
#             changed_phy_act.append('data_not_available')
#     return changed_phy_act