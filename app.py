from crypt import methods
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # __name__ locates the app files

questions = ['Is is compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']

@app.route('/') # Router
def index():
    return render_template('index.html')

# the default method of router is GET.
@app.route('/question/<int:id>', methods=['GET', 'POST']) # if an argument variable is defined in the router, it's not going to be after query mark '?'.
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == 'yes':
            return redirect(url_for('question', id=id+1))
        else:
            return redirect(url_for('question', id=id))
    return render_template('question.html', question=questions[id])

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])
    
            

if __name__ == '__main__':
    app.run(debug=True) # for dev purpose only... not good enough for production
    # app.run(host='0.0.0.0', port=5000, debug=True) # for dev purpose only... not good enough for production