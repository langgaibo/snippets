# coding: utf8
# 朗盖博 2015

# A simple login auth Class that handles a salt (but not battery).
# This version includes an additional DB hash-generating Class,
# to simulate how a DB might use and provide a salt along with the hash.

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

###### Let's test it! ######

# This Class, used by our imaginary database, makes a nice, savory random salt
# and uses that to hash the user-provided password.
class Actual_Creds(object):
    def __init__(self, login, pw):
        import random, string, hashlib
        self.username = login
        self.saltbox = random.randint(12,18)
        # thanks http://stackoverflow.com/a/2257449
        self.salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(self.saltbox))
        # raw password is hashed(salt + pw)
        self.hash = hashlib.sha256(self.salt + pw).hexdigest()

# make our target DB values. Inits with raw login, salt, and hash(salt+pw)
source = Actual_Creds('Darth','Vader')
# success case:
login1 = 'Darth'
pw1 = 'Vader'
# Wrong username:
login2 = 'Derp'
pw2 = 'Vader'
# Wrong pw:
login3 = 'Darth'
pw3 = 'Voodoo'

# run the table like Minnesota Fats
attempt1 = Validate_Creds(source.username, source.salt, source.hash, login1, pw1)
result1 = attempt1.compare()

attempt2 = Validate_Creds(source.username, source.salt, source.hash, login2, pw2)
result2 = attempt2.compare()

attempt3 = Validate_Creds(source.username, source.salt, source.hash, login3, pw3)
result3 = attempt3.compare()

# laziness drives innovation
def check_results(foo):
    result = foo
    if result == 0:
        print 'Success! Logging in...'
    elif result == 1:
        print 'FAILURE: username does not exist.'
    else:
        print 'FAILURE: wrong password.'

# if you validate yourself too much, you'll go blind
check_results(result1)
check_results(result2)
check_results(result3)
