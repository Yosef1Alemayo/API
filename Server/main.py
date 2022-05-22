from Server.Pages.LoginPage import Login
from Server.Pages.RegisterPage import Register
from Server.Pages.Search import Search


register = Register()
register.test_register_correctly()
register.test_register_with_incorrectly_name()


login = Login()
login.test_login_with_incorrectly_email()
login.test_login_with_incorrectly_password()
login.test_login_with_incorrectly_email_and_password()
login.test_login_correctly()


search = Search()
search.test_search_correctly('Paris')
search.test_search_incorrectly('1551')

