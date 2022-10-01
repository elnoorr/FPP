from lib import mysql
from flask import session
from application import utils

def get_all():
    return mysql.Query('select `posts`.*, `blog_categories`.`category_name_az`, `users`.`name` from `posts`, `blog_categories`, `users` where `posts`.`deleted_at` IS NULL and `posts`.`category_id` = `blog_categories`.`id` and `posts`.`user_id`=`users`.`id` order by `posts`.`id` desc').get(True)

def insert(data, image):
    return mysql.Table('posts').create({
        'title_az': data['title_az'],
        'title_en': data['title_en'],
        'category_id': data['category_id'],
        'image': image,
        'content_az': data['content_az'],
        'content_en': data['content_en'],
        'keywords': data['keywords'],
        'description': data['description'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'created_at': utils.get_timestamp_date()
    })

def read(id):
    return mysql.Query(f"select * from `posts` where `id` = {id}").get()


def update(data, image, id):
    updateble = {
        'title_az': data['title_az'],
        'title_en': data['title_en'],
        'category_id': data['category_id'],
        'content_az': data['content_az'],
        'content_en': data['content_en'],
        'keywords': data['keywords'],
        'description': data['description'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()
    }
    
    if image != '':
        updateble['image'] = image
        
    return mysql.Table('posts').update(updateble, id)


def delete(id):
    return mysql.Table('posts').update({
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'deleted_at': utils.get_timestamp_date()
    }, id)