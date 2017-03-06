from models.topic import Topic

from . import *


main = Blueprint('index', __name__)

Model = Topic


@main.route('/')
def index():
    ms = Model.query.all()
    print('index')
    return render_template('index.html', topics=ms)


# @main.route('/topic')
# def topic():
#     ms = Model.query.all()
#     ms = [1,2,3]
#     return render_template('index.html', topics=ms)


@main.route('/add', methods=['POST'])
def add():
    data = request.form
    print('data', data)
    m = Model(data)
    print('m:', m)
    m.save()
    return redirect('/index/')
