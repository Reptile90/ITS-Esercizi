from user import User, Privileges, Admin  # Import the necessary classes

# Create a User instance
user_info = User('marco', 'cascio', 'mcascio', 'mcascio@example.com')

# Define a set of privileges
admin_privileges = Privileges(['can add post', 'can delete post', 'can ban user'])

# Create an Admin instance with the user and privileges
admin_user = Admin(user_info, admin_privileges)

# Demonstrate the methods
admin_user.describe_user()
admin_user.show_privileges()