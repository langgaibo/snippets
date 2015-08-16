# coding: utf8

class Validate_Creds(object):
    def __init__(self, login, pw):
        import hashlib
        self.login = hashlib.sha256(login).hexdigest()
        self.pw = hashlib.sha256(pw).hexdigest()

    def retrieve_actual(self, source):
        # from elsewhere, import creds
        self.t_login = source.username
        self.t_pw = source.password

    def compare_creds(self):
        if self.login == self.t_login:
            if self.pw == self.t_pw:
                return True
            else:
                self.t_login = None
                self.t_pw = None
                return False
        else:
            self.t_login = None
            self.t_pw = None
            return False

# A dummy for our testing purposes
class Actual_Creds(object):
    def __init__(self):
        import hashlib
        self.username = hashlib.sha256('Darth').hexdigest()
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
