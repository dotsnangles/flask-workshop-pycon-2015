from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField, StringField
from guess import Guess

app = Flask(__name__) # __name__ locates the app files
app.config['SECRET_KEY'] = 'secret!'

game = Guess('Python')
game.expand('Python', 'C++', 'Is it interpreted?', False)
game.expand('C++', 'Java', 'Does it run on a VM?', True)

questions = ['Is is compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']

class YesNoQuestionForm(Form):
    answer = RadioField('Your answer', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')

class LearnForm(Form):
    language = StringField('What language did you pick?')
    question = StringField('what is a question that differentiates your '
                           'language from mine?')
    answer = RadioField('what is the answer for your language?',
                        choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')

@app.route('/') # Router
def index():
    return render_template('index.html')

# the default method of router is GET.
@app.route('/question/<int:id>', methods=['GET', 'POST']) # if an argument variable is defined in the router, it's not going to be after query mark '?'.
def question(id):
    question = game.get_question(id)
    if question == None:
        return redirect(url_for('guess', id=id))

    form = YesNoQuestionForm()
    if form.validate_on_submit():
        new_id = game.answer_question(form.answer.data == 'yes', id)
        return redirect(url_for('question', id=new_id))

    return render_template('question.html', question=question, form=form)

@app.route('/guess/<int:id>', methods= ['GET', 'POST'])
def guess(id):
    form = YesNoQuestionForm()
    if form.validate_on_submit():
        if form.answer.data == 'yes':
            return redirect(url_for('learn', id=id))
    return render_template('guess.html', guess=game.get_guess(id), form=form)

@app.route('/learn/<int:id>', methods=['GET', 'POST'])
def learn(id):
    guess = game.get_guess(id)
    form = LearnForm()
    if form.validate_on_submit():
        game.expand(guess, form.language.data, form.question.data, form.answer.data == 'yes')
        return redirect(url_for('index'))
    return render_template('learn.html', guess=guess, form=form)
    
            

if __name__ == '__main__':
    app.run(debug=True) # for dev purpose only... not good enough for production
    # app.run(host='0.0.0.0', port=5000, debug=True) # for dev purpose only... not good enough for production