import google.generativeai as genai
import json

# Lê a chave da API do arquivo de configuração
with open('config') as config_file:
    config_data = json.load(config_file)
    google_api_key = config_data.get('google_api_key')

# Configura a chave da API
genai.configure(api_key=google_api_key)

def ask_question_from_file(text, question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text + " " + question)
    return response.text