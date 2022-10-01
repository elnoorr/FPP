from lib import mysql
from flask import session 
import hashlib

def auth(email, password):
    password = password.encode('utf-8')
    password = hashlib.sha256(password).hexdigest()
    check = mysql.Query(f"select * from `users` where `email` = '{email}' and `password` = '{password}'")
    
    if check.count() > 0:
        
        userData = check.get()
        
        session['auth'] = True
        session['id'] = userData[0]
        
        return True
    else:
        return False