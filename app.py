from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField

app = Flask(__name__) # __name__ locates the app files
app.config['SECRET_KEY'] = 'secret!'

questions = ['Is is compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']

class YesNoQuestionForm(Form):
    answer = RadioField('Your answer', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')

@app.route('/') # Router
def index():
    return render_template('index.html')

# the default method of router is GET.
@app.route('/question/<int:id>', methods=['GET', 'POST']) # if an argument variable is defined in the router, it's not going to be after query mark '?'.
def question(id):
    form = YesNoQuestionForm()

    if form.validate_on_submit():
        if form.answer.data == 'yes':
            return redirect(url_for('question', id=id+1))
        else:
            return redirect(url_for('question', id))
    return render_template('question.html', question=questions[id], form=form)

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])
    
            

if __name__ == '__main__':
    app.run(debug=True) # for dev purpose only... not good enough for production
    # app.run(host='0.0.0.0', port=5000, debug=True) # for dev purpose only... not good enough for production