# NotPixTod

Auto paint and claim for N*t P*xel

# Table of Contents
- [NotPixTod](#notpixtod)
- [Table of Contents](#table-of-contents)
- [Registration](#registration)
- [Features](#features)
- [Support Me](#support-me)
- [Warning](#warning)
- [How to Use](#how-to-use)
  - [About Config.json](#about-configjson)
  - [Command Line Options / Arguments](#command-line-options--arguments)
  - [About Proxy](#about-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Thank You](#thank-you)

# Registration

Follow this link to register: [https://t.me/notpixel/app?startapp=f629438076](https://t.me/notpixel/app?startapp=f629438076)

# Features

- [x] Automatic Painting
- [x] Automatic Mining Claims
- [x] Automatic Boost Upgrades
- [x] Proxy Support
- [x] Uses fake user agent
- [x] Participate in balance event x3

# Support Me

If you like my work, you can support me through the following links:

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- If you want to send support in other forms, you can contact me via Telegram.

# Warning

This program uses third-party libraries to log into Telegram accounts.

According to Telegram's TOS, all accounts that register or log in using unofficial Telegram API clients will automatically be monitored to prevent violations of the Terms of Service.

So be careful, and hopefully your account won't get blocked.

All risks are borne by the user!

# How to Use

## About Config.json

Here's an explanation of the config.json contents:

| Keyword           | Description                                                                                                                                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_id            | To fill this key, you can register first at my.telegram.org/apps. This is not mandatory; you can use mine which is already stored in the `config.json.example` file                                                                                                                                 |
| api_hash          | To fill this key, you can register first at my.telegram.org/apps. This is not mandatory; you can use mine which is already stored in the `config.json.example` file                                                                                                                                 |
| referral_code     | Fill this key with your main account's invitation code                                                                                                                                                                                                                                              |
| colors            | Fill this key with a list of colors you want to apply to the canvas. You can get the color codes (hexcode) inside the Telegram bot (follow the existing format). You can watch this video to learn how to get hex colors from the bot: [https://youtu.be/r7qhx95gwVw](https://youtu.be/r7qhx95gwVw) |
| auto_upgrade      | this key is to activate the auto upgrade feature, inside there are several more keys, give value/fill `true` to activate it and give value/fill `false` to deactivate it.                                                                                                                           |
| countdown         | This key determines how long to wait for energy to fill up, fill this key with a positive value (in seconds)                                                                                                                                                                                        |
| time_before_start | This key is used to create random countdown times before starting the script, the key has 2 values that need to be filled [small,large], example as shown in the config itself (unit: seconds)                                                                                                      |

## Command Line Options / Arguments

This script/program also supports several argument parameters that can be used. Here's an explanation of the arguments:

`--proxy` / `-P` can be used when you have a different filename for storing the proxy list. The default filename used by this script/program to store proxy lists is `proxies.txt`. If you have a file named `prox.txt` as your proxy list file, you just need to add the `--proxy` / `-P` argument parameter to use your proxy file. Example: `python bot.py --proxy prox.txt`

`--worker` / `-W` this argument is used to customize the number of threads/workers used when the bot script runs. By default, this script/software uses (total CPU cores / 2) workers. For example, if your CPU has 6 cores, then the number of workers used is 3. You can customize the number of workers using this argument. For example, if you want to set the number of workers to 100, run `bot.py` with the argument like this: `python bot.py --worker 100`. And if you don't like using workers/threads/multiprocessing, you can customize the worker to 1, example: `python bot.py --worker 1`.

`--action` / `-A` this argument is used to directly enter the desired menu. For example, if this bot script has 5 menus and you don't want to input manually, you can use this argument to directly enter the desired menu. Example: `python bot.py --action 5` means you will directly enter menu number 5. This argument is useful if you use docker/pm2 to run the bot script in the background process.

## About Proxy

Register at the Following Websites to Get Free Proxy: [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website with cheapest proxy price $1/GB [Here](https://dataimpulse.com/?aff=48082)

You can add proxy lists in the `proxies.txt` file and the proxy format is as follows:

If there is authentication:

Format:
```
protocol://user:password@hostname:port
```

Example:
```
http://admin:admin@69.69.69.69:6969
```

If there is no authentication:

Format:
```
protocol://hostname:port
```

Example:
```
http://69.69.69.69:6969
```

Please carefully note whether the proxy you are using requires authentication or not, as many people DM me asking about how to use proxies.

Here's how to use it on different operating systems:

## Windows

1. Make sure your computer has Python and Git installed. If not, you can install them first

    Recommended Python version is 3.10

    Download Python: [https://python.org](https://python.org)

    Download Git: [https://git-scm.com](https://git-scm.com/)

2. Open Terminal/CMD

3. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

4. Enter the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

5. Install required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Copy `config.json.example` to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then adjust the config according to your preferences, you can see [About Config.json](#about-configjson) for the explanation.
   
   Follow one of the commands below and adjust according to your OS:
   
   Windows CMD/Powershell
   ```shell
   copy config.json.example config.json
   ```
   
   Linux/Unix
   ```shell
   cp config.json.example config.json
   ```

7. Run/execute the main file
   ```shell
   python bot.py
   ```

## Linux

1. Make sure your computer has Python and Git installed. If not, you can install them first

    Linux command to install Python and Git:
    ```shell
    sudo apt install python3 python3-venv python3-pip git -y
    ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

3. Enter the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

4. Create and activate virtual environment
   ```shell
   python3 -m venv env && source env/bin/activate
   ```

5. Install required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

6. Copy `config.json.example` to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then adjust the config according to your preferences, you can see [About Config.json](#about-configjson) for the explanation.

   Follow one of the commands below and adjust according to your OS:

   Windows CMD/Powershell
   ```shell
   copy config.json.example config.json
   ```

   Linux/Unix
   ```shell
   cp config.json.example config.json
   ```

7. Run the main file
   ```shell
   python bot.py
   ```

## Termux

1. Make sure Python and Git are installed in your Termux app. If not, install them first:
   ```shell
   pkg update -y && pkg upgrade -y && pkg install python git -y
   ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

3. Enter the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

4. Install required libraries
   ```shell
   python -m pip install -r requirements.txt
   ```

5. Copy `config.json.example` to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then adjust the config according to your preferences, you can see [About Config.json](#about-configjson) for the explanation.

   Follow one of the commands below and adjust according to your OS:

   Windows CMD/Powershell
   ```shell
   copy config.json.example config.json
   ```

   Linux/Unix
   ```shell
   cp config.json.example config.json
   ```

6. Run the main file
   ```shell
   python bot.py
   ```

# Thank You