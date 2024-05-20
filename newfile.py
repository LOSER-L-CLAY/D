import os
import getpass
import time
import sys
from colorama import init, Fore, Style
from moviepy.editor import VideoFileClip

# Initialize colorama
init(autoreset=True)

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for ASCII art animation
def ascii_art_animation():
    ascii_art = """
    ███████▄     ▄████████    ▄████████     ███        ▄█    █▄         ███▄▄▄▄    ▄██████▄      ███        ▄████████ 
    ███   ▀███   ███    ███   ███    ███ ▀█████████▄   ███    ███        ███▀▀▀██▄ ███    ███ ▀█████████▄   ███    ███ 
    ███    ███   ███    █▀    ███    ███    ▀███▀▀██   ███    ███        ███   ███ ███    ███    ▀███▀▀██   ███    █▀  
    ███    ███  ▄███▄▄▄       ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄      ███   ███ ███    ███     ███   ▀  ▄███▄▄▄     
    ███    ███ ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀▀███▀       ███   ███ ███    ███     ███     ▀▀███▀▀▀     
    ███    ███   ███    █▄    ███    ███     ███       ███    ███        ███   ███ ███    ███     ███       ███    █▄  
    ███   ▄███   ███    ███   ███    ███     ███       ███    ███        ███   ███ ███    ███     ███       ███    ███ 
    ███████▀    ██████████   ███    █▀     ▄████▀     ███    █▀          ▀█   █▀   ▀██████▀     ▄████▀     ██████████ 
    """
    color = Fore.BLUE
    lines = ascii_art.split("\n")
    for i in range(len(max(lines, key=len))):
        clear()
        for line in lines:
            print(color + line[:i] + Fore.RESET)
        time.sleep(0.02)

# Function to print normal centered text
def print_normal_centered(text):
    center_position = (os.get_terminal_size().columns - len(text)) // 2
    print(' ' * center_position + text)

# Function for login
def login():
    clear()
    expected_user = ""  # Expected empty username
    expected_passwd = ""  # Expected empty password

    print_normal_centered("YOU ARE CALLING DEATH")
    print()  # Print a blank line for spacing
    username = input(Fore.BLUE + "WHO WAS FAN OF L: " + Fore.RESET)

    clear()  # Clear the screen after the first prompt

    print_normal_centered("YOU ARE CALLING DEATH")
    print()  # Print a blank line for spacing
    password = getpass.getpass(prompt=Fore.BLUE + 'WHO WAS FAN OF LIGHT: ' + Fore.RESET)

    if username != expected_user or password != expected_passwd:
        print(Fore.RED + "\nPassword/Username incorrect" + Fore.RESET)
        sys.exit(1)
    else:
        print(Fore.GREEN + "\nLogin successful" + Fore.RESET)
        time.sleep(0.3)
        ascii_art_animation()  # Display ASCII art animation after successful login
        time.sleep(0.3)
        video_clip = VideoFileClip("st.mp4")
        try:
            import pygame
            pygame.init()
            pygame.display.set_caption("Death Note")
            screen = pygame.display.set_mode((video_clip.size[0], video_clip.size[1]))
            video_clip.preview()
            video_clip.close()
            pygame.quit()  # Close pygame after video preview
        except ImportError:
            print(Fore.RED + "Pygame is not installed. Please install it using 'pip install pygame'." + Fore.RESET)
            sys.exit(1)


# Function for writing a note with blue color, animation, and centered text
def write_note():
    clear()
    print_normal_centered(Fore.YELLOW + Style.BRIGHT + "CHOOSE YOUR NOTE\n")
    methods = [
        "LIGHT  - his world is rotten and those who are making it rot deserve to die                                     ",
        "L      - Looks Like Someone Dropped This Cell Phone In The Crowd Earlier                                        ",
        "RYUK   - I Told You In The Very Beginning That I Would Be The One Writing Your Name In The Notebook When You Die",
        "NEAR   - If You Can't Beat The Game, If You Can't Solve The Puzzle, You're Nothing But A Loser                  ",
        "MELLO  - No matter what I have to do, I will get it before Near                                                 ",
        "TERU   - There is no reason for me to question. God is absolute. My job is to do as God wishes                  ",
    ]
    for method in methods:
        print_normal_centered(Fore.BLUE + method)
        time.sleep(0.2)
    print_normal_centered(Fore.BLUE + "HOW TO USE")
    print_normal_centered(Fore.YELLOW + "NOTE_NAME  PASTE_TARGET_URL  DURATION")
    input(Fore.GREEN + "Press Enter to continue..." + Fore.RESET)

# Function for displaying available ports
def ports():
    clear()
    print("Ports method selected")
    # Add your ports method implementation here

# Function for displaying the menu with golden color and centered text
def menu():
    clear()
    print_normal_centered(Fore.YELLOW + Style.BRIGHT + "LET'S MAKE A BOOM"  )
    
    print_normal_centered(Fore.YELLOW + "IF YOU NEED"  )
   
    print_normal_centered(Fore.YELLOW + "WRITE NOTE - FOR SHOW NOTES. ")
    print_normal_centered(Fore.YELLOW + "     CLEAR - FOR CLEAR NOTES.")
    print_normal_centered(Fore.YELLOW + "      HELP - FOR KIDS        ")
    print(Style.RESET_ALL)

def main():
    menu()
    while True:
        try:
            cnc = input(Fore.BLUE + "NOTES " + Fore.RESET)
            if cnc.lower() == "write note":
                write_note()
            elif cnc.lower() == "clear":
                clear()
                menu()
            elif cnc.lower() == "ports":
                ports()
            elif "tls" in cnc.lower():
                # Add TLS method implementation
                pass
            # Add other methods and options here
            elif cnc.lower() == "help":
                print(Fore.GREEN + "Help Information:")
                print(Fore.CYAN + "Use 'WRITE NOTE' FOR SHOW NOTES.")
                print("Use 'CLEAR' to FOR CLEAR NOTES.")
                print("Use 'HELP' to display this help information.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "Command not found")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInterrupted by user, exiting..." + Fore.RESET)
            sys.exit(0)

# Entry point of the program
if __name__ == "__main__":
    ascii_art_animation()  # Display ASCII art animation
    login()
    main()
