import re
from flask import Flask, Blueprint, render_template, request, url_for, redirect

def create_app(settings=None):
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'you-will-never-guess'
    if settings:
        application.config.update(settings)
    application.register_blueprint(app)

    @application.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('main.index'))

    return application

def replace_words(text):
    # inspired by this @AnjumSayed tweet:
    # https://twitter.com/AnjumSayed/status/1183611121590140929?s=20
    dictionary = {
        'refund':'???',
        'complex':'complicated',
        'gate':'door',
        'researching':'copying',
        'implement':'mimic',
        'fundamental':'basic',
        'we':'I',
        'us':'me',
        'our':'my',
        'ours':'mine',
        'clear':'evident',
        'my team':'myself',
        'difficult':'trivial',
        'easy':'hard',
        'simple':'complex'
    }
    for word, replacement in dictionary.items():
        func = re.compile(re.escape(word), re.IGNORECASE)
        text = func.sub(replacement, text)
        del func
    return text if text else ''

app = Blueprint('main', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = request.form.get('FormText', '')
    if request.method=='POST':
        text = replace_words(text)
    return render_template('index.html', text=text)


# Development entrypoint
if __name__ == '__main__':
    settings = dict(
        env='development',
        testing=False
    )
    run_args = dict(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True,
    )
    application = create_app(settings)
    application.run(**run_args)
