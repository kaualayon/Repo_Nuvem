#Dockerfile é a arquitetura da solução
# Usa imagem base oficial do Python
FROM python:3.11-slim

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractiveS

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Define a variável para o Gradio escutar em todas as interfaces
ENV GRADIO_SERVER_NAME=0.0.0.0

# Expõe a porta do Gradio
EXPOSE 7860

# Comando para rodar o app
CMD ["python", "main.py"]