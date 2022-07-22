# Projeto Regex - Encontrar telefone, cpf e e-mail em um documento

# Importando biblioteca
import re

# Criando a regex do telefone - (xx) xxxxx-xxxx
phone_regex = re.compile(r'''(
(\d{2}|\(\d{2}\))? #Códio de área (opcional)
(\s)? #Separador espaço
(\d)? #Dígito 9 (opcional)
(\d{4}) #Primeiros 4 dígitos
(\s|-|\.) # Separador
(\d{4}) #Últimos 4 dígitos
)''', re.VERBOSE)

# Criando a regex do e-mail - xxx@xxx.xxx
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #nome usuario
@ #@
[a-zA-Z0-9.-]+ #Nome domínio
\.[a-zA-Z]{2,4} #. seguido de outros caracteres
(\.[a-zA-Z]{2,4})? #. seguido de outros caracteres (opcional)
)''', re.VERBOSE)

# Criando a regex do cpf - xxx.xxx.xxx-xx
cpf_regex = re.compile(r'''(
(\d{3}) # 3 primeiros dígitos
\. #ponto
(\d{3}) # 3 dígitos
\. # ponto
(\d{3}) # 3 dígitos
\- #hífen 
(\d{2}) # 2 últimos dígitos
)''', re.VERBOSE)

# Variáveis
emails = []
telefones = []
cpfs = []
informacoes = {'telefones': '', 'emails': '', 'cpfs': ''}

# Abrindo arquivo

with open(r'C:\Users\DELL\Desktop\documento.txt', 'r') as file:

    # Pegando os telefones
    for item in phone_regex.findall(file.read()):
        telefones.append(item[0])

    # Retornando cursor do arquivo para início do arquivo
    file.seek(0)
    # Pegando os e-mails
    for item in email_regex.findall(file.read()):
        emails.append(item[0])

    # Retornando cursor do arquivo para início do arquivo
    file.seek(0)
    # Pegando o cpf
    for item in cpf_regex.findall(file.read()):
        cpfs.append(item[0])
