import pandas as pd
import numpy as np
import os

df = pd.read_excel('D:\\Shweta\\799_cases\\2021_02_09_799_cases_Orchids2010_2018_rb_dk.xlsx')

null_values = df.isnull().sum()
null_values = null_values.reset_index()

# null_values.to_excel('D:\\Shweta\\799_cases\\2021_03_27_null_values_count_of_idc_data_sk.xlsx')
des = df.describe()

counts = df['menopause_clean'].value_counts()

def get_value_count_for_each_column(folder, file):
    df_path = os.path.join(folder, file)
    df = pd.read_excel(df_path)
    df2 = df.select_dtypes(include=['object'])
    df_cols = df2.columns
    # print(df_cols)
    col_list = ['file_number', 'patient_name', 'biopsy_date', 'biopsy_date_clean',
                'surgery_date', 'recurrence_date']
    writer = pd.ExcelWriter('D:/Shweta/799_cases/2021_03_30_value_counts.xlsx',
                            engine='xlsxwriter')

    unique_value_count_list = []
    for col in df_cols:
        if col in col_list:
            continue
        col_value_counts = df[col].value_counts()
        col_value_counts = col_value_counts.reset_index()
        print(col_value_counts)
        if len(col) >= 31:
            col = col[0:31]
        else:
            col = col
        col_value_counts.to_excel(writer, sheet_name=col, index=False)
        unique_value_count_list.append(col_value_counts)
    writer.save()
    output_df = pd.DataFrame(unique_value_count_list, columns=df_cols)
    return unique_value_count_list, output_df

unique_value_count_list, output_df = get_value_count_for_each_column(folder='D:\\Shweta\\799_cases', file='2021_02_09_799_cases_Orchids2010_2018_rb_dk.xlsx')
lst_df = pd.DataFrame(unique_value_count_list)
unique_value_count_list.to_excel('D:\\Shweta\\799_cases\\2021_03_27_null_values_count_sk.xlsx')

model = LinearRegression()


def get_unique_values(folder, file):
    df_path = os.path.join(folder, file)
    df = pd.read_excel(df_path)
    df_cols = df.columns
    unique_value_list = []
    for col in df_cols:
        col_dat = df[col]
        unique_values = col_dat.unique()
        unique_values_output = np.append(col, unique_values)
        unique_value_list.append(unique_values_output)
    output_df = pd.DataFrame(unique_value_list)
    return output_df, unique_value_list

unique_df, unique_value_list = get_unique_values(folder='D:\\Shweta\\799_cases', file='2021_02_09_799_cases_Orchids2010_2018_rb_dk.xlsx')