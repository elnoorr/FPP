from flask import render_template, url_for, request, redirect
from application.models import user
from application.models import blog_category
from application.validators import blog_categories_validator
from application.validators import blog_posts_validator
from werkzeug.utils import secure_filename
import os
from application.config import server as serverConfig
from application.models import post
# from server import app


# index
def admin_blog_categories():
    return render_template('admin/blog_categories.html', title='Kateqoriyalar', blog_categories=blog_category.get_all())
# index

# blog categories start


def category_create():
    if blog_categories_validator.validate():
        blog_category.create(request.form)
        
        return redirect('/admin/blog/categories')
    else:
        return redirect('/admin/blog/categories')


def category_edit(id):
    return render_template('admin/blog_categories_edit.html', title='Redakte', data=blog_category.read(id))


def category_update(id):
    if blog_categories_validator.validate():
        blog_category.update(request.form, id)
        return redirect('/admin/blog/categories/edit/' + str(id))
    else:
        return redirect('/admin/blog/categories/edit/' + str(id))


def category_delete(id):
    blog_category.delete(id)

    return redirect('/admin/blog/categories')

# blog categories end

# blog posts start

def blog_post():
    # print(post.get_all())
    return render_template('admin/blog_posts.html', title='Postlar', posts=post.get_all())


# select-e blog kategoriyadaki melumatari cixardir
def admin_blog_new():
    return render_template('admin/blog_new.html', title='Yeni post', blog_categories=blog_category.get_all())


def store_blog():
    if blog_posts_validator.validate():
        
        image = request.files['image']
        image_name = image.filename
        secured_filename = secure_filename(image_name)
        
        post.insert(request.form, image_name)
        image.save(os.path.join(serverConfig.UPLOAD_FOLDER, secured_filename))
        
        return redirect('/admin/blog/new')


def edit_blog(id):
    return render_template('admin/blog_post_edit.html', title='Redakte', data=post.read(id), blog_categories=blog_category.get_all())


def update_blog(id):
    image = request.files['image']
    image_name = image.filename
    
    post.update(request.form, image_name, id)
    
    if image_name != "":
        secured_filename = secure_filename(image_name)
        image.save(os.path.join(serverConfig.UPLOAD_FOLDER, secured_filename))

    return redirect('/admin/blog/posts/edit/' + str(id))
        
        
def delete_blog(id):
    post.delete(id)
    return redirect('/admin/blog/posts')
