from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        inspiration = request.form.get('text_field')
        return render_template('index.html', result=inspiration)
    return render_template('index.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
