from gevent import monkey
monkey.patch_all()
import bottle
import threading
import globals
from Bot import Client
import config
from web import give_donor
from web import clear_donor
from helpers import db
def bottle_server(host='127.0.0.1', port=8888):
    bottle.run(host=host, port=port, server='gevent')

if __name__ == "__main__":
    globals.client = Client(command_prefix='!')
    print('Starting bottle.......')
    threading.Thread(target=bottle_server).start()
    print('Starting client.........')
    globals.client.run(config.token)
