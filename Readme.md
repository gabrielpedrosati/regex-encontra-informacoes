# Regex - Encontrar informações pessoais em um arquivo de texto

## Sobre o Programa
 
  O programa abre um arquivo de texto e procura por expressões regulares criadas seguindo o formato brasileiro de telefone e cpf e por e-mail. E por fim printa na tela o que foi encontrado.

## Regex - Expressões Regulares

  Para a criação desse programa utilizei a biblioteca 're' que me auxilia na criação de expressões regulares - padrões de texto.
  
  Com a biblioteca 're' criei as expressões regulares para telefone, e-mail e cpf.
  
  Essas expressões são padrões que passamos para o programa procurar dentro de um texto. 
  
## Expressões regulares utilizadas neste programa

  #### Telefone:
  
    No Brasil o padrão é (xx) xxxxx-xxxx - entre parêntesis é o número do código de área, seguido de um dígito opcional que é o 9, e por fim o número de telefone. 
    
    Obs.: O número 8 aqui foi utilizado apenas como exemplo para simular um número real.
    
    Obs.2: O número de telefone pode ser escrito de diversas maneiras com código de área dentro de parêntesis ou sem parêntesis, sem código de área, com o número 9 na frente do número de telefone... existem n maneiras de se escrever um número de telefone.
    
    A regex do programa irá procurar por: (82) 98888-8888, 82 98888-8888, 98888-8888, 8888-8888.
    
   #### Cpf:
   
    No Brasil o padrão é xxx.xxx.xxx-xx. O regex do cpf é mais básico, pois não há muitas maneiras diferentes de se escrever um número de cpf.
   
   #### E-mail:
    O padrão que será procurado será: xxxx@xxx.xxx.xx
    
    Obs.: Os dois últimos dígitos são opcionais, caso haja um e-mail com o final '.com.br'.
