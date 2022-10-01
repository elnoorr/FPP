from flask import render_template, url_for, request, redirect
import jsonpickle
from application.models import product
from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response
from application.validators import product_validator
import os
from application.config import server as serverConfig

def product_index():
    return render_template('admin/product_index.html', title='Məhsullar', products=product.get_all(), decoder=jsonpickle.decode)

def product_create():
    return render_template('admin/product_create.html', title='Yeni məhsul')

def product_store():
    if product_validator.validate():
        title = {
            "az": request.form['title[az]'],
            "en": request.form['title[en]']
        }
        title = jsonpickle.encode(title)
        content = {
            "az": request.form['content[az]'],
            "en": request.form['content[en]']
        }
        content = jsonpickle.encode(content)
        
        if 'rent' in request.form:
            rent = 1
        else:
            rent = 0
                 
        files = []
        for file in request.files.getlist('images[]'):
            files.append(file.filename)
        
        if len(files) > 0 and files[0] != "":
            files = jsonpickle.encode(files)
            for file in request.files.getlist('images[]'):
                file.save(os.path.join(serverConfig.UPLOAD_FOLDER, secure_filename(file.filename)))
            product.insert(request.form, title, content, files, rent)
            
            return redirect('/admin/products/store')
        else:
            return render_template('admin/product_create.html', title='Yeni məhsul', error='sekil bos olmamalidir')

        # return jsonpickle.encode(files)
    return render_template('admin/product_create.html', title='Yeni məhsul', error='bos olmamalidir')
    
   
   
def product_edit(id):
    return render_template('admin/product_edit.html', title='Redakte', data=product.read(id), decoder=jsonpickle.decode)


def product_update(id):
    if product_validator.validate():
        title = {
            "az": request.form['title[az]'],
            "en": request.form['title[en]']
        }
        title = jsonpickle.encode(title)
        content = {
            "az": request.form['content[az]'],
            "en": request.form['content[en]']
        }
        content = jsonpickle.encode(content)

        if 'rent' in request.form:
            rent = 1
        else:
            rent = 0

        files = []
        for file in request.files.getlist('images[]'):
            files.append(file.filename)
        # return jsonpickle.encode(files)
        if len(files) > 0 and files[0] != "":

            files = jsonpickle.encode(files)
            for file in request.files.getlist('images[]'):
                file.save(os.path.join(serverConfig.UPLOAD_FOLDER, secure_filename(file.filename)))
            product.update(request.form, title, content, files, id, rent)

            return redirect('/admin/products/index')
        else:

            product.update(request.form, title, content, '', id, rent)
            return redirect('/admin/products/index')
        
        # else:
        #     return render_template('admin/product_create.html', title='Yeni məhsul', error='sekil bos olmamalidir')

        # return jsonpickle.encode(files)
    return render_template('admin/product_create.html', title='Yeni məhsul', error='bos olmamalidir')

def product_delete(id):
    product.delete(id)
    return redirect('/admin/products/index')
