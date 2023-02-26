import logging

from functions.create_files import create_files
from data.models import ProgramAction
from functions.generate import generate
from functions.retrieve import retrieve

if __name__ == '__main__':
    create_files()
    while True:
        action = None
        print('''Select the action:
1) Generate mnemonics;
2) Retrieve private keys and addresses from mnemonics or private keys;
3) Exit.''')
        try:
            action = int(input('> '))
            if action == ProgramAction.Generate:
                generate()

            elif action == ProgramAction.Retrieve:
                retrieve()

            else:
                break

        except KeyboardInterrupt:
            pass

        except ValueError:
            print(f"You didn't enter a number!")

        except:
            logging.exception('main')
            print(f'\nSomething went wrong!\n')

        if action:
            input(f'\nPress Enter to exit.\n')
            break
