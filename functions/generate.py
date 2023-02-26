from eth_account.hdaccount import Mnemonic
from eth_account.signers.local import LocalAccount
from web3 import Web3

from data.config import MNEMONICS_FILE


def generate() -> None:
    try:
        number = int(input('Enter the number of mnemonics to generate: '))
        if number:
            w3 = Web3()
            w3.eth.account.enable_unaudited_hdwallet_features()
            headers = 'Mnemonic\tPrivate key\tAddress'
            wallets = ''
            for _ in range(number):
                mnemonic = Mnemonic().generate()
                account: LocalAccount = w3.eth.account.from_mnemonic(mnemonic)
                wallets += f'\n{mnemonic}\t{account.privateKey.hex()}\t{account.address}'

            with open(MNEMONICS_FILE) as f:
                file_text = f.read()

            text = file_text + wallets
            if not file_text:
                text = headers + text

            elif file_text.split('\n')[0] != headers:
                text = f'{headers}\n{text}'

            with open(MNEMONICS_FILE, mode='w') as file:
                file.write(text)

            print(f'\nDone! {number} mnemonics were generated and saved to the mnemonics.txt file.')

        else:
            print(f'You entered 0!')

    except ValueError:
        print(f"You didn't enter a number!")
