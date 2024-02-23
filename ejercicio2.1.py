'''
Dadas las variables: product_name y quantity, complete la función
is_product_available con el siguiente objetivo:

- Buscar en un pandas DataFrame y devolver True si existe stock, False caso
contrario.
'''

import pandas as pd
from colorama import init, deinit, Fore

def show_products(list):
    print()
    print(Fore.MAGENTA + 'Los productos disponibles son:\n')
    init()
    print(Fore.GREEN + "-" * 25)
    print("Product Name:".ljust(25))
    print("-"*25 + Fore.RESET)
    deinit()
    for i, row in list.iterrows():
        print(f"{row['product_name'].ljust(25)}")


def is_product_available(product_name,product_df):
    available_products = product_df['product_name'].tolist()
    if product_name in available_products:
        quantity_available = product_df.loc[product_df['product_name'] == product_name, 'quantity'].values[0]
        return True
    else:
        return False


def main():
    _PRODUCT_DF = pd.DataFrame({"product_name": ["chocolate",
    "granizado", "limon", "dulce de leche"], "quantity":
    [3,10,0,5]})

    show_products(_PRODUCT_DF)
    print()
    print(is_product_available('granizado', _PRODUCT_DF))

if __name__ == '__main__':
    main()


