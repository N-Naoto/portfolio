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

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/work/html&css_1')
def work_hc1():
    return render_template('works/html&css_1.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')



if __name__ == '__main__':
    #############################################
    ###### デプロイするときはdebug=Trueを消す######
    #############################################
    app.run()