from models.topic import Topic

from . import *


main = Blueprint('channel', __name__)

Model = Topic


@main.route('/')
def index():
    # ms = Model.query.all()
    return render_template('index.html')