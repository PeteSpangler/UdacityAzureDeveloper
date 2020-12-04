import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from azure.servicebus import QueueClient
from . import routes

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config.DevelopmentConfig')

app.secret_key = app.config.get('SECRET_KEY')

queue_client = QueueClient.from_connection_string(app.config.get('SERVICE_BUS_CONNECTION_STRING'),
                                                 app.config.get('SERVICE_BUS_QUEUE_NAME'))

if __name__ == "__main__":
    app.run(debug=True)