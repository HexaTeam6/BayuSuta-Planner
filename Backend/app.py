from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/edo')
def math():
    return render_template('index.html')

@app.route('/hello/<name>')
def helloDynamic(name):
    return render_template('page.html',name=name)

@app.route('/echo', methods=['POST'])
def echo():
    return render_template('echo.html', text=request.form['text'])

@app.route('/echo')
def echom():
    return render_template('echo.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')