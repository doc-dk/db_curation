import pandas as pd
import re
from fuzzywuzzy import process, fuzz
import numpy as np
import dateparser

mr_data = pd.read_excel('D:\\Shweta\\patient_lists\\Patient_Data.xlsx')
pccm_db_data = pd.read_excel('D:\\Shweta\\patient_lists\\patient_list_pccm_db.xlsx')
ffpe_data = pd.read_excel('D:\\Shweta\\Blocks_updated_data\\2021_06_01_FFPE database_Block Sr. no. 673 to 1050_Danish.xlsx')

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


###

def add_mr_no_ffpe_data(source_file, test_file, source_name_str = 'Patient Name', test_name_str = 'Patient Name',
                        source_mr_no_str = 'MR No'):
    source_cleaned_names = clean_names(source_file, source_name_str)
    test_cleaned_names = clean_names(test_file, test_name_str)
    new_mr_num = []
    for test_index, test_cleaned_name in enumerate(test_cleaned_names):
        matched_name = process.extractOne(query=test_cleaned_name, choices=source_cleaned_names,
                                          scorer=fuzz.token_sort_ratio, score_cutoff=100)
        if matched_name is not None:
            source_index = source_cleaned_names.index(matched_name[0])
            mr_no = source_file.iloc[source_index][[source_mr_no_str]]
            print(mr_no)
            new_mr_num.append(mr_no[0])
        else:
            new_mr_num.append('data_to_be_entered')
    test_file.insert(8, 'new_mr_number', new_mr_num)
    return test_file


test_file = add_mr_no_ffpe_data(mr_data, ffpe_data, source_name_str = 'Patient Name', test_name_str = 'Patient Name',
                        source_mr_no_str = 'MR No')

##
def matched_names_ffpe_patient_list(ffpe_data, patient_data, ffpe_name_str = 'Patient Name', ffpe_mr_no_str = 'Mr_number', ffpe_file_num_str = 'File_Number',
                  patient_dat_name_str = 'name', patient_dat_file_num_str = 'file_number'):
    ffpe_cleaned_names = clean_names(ffpe_data, ffpe_name_str)
    patient_dat_cleaned_names = clean_names(patient_data, patient_dat_name_str)
    ffpe_data['ffpe_'+ffpe_name_str] = ffpe_cleaned_names
    patient_data['patient_'+patient_dat_name_str] = patient_dat_cleaned_names
    matched_list = []
    for test_index, test_cleaned_name in enumerate(ffpe_cleaned_names):
            matched_name = process.extractOne(query = test_cleaned_name, choices = patient_dat_cleaned_names,
                                           scorer = fuzz.token_sort_ratio)
            print(test_cleaned_name, matched_name)
            if matched_name is not None:
                patient_dat_index = patient_dat_cleaned_names.index(matched_name[0])
                patient_dat_cols = ['patient_'+patient_dat_name_str, patient_dat_file_num_str]
                patient_dat = patient_data.iloc[patient_dat_index][patient_dat_cols]
                ffpe_cols = [ffpe_mr_no_str, ffpe_file_num_str, 'ffpe_'+ffpe_name_str]
                ffpe_dat = ffpe_data.iloc[test_index][ffpe_cols]
                score = matched_name[1]
                output_list = np.append(patient_dat, ffpe_dat)
                final_output_list = np.append(output_list, score)
                matched_list.append(final_output_list)
                col_list = ['patient_dat_patient_name', 'patient_dat_file_number', 'ffpe_mr_no', 'ffpe_file_number',
                                'ffpe_patient_name', 'patient_lst_ffpe_matched_score']
                matched_df = pd.DataFrame(matched_list, columns = col_list)
    return matched_df

matched_df_ffpe_patient_list = matched_names_ffpe_patient_list(ffpe_data, pccm_db_data, ffpe_name_str = 'Patient Name', ffpe_mr_no_str = 'Mr_number', ffpe_file_num_str = 'File_Number',
                  patient_dat_name_str = 'name', patient_dat_file_num_str = 'file_number')

matched_df_ffpe_patient_list.to_excel('D:\\Shweta\\patient_lists\\output_files\\2021_21_06_matched_df_ffpe_patient_list.xlsx', index=False)
##

def extract_mr_number_for_matched_df(matched_df_ffpe_patient_list):
    matched_lst = []
    for i in range(len(matched_df_ffpe_patient_list)):
        if matched_df_ffpe_patient_list.patient_dat_file_number[i] == matched_df_ffpe_patient_list.ffpe_file_number[i]:
            patient_name = matched_df_ffpe_patient_list.patient_dat_patient_name[i]
            mr_number = matched_df_ffpe_patient_list.ffpe_mr_no[i]
            dat = np.append(patient_name, mr_number)
            matched_lst.append(dat)
            matched_df = pd.DataFrame(matched_lst, columns=['patient_name', 'mr_number'])
    return matched_df

matched_name_file_num = extract_mr_number_for_matched_df(matched_df_ffpe_patient_list)





def add_mr_number(ffpe_data, patient_data, mr_name_str = 'Patient Name', ffpe_name_str = 'Patient Name',  ffpe_mr_no_str = 'Mr_number',
                  ffpe_file_num_str = 'File_Number', patient_dat_name_str = 'name', patient_dat_file_num_str = 'file_number'):
    mr_dat_cleaned_names = clean_names(mr_data, mr_name_str)
    ffpe_cleaned_names = clean_names(ffpe_data, ffpe_name_str)
    patient_dat_cleaned_names = clean_names(patient_data, patient_dat_name_str)
    mr_data['mr_'+mr_name_str] = mr_dat_cleaned_names
    ffpe_data['ffpe_'+ffpe_name_str] = ffpe_cleaned_names
    patient_data['patient_'+patient_dat_name_str] = patient_dat_cleaned_names
    matched_list = []
    for test_index, test_cleaned_name in enumerate(ffpe_cleaned_names):
            matched_name = process.extractOne(query = test_cleaned_name, choices = patient_dat_cleaned_names,
                                           scorer = fuzz.token_sort_ratio)
            print(test_cleaned_name, matched_name)
            if matched_name is not None:
                patient_dat_index = patient_dat_cleaned_names.index(matched_name[0])
                patient_dat_cols = ['patient_'+patient_dat_name_str, patient_dat_file_num_str]
                patient_dat = patient_data.iloc[patient_dat_index][patient_dat_cols]
                patient_dat_file_num = patient_dat[patient_dat_file_num_str]
                ffpe_cols = [ffpe_mr_no_str, ffpe_file_num_str, 'ffpe_'+ffpe_name_str]
                ffpe_dat = ffpe_data.iloc[test_index][ffpe_cols]
                ffpe_file_num = ffpe_dat[ffpe_file_num_str]
                score = matched_name[1]
                if patient_dat_file_num == ffpe_file_num:
                    output_list = np.append(patient_dat, ffpe_dat)
                    final_output_list = np.append(output_list, score)
                    matched_list.append(final_output_list)
                    col_list = ['patient_dat_patient_name', 'patient_dat_file_number', 'ffpe_mr_no', 'ffpe_file_number',
                                'ffpe_patient_name', 'matched_score']
                    matched_df = pd.DataFrame(matched_list, columns = col_list)
    return matched_df


matched_df = add_mr_number(ffpe_data, pccm_db_data, ffpe_name_str = 'Patient Name', ffpe_mr_no_str = 'Mr_number',
                           ffpe_file_num_str = 'File_Number', patient_dat_name_str = 'name', patient_dat_file_num_str = 'file_number')


def add_mr_number_matched_df(source_data, test_data, source_name_str = 'Patient Name', test_name_str = 'patient_dat_patient_name',
                             source_mr_no_str = 'MR No', test_patient_dat_file_num_str = 'ffpe_file_number',
                             test_mr_no_str = 'ffpe_mr_no', test_file_num_str = 'patient_dat_file_number'):
    source_cleaned_names = clean_names(source_data, source_name_str)
    test_cleaned_names = clean_names(test_data, test_name_str)
    source_data['source_'+source_name_str] = source_cleaned_names
    test_data['test_'+test_name_str] = test_cleaned_names
    matched_list = []
    for test_index, test_cleaned_name in enumerate(test_cleaned_names):
            matched_name = process.extractOne(query = test_cleaned_name, choices = source_cleaned_names,
                                           scorer = fuzz.token_sort_ratio)
            print(test_cleaned_name, matched_name)
            if matched_name is not None:
                source_index = source_cleaned_names.index(matched_name[0])
                source_cols = [source_mr_no_str, 'source_'+source_name_str]
                source_dat = source_data.iloc[source_index][source_cols]
                test_cols = [test_mr_no_str, test_file_num_str, 'test_'+test_name_str, test_patient_dat_file_num_str]
                test_dat = test_data.iloc[test_index][test_cols]
                score = matched_name[1]
                output_list = np.append(source_dat, test_dat)
                final_output_list = np.append(output_list, score)
                matched_list.append(final_output_list)
                col_list = ['source_mr_number', 'source_patient_name', 'test_mr_no', 'file_number',
                            'test_patient_name', 'ffpe_file_number', 'matched_score']
                matched_df = pd.DataFrame(matched_list, columns = col_list)
    return matched_df


matched_df_final = add_mr_number_matched_df(mr_data, matched_df, source_name_str = 'Patient Name', test_name_str = 'patient_dat_patient_name',
                             source_mr_no_str = 'MR No', test_patient_dat_file_num_str = 'ffpe_file_number',
                             test_mr_no_str = 'ffpe_mr_no', test_file_num_str = 'patient_dat_file_number')

matched_df_final['mr_no_comparison'] = np.where(matched_df_final.source_mr_number == matched_df_final.test_mr_no, True, False)
matched_df_final.to_excel('D:\\Shweta\\patient_lists\\output_files\\2021_06_21_matched_name_file_num_mr_no_sk.xlsx', index=False)