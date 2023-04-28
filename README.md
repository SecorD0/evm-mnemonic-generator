<h1><p align="center">eth-mnemonic-generator</p></h1><h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker](#Docker)
    - [Source code](#Source-code)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program has no injections — you can make the code review to make sure. Any cases of third parties gaining access to your wallet aren't the fault of the developer, but of you or another person. Keep your sensitive data in a safe place.

⠀By using this program you have agreed to the above and have no and won't have claims against its developer.


<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to:
- Generate a specified number of mnemonics;
- Retrieve private keys and addresses from mnemonics or private keys.  



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[eth-mnemonic-generator](https://github.com/SecorD0/eth-mnemonic-generator)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `errors.log` — a log file with errors that occurred during the work;
  - `mnenonics.txt` — a text file with generated mnemonics or inserted mnemonics or private keys.
- `eth-mnemonic-generator.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/eth-mnemonic-generator/releases).
2. Create a folder and put the EXE file in it.
3. Run the program.
4. Follow the steps depending on your goal:
   - Generate:
      - Enter `1` and press `Enter`;
      - Enter the number of wallets to generate and press `Enter`.
   - Retrieve private keys and addresses:
     - Insert mnemonics or private keys into the `mnemonics.txt` file;
     - Enter `2` and press `Enter`.
5. Open the `mnemonics.txt` file to look at the result of the program.


<h2><p align="center">Docker</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run container from image:
```sh
docker run -it --rm -v $HOME/eth-mnemonic-generator:/program/files --name eth-mnemonic-generator ghcr.io/SecorD0/eth-mnemonic-generator:main
```

**OR** you can create the image manually.
1. Clone the repository:
```sh
git clone https://github.com/SecorD0/eth-mnemonic-generator
```
2. Go to the repository:
```sh
cd eth-mnemonic-generator
```
3. Build an image:
```sh
docker build -t eth-mnemonic-generator .
```
4. Run the program.
```sh
docker run -it --rm -v $HOME/eth-mnemonic-generator/:/program --name eth-mnemonic-generator eth-mnemonic-generator
```
5. Follow the steps depending on your goal:
   - Generate:
      - Enter `1` and press `Enter`;
      - Enter the number of wallets to generate and press `Enter`.
   - Retrieve private keys and addresses:
     - Insert mnemonics or private keys into the `mnemonics.txt` file;
     - Enter `2` and press `Enter`.
6. Open the `mnemonics.txt` file to look at the result of the program.


<h2><p align="center">Source code</p></h2>

1. Install [Python](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/eth-mnemonic-generator
```
3. Go to the repository:
```sh
cd eth-mnemonic-generator
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py`.
7. Follow the steps depending on your goal:
   - Generate:
      - Enter `1` and press `Enter`;
      - Enter the number of wallets to generate and press `Enter`.
   - Retrieve private keys and addresses:
     - Insert mnemonics or private keys into the `mnemonics.txt` file;
     - Enter `2` and press `Enter`.
8. Open the `mnemonics.txt` file to look at the result of the program.


⠀If you want to build the EXE file by yourself, use the command:
```sh
pyinstaller app.py -Fn eth-mnemonic-generator -i images/icons/app.ico --add-binary "images/icons;images/icons" --add-binary "data\wordlist;eth_account\hdaccount\wordlist"
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/eth-mnemonic-generator/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
