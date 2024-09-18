'''
This module categorises the text or comments in postivie, neutral and negative
'''

import json
import requests

def emotion_detector(text_to_analyse):
    '''
    this function analysis the given tixt or comments
    '''
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson'\
    '.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    try:
        # Sending a POST request to the sentiment analysis API
        response = requests.post(url, json=myobj, headers=header, timeout=10)
    except requests.exceptions.Timeout:
        # Returning a dictionary containing request time out
        return {'message' : 'Request Time out', 'label': 'none', 'score': 'none'}

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

     # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500 , set label and score to None
    else:
        label = None
        score = None

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}