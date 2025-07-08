# generator/services.py

import google.generativeai as genai
from django.conf import settings

# --- Lembrete Importante ---
# Este código depende de duas coisas:
# 1. Que você instalou o pacote: pip install google-generativeai
# 2. Que você adicionou sua chave no settings.py: GEMINI_API_KEY = "SUA_CHAVE_AQUI"

# É uma boa prática configurar a API aqui.
# O try/except evita que o servidor quebre ao iniciar se a chave ainda não existir.
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
except AttributeError:
    pass 

def generate_content_from_gemini(prompt: str) -> str:
    """
    Função que envia um prompt para a API do Gemini e retorna o texto gerado.
    """
    # Segurança: Se a API key não estiver configurada, retorna um erro amigável.
    if not hasattr(settings, 'GEMINI_API_KEY') or not settings.GEMINI_API_KEY:
        return "ERRO: A chave da API do Gemini (GEMINI_API_KEY) não foi configurada no arquivo settings.py."

    try:
        # Usando um modelo rápido, eficiente e moderno.
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Em caso de qualquer outro erro com a API (chave inválida, problema de rede, etc.),
        # retorna uma mensagem clara em vez de quebrar a aplicação.
        return f"Ocorreu um erro ao contatar a API do Gemini: {e}"