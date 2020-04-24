from googleapiclient import discovery
from langdetect import detect
import json

API_KEY='AIzaSyBU9qBYpaMC3-RDxUeKwJmGzfAJ-bC0yow'

#Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

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
        response = service.comments().analyze(body=analyze_request).execute()
        jr = json.dumps(response, indent=2)
        x = json.loads(jr)
        score = x['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value']
        return score