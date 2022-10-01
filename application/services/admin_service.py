from flask import render_template, url_for, request, redirect
from application.models import user

def admin_login():
    return render_template('admin/login.html')

def admin_auth():
    email = request.form['email']
    password = request.form['password']
    
    checkAuth = user.auth(email, password)
    
    if checkAuth:
        return redirect('/admin/dashboard', code=302)
    else:
        return 'melumatlar sehvdir'

def admin_dashboard():
    return render_template('admin/index.html', title='Ana səhfə')


def admin_partners():
    return render_template('admin/partners.html', title="Tərəfdaşlar")
    

def admin_messages():
    return render_template('admin/messages.html', title='İsmarıclar')

