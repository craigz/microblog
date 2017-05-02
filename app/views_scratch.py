from app import app

@app.route('/')
@app.route('/index')
def index():
    return "p00t_r00t!"

@app.route('/fart')
def another():
    return "another fukcer"
