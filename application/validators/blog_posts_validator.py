from lib import validator

def validate():
    form = validator.Validator()
    
    form.add('title_az', ['required', 'min:3'])
    form.add('title_en', ['required', 'min:3'])
    form.add('content_az', ['required', 'min:3'])
    form.add('content_en', ['required', 'min:3'])
    form.add('keywords', ['reqiured', 'min:3'])
    form.add('description', ['required', 'min:3'])
    
    form.validate()
    
    return form.isValid