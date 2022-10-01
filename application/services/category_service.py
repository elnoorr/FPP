from application.models import category
from flask import render_template, url_for, request, redirect
from application.validators import service_category_validator

# method=GET
def index():
    return render_template('admin/service_categories.html', title='Kateqoriyalar', categories=category.get_all())

# method=POST
def store():
    if service_category_validator.validate():
        category.create(request.form)
        
        return redirect('/admin/service/categories')
    else:
        return redirect('/admin/service/categories')

def edit(id):
    return render_template('admin/admin_service_categories_edit.html', title="Redakte", data=category.read(id))

def update(id):
    if service_category_validator.validate():
        category.update(request.form, id)
        return redirect('/admin/service/categories/edit/' + str(id))
    else:
        return redirect('/admin/service/categories/edit/' + str(id))

def delete(id):
    category.delete(id)
    
    return redirect('/admin/service/categories')
