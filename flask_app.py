from flask import Flask, render_template, request
import os
import json
import control


app = Flask(__name__)


@app.route('/')
def flask_home():
    """Displays the HTML of the home page of the app.

    Returns
    -------
    str: the html content returned to be displayed.
    """
    print (request.args.get('lang'))
#    result = {'labels': [], 'answer': ['Hello World']}
    result = control.home()
    return(render_template('interaction.html', greeting=result))


@app.route('/api/interact', methods=['POST'])
def flask_interact():
    """.

    Returns
    -------
    str: the html content returned to be displayed in the app layout
    """
    print (request.json)
    user_input = request.json['input']
   
#    result = {  'labels': ['#getincontact'],
#                'answer': ["I have no idea what you're saying cause I'm not cognitive yet."],
#                'action': {'fake_action': 'what am I doing?'},
#                'lang': 'fr'
#             }
    result = control.interact(user_input)
    return(render_template('partials/exchange.html', input={'text':user_input}, result=result))


def flask_app_launch(**kwargs):
    """Launches the flask application server.

    Keyword Arguments
    -----------------
    **host: the host to attach the web server (default 0.0.0.0).
    **port: the port to attach the web server (default 8080).
    **debug: whether to switch to debug mode or not.
    """
    print("Setting up components")
    control.setup()
    
    host_ = kwargs.get('host', '0.0.0.0')
    port_ = kwargs.get('port', 8080)
    debug_ = kwargs.get('debug', True)
    app.run(host=host_, port=port_, debug=debug_, threaded=True)


if __name__ == '__main__':
    print("ERROR: to launch this app, run server.py instead")
    #flask_app_launch()
