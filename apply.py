import requests
from resume import resume_pdf, application_dict

with open(resume_pdf) as resume:
    encoded_resume = resume.read().encode('base64')

application_dict['resume'] = encoded_resume