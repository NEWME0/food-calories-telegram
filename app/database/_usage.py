from sqlalchemy.orm import Session

from app.database.session import Session
from app.database.models import User


session: Session = Session()

# Add into database
user_1 = User(
    telegram=12546,
    username='telegram_12546',
    api_key='asdkfaskdmfpiopdoakmfasdkmflaskmdpvofhpvufbgb-g8sd9jfgbaofijba89fhba',
)


user_2 = User(
    telegram=95467,
    username='telegram_95467',
    api_key=';aslkdf;lasndf9sd9fnsdf-g8sd9jfgbaofijba89fhba',
)


user_3 = User(
    telegram=12345,
    username='telegram_12345',
    api_key='89hasdfnasldkjnflkasjdnfog-g8sd9jfgbaofijba89fhba',
)


session.add(user_1)
session.add(user_2)
session.add(user_3)

session.commit()


# Find in database
user_12546 = session.query(User).filter_by(telegram=12546).first()
print(user_12546.username)

user_95467 = session.query(User).filter_by(telegram=95467).first()
print(user_95467.username)

user_12345 = session.query(User).filter_by(telegram=12345).first()
print(user_12345.username)
