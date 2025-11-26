import time
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    # Definindo cores kawaii
    ROSA = Fore.MAGENTA
    CIANO = Fore.CYAN
    AMARELO = Fore.YELLOW
    BRANCO = Fore.WHITE
    RESET = Style.RESET_ALL
except ImportError:
    # Cores padrão se colorama não estiver instalado
    ROSA = ""
    CIANO = ""
    AMARELO = ""
    BRANCO = ""
    RESET = ""

def apresentar_kawaii(MiyaHime):
    """
    Função de apresentação super kawaii para o GitHub! 🌸
    """
    borda = f"{ROSA}*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*{RESET}"
    
    print(f"\n{borda}")
    titulo = f"💖🎀🌸 Kawaii Welcome! Nya! 🌸🎀💖"
    print(titulo.center(55))
    print(borda)
    
    time.sleep(0.5)
    print(f"{CIANO}૮꒰ ˶• ༝ •˶꒱ა ~ Bem-vindo(a) ao meu jardim de códigos, {MiyaHime}-senpai! ✨{RESET}")
    time.sleep(0.5)

    
    print(f"{AMARELO}🌱 Estou cultivando projetos fofinhos e úteis aqui no GitHub. 🌈{RESET}")
    time.sleep(0.5)
    print(f"{ROSA}🎀 Minha linguagem favorita é Python! Pip pip, hooray! 🐍💖{RESET}")
    time.sleep(0.5)
    print(f"{CIANO}🎮 Gosto de misturar programação com criatividade e diversão! 🎨{RESET}")
    time.sleep(0.5)
    print(f"{AMARELO}💫 Fique à vontade para olhar ao redor! Não mordo! (meow) 🐱{RESET}")
    time.sleep(0.5)
    print(f"{ROSA}🌸 Espero que goste do que vê! Tenha um dia doce! 🍬{RESET}")
    
    print(f"\n{borda}")

if __name__ == "__main__":
    # Coloque seu nome ou apelido kawaii aqui! 🍓
    meu_nome_kawaii = "TechSenpai" 
    apresentar_kawaii(MiyaHime=meu_nome_kawaii)