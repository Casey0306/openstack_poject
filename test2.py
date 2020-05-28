import functools

class Test:

    token = ""

    def __init__(self):
        self.token = ""

    def auth(self, username):
        if username == "Kirill":
            self.token = "123456"
            return self.token
        else:
            return print("No auth")

    def getvms(self, token = self.token, vms):
        return print(vms)

    def authdec(self, func):
        def inner(token, *args, **kwargs):
            if token:
                func(*args, **kwargs)
            else:
                print("Нет авторизации")
        return inner



test = Test()
test.getvms("vms1")
