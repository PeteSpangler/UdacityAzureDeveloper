import os
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash, make_response, session
from flask_sqlalchemy import SQLAlchemy 
from azure.servicebus import QueueClient, Message
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config.DevelopmentConfig')

app.secret_key = app.config.get('SECRET_KEY')

queue_client = QueueClient.from_connection_string(app.config.get('SERVICE_BUS_CONNECTION_STRING'),
                                                 app.config.get('SERVICE_BUS_QUEUE_NAME'))

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conference_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    job_position = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    interests = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Text, nullable=False)
    submitted_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Conference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "Conference: {}".format(self.name)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status =  db.Column(db.Text, nullable=False)
    message =  db.Column(db.Text)
    subject =  db.Column(db.Text)
    submitted_date = db.Column(db.DateTime(timezone=True))
    completed_date = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return "Notification#{}, status:{}".format(self.id, self.status)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        attendee = Attendee()
        attendee.first_name = request.form['first_name']
        attendee.last_name = request.form['last_name']
        attendee.email = request.form['email']
        attendee.job_position = request.form['job_position']
        attendee.company = request.form['company']
        attendee.city = request.form['city']
        attendee.state = request.form['state']
        attendee.interests = request.form['interest']
        attendee.comments = request.form['message']
        attendee.conference_id = app.config.get('CONFERENCE_ID')

        try:
            db.session.add(attendee)
            db.session.commit()
            session['message'] = 'Thank you, {} {}, for registering!'.format(attendee.first_name, attendee.last_name)
            return redirect('/Registration')
        except:
            logging.error('Error occured while saving your information')

    else:
        if 'message' in session:
            message = session['message']
            session.pop('message', None)
            return render_template('registration.html', message=message)
        else:
             return render_template('registration.html')

@app.route('/Attendees')
def attendees():
    attendees = Attendee.query.order_by(Attendee.submitted_date).all()
    return render_template('attendees.html', attendees=attendees)


@app.route('/Notifications')
def notifications():
    notifications = Notification.query.order_by(Notification.id).all()
    return render_template('notifications.html', notifications=notifications)

@app.route('/Notification', methods=['POST', 'GET'])
def notification():
    if request.method == 'POST':
        notification = Notification()
        notification.message = request.form['message']
        notification.subject = request.form['subject']
        notification.status = 'Notifications submitted'
        notification.submitted_date = datetime.utcnow()

        try:
            db.session.add(notification)
            db.session.commit()
            
            msg = Message(b'{"MessageName": "notification.subject", "messageText": "notification.message"}')
            queue_client.send(msg)
            """
            ##################################################
            ## TODO: Refactor This logic into an Azure Function
            ## Code below will be replaced by a message queue
            #################################################
            
            attendees = Attendee.query.all()

            for attendee in attendees:
                subject = '{}: {}'.format(attendee.first_name, notification.subject)
                send_email(attendee.email, subject, notification.message)

            notification.completed_date = datetime.utcnow()
            notification.status = 'Notified {} attendees'.format(len(attendees))
            db.session.commit()
            # TODO Call servicebus queue_client to enqueue notification ID

            #################################################
            ## END of TODO
            #################################################
            """
            return redirect('/Notifications')
        except :
            logging.error('log unable to save notification')

    else:
        return render_template('notification.html')

def send_email(email, subject, body):
    if not app.config.get('SENDGRID_API_KEY'):
        message = Mail(
            from_email=app.config.get('ADMIN_EMAIL_ADDRESS'),
            to_emails=email,
            subject=subject,
            plain_text_content=body)

        sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
        sg.send(message)


if __name__ == "__main__":
    app.run(debug=True)