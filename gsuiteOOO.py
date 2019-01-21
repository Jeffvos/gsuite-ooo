from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic', 'https://mail.google.com/']
SERVICE_ACCOUNT_FILE = 'keyp12.p12'
SERVICE_ACCOUNT_EMAIL='serviceaccount@gserviceaccount.com'

def gstuite(fullname_leaver, user_email):
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        SERVICE_ACCOUNT_EMAIL,
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES)

    outofoffice={
        'enableAutoReply': True,
        'responseBodyHtml': "<p>Hi, I am no longer working at COMPANY.</p>"
                            "<p>Regards,</p> <p>{}</p>".format(fullname_leaver),
        'restrictToDomain': False,
        }

    credentials = credentials.create_delegated(user_email)
    service = build('gmail', 'v1', credentials=credentials)
    result = service.users().settings().updateVacation(userId='me', body=outofoffice).execute()
    return (result)