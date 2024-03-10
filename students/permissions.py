from rest_framework import permissions


class IsAdmin:
    user = None

    def __init__(self, user):
        user = user
        self.user = user

    def is_user_admin(self):
        return self.user.is_superuser
