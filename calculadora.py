class CalculadoraBinariaError(Exception):
    pass

def validar_entrada(bin_str: str) -> None:
    """
    Valida se a entrada binária tem 8 bits e contém apenas 0 ou 1.
    Lança CalculadoraBinariaError com mensagem adequada em caso de erro.
    """
    if not isinstance(bin_str, str):
        raise CalculadoraBinariaError("valor invalido")

    if len(bin_str) != 8:
        raise CalculadoraBinariaError("tamanho da entrada invalido")

    if any(c not in ('0', '1') for c in bin_str):
        raise CalculadoraBinariaError("valor invalido")

def validar_operacao(op: str) -> None:
    """
    Valida se a operação é uma das permitidas: '+', '-', 'x'.
    """
    if op not in ('+', '-', 'x'):
        raise CalculadoraBinariaError("valor invalido")

def str_para_bits(bin_str: str) -> list[int]:
    """
    Converte string binária para lista de inteiros (bits).
    """
    return [int(b) for b in bin_str]

def bits_para_str(bits: list[int]) -> str:
    """
    Converte lista de bits para string binária.
    """
    return ''.join(str(b) for b in bits)

def soma(a: list[int], b: list[int]) -> list[int]:
    """
    Realiza soma de dois números binários de 8 bits com sinal (complemento de dois).
    Detecta overflow e levanta exceção se ocorrer.
    """
    resultado = [0] * 8
    carry = 0

    for i in range(7, -1, -1):
        total = a[i] + b[i] + carry
        resultado[i] = total % 2
        carry = total // 2

    # Detecta overflow: se os sinais de a e b forem iguais, mas diferente do resultado
    if (a[0] == b[0]) and (resultado[0] != a[0]):
        raise CalculadoraBinariaError("overflow")

    return resultado

def complemento_de_dois(bits: list[int]) -> list[int]:
    """
    Calcula o complemento de dois de um número binário.
    """
    invertido = [1 - bit for bit in bits]  # Complemento de um
    um = [0] * 7 + [1]                    # Representa o número 1
    return soma(invertido, um)

def bits_para_int(bits: list[int]) -> int:
    """
    Converte bits (8 bits) em inteiro com sinal (complemento de dois).
    """
    n = 0
    for b in bits:
        n = (n << 1) | b
    if bits[0] == 1:
        n -= 1 << 8  # Ajusta para número negativo
    return n

def int_para_bits(n: int) -> list[int]:
    """
    Converte inteiro com sinal para bits (8 bits) complemento de dois.
    """
    if n < 0:
        n = (1 << 8) + n
    bits = [(n >> i) & 1 for i in reversed(range(8))]
    return bits

def multiplicar(a: list[int], b: list[int]) -> list[int]:
    """
    Multiplica dois números binários de 8 bits com sinal (complemento de dois).
    Detecta overflow e levanta exceção se ocorrer.
    """
    int_a = bits_para_int(a)
    int_b = bits_para_int(b)
    int_res = int_a * int_b

    # Checa overflow - resultado deve caber em 8 bits com sinal
    if int_res < -128 or int_res > 127:
        raise CalculadoraBinariaError("overflow")

    return int_para_bits(int_res)

def calcular(n1: str, n2: str, operacao: str) -> str:
    """
    Função principal da calculadora.
    Valida entradas, executa a operação, detecta erros e retorna resultado binário.
    """
    # Validações rigorosas
    validar_entrada(n1)
    validar_entrada(n2)
    validar_operacao(operacao)

    a = str_para_bits(n1)
    b = str_para_bits(n2)

    if operacao == '+':
        resultado = soma(a, b)
    elif operacao == '-':
        complemento_b = complemento_de_dois(b)
        resultado = soma(a, complemento_b)
    else:  # operacao == 'x'
        resultado = multiplicar(a, b)

    return bits_para_str(resultado)

if __name__ == "__main__":
    print("=== Calculadora Binária (8 bits) ===")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        try:
            n1 = input("Digite o primeiro número binário (8 bits): ").strip()
            if n1.lower() == "sair":
                break

            n2 = input("Digite o segundo número binário (8 bits): ").strip()
            if n2.lower() == "sair":
                break

            op = input("Digite a operação (+, -, x): ").strip()
            if op.lower() == "sair":
                break

            resultado = calcular(n1, n2, op)
            print("Resultado:", resultado, "\n")

        except CalculadoraBinariaError as e:
            print(f"Erro: {e}\n")
        except Exception:
            print("Erro inesperado. Verifique as entradas e tente novamente.\n")
