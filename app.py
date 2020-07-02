from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def showids():
    return render_template('selectstory.html', stories=stories.values())

@app.route('/questions')
def show_home():
    storyid = request.args["storyid"]
    story = stories[storyid]
    prompts = story.prompts
    return render_template('question.html', storyid=storyid, title=story.title, prompts=prompts)

@app.route('/story')
def show_story():
    storyid = request.args["storyid"]
    story = stories[storyid]
    text = story.generate(request.args)
    return render_template('story.html', title=story.title, text=text)