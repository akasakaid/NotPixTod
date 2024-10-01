 
# NotPixTod

Auto paint and claim for N\*t P\*xel

# Table of Contents
- [NotPixTod](#notpixtod)
- [Table of Contents](#table-of-contents)
- [Registration](#registration)
- [Features](#features)
- [Support me](#support-me)
- [Warning](#warning)
- [How to use](#how-to-use)
  - [About Config.json](#about-configjson)
  - [Command Line Options / Command Line Arguments](#command-line-options--command-line-arguments)
  - [About Proxy](#about-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Thank you](#thank-you)

# Registration

Follow the following link to register: [https://t.me/notpixel/app?startapp=f629438076](https://t.me/notpixel/app?startapp=f629438076)

# Features

- [x] Automatic Paint
- [x] Automatic Mining Claims
- [x] Automatic Boost Upgrade
- [x] Support Proxy
- [x] Uses fake useragent

# Support me

If you like my work you can support me through the link below.

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- If you want to send in other forms, you can contact me via telegram.

# Warning

This program uses a 3rd party library to log into the telegram account.

According to Telegram's TOS, all accounts that register or log in using unauthorized Telegram API clients will automatically be monitored to avoid violating the Terms of Service.

So be careful, hopefully your account will not be banned.

All risks are borne by the user!

# How to use

## About Config.json

The following describes the contents of config.json

| Keywords          | Description                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_id            | to fill in this key, you can register first at my.telegram.org/apps                                                                                                                                             |
| api_hash          | to fill in this key can register first at my.telegram.org/apps                                                                                                                                                  |
| referral_code     | in this key fill in the invitation code of your main account                                                                                                                                                    |
| colors            | in this key, fill in the list of colors that you want to apply to the canvas, you can get the color code (hexcode) in the telegram bot (follow the existing format)                                             |
| auto_upgrade      | this key is to enable the auto upgrade feature, fill in true to enable it and to disable it                                                                                                                     |
| countdown         | this key to provide how long to wait to charge, this key is filled with positive values (units of seconds)                                                                                                      |
| time_before_start | this key is used to create a random launch time before starting to run the script, the key has 2 values that need to be filled in \[small, large\], for example as stated in the config itself (units: seconds) |

## Command Line Options / Command Line Arguments

This script / program also supports several parameter arguments that can be used, here is an explanation of the argument 

<!-- `--data` / `-D` can be used when you have different file names to store account data. By default the file name used by this script / program to store account data is `data.txt`, if you have a file called `query.txt` as a file that stores account data then just run `bot.py` by adding the argumetn `--data` / `-D`. Example `python bot.py --data query.txt` -->

`--proxy` / `-P` can be used when you have different file names to store the proxy list. The file name used by this script/program to store the proxy list is `proxies.txt`, suppose you have a file called `prox.txt` as the file that stores the proxy list, you just need to add the `--proxy` / `-P` parameter argument to be able to use your proxy file. Example `python bot.py --proxy prox.txt`

`--worker` / `-W` this argument serves to customize the number of threads / workers used when this bot script runs. By default this script / software the number of workers is (total cpu cores / 2), for example your cpu has 6 cores then the number of workers used is 3. You can customize the number of workers using this argument. For example you want to make the number of workers 100 then run `bot.py` with an argument like this `python bot.py --worker 100`. And if you don't like using workers / threads / multiprocessing then you can customize the worker to 1, for example `python bot.py --worker 1`.

`--action` / `-A` this argument serves to go directly to the intended menu, for example in this bot script there are 5 menus if you don't want to do manual input you can use this argument to go directly to the intended menu. Example: `python bot.py --action 5` in this example means you will go directly to menu number 5. This argument is useful if you use docker / pm2 to run bot scripts in the background process.

## About Proxy

Register at the following website to get a free proxy: [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website with the cheapest proxy price of $1/GB [Here](https://dataimpulse.com/?aff=48082)

You can add a list of proxies in the `proxies.txt` file and the proxy format is as follows:

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

Format :

```
protocol://hostname:port
```

Example:

```
http://69.69.69.69:6969
```

Please note carefully whether the proxy you are using must use authentication or not, because many people DM me asking how to use a proxy.

Here's how to use it in several operating systems

## Windows

1. Make sure your computer has python and git installed, if not you can install it first.

    Suggested python version is 3.10

    Download python: [https://python.org](https://python.org)

    Download Git : [https://git-scm.com](https://git-scm.com/)

2. Open Terminal/CMD

3. Clone this repository
   ``shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

4. Go to the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

5. Install the required library
   ```shell
   python -m pip install -r requiremens.txt
   ```

6. Copy the `config.json.example` file to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then customize the config according to your wishes, you can see [About Config.json](#about-configjson) for an explanation.
   
7. Run/execute the main file 
   ```shell
   python bot.py
   ```

## Linux

1. Make sure your computer has python and git installed, if not you can install them first.

    Linux command to install python and git

    ```shell
    sudo apt install python3 python3-venv python3-pip git -y
    ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

3. Go to the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

4. Create a virtual environment and activate it.
   
   ```shell
   python3 -m venv env && source env/bin/activate
   ```

5. Install the required libraries
   ```shell
   python -m pip install -r requiremens.txt
   ```

6. Copy the `config.json.example` file to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then customize the config according to your wishes, you can see [About Config.json](#about-configjson) for an explanation.
   
7. Run/execute the main file 
   ```shell
   python bot.py
   ```

## Termux

8. Make sure your termux application has python and git installed, if not you can install it first
   
   ```shell
   pkg update -y && pkg upgrade -y && pkg install python git -y
   ```

9. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/NotPixTod.git
   ```

10. Go to the NotPixTod folder
   ```shell
   cd NotPixTod
   ```

11. Install the required library
   ```shell
   python -m pip install -r requiremens.txt
   ```

12. Copy the `config.json.example` file to `config.json` or you can also rename the `config.json.example` file to `config.json`. Then customize the config according to your wishes, you can see [About Config.json](#about-configjson) for an explanation.
   
13. Run/execute the main file 
   ```shell
   python bot.py
   ```

# Thank you

