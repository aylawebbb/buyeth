from web3 import Web3
from uniswap import Uniswap

# Set up your web3 provider (Infura in this example)
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Replace these with your own wallet and private key
wallet_address = 'YOUR_WALLET_ADDRESS'
private_key = 'YOUR_PRIVATE_KEY'

# Set up Uniswap
uniswap = Uniswap(address=wallet_address, private_key=private_key)

def get_eth_price():
    eth_price = uniswap.get_eth_price()
    return eth_price

def place_uniswap_order(quantity, price):
    # Replace this with your own logic for placing a Uniswap order
    # Example: uniswap.swap_exact_tokens_for_tokens(quantity, price)
    # This is a simplified example, make sure to adapt it based on the Uniswap SDK documentation
    token_in = uniswap.WETH
    token_out = uniswap.USDC
    deadline = uniswap.deadline()
    
    tx_hash = uniswap.swap_exact_tokens_for_tokens(quantity, token_in, token_out, deadline, price)
    
    print(f"Placing Uniswap order to buy {quantity} ETH at ${price}...")
    print(f"Transaction Hash: {tx_hash}")

def main():
    print("Welcome to ETH Price Tracker!")

    target_price = float(input("Enter the target price for ETH: $"))
    buy_quantity = float(input("Enter the quantity of ETH to buy: "))

    while True:
        current_price = get_eth_price()
        print(f"Current ETH Price: ${current_price}")

        if current_price <= target_price:
            print(f"ETH has reached the target price of ${target_price}. Buying {buy_quantity} ETH on Uniswap!")
            place_uniswap_order(buy_quantity, target_price)
            break

if __name__ == "__main__":
    main()
