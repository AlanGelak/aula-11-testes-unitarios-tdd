# Registro do ciclo de TDD

## 1: 2km e pedido de R$ 50

Teste: `test_taxa_para_2_km`.

Red: a funcao estava com `pass` e retornou None, mas o teste esperava 5.
Resultado: 1 falhou e 4 passaram.

Green: coloquei `return 5`. Resultado: 5 testes passaram.

Refactor: nao foi necessario, pois o codigo estava simples.

## 2: 4km e pedido de R$ 50

Teste: `test_taxa_para_4_km`.

Red: a funcao retornou 5, mas o teste esperava 7.
Resultado: 1 falhou e 5 passaram.

Green: adicionei o calculo de R$ 2 por km acima de 3 km.
Resultado: 6 testes passaram.

Refactor: nao foi necessario.

## 3: 5km e pedido de R$ 100

Teste: `test_entrega_gratis_para_pedido_de_100`.

Red: a funcao retornou 9, mas o teste esperava 0.
Resultado: 1 falhou e 6 passaram.

Green: adicionei a verificacao de pedido maior ou igual a 100 antes de calcular a taxa.
Resultado: 7 testes passaram.

Refactor: revisei a funcao e mantive os dois `if`, pois nao precisava complicar.

## Resultado final

Os 4 testes originais e os 3 testes de entrega passaram.
O relatorio completo esta em `relatorio-testes.txt`.
