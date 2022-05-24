from Server.Pages.loginPage import Login
from Server.Pages.registerPage import Register
from Server.Pages.search import Search

login = Login()
login.test_login_with_incorrectly_email()
login.test_login_with_incorrectly_password()
login.test_login_with_incorrectly_email_and_password()
login.test_login_correctly()

search = Search()
search.test_search_correctly('Jerusalem')
search.test_search_incorrectly_with_invalid_value('1515')
search.test_search_incorrectly_when_city_not_exist('Tel Aviv')

register = Register()
register.user_register_correctly()
