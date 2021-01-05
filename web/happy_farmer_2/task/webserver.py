import datetime
from hashlib import sha3_512
from random import choice, random
from io import BytesIO

import flask
from PIL import Image


jap = '零一二三四五六七八九'
artojap = dict(zip(range(10), jap))
japtoar = dict(zip(jap, range(10)))


id_to_n_of_captchas = {}
id_to_cur_captcha_dt = {}
id_to_captcha_id = {}
total_captchas = 1000


def _generate_id() -> str:
    """Generates a random id for an entity
    Returns:
        str: random hash
    """
    return sha3_512(str(random()).encode('utf-8')).hexdigest()


app = flask.Flask(__name__)


def in_time(user_id):
    return datetime.datetime.now() - id_to_cur_captcha_dt[user_id] < \
        datetime.timedelta(seconds=2)


@app.route('/')
def index():
    user_id = flask.request.cookies.get('id')
    if user_id not in id_to_n_of_captchas.keys():
        user_id = _generate_id()
        id_to_n_of_captchas[user_id] = 0
        id_to_cur_captcha_dt[user_id] = None
        id_to_captcha_id[user_id] = None

    if id_to_n_of_captchas[user_id] == total_captchas:
        return 'PB{p0sp3sh1sh_ludey_n4sm3sh1sh}'

    if id_to_captcha_id[user_id] is not None and not in_time(user_id):
        id_to_n_of_captchas[user_id] = 0
        id_to_captcha_id[user_id] = id_to_cur_captcha_dt[user_id] = None

    if id_to_captcha_id[user_id] is None:
        id_to_captcha_id[user_id] = '{}{}{}{}'.format(*(choice(jap) for i in range(4)))
        id_to_cur_captcha_dt[user_id] = datetime.datetime.now()

    resp = flask.make_response(flask.render_template('index.html',
        completed_captchas=str(id_to_n_of_captchas[user_id]),
        total_captchas=str(total_captchas),
        captcha_url='/get_captcha/' + id_to_captcha_id[user_id]
        ))
    resp.set_cookie('id', user_id)

    return resp

@app.route('/get_captcha/<captcha_id>')
def get_captcha(captcha_id):
    assert(len(captcha_id) == 4)
    bg = Image.open('digits/bg6.png').convert("RGBA")
    for i in range(4):
        digit = Image.open(f'digits/{japtoar[captcha_id[i]]}.png').convert("RGBA")
        bg.paste(digit, (50 * i, 0), digit)
    
    img_io = BytesIO()
    bg.save(img_io, 'PNG')
    del bg
    img_io.seek(0)
    #def wsgi_app(environ, start_response):
    #    start_response('200 OK', [('Content-type', 'image/png')])
    #    print(type(img_io.read(2)))
    #    return img_io.read()
    #return flask.make_response(wsgi_app)
    return flask.Response(img_io.read(), mimetype='image/png')

@app.route('/send_captcha', methods=['POST'])
def send_captcha():
    user_id = flask.request.cookies['id']
    correct_ans = ''.join(str(japtoar[i]) for i in id_to_captcha_id[user_id])

    if correct_ans == flask.request.form['ans'] and in_time(user_id):
        id_to_n_of_captchas[user_id] += 1
    else:
        id_to_n_of_captchas[user_id] = 0

    id_to_captcha_id[user_id] = None
    id_to_cur_captcha_dt[user_id] = None

    return flask.redirect('/')


if __name__ == "__main__":
    app.run('0.0.0.0', port=5091, debug=False)
