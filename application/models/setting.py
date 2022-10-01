from lib import mysql
from flask import session
from application import utils

def update(data):
    return mysql.Table('settings').update({
        'email': data['email'],
        'address': data['address'],
        'map': data['map'],
        'company_info_az': data['company_info_az'],
        'company_info_en': data['company_info_en'],
        'facebook': data['facebook'],
        'linkedin': data['linkedin'],
        'instagram': data['instagram'],
        'keywords': data['keywords'],
        'description': data['description'],
        'user_id' : session['id'],
        'user_ip' : utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()  
    }, '1')

def get_setting():
    return mysql.Query(f"select * from `settings` where `id`=1").get()