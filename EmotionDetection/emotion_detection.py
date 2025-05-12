import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        result = json.loads(response.text)['emotionPredictions'][0]['emotion']
        result['dominant_emotion'] = max(result, key=result.get)
        return result
    
    if response.status_code == 400:
        result = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
        return result
        
    return None