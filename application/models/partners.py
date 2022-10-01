
from lib import mysql
from flask import session
from application import utils

def get_all():
    return mysql.Query(f"select * from `partners` where `deleted_at` IS NULL order by `id` desc").get(True)

def create(company_name, secured_filename):
    return mysql.Table('partners').create({
        'company_name': company_name,
        'image': secured_filename,
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'created_at': utils.get_timestamp_date(),
    })
    
def read(id):
    return mysql.Query(f"select * from `partners` where `id` = {id}").get()

def update(company_name, secured_filename, id):
    return mysql.Table('partners').update({
        'company_name': company_name,
        'image': secured_filename,
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'updated_at': utils.get_timestamp_date()
    }, id)
    
def delete(id):
    return mysql.Table('partners').update({
        'user_id': session['id'],
        'user_ip': utils.get_user_ip(),
        'deleted_at': utils.get_timestamp_date()
    }, id)