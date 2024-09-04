print('-'*30)
print('{: ^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)
total = maisdemil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip() [0]
    if escolha in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {maisdemil} produto(s) custando mais de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')

