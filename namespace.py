from socketio.namespace import BaseNamespace

from chat import application

class Namespace(BaseNamespace):
    def __init__(self):
        self.logger = application.logger
        self.log('Session started')

    def log(self, message):
        self.logger.info('[%s] %s' % (self.socket.sessid, message))

    def recv_cconnect(self):
        self.log('Connected')

    def recv_disconnet(self):
        self.log('Disconected')