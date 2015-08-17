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

# A dummy for our testing purposes
class Actual_Creds(object):
    def __init__(self):
        import hashlib
        self.username = 'Darth'
        self.password = hashlib.sha256('Vader').hexdigest()

# make it work
source = Actual_Creds()

login = raw_input('Please enter your login: ')
pw = raw_input('Please enter your password: ')
print 'Checking...\n\n\n'

attempt = Validate_Creds(source.username, source.password, login, pw)
result = attempt.compare_creds()

if result == 0:
    print 'Success! Logging in...'
elif result == 1:
    print 'FAILURE: username does not exist.'
else:
    print 'FAILURE: wrong password.'
