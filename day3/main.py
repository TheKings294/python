from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/loto')
def loto():
    numbers = []
    for i in range (6):
        numbers.append(randint(1,10))

    return render_template("loto.html", numbers=numbers)

@app.route('/books')
def books():
    books = [
        {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "category": "Informatique",
            "stock": 3
        },
        {
            "title": "Le Crime de l'Orient-Express",
            "author": "Agatha Christie",
            "category": "Mystère",
            "stock": 4
        },
        {
            "title": "Les Misérables",
            "author": "Victor Hugo",
            "category": "Roman",
            "stock": 1
        },
        {
            "title": "Steve Jobs",
            "author": "Walter Isaacson",
            "category": "Biographie",
            "stock": 0
        }
    ]
    return render_template("books.html", books=books)

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    words = {
        'bonjour' : {
            'en' : 'Hello',
            'es' : 'Hola',
            'de' : 'Hallo',
        },
        'comment va tu' : {
            'en' : 'How are you',
            'es' : 'Como estas',
            'de' : 'Hallo',
        }
    }

    if request.method == "POST":
        text = request.form.get("text")
        target_lang = request.form.get("target_lang")

        if words[text.lower()]:
            translate_word = words[text.lower()][target_lang]
        else:
            translate_word = "Mot non trouvé"

        return render_template("translate.html", translated_text=translate_word)

    return render_template("translate.html")

if __name__ =="__main__":
    app.run(debug=True)