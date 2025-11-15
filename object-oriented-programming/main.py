from user import User
from admin import Admin

user = User("Ahad","Umayyad")
user2 = User("Siya", "Lily")
user3 = User("Xi", "wei")
admin = Admin("Super", "Admin")

user.greet_user()
user2.greet_user()
user3.greet_user()

user.describe_user()
user2.describe_user()
user3.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

user.increment_login_attempts()

admin.privileges.show_privileges()
admin.describe_user()
