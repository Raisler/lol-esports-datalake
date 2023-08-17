Just to remember how to use SQLALchemy


```python: 
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Replace 'your_database_name.db' with the desired database name
db_url = 'sqlite:///your_database_name.db'
engine = create_engine(db_url, echo=True)  # Set echo=True for debugging

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"
    
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

session.close()

```