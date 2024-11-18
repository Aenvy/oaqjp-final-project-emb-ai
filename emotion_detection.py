import requests

# Define the emotion detection function
def emotion_detector(text_to_analyze):
    # Define the endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Construct the input JSON
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Send POST request to the Emotion Predict API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Extract the text attribute from the response and return it
    return response.json().get('text', {})

