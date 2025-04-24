from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template with some basic styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>DevOps CI/CD Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
            background-color: #f0f2f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #1a73e8;
        }
        .description {
            color: #5f6368;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <p class="description">{{ description }}</p>
        <p>Environment: {{ environment }}</p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        title="Welcome to DevOps CI/CD Demo",
        description="This is a simple Flask application demonstrating CI/CD with GitHub Actions and Heroku.",
        environment=os.getenv('FLASK_ENV', 'development')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))