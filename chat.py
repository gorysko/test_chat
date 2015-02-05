from gevent import monkey
from flask import Flask
from flask import Response
from flask import render_template
from flask import request
from socketio import socketio_manage

monkey.patch_all()

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000

@application.route('/', methods=['GET',])
def landing():
    return "TEST"

@application.route('/socket.io/<path:remaining>'):
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/chat': ChatNamespace}, request)
    except:
        application.logger.error('Exception handling sockets', exc_info=True)

    return Response()