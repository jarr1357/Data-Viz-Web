from flask import Flask, render_template, json
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
@app.route('/api/<name>/')
def api_get_name(name):
    return json.jsonify({
        'name': name
    })
 
 
if __name__ == '__main__':
    app.run(debug=False)


