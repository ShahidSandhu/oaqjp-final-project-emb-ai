'''
This module categorises the text or comments in postivie, neutral and negative
'''

import json
import requests

def emotion_detector(text_to_analyse):
    '''
    this function analysis the given tixt or comments
    '''
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson'\
    '.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the Emotion Predict  service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # Sending a POST request to the Emotion Predict API
        response = requests.post(url, json=input_json, headers=header, timeout=10)
    except requests.exceptions.Timeout:
        # Returning a dictionary containing request time out
        return {'message' : 'Request Time out', 'label': 'none', 'score': 'none'}

    # Parsing the JSON response from the API
    response_json = json.loads(response.text)

    emotion_score = response_json['emotionPredictions'][0]['emotion']

     # If the response status code is 200, extract the score from the response_in_json 
    if response.status_code == 200:
        # Getting the key with maximum value  
        Key_max = max(zip(emotion_score.values(), emotion_score.keys()))[1]   
        emotion_score['dominant_emotion'] = Key_max 
        
    # If the response status code is 500 , set score to None
    else:
        emotion_score = {
            'anger': none, 'disgust': none,'fear': none, 'joy': none, 
            'sadness': none, 'dominant_emotion': none
            }
    # Returning a dictionary containing sentiment analysis results
    return emotion_score