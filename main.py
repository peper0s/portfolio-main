#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    if button_python:
        return render_template('index.html', button_python=button_python)
    elif button_discord:
        return render_template('index.html', button_discord=button_discord)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)