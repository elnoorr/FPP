from flask import Flask
from application.config import server as serverConfig
from application.services import admin_service
from application.services import blog_service
from application.services import service_service
from application.services import setting_service
from application.services import category_service
from application.services import partners_service
from application.services import product_service
app = Flask(__name__)

app.secret_key = 'golfcar2022*#'

app.config['UPLOAD_FOLDER'] = serverConfig.UPLOAD_FOLDER

@app.route('/')
def index():
    # return "connected" if mysql.Query("").checkConnection() else "not connected" 
    # mysql.Query("insert into `posts` (`title`, `content`) VALUES ('Salam', 'Sebuhi')").exec()
    # mysql.Table('posts').delete(6)
       
    # siqaret cekib gelirem men... xaxaaaxaaa
    return 'main'

# Admin
@app.route('/admin/login')
def admin_login():
    return admin_service.admin_login()

# Admin giris tesdiqi (authorization)
@app.route('/admin/auth', methods=['POST'])
def admin_auth():
    return admin_service.admin_auth()

# admin ana sehife
@app.route('/admin/dashboard')
def admin_dashboard():
    return admin_service.admin_dashboard()

# admin: terefdaslar sehifesi start
@app.route('/admin/partners')
def admin_partners():
    return partners_service.index()

@app.route('/admin/partners/create', methods=['POST'])
def admin_partners_create():
    return partners_service.create()

@app.route('/admin/partners/edit/<id>')
def admin_partners_edit(id):
    return partners_service.edit(id)

@app.route('/admin/partners/update/<id>', methods=['POST'])
def admin_partners_update(id):
    return partners_service.update(id)

@app.route('/admin/partners/delete/<id>')
def admin_partners_delete(id):
    return partners_service.delete(id)


# admin: teredaslar sehifesi end

# setting start
@app.route('/admin/settings')
def admin_settings():
    return setting_service.index()

@app.route('/admin/settings/update', methods=['POST'])
def admin_settings_update():
    return setting_service.update_setting()
# setting end


@app.route('/admin/messages')
def admin_messages():
    return admin_service.admin_messages()

# Category
@app.route('/admin/blog/categories')
def admin_blog_categories():
    return blog_service.admin_blog_categories()


# end category



@app.route('/admin/blog/categories/create', methods=['POST'])
def admin_blog_categories_create():
    return blog_service.category_create()

@app.route('/admin/blog/categories/edit/<id>')
def admin_blog_categories_edit(id):
    return blog_service.category_edit(id)

@app.route('/admin/blog/categories/update/<id>', methods=['POST'])
def admin_blog_categories_update(id):
    return blog_service.category_update(id)

@app.route('/admin/blog/categories/delete/<id>')
def admin_blog_categories_delete(id):
    return blog_service.category_delete(id)

#####

@app.route('/admin/blog/new')
def admin_blog_new():
    return blog_service.admin_blog_new()


@app.route('/admin/blog/posts/store', methods=['POST'])
def admin_blog_posts_store():
    return blog_service.store_blog()

@app.route('/admin/blog/posts/edit/<id>')
def admin_blog_posts_edit(id):
    return blog_service.edit_blog(id)

@app.route('/admin/blog/posts/update/<id>', methods=['POST'])
def admin_blog_posts_update(id):
    return blog_service.update_blog(id)

@app.route('/admin/blog/post/delete/<id>')
def blog_post_delete(id):
    return blog_service.delete_blog(id)

@app.route('/admin/blog/posts')
def admin_blog_posts():
    return blog_service.blog_post()


####


@app.route('/admin/service/categories')
def admin_service_categories():
    return category_service.index()

@app.route('/admin/service/categories/store', methods=['POST'])
def service_category_store():
    return category_service.store()

@app.route('/admin/service/categories/edit/<id>')
def admin_service_categories_edit(id):
    return category_service.edit(id)

@app.route('/admin/service/categories/update/<id>', methods=['POST'])
def admin_service_categories_update(id):
    return category_service.update(id)

@app.route('/admin/service/categories/delete/<id>')
def service_category_delete(id):
    return category_service.delete(id)

@app.route('/admin/service/all')
def admin_all_service():
    return service_service.admin_all_service()

@app.route('/admin/service/new')
def admin_service_new():
    return service_service.service_new()

@app.route('/admin/service/store', methods=['POST'])
def admin_service_store():
    return service_service.service_store()

@app.route('/admin/service/edit/<id>')
def admin_service_edit(id):
    return service_service.service_edit(id)

@app.route('/admin/service/update/<id>', methods=['POST'])
def admin_service_update(id):
    return service_service.service_update(id)

@app.route('/admin/service/delete/<id>')
def admin_service_delete(id):
    return service_service.service_delete(id)

# admin products start

@app.route('/admin/products/index')
def admin_products_index():
    return product_service.product_index()

@app.route('/admin/products/create')
def admin_products_create():
    return product_service.product_create()

@app.route('/admin/products/store', methods=['POST'])
def admin_products_store():
    return product_service.product_store()

@app.route('/admin/products/edit/<id>')
def admin_products_edit(id):
    return product_service.product_edit(id)

@app.route('/admin/products/update/<id>', methods=['POST'])
def admin_products_update(id):
    return product_service.product_update(id)

@app.route('/admin/products/delete/<id>')
def admin_products_delete(id):
    return product_service.product_delete(id)
# admin products end


if __name__ == "__main__":
    app.debug = serverConfig.MODE
    
    app.run(
        host = serverConfig.HOST,
        port = serverConfig.PORT
    )