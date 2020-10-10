CustosFixos = float(input('Custos fixos totais: ''\n'))
CustosVariaveis = float(input('Custos variáveis totais''\n'))

Lucro = float(input('Margem de lucro esperada: ''\n'))

Produzido = float(input('Quantidade produzida: ''\n'))

Tributos = float(input('Soma dos tributos: ''\n'))
Deprec = float(input('Custos de depreciação: ''\n'))
Oport = float(input('Custo de oportunidade: ''\n'))



Markup = lambda Tributos, Lucro: (1 - (Tributos + Lucro))
total = lambda custo, despesa: custo + despesa
unit = lambda total, produzido: total / produzido
contrib = lambda venda, varunit: venda - varunit

venda = unit(CustosVariaveis, Produzido) / Markup(Tributos, Lucro)
margem = contrib(venda, unit(CustosVariaveis, Produzido))

EqC = lambda fixos, ContMargem: fixos / ContMargem
EqE = lambda fixos, oportunidade, ContMargem: (fixos + oportunidade) / margem
EqF = lambda fixos, depreciacao, ContMargem: (fixos - depreciacao) / margem

print('Preço de venda: ', round(venda, 2))
print('Equilibrio Contábil: ', round(EqC(CustosFixos, margem)))
print('Equilibrio Econômico: ', round(EqE(CustosFixos, Oport, margem)))
print('Equilibrio Financeiro: ', round(EqF(CustosFixos, Deprec, margem)))

