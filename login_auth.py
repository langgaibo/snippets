# coding: utf8
# 朗盖博 2015

# Expects 4 params: raw user login and password,
# raw DB login, and hashed DB password.
class Validate_Creds(object):
    def __init__(self, DBlogin, DBpw, login, pw):
        import hashlib
        self.DBlogin = DBlogin
        self.DBpw = DBpw
        self.login = login
        # hashes the user's PW for comparison to hashed DB PW
        self.pw = hashlib.sha256(pw).hexdigest()

    def compare_creds(self):
        # check all the possibilities and return an error code
        if self.login == self.DBlogin:
            if self.pw == self.DBpw:
                # success
                return 0
            else:
                # wrong password
                return 2
        else:
            # username does not exist
            return 1
