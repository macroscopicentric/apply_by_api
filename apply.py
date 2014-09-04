import requests
import json
from data import resume_pdf, application_dict, url

def send_resume():
    with open(resume_pdf) as resume:
        encoded_resume = resume.read().encode('base64')
    application_dict['resume'] = encoded_resume

    header = {'content-type': 'application/json'}

    requests.post(url, data=json.dumps(application_dict), headers=header)

if '__name__' == '__main__':
    send_resume()