from flask import request
import re 



# request = {
#     "name": "John",
#     "surname": "Doe",
#     "email" : "john@gmail.com",
#     "username": 'johndoe',
#     "age": '33',
#     "bday": '19-05-1989',
#     "time" : '00:00:00',
#     "created": '00-00-1111 00:00:00'
# }

class Validator:

    def __init__(self):
        self.req = request.form
        self.form = {}
        self.isValid = False
        self.errors = []
    
    def add(self, field:str, rule:list):
        self.form[field] = rule
    
    def validate(self):
        for key in self.form:
            
            for rule in self.form[key]:
                
                if 'required' == rule:
                    if not self.req[key]:
                        self.errors.append('error')      

                if re.match(r'^min:\d+$', rule):
                    parseMinRule = rule.split(':')
                    
                    if len(self.req[key]) < int(parseMinRule[1]):
                        self.errors.append('error')

            
                if re.match(r'^max:\d+$', rule):
                    parseMaxRule = rule.split(':')
                
                    if len(self.req[key]) > int(parseMaxRule[1]):
                        self.errors.append('error')
                
                if 'email' == rule:
                    if not re.match(r'^[a-zA-Z0-9\.\-_]{3,}@{1}[a-zA-Z]{2,}\.{1}[a-zA-Z]{2,8}$', self.req[key]):
                        self.errors.append('error')
                        
                if 'trim' == rule:
                    # if re.match(r'\s', request[key]):
                    if ' ' in self.req[key]:
                        self.errors.append('error')
                
                if 'alpha' == rule:
                    if self.req[key].isalpha() == False:
                        self.errors.append('error')
                
                if 'digit' == rule:
                    if self.req[key].isdigit() == False:
                        self.errors.append('error')
                        
                if 'date' == rule:
                    if not re.match(r'^[0-9]{2}\-{1}[0-9]{2}\-{1}[0-9]{4}$', self.req[key]):
                        self.errors.append('error')
                        
                if 'time' == rule:
                    if not re.match(r'^[0-9]{2}:{1}[0-9]{2}:{1}[0-9]{2}$', self.req[key]):
                        self.errors.append('error')
                        
                if "datetime" == rule:
                    if not re.match(r'^[0-9]{2}\-{1}[0-9]{2}\-{1}[0-9]{4}\s{1}[0-9]{2}:{1}[0-9]{2}:{1}[0-9]{2}$', self.req[key]):
                        self.errors.append('error')
                    
            
        if len(self.errors) == 0:
            self.isValid = True
            
    def get_errors(self):
        return self.errors
        
    
        
# form = Validator(request)

# form.add('name', ['required', 'min:3', 'max:24'])
# form.add('surname', ['required', 'min:3', 'max:32'])
# form.add('email', ['required', 'email'])
# form.add('username', ['required', 'trim', 'alpha'])
# form.add('age', ['required', 'digit'])
# form.add('bday', ['required', 'date'])
# form.add('time', ['time'])
# form.add('created', ['datetime'])



# form.validate()

# print(form.isValid)

"""
required
min:value
max:value
mail
date
time
datetime
alpha
digit
trim
"""
        
