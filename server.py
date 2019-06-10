from bottle import get, post, request, route, run

options = {
    'certfile': '',
    'keyfile': ''
}


run(host='localhost', port=8080, server='cheroot', options=options, debug=True)