from googleapiclient import discovery
from langdetect import detect
import file_io
import json

API_KEY=''

#Generates API client object dynamically based on service name and version.
service = None

def is_english(comment):
    try:
        lang = detect(comment)
        return lang == 'en'
    except:
        return False

def get_toxicity(comment):
        analyze_request = {
            'comment': {'text': comment },
            'requestedAttributes': {'SEVERE_TOXICITY': {}}
        }
        try:
            response = service.comments().analyze(body=analyze_request).execute()
        except:
            return -1
            
        jr = json.dumps(response, indent=2)
        x = json.loads(jr)
        score = x['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value']
        return score

def set_API_key(filename):
    global service
    API_KEY = file_io.read_txt(filename)
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)