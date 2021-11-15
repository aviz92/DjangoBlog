import logging
import smtplib

""" 
In this py file have 1 class
    - SendOutlookMailClass
"""


class SendingMaliClass:
    def __init__(self):
        pass


class SendOutlookMailClass:
    """ This class ("SendOutlookMailClass") responsible for send emails from outlook account """

    def __init__(self):
        self.logger = logging.getLogger('Logger_Infrastructure.Projects_Logger.' + self.__class__.__name__)

    def send_outlook_mail(self, subject, text, server_name="mail.airspan.com",
                          sender='DjangoBlog@airspan.com', receives=None, username=None, password=None,):
        """
        This function responsible to check for send emails from outlook account

        The function get 7 parameter:
            - "server_name" - the server name for connection (string type)
            - "username" - the username for connection (string type)
            - "password" - the password for connection (string type)
            - "sender" - the sender name for connection (string type)
            - "receives" - the receives name for connection (list type)
            - "subject" - the subject for connection (string type)
            - "text" - the text for connection (string type)

        The function return 0 parameters
        """

        try:
            self.logger.info('Start sending a mail')
            if receives is None:
                receives = ['azaguri@airspan.com']

            # Prepare actual message
            message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
            """ % (sender, ", ".join(receives), subject, text)

            # Send the mail
            server = smtplib.SMTP(server_name)
            if username and password:
                server.login(username, password)
            #
            server.sendmail(sender, receives, message)
            # server.sendmail(FROM, TO, message)
            server.quit()
            self.logger.info('Finish sending a mail')
        except Exception:
            self.logger.exception('')
            return
