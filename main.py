# импорт библиотек
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return password




# создание пароля
letter = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLXCVBNM,.;"\[]{}!@#$%^&*()_+=-:?><|*/'
password = ''
for i in range(12):
    r = random.choice(letter)
    password = password+r
# всё, пароль готов





if __name__ == "__main__":
    app.run(debug=True)
