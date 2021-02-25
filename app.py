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

@app.route('/works/html&css_3')
def work_hc3():
    return render_template('works/html&css_3.html')

@app.route('/works/html&css_4')
def work_hc4():
    return render_template('works/html&css_4.html')

@app.route('/works/html&css_5')
def work_hc5():
    return render_template('works/html&css_5.html')

@app.route('/works/html&css_6')
def work_hc6():
    return render_template('works/html&css_6.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



if __name__ == '__main__':
    #############################################
    ###### デプロイするときはdebug=Trueを消す######
    #############################################
    app.run()