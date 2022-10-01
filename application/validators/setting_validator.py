from lib import validator

def validate():
    
    form = validator.Validator()
    
    form.add('email', ['required', 'email'])
    form.add('address', ['required', 'min:6'])
    form.add('map', ['required'])
    form.add('company_info_az', ['required'])
    form.add('company_info_en', ['required'])
    form.add('facebook', ['required'])
    form.add('linkedin', ['reqiured'])
    form.add('instagram', ['reqiured'])
    form.add('keywords', ['required', 'min:3'])
    form.add('description', ['required', 'min:3'])
   
    form.validate()
    
    return form.isValid


# form = Validator(request)

# form.add('name', ['required', 'min:3', 'max:24'])
# form.add('surname', ['required', 'min:3', 'max:32'])
# form.add('email', ['required', 'email'])
# form.add('username', ['required', 'trim', 'alpha'])
# form.add('age', ['required', 'digit'])
# form.add('bday', ['required', 'date'])
# form.add('time', ['time'])
# form.add('created', ['datetime'])
