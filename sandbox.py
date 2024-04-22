from utils.api_gemini import ask_question_from_file

file_path = r'C:/Projects/PESSOAL/aiEngineeringChallenge/challenge-artificial-intelligence/resources/modulos_aprendizagem_gerados_chatGPT'

print("Bem-vindo ao Chatbot da +A Educação!")
print("Digite 'sair' a qualquer momento para encerrar o chat.")

while True:
    # Pergunta ao usuário
    user_input = input("Qual sua dúvida sobre o conteúdo abordado: ")

    # Verifica se o usuário deseja sair
    if user_input.lower() == 'sair':
        print("Chat encerrado.")
        break

    # Gera resposta com base na pergunta do usuário
    resposta = ask_question_from_file(file_path, user_input)
    print("Chatbot: " + resposta)
