class UserNotFoundException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, username: str):
        self.message = "User "+username + " not found"
        super().__init__(self.message)
