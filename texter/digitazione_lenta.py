import pyautogui
import time

# Funzione per digitare lentamente
def digita_lentamente(testo, delay=1.5):
    for carattere in testo:
        pyautogui.write(carattere)
        time.sleep(delay)

# Esegui il programma
def main():
    print("Incolla il testo che vuoi riscrivere lentamente e premi Invio:")
    testo = input("Testo: ")
    
    print("Hai 5 secondi per posizionare il cursore dove vuoi scrivere...")
    time.sleep(5)  # Ti dà il tempo di posizionare il cursore
    
    digita_lentamente(testo)

if __name__ == "__main__":
    main()
