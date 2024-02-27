
from flask import Flask,render_template,redirect,request,send_from_directory
import model,upload
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloz():
    datas = model.selectfunction()
    return render_template('halamanutama.html', title="Jinja Demo Site", results=datas)

@app.route('/Tambah', methods=['GET'])
def Pluz():
    return render_template('tambah.html' , title="Jinja Demo Site")

@app.route('/Tambah',methods=['POST'])
def PLuz2():
    loc_cover = upload.upload()
    print(loc_cover)
    model.simpandata( loc_cover)
    return redirect("/Tambah")

@app.route('/up/<path:path>')
def send_js(path):
    return send_from_directory('up', path)

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE soals SET data=%s WHERE id=%s", (id_data))
    mysql.connection.commit()
    return redirect(url_for('home'))




app.debug = True

#netstat -ano |find /i "listening"
#taskkill /PID xxxx /F


if __name__=='__main__':
    app.run(port=4545)