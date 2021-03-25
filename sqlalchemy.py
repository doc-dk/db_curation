import sqlalchemy
sqlalchemy.__version__
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float

# folder = 'D:/Shweta/pccm_db'
# file = 'PCCM_BreastCancerDB_2021_02_22.db'
# path_db = os.path.join(folder, file)

engine = create_engine('sqlite:///D://Shweta//pccm_db//PCCM_BreastCancerDB_2021_02_22.db')
meta = MetaData()

phy_act = Table(
    'physical_activities', meta,
    Column('pk' , String, primary_key = True),
    Column('file_number', String),
    Column('phy_acy_y_n', Boolean),
    Column('phy_act_type', String),
    Column('phy_act_freq_in_hrs', Float)
)

# meta.create_all(engine)
# conn = engine.connect()
#
# sql_stat = text("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
# tabs = conn.execute(sql_stat)
#
# tables = pd.read_sql(sql_stat, conn)