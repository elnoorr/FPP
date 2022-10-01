from flask import render_template, url_for, request, redirect
from application.models import user
from application.models import category
from application.models import service
from application.validators import service_validator
from werkzeug.utils import secure_filename
import os
from application.config import server as serverConfig

def admin_service_categories():
    return render_template('admin/service_categories.html',title='Kateqoriyalar', service_categories=category.get_all())

def admin_all_service():
    return render_template('admin/all_service.html', title='Xidmətlər', services=service.get_all())

def service_new():
    return render_template('admin/new_service.html', title='Yeni xidmət', service_categories=category.get_all())

def service_store():
    if service_validator.validate():
    
        image = request.files['image']
        image_name = image.filename
        secured_filename = secure_filename(image_name)
        
        service.insert(request.form, image_name)
        image.save(os.path.join(serverConfig.UPLOAD_FOLDER, secured_filename))
        
        return redirect('/admin/service/new')
        
        
def service_edit(id):
    return render_template('admin/service_edit.html', title='Redakte', data=service.read(id), service_categories=category.get_all())
    

def service_update(id):
    image = request.files['image']
    image_name = image.filename
    
    service.update(request.form, image_name, id)
    
    if image_name != "":
        secured_filename = secure_filename(image_name)
        image.save(os.path.join(serverConfig.UPLOAD_FOLDER, image_name))
    
    return redirect('/admin/service/edit/' + str(id))

def service_delete(id):
    service.delete(id)
    return redirect('/admin/service/all')
