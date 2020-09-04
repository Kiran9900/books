from flask impofrom flask import Flask, request, jsonify
app = Flask(__name__)


books_list=[
        {
            "id":0,
            "author":"Stendhal",
            "language":"English",
            "title":"The Red And The Black",
        },
        {
            "id":1,
            "author":"Anita Desai",
            "language":"English",
            "title":"A Life Of Kalpana Chawla",
        },
        {
            "id":2,
            "author":"Kalidasa",
            "language":"English",
            "title":"Megdoot",
        },
        {
            "id":3,
            "author":"Kautilya",
            "language":"English",
            "title":"Arthashastra",
        },
        {
            "id":4,
            "author":"Mahatma Gandhi",
            "language":"English",
            "title":"My Experiments With Truth",
        },
        {
            "id":5,
            "author":"Vedavyasa",
            "language":"Sanskrit",
            "title":"Mahabharath",
        },
 ]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method=='GET':
        if len(books_list)>0:
             return jsonify(books_list)
        else:
            'Nothing found',404

    if request.method=='POST':
        new_author=request.form['author']
        new_author=request.form['language']
        new_auhor=request.form['title']
        iD=books_list[-1]['id']+1

        new_obj={
            'id':iD,
            'author':new_author,
            'languge':new_lang,
            'title':new_title,
        }
        books_list.append(new_obj)
        return jsonify(books_list),201

@app.route('/book/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method=='GET':
        for book in books_list:
            if book['id']==id:
                return jsonify(book)
            pass
    if request.method=='PUT':
        for book in books_list:
            if book['id']==id:
                book['author']=request.form['author']
                book['language']=request.form['language']
                book['title']=request.form['title']
                updated_book={
                    'id':id,
                    'author':book['author'],
                    'language':book['language'],
                    'title':book['title']
                }
                return jsonify(updated_book)
    if requested.method=='DELETE':
        for index,book in enumerate(books_list):
            if book['id']==id:
                books_list.pop(index)
                return jsonify(books_list)

if __name__=='__main__':
    app.run()
              
