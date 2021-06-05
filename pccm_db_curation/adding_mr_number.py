import pandas as pd
import re
from fuzzywuzzy import process, fuzz
import numpy as np
import dateparser

mr_data = pd.read_excel('D:\\Shweta\\patient_lists\\Patient_Data.xlsx')
pccm_db_data = pd.read_excel('D:\\Shweta\\patient_lists\\patient_list_pccm_db.xlsx')

def clean_names(df, name_str):
    cleaned_names = []
    for name in df[name_str]:
        name = re.sub('[^a-zA-Z]', ' ', str(name))
        name = name.lower()
        cleaned_names.append(name)
    return cleaned_names

def convert_all_dates_into_one_format(dates):
    dts = []
    for date in dates:
        dt_find = dateparser.parse(str(date))
        match = re.search('\d{4}-\d{2}-\d{2}', str(dt_find))
        if match is not None:
            dts.append(match[0])
        else:
            dts.append(date)
    return dts

dts = convert_all_dates_into_one_format(mr_data['Date'])
dts_tes = convert_all_dates_into_one_format(pccm_db_data['firstvisit_date'])

def add_mr_number(source_data, test_data, source_name_str = 'Patient Name', test_name_str = 'name', source_mr_no_str =
                  'MR No', test_file_num_str = 'file_number', source_dt_str = 'Date', test_dt_str = 'firstvisit_date'):
    source_cleaned_names = clean_names(source_data, source_name_str)
    test_cleaned_names = clean_names(test_data, test_name_str)
    source_data['source_'+source_name_str] = source_cleaned_names
    test_data['test_'+test_name_str] = test_cleaned_names
    source_dates = convert_all_dates_into_one_format(source_data[source_dt_str])
    test_dates = convert_all_dates_into_one_format(test_data[test_dt_str])
    source_data['source_'+source_dt_str] = source_dates
    test_data['test_'+test_dt_str] = test_dates
    matched_list = []
    for test_index, test_cleaned_name in enumerate(test_cleaned_names):
            matched_name = process.extractOne(query = test_cleaned_name, choices = source_cleaned_names,
                                           scorer = fuzz.token_sort_ratio)
            print(test_cleaned_name, matched_name)
            if matched_name is not None:
                source_index = source_cleaned_names.index(matched_name[0])
                source_cols = [source_mr_no_str, 'source_'+source_name_str, 'source_'+source_dt_str]
                source_dat = source_data.iloc[source_index][source_cols]
                test_cols = [test_file_num_str, 'test_'+test_name_str, 'test_'+test_dt_str]
                test_dat = test_data.iloc[test_index][test_cols]
                score = matched_name[1]
                output_list = np.append(source_dat, test_dat)
                final_output_list = np.append(output_list, score)
                matched_list.append(final_output_list)
                col_list = ['mr_number', 'source_patient_name', 'source_date', 'file_number', 'test_patient_name',
                            'test_date', 'matched_score']
                matched_df = pd.DataFrame(matched_list, columns = col_list)
    return matched_df

matched_df = add_mr_number(mr_data, pccm_db_data, source_name_str = 'Patient Name', test_name_str = 'name',
                    source_mr_no_str = 'MR No', test_file_num_str = 'file_number', source_dt_str = 'Date',
                    test_dt_str = 'firstvisit_date')


matched_df.to_excel('D:\\Shweta\\patient_lists\\2021_06_05_matched_names_mr_num_sk.xlsx', index = False)






