import json
from sqlalchemy.orm import sessionmaker

from app.database import engine
from app.models import Dictionary

Session = sessionmaker(bind=engine)
session = Session()


data = {}
with open("dictionary.json") as file:
    data = json.load(file)

dictionaries = []
for k, v in data.items():
    dictionaries.append(
        Dictionary(
            word=k,
            detail=v,
        )
    )
session.bulk_save_objects(dictionaries)
session.commit()
session.close()
