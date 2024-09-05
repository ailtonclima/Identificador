Explicação do Código:

Função contar_as:

Recebe a string: A função recebe a string a ser analisada como parâmetro.
Converte para minúsculas: A função lower() converte toda a string para minúsculas, simplificando a contagem.
Conta as ocorrências: A função count('a') conta quantas vezes a letra 'a' aparece na string convertida.
Retorna o resultado: A função retorna a quantidade de ocorrências encontradas.
Exemplos de uso:

Exemplo 1: A string é definida diretamente no código.
Exemplo 2: A string é fornecida pelo usuário através da função input().
Como funciona:

A função contar_as é chamada com a string como argumento.
A string é convertida para minúsculas para garantir que tanto 'a' quanto 'A' sejam contabilizados.
A função count() retorna o número de ocorrências da letra 'a'.
O resultado é impresso na tela, junto com a string original.
Pontos-chave:

Eficiência: A função count() é otimizada para realizar a contagem de forma eficiente.
Flexibilidade: O código pode ser facilmente adaptado para contar outras letras ou caracteres.
Claridade: O código é bem comentado, facilitando a compreensão.
Personalizando o código:

Outras letras: Para contar outras letras, basta substituir 'a' na função count().
Maiúsculas e minúsculas separadas: Se quiser contar as ocorrências de 'a' e 'A' separadamente, remova a linha que converte a string para minúsculas.
Ignorar caracteres especiais: Para ignorar caracteres especiais, você pode usar expressões regulares.
