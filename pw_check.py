# coding: utf8

class Validate_Creds(object):
    def __init__(self, login, pw):
        import hashlib
        self.login = login
        self.pw = hashlib.sha256(pw).hexdigest()

    def retrieve_actual(self, source):
        # from elsewhere, import creds.
        # expects sha256 hashed values!
        self.true_login = source.username
        self.true_pw = source.password

    def compare_creds(self):
        if self.login == self.true_login:
            if self.pw == self.true_pw:
                return True
            else:
                self.true_login = None
                self.true_pw = None
                return False
        else:
            self.true_login = None
            self.true_pw = None
            return False

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

attempt = Validate_Creds(login, pw)
attempt.retrieve_actual(source)
result = attempt.compare_creds()

if result == True:
    print 'Success! Logging in...'
else:
    print 'YOU FAILED'
