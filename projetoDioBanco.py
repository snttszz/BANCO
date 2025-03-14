menu = """   
            BTG Pactual Digital

    Bem-vindo ao [BTG Pactual Digital]! 🚀  

Gerencie sua conta com segurança e praticidade. Escolha uma opção para continuar:  

[💰] Depósito (d)
[📓] Extrato (e)
[🔄] Saques (s)
[💳] Limites (l)
[💨] Sair (q)

Se precisar de ajuda, estamos aqui para você! 💙

Onde deseja ir: """


saldo = 0
extrato = " "
limite = 500
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        Valor = float(input("Informe o Valor do Depósito: "))

        if Valor > 0:
            saldo += Valor
            extrato += f"Depósito: R${Valor:.2f}"
        
        else:
            print("Depósito não concluído: o valor informado é inválido. Verifique e tente novamente.")

    
    elif opcao == "s":
        Valor = float(input("Informe o Valor para Saque: "))

        excedeu_saldo = Valor > saldo
        excedeu_limite = Valor > limite
        excedeu_saque = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente! O valor do saque excede o saldo disponível. Verifique seu saldo e tente novamente.")

        elif excedeu_saque:
            print("Limite de saques diários excedido! Você já atingiu o número máximo de saques permitidos para hoje.")

        elif excedeu_limite:
            print("Valor de retirada excedido! O montante solicitado ultrapassa o limite de retirada permitido.")

        elif Valor > 0:
            saldo -= Valor
            extrato += f"Saque: R${Valor:.2f}"

        else:
            print("Saque não concluído: o valor informado é inválido. Verifique e tente novamente.")

    
    elif opcao == "l":
        print(f"O seu limite de saque é de: R${limite}")

    elif opcao == "e":
        print("""
              ()()()()()()())()()()()()()()()()()()()()()()()()
              """)
        print("""
              📄 Extrato de Depósitos e Saques:
              """)
        print("""
              Não foram realizadas movimentações""" if not extrato else extrato)
        print(f"""
              💰 Saldo disponível: R${saldo}
              """)
        print("""
              Para mais detalhes, consulte seu extrato completo no app.
              """)
        print("""
              ()()()()()()())()()()()()()()()()()()()()()()()()
                """)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida! Verifique as informações e tente novamente.")
        