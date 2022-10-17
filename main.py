from bs4 import BeautifulSoup
import requests
import csv

# House


webcontent = requests.get('https://www.capitol.tn.gov/house/members').text


soup = BeautifulSoup(webcontent, 'html.parser')


Government_file = open('Government_file.csv', 'w')
csv_writer = csv.writer(Government_file)
csv_writer.writerow(['fname', 'lname', 'email', 'phone', 'party', 'district', 'state', 'assembly'])


for tr in soup.find_all('tr'):
  row = tr.text
 

  try:

    # first name
    fname = row.split(',')[1]
    fname = fname.split('\n')[0].strip()
    print(fname)
    # last name
    lname = row.split(',')[0].strip()
    print(lname)
    # email
    email = tr.find(class_='email icon-mail')['href']
    email = email.split(':')[1].strip()
    print(email)
    # phone
    phone = row.split('\n')[7].strip()
    print(phone)
    # party
    party = row.split('\n')[3].strip()
    print(party)
    # district
    district = tr.find(class_='button small icon-location').text.strip()
    print(district)
    # state
    state = "TN"
    print(state)
    # assembly
    assembly = "House"
    print(assembly)
    print('\n')

 
  except:
    fname = None
    lname = None
    email = None
    phone = None
    party = None
    district = None
    state = None
    assembly = None

  csv_writer.writerow([fname, lname, email, phone, party, district, state, assembly])

Government_file.close()

# Senate


webcontent = requests.get('https://www.capitol.tn.gov/senate/members').text


soup = BeautifulSoup(webcontent, 'html.parser')


Government_file = open('Government_file.csv', 'a')
csv_writer = csv.writer(Government_file)


for tr in soup.find_all('tr'):
  row = tr.text


  try:

    # first name
    fname = row.split(',')[1]
    fname = fname.split('\n')[0].strip()
    print(fname)
    # last name
    lname = row.split(',')[0].strip()
    print(lname)
    # email
    email = tr.find(class_='icon-mail')['href']
    email = email.split(':')[1].strip()
    print(email)
    # phone
    phone = row.split('\n')[7].strip()
    print(phone)
    # party
    party = row.split('\n')[3].strip()
    print(party)
    # district
    district = tr.find(class_='button small icon-location').text.strip()
    print(district)
    # state
    state = "TN"
    print(state)
    # assembly
    assembly = "Senate"
    print(assembly)
    print('\n')

  except:
    fname = None
    lname = None
    email = None
    phone = None
    party = None
    district = None
    state = None
    assembly = None

 
  csv_writer.writerow([fname, lname, email, phone, party, district, state, assembly])


Government_file.close()


