from backend.flask_test.bluehome.home import home


@home.route('/index')
def index():
    print('index')
    return 'index'