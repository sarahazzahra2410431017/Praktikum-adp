import time
import os
from termcolor import colored
def loading_screen():
    os.system('cls')   
    print(colored("====================================", 'blue'))
    print(colored("       APLIKASI KEREN ", 'yellow', attrs=['bold']))
    print(colored("====================================", 'blue'))       
    icon = [
        colored("   ╭────╮   ", 'yellow'),
        colored("   │ ^ ^│   ", 'yellow'),
        colored("   │ ── │   ", 'yellow'),
        colored("   ╰────╯   ", 'yellow')
    ]        
    for line in icon:
        print(line)      
    print("\nMemuat...")    
    for i in range(1, 101):
        time.sleep(0.03)
        bar = colored("[" + "█" * (i//5) + " " * (20 - i//5) + "]", 'green')
        print(f"\r{bar} {i}%", end='', flush=True)      
    print("\n\n" + colored("Siap digunakan!", 'green'))
if __name__ == "__main__":
    loading_screen()
