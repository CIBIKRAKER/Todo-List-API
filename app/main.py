import bcrypt
import todo
import auth



def main():
    authentication = auth.Authentication()


    loginResult = authentication.login("murhi@gmail.com", "571632gemi")

    print("Login successful:", loginResult)

if __name__ == "__main__":
    main()
