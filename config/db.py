from sqlalchemy import create_engine, MetaData

url = "mysql+mysqldb://scicognos_test:sciCognos$#785@scicognos_test.mysql.dbaas.com.br/scicognos_test"

engine = create_engine(url, echo=True) 
meta = MetaData()
connection = engine.connect()