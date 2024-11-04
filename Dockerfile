
FROM python:3.10

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/code:/code"

# Define o diretório de trabalho
WORKDIR /code

# Copia o arquivo de requisitos

# Instala as dependências do apk e do pip

COPY . .

