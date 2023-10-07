from ..model.s import Match, League, Session

# Create an SQLAlchemy engine to connect to your database
#engine = create_engine('sqlite:///shiba.db')  # Replace with your database URL

# Create a session
#Session = sessionmaker(bind=engine)
session = Session()

results = session.query(League).all()
