from flask import Flask

app = Flask(__name__) # __name__ locates the app files

guesses = ['Python', 'Java', 'C++']

@app.route('/') # Router
def index():
    return '<h1>Guess the Language!</h1>'

@app.route('/guess/<int:id>')
def guess(id):
    return (
        '<h1>Guess the Language!</h1>'
        f'<p>My guess: {guesses[id]}</p>'
    )
    
            

if __name__ == '__main__':
    app.run(debug=True) # for dev purpose only... not good enough for production
    # app.run(host='0.0.0.0', port=5000, debug=True) # for dev purpose only... not good enough for production