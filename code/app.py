from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

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
        'my team':'myself',
        'easy':'hard',
        'simple':'complex'
    }
    for word, replacement in dictionary.items():
        func = re.compile(re.escape(word), re.IGNORECASE)
        text = func.sub(replacement, text)
        del func
    return text


@app.route('/', methods=['GET', 'POST'])
def index():
    text = request.form.get('target', '')
    if request.method=='POST' and text:
        text = replace_words(text)
    return render_template('index.html', text=text)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
