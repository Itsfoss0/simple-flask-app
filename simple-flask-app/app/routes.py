from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hi Mom!, this is home"
