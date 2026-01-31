import models
import database
from models import ModelActions, metadata

def main():
    engine = database.DatabaseURL().get_connection() 

    metadata.create_all(engine)

    db = ModelActions(engine)
    db.insert_user("Dayi", "dayi@gmail.com", "aponunanasinisikeyim3169")


if __name__ == "__main__":
    main()