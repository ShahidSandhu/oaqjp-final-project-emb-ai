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

    response = requests.post(url, json=input_json, headers=header, timeout=10)
    
        # if the response status code is 200, extract the score
    if response.status_code == 200:
        # Parsing the JSON response from the API
        response_json = json.loads(response.text)

        emotion_score = response_json['emotionPredictions'][0]['emotion']
        # Getting the key with maximum value  
        Key_max = max(zip(emotion_score.values(), emotion_score.keys()))[1]   
        emotion_score.update({'dominant_emotion': Key_max})
    elif response.status_code == 400:
        emotion_score = {
            'anger': None, 'disgust': None,'fear': None, 'joy': None, 
            'sadness': None, 'dominant_emotion': None
            }
    else:
        emotion_score = {
            'anger': None, 'disgust': None,'fear': None, 'joy': None, 
            'sadness': None, 'dominant_emotion': None
            }
    # Returning a dictionary containing sentiment analysis results
    return emotion_score