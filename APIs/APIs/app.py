from flask import Flask, render_template,url_for,request,redirect,make_response
import random
import json
from flask_dance.contrib.github import make_github_blueprint , github
import os 
import templates
import pprint

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app = Flask(__name__)
app.config["SECRET_KEY"]="SECRET KEY  "

github_blueprint = make_github_blueprint(client_id='27335c72106ddca20f4c',
                                         client_secret='d5f0eb9ae0dcd60233d356420fdb581ef8f13120')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():
    
    templates="index.html"
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            usuario=account_info_json['login']
            imagens=account_info_json['avatar_url']
            return render_template(templates,usuario=usuario,imagens=imagens)

    return '<h1>Request failed!</h1>'

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação



