from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# creation of an engine
engine = create_engine("postgresql://postgres:123@localhost:5432/flight")
# creation of a session
db = scoped_session(sessionmaker(bind=engine))
# creation of the table flights with all the attributes
db.execute("CREATE TABLE test (id INTEGER NOT NULL, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL, PRIMARY KEY (id));")
# insertion of values into the table flights 
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);")
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);")
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);")
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);")
# commit the changes 
db.commit()
# close the session
db.close()