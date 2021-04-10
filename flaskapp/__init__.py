from flask import Flask
app = Flask(__name__)
import search

app.add_url_rule('/', 'login', search.login)
app.add_url_rule('/refresh', 'refresh', search.search, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=False)

