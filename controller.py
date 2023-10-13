from model import Person
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib


def return_session():
    CONN = "sqlite:///login_project.db"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class ControllerRegister():
    @classmethod
    def verify_data(cls, name, email, password):
        if len(name) > 50 or len(name) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(password) > 100 or len(password) < 6:
            return 4

        return 1

    @classmethod
    def register(cls, name, email, password):
        session = return_session()
        client = session.query(Person).filter(Person.email == email).all()

        if len(client) > 0:
            return 5
        verified_data = cls.verify_data(name, email, password)

        if verified_data != 1:
            return verified_data

        try:
            password = hashlib.sha256(password.encode()).hexdigest()
            p1 = Person(name=name, email=email, password=password)
            session.add(p1)
            session.commit()
            return 1

        except:
            return 3


print(ControllerRegister.register('Sergio', 'scarlosjazz2@gmail.com', 'sergio123456'))
