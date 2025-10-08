def get_creds():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open("config.ini", "w") as f:
            f.write(f"[General]\n")
            f.write(f"login={login}\n")
            f.write(f"password={password}\n")


if __name__ == "__main__":
    get_creds()
