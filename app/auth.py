import datetime
import database
import bcrypt

db = database.Database()

class Authentication:

    #Init Database
    db.createUsersDb()

    def register(self, name:str, email:str, password:str):

        created_at = datetime.datetime.now()

        bytes = password.encode("utf-8")
        
        salt = bcrypt.gensalt()

        hash = bcrypt.hashpw(bytes, salt)

        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO Users (name, email, password_hash, created_at) VALUES(%s, %s, %s, %s)", 
                            (name, email, hash, created_at))
                
        return "User registered successfully"

    def login(self, email:str, userPassword:str):
        with db.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT password_hash FROM Users WHERE email = %s", (email,))
                result = cur.fetchone()
        
        stored_hash = bytes(result[0])

        userBytes = userPassword.encode("utf-8")

        result_hash = bcrypt.checkpw(userBytes,stored_hash)

        print(f"{stored_hash}\n")
        print(result_hash)

        if(result_hash):
            return True
        else:
            return False