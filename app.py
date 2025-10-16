from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "This update was deployed automatically by my awesome CI/CD pipeline! Version 4.0"

if __name__ == '__main__':
    # Run on port 80 to be accessible from the browser
    app.run(host='0.0.0.0', port=80)