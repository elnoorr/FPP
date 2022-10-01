from lib import mysql
from flask import session
from application import utils
# import socket

# host = socket.gethostname() # istifadecinin islediyi serverin(komputer) adi
# ip_address = socket.gethostbyname(host) # serverin adina gore ip adresi almaq

def get_all():
    return mysql.Query(f"select `service_categories`.*, `users`.`name` from `service_categories`, `users` where `service_categories`.`deleted_at` IS NULL and `users`.`id` = `service_categories`.`user_id` order by `id` desc").get(True)

def create(data):
    return mysql.Table('service_categories').create({
        'categ_name_az': data['category_name_az'],
        'categ_name_en': data['category_name_en'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'created_at': utils.get_timestamp_date(),
        # 'updated_at': '',
        # 'deleted_at': ''
    })
    
def get_category():
    return mysql.Query(f"select * from `service_categories` where `id`=1").get()

def delete(id):
    return mysql.Table('service_categories').update({
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'deleted_at': utils.get_timestamp_date(),
    }, id)

def read(id):
    return mysql.Query(f"select * from `service_categories` where `id` = {id}").get()

def update(data, id):
    return mysql.Table('service_categories').update({
        'categ_name_az': data['category_name_az'],
        'categ_name_en': data['category_name_en'],
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()
    }, id)