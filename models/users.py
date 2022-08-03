from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta 

users = Table(
    'user_test', meta,
    Column('user_id',Integer, primary_key=True),
    Column('user_name',String(100)),
    Column('user_email',String(100)),
    Column('user_cpf',String(100)),
    Column('user_password',String(100)),
    Column('user_password_confirm',String(100)),
    Column('user_birth_date',Date),
    Column('user_sex',String(1)),
    Column('user_fone',String(45)),
    Column('user_fone_whatsapp',String(45)),
    Column('user_receive_offers',String(1)),
    Column('user_receive_offers_whatsapp',String(1)),
    Column('user_status',String(1)),
)