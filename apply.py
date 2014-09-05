import requests
import json
from data import resume_pdf, application_dict, url

def format_json():
    with open(resume_pdf) as resume:
        encoded_resume = resume.read().encode('base64')
    print encoded_resume
    application_dict['resume'] = encoded_resume
    # print application_dict

def sanity_check(encoded_resume):
    with open('resume_test.pdf', 'w') as resurrected_resume:
        resurrected_resume.write(encoded_resume.decode('base64'))

def send_resume():
    header = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(application_dict), headers=header)

if __name__ == '__main__':
    format_json()
    sanity_check(application_dict['resume'])