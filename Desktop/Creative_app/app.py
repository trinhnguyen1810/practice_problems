# app.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

story = []

@app.route('/')
def index():
    last_sentence = story[-1] if story else None
    return render_template('index.html', last_sentence=last_sentence, story=story)

@app.route('/add_sentence', methods=['POST'])
def add_sentence():
    new_sentence = request.form.get('sentence')
    if new_sentence:
        story.append(new_sentence)
        if len(story) >= 10:
            return redirect('/full_story')
    return redirect('/')

@app.route('/reset_story')
def reset_story():
    story.clear()
    return redirect('/')

@app.route('/full_story')
def full_story():
    return render_template('full_story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
