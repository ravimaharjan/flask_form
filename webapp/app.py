from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'FlaskUser'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()

