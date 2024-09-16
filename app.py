from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../frontend'))

data_file_path = os.path.join(os.path.dirname(__file__), '../frontend/data.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    # Открываем файл с указанием кодировки
    with open(data_file_path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
