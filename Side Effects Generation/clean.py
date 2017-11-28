import argparse
import json
import sys
import os
import csv

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords


from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


# words = lower_case.split()
# words = [w for w in words if not w in stopwords.words("english")]
# print(lower_case)


def get_service():
    credentials = GoogleCredentials.get_application_default()
    scoped_credentials = credentials.create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    scoped_credentials.authorize(http)
    return discovery.build('language', 'v1beta1', http=http)


def get_native_encoding_type():
    """Returns the encoding type that matches Python's native strings."""
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'


def analyze_entities(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding,
    }

    service = get_service()

    request = service.documents().analyzeEntities(body=body)
    response = request.execute()
    entities = []
    for i in range(len(response['entities'])):
    	if(response['entities'][i]['salience']>0.001 and (response['entities'][i]['type']=="OTHER" or response['entities'][i]['type']=="EVENT")):
    		entities.append(response['entities'][i]['name'])
    return(set(entities))

side_effects = {}

for filename in os.listdir(r'C:\Users\amrit\OneDrive\Documents\Projects\wikidrugs\Final_Side_effects\Side_effects_Final'):
	if filename.endswith('.txt'):
		pathname = os.path.join(r'C:\Users\amrit\OneDrive\Documents\Projects\wikidrugs\Final_Side_effects\Side_effects_Final', filename)
		textfile = open(pathname,encoding = 'utf8')
		buffer = []
		for line in textfile:
			buffer.append(line)
			text = ' '.join(map(str, buffer))
		else:
			soup = BeautifulSoup(text)
			letters_only = re.sub("[^a-zA-Z]", " ", soup.get_text())
			lower_case = letters_only.lower()
			# entities = analyze_entities(lower_case)
			side_effects[filename.replace(".txt", "")] = lower_case
			textfile.close()


with open('Side_effects_final_paragraph.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in side_effects.items():
       writer.writerow([key, value])
