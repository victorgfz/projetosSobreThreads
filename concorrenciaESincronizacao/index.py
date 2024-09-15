import threading
import queue
import time

bankBalance = 100
name = "Lucas Lopes"
dateOfBirth = "29/08/2002"
generous = "Masculino"
Cpf = "793.256.525-10"
countNumber = "544544"

balance_update_queue = queue.Queue()

def menu():
    global bankBalance
    
    producer_thread = threading.Thread(target=produce_balance_updates)
    
    consumer_thread = threading.Thread(target=consume_balance_updates)
    
    producer_thread.daemon = True
    
    consumer_thread.daemon = True
    
    producer_thread.start()
    
    consumer_thread.start()

    while True:
        print("\n--- BankNow ---")
        print("1. Informações Pessoais")
        print("2. Saldo")
        print("3. Depositar")
        print("4. Saque")
        print("5. Sair")

        opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")

        if opcao == "1":
            printInfo(name, dateOfBirth, generous, Cpf, countNumber)
        elif opcao == "2":
            printSaldo(bankBalance)
        elif opcao == "3":
            try:
                newValue = float(input("Quanto você deseja depositar? : R$ "))
                if newValue > 0:
                    bankBalance += newValue
                    printSaldo(bankBalance)
                else:
                    print("O valor do depósito deve ser positivo.")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        elif opcao == "4":
            try:
                newValue = float(input("Quanto você deseja sacar? : R$ "))
                if newValue > bankBalance:
                    print("Você não tem esse valor!")
                elif newValue > 0:
                    bankBalance -= newValue
                    printSaldo(bankBalance)
                else:
                    print("O valor do saque deve ser positivo.")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

def produce_balance_updates():
    while True:
        time.sleep(10) 
        balance_update_queue.put(0.01)  
        
def consume_balance_updates():
    global bankBalance
    while True:
        update_value = balance_update_queue.get() 
        if update_value is not None:
            bankBalance *= 1 + update_value  
        balance_update_queue.task_done()  

def printInfo(name, dateOfBirth, generous, CPF, countNumber):
    print("\n+" + "-" * 40 + "+")
    print("|{:^40}|".format("Informações Pessoais"))
    print("+" + "-" * 40 + "+")
    print(f"| Nome Completo: {name:<23} |")
    print(f"| Data De Nascimento: {dateOfBirth:<18} |")
    print(f"| Gênero: {generous:<30} |")
    print(f"| CPF: {CPF:<33} |")
    print(f"| Número da Conta: {countNumber:<21} |")
    print("+" + "-" * 40 + "+")

def printSaldo(value):
    print("\n+" + "-" * 40 + "+")
    print("|{:^40}|".format("Saldo Da Sua Conta"))
    print("+" + "-" * 40 + "+")
    print(f"| Saldo: R${value:<29.2f} |")
    print("+" + "-" * 40 + "+")

menu()
