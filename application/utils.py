import socket
import datetime

def get_user_ip():
    host = socket.gethostname()
    return socket.gethostbyname(host)

def get_timestamp_date():
    date_time = datetime.datetime.now()
    return str(date_time)[0:19]