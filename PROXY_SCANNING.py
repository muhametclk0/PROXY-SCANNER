import os
import requests
from colorama import Fore, Style, init
import json

init()

Diadlo = r"""
.......................           .......................
....................               ....................
..................                   ..................
.................                     .................
................                       ................
...............                         ...............
..............                           ..............
.............   insta - muhametclk0      ..............
..............                           ..............
...............                         ...............
................                       ................
.................                     .................
..................                   ..................
....................               ....................
.......................           .......................
"""

def parse_proxy(proxy):
    if isinstance(proxy, dict):
        proxy = proxy.get('http', proxy.get('https', ''))
    if not proxy.startswith('http://') and not proxy.startswith('https://'):
        proxy = 'http://' + proxy
    return proxy

def check_proxy(proxy):
    try:
        parsed_proxy = parse_proxy(proxy)
        response = requests.get('http://www.example.com', proxies={"http": parsed_proxy, "https": parsed_proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

def list_files_in_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
    for i, file in enumerate(files, 1):
        print(f"{i}) {file}")
    return files

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + Diadlo + Style.RESET_ALL)
        print("Menü:")
        print("1) Proxy kontrol et")
        print("2) Çıkış")
        choice = input("Bir seçenek belirleyin :  ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            files = list_files_in_directory()
            file_choice = input("İncelemek istediğiniz dosyayı seçin (bir sayı girin) : örn(proxy_dosya.txt) ")
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                file_index = int(file_choice) - 1
                if 0 <= file_index < len(files):
                    selected_file = files[file_index]
                    with open(selected_file, 'r') as file:
                        proxies = file.read().splitlines()

                    working_proxies = []

                    for proxy in proxies:
                        try:
                            proxy = json.loads(proxy)
                        except json.JSONDecodeError:
                            pass
                        if check_proxy(proxy):
                            print(Fore.GREEN + f"İşe yarıyor : {proxy}" + Style.RESET_ALL)
                            working_proxies.append(proxy)
                        else:
                            print(Fore.RED + f"Çalışmıyor : {proxy}" + Style.RESET_ALL)

                    create_file = input("Çalışan proxy'lerle bir dosya oluşturmak ister misiniz? (evet/hayır) : ").lower()
                    if create_file == 'evet':
                        new_filename = input("Bir dosya nasıl adlandırılır : ")
                        with open(new_filename, 'w') as new_file:
                            for proxy in working_proxies:
                                new_file.write(json.dumps(proxy) + '\n')
                        print(f"Çalışan proxy'lerle oluşturulan '{new_filename}' dosyası.")
                    else:
                        print("Dosya oluşturulmadı.")
                else:
                    print("Yanlış dosya seçimi.")
            except ValueError:
                print("Yanlış dosya seçimi.")

        elif choice == '2':
            print("Programdan çıkmak.")
            break

        else:
            print("Yanlış seçim. Lütfen 1 veya 2'yi seçin.")

if __name__ == "__main__":
    main()