from flask import request

def upload():
    upload_dest = './up/'
    if request.method == 'POST':
        f = request.files['photo']
        ddest = upload_dest + f.filename

        f.save(ddest)
        return ddest

