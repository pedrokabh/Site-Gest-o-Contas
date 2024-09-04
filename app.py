from flask import Flask
from routes.login import login

app = Flask(__name__)
app.register_blueprint(login)

# Execução
if __name__ == "__main__":
    app.run(debug=True)