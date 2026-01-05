import datetime
import jwt
import database
import bcrypt
from config import SECRET

db = database.Database()

class Authentication:

    #Init Database
    try:
        db.createUsersDb()
    except Exception as e:
        print("An error occurred during Users table creation:", e)

    def register(self, name:str, email:str, password:str):

        created_at = datetime.datetime.now()
        try:
            bytes = password.encode("utf-8")
            
            salt = bcrypt.gensalt()

            hash = bcrypt.hashpw(bytes, salt)
        except Exception as e:
            print("An error occurred during password hashing:", e)
            return "Error during registration"

        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO Users (name, email, password_hash, created_at) VALUES(%s, %s, %s, %s)", 
                                (name, email, hash, created_at))
                    
            return "User registered successfully"
        except Exception as e:
            print("An error occurred during user registration:", e)
            return "Error during registration"

    def login(self, email:str, userPassword:str):
        try:
            with db.get_connection() as conn:
                with conn.cursor() as cur:
                        try:
                            cur.execute("SELECT password_hash, id, name, email FROM Users WHERE email = %s", (email,))
                            result = cur.fetchone()
                        except Exception as e:
                            print("An error occurred while fetching user data:", e)
                            return False
        except Exception as e:
            print("An error occurred during login:", e)
            return False
        

        if result is None:
            print("Login failed: User not found")
            return False
        
        try:
            password_hash = result[0]
            id_user = result[1]
            name_user = result[2]
            email_user = result[3]
        except Exception as e:
            print("An error occurred while extracting user data:", e)
            return False

        
        stored_hash = password_hash

        userBytes = userPassword.encode("utf-8")

        try:
            result_hash = bcrypt.checkpw(userBytes,stored_hash)

        except Exception as e:
            print("An error occurred during password verification:", e)
            return False


        if(result_hash):
            print("Login successful")

            header = {"alg": "HS256", "typ": "JWT"}
            payload = {
                "id": id_user,
                "name": name_user,
                "email": email_user
            }
            try:
                token = jwt.encode(payload, SECRET, algorithm="HS256", headers=header)
            except Exception as e:
                print("An error occurred during token generation:", e)
                return False

            return token
            
        else:
            print("Login failed: Incorrect password")
            return False   
        
        
        