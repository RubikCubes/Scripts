# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup
import requests

LOGIN_FORM_URL = 'https://nerdwallet.greenhouse.io/users/sign_in'
CREATE_SESSION_URL = 'https://nerdwallet.greenhouse.io/users/sign_in'
NEW_CANDIDATE_FORM_URL = 'https://nerdwallet.greenhouse.io/people/new?hiring_plan_id=24047'
CREATE_CANDIDATE_URL = 'https://nerdwallet.greenhouse.io/people'
COOKIE = {'_session_id':''} ## add session ID

def read_csv():
  open_csv = open('','rU') ##add CSV File
  csv_reader = csv.reader(open_csv)
  return csv_reader

def get_meta_value(client, url, name):
  html = requests.get(url, cookies=COOKIE).content
  soup = BeautifulSoup(html)
  csrf_metatags = soup.find_all('meta',attrs={'name':name})
  print csrf_metatags
  return csrf_metatags[0].get('content')

def get_form_csrf_token(client, url):
  return get_meta_value(client, url, 'csrf-token') 

def login(client, username, password):
  csrf_token = get_form_csrf_token(client, LOGIN_FORM_URL)
  form_credentials = {'user[email]':username, 'user[password]':password}
  headers = {'X-CSRF-Token': csrf_token}
  response = client.post(CREATE_SESSION_URL, headers=headers, data=form_credentials)

def add_candidate(client, list_of_candidates):
  """Assumes that client already has the session cookie set"""
  csrf_token = get_form_csrf_token(client, NEW_CANDIDATE_FORM_URL)
  for candidate in list_of_candidates:
    #email, first, last, company, title, linkedin
    email = candidate[0]
    first = candidate[1]
    last = candidate[2]
    company = candidate[3]
    title = candidate[4]
    linkedin = candidate[5]
    candidate_data = {
      'utf8': u'✓',
      'authenticity_token':csrf_token,
      'person[applications_attributes][0][prospect]':'true',
      'prospect_type':'for-job',
      'person[applications_attributes][0][referral]':'false',
      'prospective_hiring_plan_ids[]': 18876,
      'person[first_name]':first,
      'person[last_name]':last,
      'email_-6':email,
      'person[company]':company,
      'person[title]':title,
      'person[applications_attributes][0][source_id]':'16', 
      'person[applications_attributes][0][referred_by_id]':'', ##add referred by ID
      'person[recruiter_id]':'', ## add recruiter ID
      'tags':'[]',
      'json':'{"phone_numbers_attributes":[],"email_addresses_attributes":[{"id":"","value":"'+email+'","email_address_type_id":"1"}],"social_media_addresses_attributes":[{"id":"","value":"'+linkedin+'"}],"website_addresses_attributes":[],"addresses_attributes":[]}'
    }
    print first, last, company#, email
    
    headers = {'X-CSRF-Token': csrf_token}
    a = client.post(CREATE_CANDIDATE_URL, headers=headers, data=candidate_data, cookies=COOKIE)
    print a.text
    if "/people/duplicates/create_or_merge" in a.text:
      csrf_token = get_form_csrf_token(client,'https://app.greenhouse.io/people/duplicates/create_or_merge')
      data = {'authenticity_token':csrf_token}
      b = client.post('https://app.greenhouse.io/people/duplicates/create_or_merge?create=true', data=data, cookies=COOKIE)
      
def main():
  list_of_candidates = read_csv()
  client = requests.Session()
  add_candidate(client, list_of_candidates)

if __name__ == '__main__':
  main()






