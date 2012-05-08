from flask import Flask
from flask import render_template
import subprocess
import os

app = Flask(__name__)
cred = {}

@app.route('/')
def index():
    sounds = ['alpha-beta.wav', 'gamma-delta.wav']
    return render_template('index.html', sounds=sounds) # send tuples

@app.route('/test')
def test():
    [ user, password ] = get_cred()
    cmd = [ 'sshpass', '-p', password, 'ssh',
            '-o', 'StrictHostKeyChecking=no',
            '-o', 'UserKnownHostsFile=/dev/null',
            user, 'ls' ]
    p = subprocess.call(['ls'])
    return 'OK'

def get_cred():
    global cred
    cred['user'] = os.environ['USER'] + '@horsy'
    cred['password'] = os.environ['PASSWORD']

    return [ cred['user'], cred['password'] ]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
