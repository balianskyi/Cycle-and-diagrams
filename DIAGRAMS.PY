# Solving the situation when a client want to pay for a service
# - trying to pay by cash
# - trying to pay by card
# - trying to pay by cryptocurrency

service_price = 100

client_cash_amount = int(input("Enter cash amount :"))
if client_cash_amount >= service_price:
    print("CASH Payment success!!!")
else:
    print("Cash payment FAILURE!!!")
    client_card_amount = int(input("Enter card amount :"))
    if client_card_amount >= service_price:
        print("CARD Payment succes")
    else:
        print("CARD Payment FAILURE!!!")
        client_card_crypto = int(input("Enter crypyo amount :"))
        if client_card_crypto >= service_price:
            print("CRYPTO Payment succes")
        else:
             print("CRYPTO Payment FAILURE!!!")