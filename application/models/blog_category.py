from lib import mysql
from flask import session
from application import utils


def get_all():
    return mysql.Query(f"select `blog_categories`.*, `users`.`name` from `blog_categories`, `users` where `blog_categories`.`deleted_at` IS NULL and `users`.`id` = `blog_categories`.`user_id` order by `id` desc ").get(True)


def create(data):
    return mysql.Table('blog_categories').create({
        'category_name_az': data['category_name_az'],
        'category_name_en': data['category_name_en'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'created_at': utils.get_timestamp_date()
    })


def read(id):
    return mysql.Query(f"select * from `blog_categories` where `id` = {id}").get()


def update(data, id):
    return mysql.Table('blog_categories').update({
        'category_name_az': data['category_name_az'],
        'category_name_en': data['category_name_en'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()
    }, id)


def delete(id):
    return mysql.Table('blog_categories').update({
      'user_id': session['id'],
      'user_ip': utils.get_user_ip(),
      'deleted_at': utils.get_timestamp_date(),
    }, id)
