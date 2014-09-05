import requests
import json
from data import resume_pdf, application_dict, url

def format_json():
    with open(resume_pdf) as resume:
        encoded_resume = resume.read().encode('base64')
    application_dict['resume'] = encoded_resume


def send_resume():
    header = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(application_dict), headers=header)

if __name__ == '__main__':
    format_json()