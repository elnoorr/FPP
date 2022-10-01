from lib import mysql
from flask import session
from application import utils

def get_all():
    return mysql.Query('select `products`.*, `users`.`name` from `products`, `users` where `products`.`deleted_at` IS NULL and `products`.`user_id` = `users`.`id` order by `id` desc').get(True)

def insert(data, title, content, image, rent=0):
    return mysql.Table('products').create({
        'title': title,
        'content': content,
        'images': image,
        'keywords': data['keywords'],
        'description': data['description'],
        'seats': data['seats'],
        'warranty': data['warranty'],
        'maxspeed': data['maxspeed'],
        'charging_time': data['charging_time'],
        'range_for_a_charge': data['range_for_a_charge'],
        'climb_up': data['climb_up'],
        'price': data['price'],
        'rent': rent, 
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'created_at': utils.get_timestamp_date()
    })
    
def read(id):
    return mysql.Query(f"select * from `products` where `id` = {id}").get()

def update(data, title, content, image, id, rent):
    updateble = {
        'title': title,
        'content': content,
        'keywords': data['keywords'],
        'description': data['description'],
        'seats': data['seats'],
        'warranty': data['warranty'],
        'maxspeed': data['maxspeed'],
        'charging_time': data['charging_time'],
        'range_for_a_charge': data['range_for_a_charge'],
        'climb_up': data['climb_up'],
        'price': data['price'],
        'rent': rent,
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()
    }
    
    if image != '':
        updateble['image'] = image
    
    return mysql.Table('products').update(updateble, id)

def delete(id):
    return mysql.Table('products').update({
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'deleted_at': utils.get_timestamp_date()
        
    }, id)