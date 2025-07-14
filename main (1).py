import os
import time

def make_banner_normal():
    os.system("clear")
    banner = input("Enter your banner text (Normal): ")
    os.system(f"figlet '{banner}' > $HOME/banner.txt")
    with open(os.path.expanduser("~/.bashrc"), "w") as f:
        f.write("clear\n")
        f.write("cat $HOME/banner.txt\n")
        f.write("neofetch\n")
    print("✅ Normal Banner Set Successfully!")
    time.sleep(2)

def make_banner_login():
    os.system("clear")
    banner = input("Enter your login banner text: ")
    password = input("Set a password to show Termux: ")
    script = f"""clear
echo -e "\e[32m"
figlet '{banner}'
echo -e "\e[0m"
read -p "Enter password: " pass
if [ "$pass" == "{password}" ]; then
    clear
    neofetch
else
    echo "Wrong password!"
    exit
fi
"""
    with open(os.path.expanduser("~/.bashrc"), "w") as f:
        f.write(script)
    print("✅ Login Banner Set with Password!")
    time.sleep(2)

def open_facebook():
    os.system("xdg-open https://www.facebook.com/profile.php?id=100001889177878")
    time.sleep(2)

while True:
    os.system("clear")
    os.system("figlet TERMUX SETUP COMPLETE | lolcat")
    print("""
[01] MAKE TERMUX BANNER(NORMAL)
[02] MAKE TERMUX BANNER(LOGISYSTEM)
[03] FIND US ON FB
[04] EXIT TOOLS
""")
    choice = input("[•] YOUR CHOICE : ")

    if choice == "01":
        make_banner_normal()
    elif choice == "02":
        make_banner_login()
    elif choice == "03":
        open_facebook()
    elif choice == "04":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")
        time.sleep(1)
