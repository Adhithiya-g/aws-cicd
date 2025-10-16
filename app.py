import os
from flask import Flask, render_template_string
import socket

app = Flask(__name__)

# The HTML template for our status page.
# It reads data from environment variables.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deployment Status</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(to right, #2c3e50, #3498db);
            color: #ecf0f1;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        .container {
            background-color: rgba(44, 62, 80, 0.8);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 {
            color: #3498db;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
            margin: 10px 0;
        }
        strong {
            color: #95a5a6;
        }
        code {
            background-color: #2c3e50;
            padding: 3px 6px;
            border-radius: 5px;
            font-family: "Courier New", Courier, monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Deployment Successful! Version 1</h1>
        <p>This application was automatically deployed by the CI/CD pipeline.</p>
        <p><strong>Repository:</strong> {{ repo_name }}</p>
        <p><strong>Commit SHA:</strong> <code>{{ commit_sha }}</code></p>
        <p><strong>Deployed At:</strong> {{ deploy_time }} (UTC)</p>
        <p><strong>Running on Container ID:</strong> <code>{{ container_id }}</code></p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    # Fetch data from environment variables
    repo_name = os.getenv('REPO_NAME', 'N/A')
    commit_sha = os.getenv('COMMIT_SHA', 'N/A')
    deploy_time = os.getenv('DEPLOY_TIME', 'N/A')
    
    # Get the container ID (hostname inside a container)
    container_id = socket.gethostname()

    # Render the HTML template with the dynamic data
    return render_template_string(
        HTML_TEMPLATE,
        repo_name=repo_name,
        commit_sha=commit_sha,
        deploy_time=deploy_time,
        container_id=container_id
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)