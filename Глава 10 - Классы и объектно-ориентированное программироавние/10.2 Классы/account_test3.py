import bankaccount
import bankaccount2

def main():
    account1 = bankaccount.BankAccount(1000)
    account2 = bankaccount2.BankAccount(1200)
    account2.deposit(1500)
    account2.withdraw(2700)
    print(account1)
    print(account2)


if __name__ == '__main__':
    main()