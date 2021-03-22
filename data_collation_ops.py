import pandas as pd
import os

folder = 'D:\\Shweta\\pccm_db\\pccm_excel'
db1_name = 'db_1_2021-03-15.xlsx'
db2_name = 'db_2_2021-03-15.xlsx'

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