# Ponto_de_Equilibrio_Contabil
Script simples para cálculo do preço de venda de um determinado produto e ponto de equilíbrio baseado nos custos de produção


Este script utiliza-se das fórmulas amplamente difundidas pela contabilidade de custos para dispor-se como ferramenta de 
automação no cálculo de do preço de venda de um respectivo produto baseado nos seus custos de produção. Ao executa-lo, as
seguintes informações serão solicitadas: 

**Custos fixos** = Todo e qualquer custo produção que tem custos independentes do nível de atividade da empresa. Qualquer que seja
a quantidade produzida ou vendida, mesmo que seja zero, os custos fixos se mantêm os mesmos. 

**Custos variáveis** =  Soma dos fatores variáveis de produção. Custos que mudam de acordo com a produção ou a quantidade de trabalho, 
exemplos incluem o custo de materiais, suprimentos.

**Margem de lucro esperada** = Insira aqui, em valores decimais, quantos % do valor final de venda você deseja que seja revertido em 
lucro para empresa, exemplo: Se desejo uma margem de lucro de 30%, colocarei neste campo o valor 0.3 .
9Us

**Quantidade produzida** = Quantas unidades do produto correspondem aos custos que foram inseridos acima.

**Soma dos tributos** = valor, em decimais, correspondente à soma de todos os tributos incidentes sobre o produto. 
Exemplo: se incidem sobre o produto  ICMS de 18,00%, PIS e COFINS num total de 4,65% e comissões de 2,50%, o valor 
total dos tributos será de 45,15%, logo, deve-se inserir 0.4515 .

**Custos de depreciação** = A depreciação ou desvalorização é o custo ou a despesa da obsolescência dos ativos imobilizados, 
como por exemplo máquinas, veículos, móveis, imóveis ou instalações. É um fenômeno contábil, que indica a redução de valor 
de um bem tangível em decorrência de uso, natureza ou obsolescência.

**Custo de oportinidade** = Custo relacionado à quanto hipoteticamente seria ganho, caso todo o dinheiro relacionado a produção 
estivesse empregado à outra atividade que fosse livre de risco. Exemplo: Se todo o dinheiro aplicado na produção de um produto
ao longo do mês estivesse em uma aplicação de renda fixa, teria me rendido R$ 20.000,00 (vinte e cinco mil reais), o meu custo 
de oportunidade seria de 25000.


Após inseridos todos os dados, o script retornará os seguintes resultados: 

**Preço de venda** = O preço de venda mínimo baseado nas informações apresentadas.

**Ponto de equilibrio contábil** = Quantidade mínima a partir da qual a empresa começa a ter lucro efetivamente.
**Ponto de equilibrio econômico** = Quantiade minima a partir da qual o lucro da empresa superará o custo de oportunidade.
**Ponto de equilibrio financeiro** = Quantiade minima de unidades a serem vendidas para conseguir pagar os custos imediatos da empresa.




