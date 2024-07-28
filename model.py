import connect
from random import randint
from flask import request,jsonify
import os


def selectfunction():
    conn = connect.sqlconnect()
    kurs = conn.cursor()

    slc_profile = "SELECT * FROM Book_Data ORDER BY id DESC"
    print(slc_profile)
    datas = []
    kurs.execute(slc_profile)
    for profile in kurs.fetchall():
        res = { 'id' : profile[0],
                'Book_Title' : profile[1],
                'Author': profile[2],
                'Written_year': profile[4],
                'Genre': profile[3],
                'cover': profile[5]
                }
        datas.append(res)
        
    return datas

def simpandata(cvr):
    id_book = randint(0,999999)
    book_title = request.form.get('book')
    author = request.form.get('author')
    written_year = request.form.get('tgl_lahir')
    genre = request.form.get('genre')
    image = cvr
    conn = connect.sqlconnect()

    if not validate_fields(book_title, written_year, author, genre):
        return jsonify({"error": "All fields must be filled."}), 400

    query = "INSERT INTO Book_Data (id,Book_Title,author,written_year,genre, cover)" \
           "VALUES ('{id}','{nama}','{author}','{written_year}','{genre}','{cover}')"\
        .format(id=id_book,nama=book_title,author=author,written_year=written_year,genre=genre,cover = image)

    connect.sqlquery(query,conn)

    conn.commit()

    return ('True')

def deletet(book_id):
    conn = connect.sqlconnect()

    query_select = "SELECT cover FROM Book_Data WHERE id = '{id}';".format(id=book_id)
    cur = connect.sqlquery(query_select, conn)
    result = cur.fetchone()

    if result:
        image_path = result[0]
        if os.path.exists(image_path):
            os.remove(image_path)  # Delete the image file from the file system

        # Delete the record from the database
        query_delete = "DELETE FROM Book_Data WHERE id = '{id}';".format(id=book_id)
        print(query_delete)
        cur = connect.sqlquery(query_delete, conn)
        conn.commit()
        return True

    return False

def validate_fields(book_title, written_year, author, genre):
    return all([book_title, written_year, author, genre])
