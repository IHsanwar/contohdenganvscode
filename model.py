import connect
from random import randint
from flask import request



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
                'Written_year': profile[3],
                'Genre': profile[4],
                'cover': profile[5]
                }
        datas.append(res)

    print(datas)
    return datas

def simpandata(cvr):
    id_book = randint(0,999999)
    book_title = request.form.get('book')
    author = request.form.get('author')
    year = request.form.get('year')
    genre = request.form.get('genre')
    image = cvr
    conn = connect.sqlconnect()

    query = "INSERT INTO Book_Data (id,Book_Title,author,genre,written_year, cover)" \
           "VALUES ('{id}','{nama}','{author}','{year}','{genre}','{cover}')"\
        .format(id=id_book,nama=book_title,author=author,year=year,genre=genre,cover = image)

    connect.sqlquery(query,conn)

    conn.commit()

    return True

def deletetamu(book_id):

    query = "delete from soals where id = '{id}';".format(id = book_id)
    print(query)
    conn = connect.sqlconnect()
    cur = connect.sqlquery(query,conn)
    conn.commit()
    return True
