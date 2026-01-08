#Progrma 4.3 - Calculo_imposto_de_renda
salário = float(input("Digite o salário para o calculo do imposto de renda: "))
base = salário
imposto = 0 
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000)*0.20)
print(f"Salário: R${salário:6.2f} Imposto a pagar: R${imposto:6.2f}")
