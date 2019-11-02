from flask import Flask, render_template, request
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    text = TextAreaField('Paste your research here:', validators=[DataRequired()])
    submit = SubmitField('Publish')

def replace_words(text):
    import re
    dictionary = {
        'complex':'complicated',
        'gate':'door',
        'refund':'trophy',

        'researching':'copying',
        'implementation':'paste',

        'we':'I',
        'our':'my',
        'ours':'mine',
        'clear':'evident',
        'my team':'myself'
    }
    for word, replacement in dictionary.items():
        func = re.compile(re.escape(word), re.IGNORECASE)
        text = func.sub(replacement, text)
    return text


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        text = form.text.data
        print('Text: {}'.format(text))
        print('Form: {}'.format(request.form['text']))

        form.text.data = replace_words(text)
        return render_template('home.html', form=form)
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
