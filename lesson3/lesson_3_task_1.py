from user import User


my_user = User("Ramziya", "Giniyatullina")

# Ожидаемый результат: "Ramziya"
my_user.print_first_name()

# Ожидаемый результат: "Giniyatullina"
my_user.print_last_name()

# Ожидаемый результат: "First Name: Ramziya, Last Name: Giniyatullina"
my_user.print_full_name()
