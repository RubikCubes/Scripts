import requests
import csv

NAME = '' ##add csv file
FILE_TYPE = '.csv'
CSV = NAME+FILE_TYPE

def read_csv():
  csv_file = open(CSV,'rU') 
  csv_reader = csv.reader(csv_file)
  return csv_reader
  
def check_for_dupes(checking_file): 
  new_list = []
  for row in checking_file:
    email = row[0]
    url = 'https://nerdwallet.greenhouse.io/people?utf8=%E2%9C%93&type=all&job_status=all&search_terms='+email+'&commit='

    cookies = {'_session_id':''} ##add session ID   
    r = requests.get(url, cookies=cookies)
    if "No candidates found" in r.text:
      pass
    else:
      print 'DUP FOUND: '+ email
  return new_list
  
    
def main():
  checking_file = read_csv()
  new_data = check_for_dupes(checking_file) #took out writer (checking_file, writer)
  
if __name__ == '__main__':
  main()
