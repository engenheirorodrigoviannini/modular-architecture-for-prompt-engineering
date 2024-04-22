from fastapi import FastAPI
from utils.api_gemini import ask_question_from_file

app = FastAPI()

file_path = r'C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/modulos_aprendizagem_gerados_chatGPT'

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Chatbot da +A Educação!"}

@app.get("/chat/{user_input}")
def chat(user_input: str):
    if user_input.lower() == 'sair':
        return {"message": "Chat encerrado."}
    resposta = ask_question_from_file(file_path, user_input)
    return {"message": resposta}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
