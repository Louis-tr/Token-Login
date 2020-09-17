from colorama import Fore
from selenium import webdriver

print(f"{Fore.RED}Enter a token")
_token = input(">")
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome('chromedriver.exe', options=opts)
script = """
        function login(token) {
        setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
        location.reload();
        }, 2500);
        }   
        """
driver.get("https://discordapp.com/login")
driver.execute_script(script + f'\nlogin("{_token}")')
