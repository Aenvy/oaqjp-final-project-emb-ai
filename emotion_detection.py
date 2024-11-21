import requests

import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    res = json.loads(response.text)
    formatted_output = res["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(formatted_output, key = lambda x: formatted_output[x])
    formatted_output["dominant_dictionary"] = dominant_emotion
    return formatted_output