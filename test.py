from bs4 import BeautifulSoup

from app.database import create_session
from app.models import Dictionary

session = create_session()

words = Dictionary.get_random_words(session)
for word in words:
    soup = BeautifulSoup(word.detail, "html.parser")
    print(soup.get_text("\n"))
