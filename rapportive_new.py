import urllib
import requests
from StringIO import StringIO
import xml.etree.ElementTree as ET
import csv
from unidecode import unidecode
import time


def main():
  list_of_emails = open_csv()
  csv_writer = write_to_csv()
  print list_of_emails
  for email in list_of_emails:
    time.sleep(1)
    text_string = get_rap_info(email)
    if ' token expired' in text_string:
      print 'token expired'
      break
    else:
      list_of_info = parse_data(text_string, email)
    csv_writer.writerow(list_of_info)
    print list_of_info
  

def get_rap_info(email):
  token = '' #add token
  headers = {"oauth_token": str(token)}
  rapportive_url = 'https://api.linkedin.com/v1/people/email='+urllib.quote(email)+':(first-name,last-name,headline,location)'
  r = requests.get(rapportive_url, headers=headers, timeout=60.00)
  return r.text
  
def parse_data(text_string, email):
  empty_list = []
  data = StringIO(unidecode(text_string))
  tree = ET.parse(data)
  root = tree.getroot()
  first = root.findtext('first-name')
  last = root.findtext('last-name')
  location = root.findtext('.//location/name')
  empty_list.append(email)
  if first:
    empty_list.append(unidecode(first))
  else:
    empty_list.append('None')
  if last:
    empty_list.append(unidecode(last))
  else:
    empty_list.append('None')
  if location:
    empty_list.append(unidecode(location))
  else:
    empty_list.append('None')
  return empty_list

def write_to_csv():
  open_csv = open('write_to_file.csv', 'wb')
  writer = csv.writer(open_csv)
  return writer
  
def open_csv():
  list_of_emails = []
  open_csv = open('test.csv', 'rU')
  reader = csv.reader(open_csv)
  for row in reader:
    list_of_emails.append(row[0])
  return list_of_emails
  
if __name__ == '__main__':
  main()