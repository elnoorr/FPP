from flask import render_template, url_for, request, redirect
from application.models import user
from application.models import setting
from application.validators import setting_validator


def index():
    return render_template('admin/settings.html', title='Tənzimləmələr', setting=setting.get_setting())

def update_setting():

    if setting_validator.validate():
        setting.update(request.form)
        
        return redirect('/admin/settings')
    else:
        return render_template(
            'admin/settings.html',
            title='Tənzimləmələr', 
            setting=setting.get_setting(),
            error= 'duz yaz yetkaaa'
        )
