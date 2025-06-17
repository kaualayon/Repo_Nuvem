import os  # Biblioteca para interagir com o sistema operacional
import gradio as gr  # Interface web simples
from groq import Groq  # Cliente da API Groq

# Carrega a chave da API Groq da variável de ambiente
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Valida se a chave foi fornecida
if not GROQ_API_KEY:
    raise ValueError("❌ A variável de ambiente GROQ_API_KEY não foi definida!")

# Inicializa o cliente Groq
client = Groq(api_key=GROQ_API_KEY)

# Função que interage com o modelo da Groq
def assistente_agricultura(user_prompt):
    if user_prompt.strip() == "15":
        return "Encerrando assistente Agro! Até mais! 🚜"

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em agricultura."},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False
    )

    return completion.choices[0].message.content

# Interface Gradio
iface = gr.Interface(
    fn=assistente_agricultura,
    inputs=gr.Textbox(lines=2, placeholder="Digite sua pergunta sobre agricultura..."),
    outputs="text",
    title="🌾 Assistente Agro IA",
    description="Digite sua pergunta sobre agricultura e receba respostas de IA especializadas! 🚜",
    live=True
)

# Executa a interface web
if __name__ == "__main__":
    iface.launch()