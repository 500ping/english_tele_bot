import json
from sqlalchemy.orm import sessionmaker

from app.database import engine
from app.models import Dictionary

Session = sessionmaker(bind=engine)
session = Session()

# Delete all old record
try:
    session.query(Dictionary).delete()
    session.commit()
except:
    session.rollback()


data = {}
with open("3000_words.json") as file:
    data = json.load(file)

dictionaries = []
for k, v in data.items():
    dictionaries.append(
        Dictionary(
            word=k,
            detail=v[1],
            pronounce=v[0],
        )
    )
session.bulk_save_objects(dictionaries)
session.commit()
session.close()
