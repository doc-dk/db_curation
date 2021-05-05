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
        print(val)
        if val is not None:
            print(val)
            vocab_type = get_value_from_key(physical_activity_dict, val)
            print(vocab_type)
            if len(vocab_type) != 0:
                changed_phy_act.append(vocab_type)
            else:
                split_val = val.split()
                lst = []
                for value in split_val:
                    cleaned_value = re.sub('[^a-zA-Z]', '', value)
                    cleaned_value = cleaned_value.lower()
                    key_reqd = get_value_from_key(physical_activity_dict, cleaned_value)
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
                changed_phy_act.append(lst)
        else:
            changed_phy_act.append('data_not_available')
    return changed_phy_act, lst

changed_phy_acts_lst, lst = repalce_values_by_dict_keys(physical_activity_dict, vals_dict)

changed_phy_acts_sr = pd.Series(changed_phy_acts_lst)
phy_act_df = pd.concat([patient_info['type_physical_activity'], changed_phy_acts_sr], axis=1)

## diet

diet_dict = {'vegetarian': 'vegetarian',
             'vegan': 'vegan',
             'non_vegetarian': ['non-vegetarian', 'non vegetarian', 'non_vegetarian'],
             'ovo_vegetarian': ['ovo-vegetarian', 'ovo vegetarian', 'ovo_vegetarian'],
             'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
             'data_not_available': ['data not available', 'data_not_available', 'data not in report']
             }

patient_diet = patient_info['diet'].str.lower()
patient_diet_dict = patient_diet.to_dict()

changed_diet, lst = repalce_values_by_dict_keys(diet_dict, patient_diet_dict)

changed_diet_sr = pd.Series(changed_diet)
df = pd.concat([patient_info['diet'], changed_diet_sr], axis=1)
df.to_excel('D:\\Shweta\\pccm_db\\diet_table\\diet_tab_comparison.xlsx')

menopause_status_dict = {'pre_menopausal': ['pre-menopausal', 'premenopausal'],
                         'post_menopausal': ['post-menopausal', 'post-menopause', 'post menopausal'],
                         'peri_menopausal': 'peri-menopausal',
                         'hysterectomy': ['hysterectomy', 'hysterctomy', 'post hysterectomy', 'hysterectome',
                                         'post -menopausal(hysterectomy done in 2012)'],
                        'oopherectomy': ['oophorectomy', 'bilateral oopherectomy'],
                        'other': 'male',
                        'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                        'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                         }

patient_menopause_status = patient_info['menopause_status'].str.lower()
patient_menopause_status_dict = patient_menopause_status.to_dict()

changed_menopause_status, lst = repalce_values_by_dict_keys(menopause_status_dict, patient_menopause_status_dict)

changed_menopause_status_sr = pd.Series(changed_menopause_status)
df = pd.concat([patient_info['menopause_status'], changed_menopause_status_sr], axis=1)
df.to_excel('D:\\Shweta\\pccm_db\\diet_table\\menopause_status_comparison.xlsx')

## age_at_menopause_yrs

age_at_menopause_yrs_dict = {'NA': ['pre-menopausal', 'peri-menopausal', 'hysterectomy', 'bilateral oopherectomy',
                                    'male', 'hysterectome', '54 (Hysterectomy done)', '44 (Hysterectomy done in 2012)'],
                            'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                            'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                            }

def repalce_values_by_dict_keys_for_numeric_type(variable_defined_dict, dict_values):
    changed_phy_act = []
    for val in dict_values.values():
        print(val)
        if val is not None:
            if val.isdigit():
                changed_phy_act.append(val)
            else:
                vocab_type = get_value_from_key(variable_defined_dict, val)
                print(vocab_type)
                if len(vocab_type) != 0:
                    changed_phy_act.append(vocab_type)
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
                    changed_phy_act.append(lst)
    return changed_phy_act, lst


patient_age_at_menopause_yrs = patient_info['age_at_menopause_yrs'].str.lower()
patient_age_at_menopause_yrs_dict = patient_age_at_menopause_yrs.to_dict()

changed_age_at_menopause_yrs, lst = repalce_values_by_dict_keys_for_numeric_type(age_at_menopause_yrs_dict, patient_age_at_menopause_yrs_dict)

changed_age_at_menopause_yrs_sr = pd.Series(changed_age_at_menopause_yrs)
df = pd.concat([patient_info['age_at_menopause_yrs'], changed_age_at_menopause_yrs_sr], axis=1)
df.to_excel('D:\\Shweta\\pccm_db\\diet_table\\age_at_menopause_yrs_comparison.xlsx')

## current_breast_cancer_detected_by

current_breast_cancer_detected_by_dict = {'self': 'self',
                                          'physician': 'physician',
                                          'routine_checkup': 'Annual body check up',
                                          'screening_camp': ['Screening Camp ID NA', 'Screening Camp ID 1',
                                                             'Screening Camp ID Data not in Report',
                                                             'Screening Camp ID Requires Follow-up'],
                                          'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                                 'requires follow up'],
                                          'data_not_available': ['data not available', 'data_not_available',
                                                                 'data not in report']
                                          }
## rb_symptoms

rb_lb_symptoms_dict = {'lumps':['lumps','lump'],
                    'nipple_retraction':'nipple retraction',
                    'nipple_discharge': 'nipple discharge',
                    'pain_or_tenderness': 'pain or tenderness',
                    'dimpling':'dimpling',
                    'discolouration':['discolouration','redness'],
                    'ulceration':'ulceration',
                     'eczema':'eczema',
                    'requires_follow_up': ['requires_follow_up', 'requires follow-up', 'requires follow up'],
                    'data_not_available': ['data not available', 'data_not_available', 'data not in report']
                    }

## patient_metastasis_symptoms

patient_metastasis_symptoms_dict = {'weight_loss': 'weight loss',
                                    'cough': 'cough',
                                    'bone_pain': 'bone pain',
                                    'headache':'headache',
                                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                           'requires follow up'],
                                    'data_not_available': ['data not available', 'data_not_available',
                                                           'data not in report']
                                    }
