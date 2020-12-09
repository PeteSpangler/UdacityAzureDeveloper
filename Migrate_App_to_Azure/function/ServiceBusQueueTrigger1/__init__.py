import azure.functions as func
import logging
import os
from datetime import datetime
import psycopg2
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s', notification_id)
 
    # Done: Get connection to database
    connection = psycopg2.connect(os.environ["MyDbConnection"])
    cursor = connection.cursor()
    try:
        # TODO: Get notification message and subject from database using the notification_id
        notification_message = cursor.execute("SELECT message FROM Notification WHERE id=notification_id;")
        notification_subject = cursor.execute("SELECT subject FROM Notification WHERE id=notification_id")
        # TODO: Get attendees email and name
        cursor.execute("SELECT first_name, last_name, email FROM Attendee;")
        attendees = cursor.fetchall()

        for attendee in attendees:
            subject = '{}: {}'.format(attendee.first_name, notification_subject)
            send_email(attendee.email, subject, notification_message)

        notification_completed_date = datetime.utcnow()
        notification_status = 'Notified {} attendees'.format(len(attendees))
        connection.commit()
        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        pass
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        # Done: Close connection
