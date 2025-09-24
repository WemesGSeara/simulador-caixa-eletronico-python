# --- Simulador de Caixa Eletrônico (ATM) ---

# Mensagem de boas-vindas e menu
menu = """
================================
  BEM-VINDO AO BANCO DIGITAL
================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
================================
=> """

# Variáveis iniciais
saldo = 1500.00
limite_saque_diario = 500.00
extrato = ""
numero_saques_realizados = 0
LIMITE_DE_SAQUES = 3

# Loop principal do programa
while True:
    
    # Exibe o menu e captura a opção do usuário
    opcao = input(menu).lower()

    # --- Operação de Depósito ---
    if opcao == 'd':
        print("\n--- Depósito ---")
        try:
            valor_deposito = float(input("Informe o valor do depósito: R$ "))
            
            if valor_deposito > 0:
                saldo += valor_deposito
                # Adiciona a transação ao extrato
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um número válido.")

    # --- Operação de Saque ---
    elif opcao == 's':
        print("\n--- Saque ---")
        try:
            valor_saque = float(input("Informe o valor do saque: R$ "))

            # Validações
            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite_saque_diario
            excedeu_saques = numero_saques_realizados >= LIMITE_DE_SAQUES

            if excedeu_saldo:
                print(f"Operação falhou! Você não tem saldo suficiente. Saldo atual: R$ {saldo:.2f}")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite diário de R$ {limite_saque_diario:.2f}.")
            elif excedeu_saques:
                print(f"Operação falhou! Número máximo de {LIMITE_DE_SAQUES} saques diários excedido.")
            elif valor_saque > 0:
                saldo -= valor_saque
                # Adiciona a transação ao extrato
                extrato += f"Saque:     R$ {valor_saque:.2f}\n"
                numero_saques_realizados += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso! Retire o dinheiro na boca do caixa.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um número válido.")
            
    # --- Operação de Extrato ---
    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        # Verifica se houve alguma transação
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")

    # --- Sair do Programa ---
    elif opcao == 'q':
        print("Obrigado por usar nosso banco. Volte sempre!")
        break
    

    # --- Opção Inválida ---
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")