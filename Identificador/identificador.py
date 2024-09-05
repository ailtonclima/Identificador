def contar_as(texto):
  """Conta a quantidade de letras 'a' (maiúsculas ou minúsculas) em uma string.

  Args:
    texto: A string a ser analisada.

  Returns:
    int: A quantidade de vezes que a letra 'a' aparece.
  """

  # Converte toda a string para minúsculas para facilitar a contagem
  texto_minusculo = texto.lower()

  # Conta as ocorrências da letra 'a'
  contagem = texto_minusculo.count('a')

  return contagem

# Exemplo 1: String definida no código
texto = "Olá, mundo! Como você está hoje?"
resultado = contar_as(texto)
print(f"A letra 'a' aparece {resultado} vezes em: {texto}")

# Exemplo 2: String fornecida pelo usuário
texto = input("Digite uma frase: ")
resultado = contar_as(texto)
print(f"A letra 'a' aparece {resultado} vezes em: {texto}")