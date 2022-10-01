
from flask import render_template, request, redirect, url_for
from application.models import partners
import os
from werkzeug.utils import secure_filename
from application.config import server as serverConfig
from server import app

def index():
    return render_template('admin/partners.html', title="Tərəfdaşlar", partners=partners.get_all())

def create():
    company_name = request.form['company_name']
    image = request.files['image']
    image_name = image.filename
    secured_filename = secure_filename(image_name)
    
    partners.create(company_name, secured_filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], secured_filename))
        
    return redirect('/admin/partners')

def edit(id):
    return render_template('admin/partners_edit.html', title='Redakte', data=partners.read(id))

def update(id):
    company_name = request.form['company_name']
    image = request.files['image']
    image_name = image.filename
    secured_filename = secure_filename(image_name)
    partners.update(company_name, secured_filename, id)
    return redirect('/admin/partners/edit/' + str(id))

def delete(id):
    partners.delete(id)
    
    return redirect('/admin/partners')
      