import time
import textwrap
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
    ROSA = "\033[95m"
    CIANO = "\033[96m"
    AMARELO = "\033[93m"
    BRANCO = "\033[97m"
    RESET = "\033[0m"

def apresentar_kawaii(MiyaHime):
    """
    Função de apresentação super kawaii para o GitHub! 🌸
    """
    borda = f"{ROSA}*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*{RESET}"
    bordac = f"{CIANO}✼═══════ •❅• ═══════ ✼✿             ✿✻ ═══════ •❅• ═══════✼{RESET}"

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
    print(f"\n{bordac}")

    LARGURA_TOTAL = 80
    arte_coelho = f"""
(\_/)
(^.^)
(>♥<)z"""
    arte_coelho = textwrap.dedent(arte_coelho).strip()

    linhas = arte_coelho.split('\n')
    num_linhas = len(linhas)

    for i, linha in enumerate(linhas):
       linha_centralizada = linha.center(60)
       print(linha_centralizada)
       time.sleep(1.0)
    print (RESET, end="")

    print(f"\n{bordac}")
    print(f"\n{borda}")

if __name__ == "__main__":
    # Coloque seu nome ou apelido kawaii aqui! 🍓
    meu_nome_kawaii = "TechSenpai" 
    apresentar_kawaii(MiyaHime=meu_nome_kawaii)
