import re

from eth_account.signers.local import LocalAccount
from web3 import Web3

from data.config import MNEMONICS_FILE
from functions.utils.read_lines import read_lines


def retrieve():
    rows = read_lines(MNEMONICS_FILE, True)
    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    retrieved = 0
    text = 'Mnemonic\tPrivate key\tAddress'
    if rows[0] == text:
        rows = rows[1:]

    for row in rows:
        mnemonic = row.split('\t')[0]
        if re.match((r'\w+ ' * 12)[:-1], mnemonic):
            account: LocalAccount = w3.eth.account.from_mnemonic(mnemonic)
            text += f'\n{mnemonic}\t{account.privateKey.hex()}\t{account.address}'
            retrieved += 1

        elif re.match(r'\w' * 64, mnemonic):
            account: LocalAccount = w3.eth.account.from_key(mnemonic)
            text += f'\n\t{account.privateKey.hex()}\t{account.address}'
            retrieved += 1

        else:
            text += '\n' + mnemonic

    with open(MNEMONICS_FILE, mode='w') as file:
        file.write(text)

    print(f'\nDone! {retrieved}/{len(rows)} private keys and addresses were retrieved '
          f'and saved to the mnemonics.txt file.')
