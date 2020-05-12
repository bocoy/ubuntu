from flask import Flask, request, jsonify

app = Flask(__name__)
app.users = {}
app.id_count = 1
app.tweets = []

@app.route('/new_user', methods = ['POST'])
def welcome():
    new_user = request.json
    new_user['id'] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count = app.id_count+1
    
    return jsonify(app.users)

@app.route('/login', methods = ['POST'])
def login():
    log_info = request.json
    log_id = int(log_info['id'])
    log_pw = int(log_info['password'])
    if log_id not in app.users:
        return "you're not user!!", 400
    else:
        if log_pw not in app.users:
            return "wrong password", 400
        return "OK Welcome", 200

@app.route('/tweet', methods = ['POST'])
def tweet():
    payload = request.json
    user_id =int(payload['id'])
    tweet = payload['tweet']
    if user_id not in app.users:
        return "yor're not user", 400
    if len(tweet) > 300:
        return "overwirte", 400
    
    app.tweets.append({
        'user_id' : user_id,
        'tweet' : tweet
        })
    return jsonify(app.tweets)
