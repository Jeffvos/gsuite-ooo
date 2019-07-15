from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic', 'https://mail.google.com/']

# 'keyp12.p12' should be replaced with the path to your generated p12 key
#'serviceaccount@gserviceaccount.com' should be replaced with the generated service gsuite account
SERVICE_ACCOUNT_FILE = 'keyp12.p12'
SERVICE_ACCOUNT_EMAIL='serviceaccount@gserviceaccount.com'

def outReply(fullname_leaver, user_email):
    credentials = ServiceAccountCredentials.from_p12_keyfile(
        SERVICE_ACCOUNT_EMAIL,
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES)
#You can use html for the body of the Out of office reply. 
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
