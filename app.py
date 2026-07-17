import re
from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import pandas as pd
import book_recom



books = pd.read_csv('books_input_data.csv')
app = Flask(__name__)

# outputBooks = []

bookData = {
             "Book Name":books['bookTitle'].tolist(),
            "Author":books['bookAuthor'].tolist(),
             "ISBN Number":books['ISBN'].tolist(),
         }

processData = []
data = ""

@app.route("/",methods=['GET','POST'])
def bookInput():
    global data
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))[2]
        redirect(url_for('bookOutput'))
    return render_template('bookInput.html',bookData=bookData)
@app.route("/output",methods=['GET','POST'])
def bookOutput():
    global data
    global processData
    # processData = outputBooks
    booksTitle = []
    print(data)
    if len(data) <2:
        processData = []
        return render_template('bookInput.html',bookData=bookData)
    else:
        processData = book_recom.recom_id(data,k=5)
        print(processData)
        booksTitle = books[books["ISBN"].isin(processData)]["bookTitle"].values.tolist()
        print(booksTitle)
        data = ""
        return render_template('bookOutput.html',processData=processData,length = len(processData),booksTitle=booksTitle)

if __name__ == '__main__':
    app.run(debug=True)