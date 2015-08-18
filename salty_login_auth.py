# coding: utf8
# 朗盖博 2015

# A simple login auth Class that handles a salt (but not battery).

class Validate_Creds(object):
    # Expects 5 params: raw user login and password, raw DB login and DB salt,
    # and DB hash(DB salt + DB pw)
    def __init__(self, DB_login, DB_salt, DB_hash, login, pw):
        import hashlib
        self.DB_login = DB_login
        self.DB_hash = DB_hash
        self.login = login
        # hash pw with the same salt as DB
        self.salt = DB_salt
        self.hash = hashlib.sha256(self.salt + pw).hexdigest()

    # check all the possibilities and return a code
    def compare(self):
        if self.login == self.DB_login:
            if self.hash == self.DB_hash:
                # success
                return 0
            else:
                # wrong password
                return 2
        else:
            # username does not exist
            return 1
