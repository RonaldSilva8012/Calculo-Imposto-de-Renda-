# Cálculo de Imposto de Renda Progressivo 📑

Este é um script simples em Python desenvolvido para fins de estudo, que automatiza o cálculo do imposto de renda com base em faixas salariais progressivas.

## 🚀 Como funciona o código

O programa utiliza uma lógica de **tributação por fatias**. Em vez de aplicar uma alíquota única sobre o valor total, ele calcula o imposto de acordo com o excedente de cada faixa:

1.  **Entrada:** O usuário digita o valor do salário.
2.  **Faixa Superior (35%):** Aplica-se 35% sobre o valor que ultrapassa R$ 3.000,00.
3.  **Faixa Intermediária (20%):** Aplica-se 20% sobre o valor que ultrapassa R$ 1.000,00 (limitado à faixa anterior).
4.  **Saída:** Exibe o salário original e o total acumulado do imposto a pagar, formatado como moeda (R$).

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Estruturas de controle condicional (`if`)
* Formatação de strings com `f-strings`

## 📖 Exemplo de Execução

Se o salário for **R$ 3.500,00**:
* **35%** sobre os R$ 500,00 excedentes de R$ 3.000,00 = `R$ 175,00`
* **20%** sobre os R$ 2.000,00 (entre R$ 1.000 e R$ 3.000) = `R$ 400,00`
* **Total de Imposto:** `R$ 575,00`

---
