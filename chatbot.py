import google.generativeai as genai

# Configure the API key
# A chave API está diretamente no código, como solicitado.
genai.configure(api_key="AIzaSyDo-cB-kgkWERn1HmE1pk6VJ00SC7ISMVU")

# Choose the model to use (e.g., "gemini-pro")
# Adicionando um bloco try-except para a inicialização do modelo
try:
    model = genai.GenerativeModel("gemini-pro")
except Exception as e:
    print(f"ERRO: Não foi possível inicializar o modelo Gemini Pro. Verifique sua chave API e conexão com a internet.")
    print(f"Detalhes: {e}")
    exit() # Sai do programa se o modelo não puder ser inicializado

# Start a chat session
chat = model.start_chat(history=[])

def get_chatbot_response(user_message):
    """
    Sends a user message to the chatbot and returns its response.
    Includes error handling for API calls.
    """
    try:
        response = chat.send_message(user_message)
        return response.text
    except Exception as e:
        print(f"ERRO ao enviar mensagem para o chatbot: {e}")
        return "Desculpe, tive um problema ao processar sua solicitação."

def main():
    print("Bem-vindo ao Chatbot do Google AI Studio!")
    print("Tipo 'exit' para encerrar a conversa.")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Adeus!")
            break

        chatbot_response = get_chatbot_response(user_input)
        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()