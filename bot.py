import os
import re
import sys
import json
import anyio
import httpx
import random
import argparse
import asyncio
import platform
import aiofiles
import aiofiles.ospath
import python_socks
from glob import glob
from urllib.parse import unquote, parse_qs
from telethon import TelegramClient
from telethon.tl.types import InputBotAppShortName
from telethon.tl.functions.messages import RequestAppWebViewRequest
from telethon.errors import (
    SessionPasswordNeededError,
    UserDeactivatedBanError,
    UserDeactivatedError,
    PhoneNumberBannedError,
)
from colorama import init, Fore, Style
from datetime import datetime
from pathlib import Path
from models import *
from fake_useragent import UserAgent
from httpx_socks import AsyncProxyTransport

init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX
proxy_file = "proxies.txt"
log_file = "http.log"
ses_dir = "sessions"


class Config:
    def __init__(
        self,
        api_id,
        api_hash,
        colors,
        countdown,
        start_param,
        auto_upgrade,
        swtime,
        ewtime,
        disable_log,
    ):
        self.api_id = api_id
        self.api_hash = api_hash
        self.colors = colors
        self.countdown = countdown
        self.start_param = start_param
        self.auto_upgrade = auto_upgrade
        self.swtime = swtime
        self.ewtime = ewtime
        self.disable_log = disable_log


class NotPixTod:
    def __init__(self, no, config, proxies):
        self.cfg: Config = config
        self.p = no
        self.proxies = proxies
        if len(proxies) > 0:
            proxy = self.get_random_proxy(no)
            transport = AsyncProxyTransport.from_url(proxy)
            self.ses = httpx.AsyncClient(transport=transport, timeout=1000)
        else:
            self.ses = httpx.AsyncClient(timeout=1000)

    def log(self, msg):
        now = datetime.now().isoformat().split("T")[1].split(".")[0]
        print(
            f"{black}[{now}]{white}-{blue}[{white}acc {self.p + 1}{blue}]{white} {msg}{reset}"
        )

    async def ipinfo(self):
        ipinfo1_url = "https://ipapi.co/json/"
        ipinfo2_url = "https://ipwho.is/"
        ipinfo3_url = "https://freeipapi.com/api/json"
        headers = {"user-agent": "marin kitagawa"}
        try:
            res = await self.http(ipinfo1_url, headers)
            ip = res.json().get("ip")
            country = res.json().get("country")
            if not ip:
                res = await self.http(ipinfo2_url, headers)
                ip = res.json().get("ip")
                country = res.json().get("country_code")
                if not ip:
                    res = await self.http(ipinfo3_url, headers)
                    ip = res.json().get("ipAddress")
                    country = res.json().get("countryCode")
            self.log(f"{green}ip : {white}{ip} {green}country : {white}{country}")
        except json.decoder.JSONDecodeError:
            self.log(f"{green}ip : {white}None {green}country : {white}None")

    def get_random_proxy(self, isself, israndom=False):
        if israndom:
            return random.choice(self.proxies)
        return self.proxies[isself % len(self.proxies)]

    async def http(self, url, headers, data=None):
        while True:
            try:
                if not self.cfg.disable_log:
                    if not await aiofiles.ospath.exists(log_file):
                        async with aiofiles.open(log_file, "w") as w:
                            await w.write("")
                    logsize = await aiofiles.ospath.getsize(log_file)
                    if logsize / 1024 / 1024 > 1:
                        async with aiofiles.open(log_file, "w") as w:
                            await w.write("")
                if data is None:
                    res = await self.ses.get(url, headers=headers)
                elif data == "":
                    res = await self.ses.post(url, headers=headers)
                else:
                    res = await self.ses.post(url, headers=headers, data=data)
                if not self.cfg.disable_log:
                    async with aiofiles.open(log_file, "a", encoding="utf-8") as hw:
                        await hw.write(f"{res.status_code} {res.text}\n")
                if "<title>" in res.text or "upstream request timeout" in res.text or "upstream connect error or disconnect/reset" in res.text:
                    self.log(f"{yellow}failed get json response !")
                    await countdown(3)
                    continue

                return res
            except (
                httpx.ProxyError,
                python_socks._errors.ProxyTimeoutError,
                python_socks._errors.ProxyError,
                python_socks._errors.ProxyConnectionError,
            ):
                proxy = self.get_random_proxy(0, israndom=True)
                transport = AsyncProxyTransport.from_url(proxy)
                self.ses = httpx.AsyncClient(transport=transport)
                self.log(f"{yellow}proxy error,selecting random proxy !")
                await asyncio.sleep(3)
                continue
            except httpx.NetworkError:
                self.log(f"{yellow}network error !")
                await asyncio.sleep(3)
                continue
            except httpx.TimeoutException:
                self.log(f"{yellow}connection timeout !")
                await asyncio.sleep(3)
                continue
            except httpx.RemoteProtocolError:
                self.log(f"{yellow}connection close without response !")
                await asyncio.sleep(3)
                continue
            except Exception as e:
                self.log(f"{yellow}{e}")
                await asyncio.sleep(3)
                continue

    async def telegram_login(self, phone, proxy=None, return_data=False):
        if not os.path.exists(ses_dir):
            os.makedirs(ses_dir)
        if return_data:
            wtime = random.randint(self.cfg.swtime, self.cfg.ewtime)
            await countdown(wtime)
        if proxy:
            split = proxy.split("://")
            proxy_type = split[0]
            auth = split[1].split("@")
            proxy_user = auth[0].split(":")[0]
            proxy_pass = auth[0].split(":")[1]
            proxy_host = auth[1].split(":")[0]
            proxy_port = int(auth[1].split(":")[1])
            proxy = {
                "proxy_type": proxy_type,
                "addr": proxy_host,
                "port": proxy_port,
                "username": proxy_user,
                "password": proxy_pass,
            }
        bot_username = "notpixel"
        client = TelegramClient(
            session=f"{ses_dir}/{phone}",
            api_id=self.cfg.api_id,
            api_hash=self.cfg.api_hash,
            app_version="SDSProject O.R.G",
            device_model=f"{platform.python_implementation()} {platform.python_version()}",
            system_version=f"{platform.system()} {platform.release()}",
            proxy=proxy,
        )
        try:
            await client.connect()
            if not await client.is_user_authorized() and return_data:
                self.log(f"{yellow}{phone} is not authorized !")
                return None
            if not await client.is_user_authorized():
                try:
                    result = await client.send_code_request(phone=phone)
                    code = input(
                        f"{white}[{yellow}?{white}] {yellow}input login code : {reset}"
                    )
                    await client.sign_in(
                        phone=phone, code=code, phone_code_hash=result.phone_code_hash
                    )
                except SessionPasswordNeededError:
                    twofa = input(
                        f"{white}[{yellow}?{white}] {yellow}input 2fa password : {reset}"
                    )
                    await client.sign_in(phone=phone, password=twofa)
            me = await client.get_me()
            uid = me.id
            first_name = me.first_name
            last_name = me.last_name
            username = me.username
            res = await get_by_id(uid)
            if not res:
                await insert(uid, first_name)
                ua = UserAgent().random
                await update_useragent(uid, ua)
            self.log(f"{green}login as {white}{first_name} {last_name}")
            data = True
            if return_data:
                result = await client(
                    RequestAppWebViewRequest(
                        peer=bot_username,
                        app=InputBotAppShortName(
                            bot_id=await client.get_input_entity(peer=bot_username),
                            short_name="app",
                        ),
                        platform="android",
                        write_allowed=True,
                        start_param=self.cfg.start_param,
                    )
                )
                data = unquote(
                    result.url.split("#tgWebAppData=")[1].split("&tgWebAppVersion=")[0]
                )
            if client.is_connected():
                await client.disconnect()
            return data
        except (UserDeactivatedBanError, UserDeactivatedError, PhoneNumberBannedError):
            self.log(f"{white}{phone}{red}account/phone has banned from telegram !")
            return None

    def marinkitagawa(self, phone):
        x = "".join(filter(str.isdigit, phone))
        s = sum(int(_) for _ in x)
        return s % len(self.proxies)

    async def start(self, phone):
        proxy = None
        if len(self.proxies) > 0:
            unique = self.marinkitagawa(phone=phone)
            proxy = self.proxies[unique]
            await self.ipinfo()
        query = await self.telegram_login(phone=phone, proxy=proxy, return_data=True)
        if query is None:
            return
        marin = lambda data: {key: value[0] for key, value in parse_qs(data).items()}
        parser = marin(query)
        user = parser.get("user")
        uid = re.search(r'id":(.*?),', user).group(1)
        res = await get_by_id(uid)
        useragent = res.get("useragent")
        headers = {
            "accept": "application/json, text/plain, */*",
            "authorization": f"initData {query}",
            "user-agent": useragent,
            "origin": "https://app.notpx.app",
            "x-requested-with": "org.telegram.messenger",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.notpx.app/",
            "accept-language": "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
        }
        me_url = "https://notpx.app/api/v1/users/me"
        status_url = "https://notpx.app/api/v1/mining/status"
        paint_url = "https://notpx.app/api/v1/repaint/start"
        claim_url = "https://notpx.app/api/v1/mining/claim"
        boost_buy_url = "https://notpx.app/api/v1/mining/boost/check/"
        boosts = ["energyLimit", "paintReward", "reChargeSpeed"]
        res = await self.http(me_url, headers)
        while True:
            res = await self.http(status_url, headers)
            balance = res.json().get("userBalance", 0)
            await update_balance(uid, balance)
            self.log(f"{green}account balance : {white}{balance}")
            charges = res.json().get("charges")
            if charges <= 0:
                break
            for i in range(charges):
                pixel_id = random.randint(1, 1000000)
                new_color = random.choice(self.cfg.colors)
                data = {"pixelId": pixel_id, "newColor": new_color}
                res = await self.http(paint_url, headers, json.dumps(data))
                if res.status_code != 200:
                    self.log(f"failed paint pixel id : {white}{pixel_id}")
                    continue
                self.log(f"{green}success paint pixel id : {white}{pixel_id}")
                await countdown(3)
        res = await self.http(claim_url, headers)
        if res.status_code != 200:
            self.log(f"{yellow}failed claim mining !")
        else:
            claimed = res.json().get("claimed")
            self.log(f"{green}success claim mining, {white}{claimed}")
        if self.cfg.auto_upgrade:
            self.log(f"{yellow}auto buy boost is enable !")
            for boost in boosts:
                buy_url = f"{boost_buy_url}{boost}"
                res = await self.http(buy_url, headers)
                if res.status_code != 200:
                    self.log(f"{red}failed buy booster {white}{boost}")
                    continue
                self.log(f"{green}success buy booster {white}{boost}")


def get_sessions():
    return glob(f"{ses_dir}/*.session")


def get_datas(proxy_file):
    if not os.path.exists(proxy_file):
        open(proxy_file, "a")
    proxies = open(proxy_file).read().splitlines()
    return proxies


async def bound(sem, data, phone):
    async with sem:
        return await NotPixTod(*data).start(phone)


async def main():
    await initdb()
    arg = argparse.ArgumentParser()
    arg.add_argument(
        "--proxy",
        "-P",
        default=proxy_file,
        help=f"Perform custom input for proxy files (default : {proxy_file})",
    )
    arg.add_argument(
        "--action",
        "-A",
        help="Function to directly enter the menu without displaying input",
    )
    arg.add_argument(
        "--worker",
        "-W",
        help="Total workers or number of threads to be used (default : cpu core / 2)",
    )
    arg.add_argument("--marin", action="store_true")
    arg.add_argument("--disable-log", action="store_true")
    args = arg.parse_args()
    disable_log = args.disable_log
    async with aiofiles.open("config.json") as r:
        read = await r.read()
        cfg = json.loads(read)
        config = Config(
            api_id=cfg.get("api_id"),
            api_hash=cfg.get("api_hash"),
            colors=cfg.get("colors"),
            countdown=cfg.get("countdown"),
            start_param=cfg.get("referral_code"),
            auto_upgrade=cfg.get("auto_upgrade"),
            swtime=cfg.get("time_before_start", [30, 60])[0],
            ewtime=cfg.get("time_before_start", [30, 60])[1],
            disable_log=disable_log,
        )
    banner = f"""
{magenta}┏┓┳┓┏┓  ┏┓    •      {white}NotPixTod Auto Claim for {green}N*t P*xel
{magenta}┗┓┃┃┗┓  ┃┃┏┓┏┓┓┏┓┏╋  {green}Author : {white}[redacte]
{magenta}┗┛┻┛┗┛  ┣┛┛ ┗┛┃┗ ┗┗  {green}Note : {white}Every Action Has a Consequence
{magenta}              ┛      
        """
    main_menu = f"""
    {white}1{green}. {white}Add/Create Session 
    {white}2{green}. {white}Start Bot (Multi Process)
    {white}3{green}. {white}Start Bot (Single Process)
    """
    sessions = get_sessions()
    proxies = get_datas(proxy_file=args.proxy)
    your_data = f"""
{white}Total session : {green}{len(sessions)}
{white}Total proxy : {green}{len(proxies)}
        """
    while True:
        if not args.marin:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)
        print(your_data)
        if args.action:
            option = args.action
        else:
            print(main_menu)
            option = input(f"{white}[{yellow}?{white}] {yellow}input number : {reset}")
        if option == "1":
            phone = input(
                f"{white}[{yellow}?{white}] {yellow}input phone number : {reset}"
            )
            proxy = None
            x = NotPixTod(no=0, config=config, proxies=proxies)
            if len(proxies) > 0:
                unique = x.marinkitagawa(phone=phone)
                proxy = proxies[unique]
                transport = AsyncProxyTransport.from_url(proxy)
                x.ses = httpx.AsyncClient(transport=transport, timeout=1000)
                await x.ipinfo()
            await x.telegram_login(phone=phone, proxy=proxy, return_data=False)
            input(f"{blue}press enter to continue !")
            continue
        elif option == "2":
            if args.worker:
                worker = int(args.worker)
            else:
                worker = int(os.cpu_count() / 2)
                if worker <= 0:
                    worker = 1
            sema = asyncio.Semaphore(worker)
            while True:
                sessions = get_sessions()
                proxies = get_datas(proxy_file=args.proxy)
                tasks = [
                    asyncio.create_task(
                        bound(sema, (no, config, proxies), Path(phone).stem)
                    )
                    for no, phone in enumerate(sessions)
                ]
                result = await asyncio.gather(*tasks)
                await countdown(config.countdown)
        elif option == "3":
            while True:
                sessions = get_sessions()
                proxies = get_datas(proxy_file=args.proxy)
                for no, phone in enumerate(sessions):
                    await NotPixTod(no=no, config=config, proxies=proxies).start(
                        phone=Path(phone).stem
                    )
                await countdown(config.countdown)


async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"waiting for {hour}:{minute}:{seconds} ", flush=True, end="\r")
        await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()
