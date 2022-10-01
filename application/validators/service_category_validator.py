from lib import validator

def validate():
    form = validator.Validator()
    
    form.add('category_name_az', ['required', 'min:3'])
    form.add('category_name_en', ['required', 'min:3'])
    
    form.validate()
    
    return form.isValid