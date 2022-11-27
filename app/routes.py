from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    users = {
        "name":"John Doe",
        "posts": 13
    }
    return (render_template('index.html',title="Home", user=users))


@app.route('/posts')
def posts():
    posts = [ {
        "id":"4354",
        "title":"Getting good at git",
        "text":"Diving deep into git and VCS",
        "author":"John Doe",
        "time_creation":"17-10-2022"
    },
    {
        "id":"435432",
        "title":"Getting started with DevOps",
        "text":"So, what is DevOps and why is it important in the first place?",
        "author":"Itsfoss",
        "time_creation":"17-10-2022"
    },
      {
        "id":"4354332",
        "title":"Developer Trends in 2022",
        "text":"It is November 28th 2022 and you are reading the code report",
        "author":"Fireship",
        "time_creation":"28-10-2022"
    }
    ]
    return(render_template('posts.html', posts=posts))
