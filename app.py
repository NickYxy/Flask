from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import logging


from models import db
# from models.user import User
from models.topic import Topic
# from models.chat import Chat


app = Flask(__name__)
manager = Manager(app)


def register_routes(app):
    from routes.index import main as routes_index
    # from routes.chat import main as routes_chat
    # from routes.user import main as routes_user
    app.register_blueprint(routes_index, url_prefix='/index')
    # app.register_blueprint(routes_chat, url_prefix='/chat')
    # app.register_blueprint(routes_user, url_prefix='/user')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # secret_key 和 数据库配置都放在 config.py 文件中, 例子如下
    # db_uri = 'sqlite:///{}'.format('demo.sqlite')
    # 自行添加
    import config
    app.secret_key = config.secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_uri
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3001,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()

# (gunicorn wsgi --worker-class=gevent -t 4 -b 0.0.0.0:8000 &)