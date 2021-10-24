class User:
    """
    User class
    Args:
    login_name: To sign into the application.(str)
    pin : To sign into the application.(str)
    """
    user_list = []

    def __init__(self, login_name, pin):
        self.login_name = login_name
        self.pin = pin

    def save_user(self):
        """
        this method appends new object to user_list
        """
        User.user_list.append(self)

   