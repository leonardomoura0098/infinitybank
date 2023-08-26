from banco import obterConta, banco


def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('Transferencia realizada com sucesso!')
        else:
            print('Saldo insuficiente para transferência!')
    else:
        print('Uma ou mais conta não encontradas!')



