from datetime import datetime


def log(request):
    ip = request.remote_addr
    action = request.form.get('action')
    filename = request.files.get('file').filename
    record = f'[{datetime.now()}] | {ip} | {action} | {filename}\n'
    with open('requests.log', 'a') as logfile:
        logfile.write(record)
