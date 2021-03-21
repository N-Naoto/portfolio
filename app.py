from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def work():
    return render_template('works.html')

@app.route('/works/html&css_1')
def work_hc1():
    return render_template('works/html&css_1.html')

@app.route('/works/html&css_2')
def work_hc2():
    return render_template('works/html&css_2.html')

@app.route('/works/js_1')
def work_js1():
    return render_template('works/js_1.html')

@app.route('/works/js_2')
def work_js2():
    return render_template('works/js_2.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)