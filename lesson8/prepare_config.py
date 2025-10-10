def get_creds():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open("config.ini", "w") as f:
        f.write("[General]\n")
        f.write("login={login}\n")
        f.write("password={password}\n")


if __name__ == "__main__":
    get_creds()
