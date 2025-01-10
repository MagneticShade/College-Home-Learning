from sqlmodel import create_engine

link = "mysql+mysqlconnector://root:root@db/base"
engine = create_engine(link, echo=True)
