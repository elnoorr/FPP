from lib import validator
def validate():
    form = validator.Validator()

    form.add('title[az]', ['required'])
    form.add('title[en]', ['required'])
    form.add('content[az]', ['required'])
    form.add('content[en]', ['required'])
    form.add('keywords', ['required'])
    form.add('description', ['required'])
    form.add('seats', ['required'])
    form.add('warranty', ['required'])
    form.add('maxspeed', ['required'])
    form.add('charging_time', ['required'])
    form.add('range_for_a_charge', ['required'])
    form.add('climb_up', ['required'])
    form.add('price', ['required'])
    
    form.validate()
    return form.isValid