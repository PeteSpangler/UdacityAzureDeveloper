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

    dbconnect = psycopg2.connect(os.environ["MyDbConnection"])
    # TODO: Get connection to database

    try:
        # TODO: Get notification message and subject from database using the notification_id

        # TODO: Get attendees email and name

        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        pass
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        dbconnect.close()
        # TODO: Close connection
