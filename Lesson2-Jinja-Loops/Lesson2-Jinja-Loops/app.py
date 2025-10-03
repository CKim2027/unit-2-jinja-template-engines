from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Home page with link to roster"""
    return '''
    <html>
        <head>
            <title>Class Roster App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 600px;
                    margin: 50px auto;
                    text-align: center;
                }
                h1 { color: #4fc3f7; }
                a {
                    display: inline-block;
                    padding: 15px 30px;
                    background: #4fc3f7;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 18px;
                }
                a:hover { background: #3ba8d6; }
            </style>
        </head>
        <body>
            <h1>Class Roster Application</h1>
            <p>View the student roster for Advanced Programming</p>
            <a href="/roster">View Roster</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
