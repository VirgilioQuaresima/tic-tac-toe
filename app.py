from tkinter import font, messagebox
from typing import List
from player import Player
from game import Game
from tkinter import *
from tkmacosx import Button

# view controller
class Tris:
    def __init__(self) -> None:
        
        # APP
        self.root = Tk()
        
        # MODEL
        self.table = Game()

        # VIEW 
        self.buttons = []

        # PLAYER
        self.p1 = Player(StringVar(), 'X')
        self.p2 = Player(StringVar(), 'O')
        self.player = self.p1
        self.game = True

# ACTION
# esegue l'azione all'click di una casella
    def b_click(self, b: Button, pos: tuple, pointer: Label)-> None:

        # recupera le caselle disponibili dal Model
        avalaible = self.table.available()
        pos = pos[0]+1, pos[1]+1

        # verifica se la casella scelta è disponibile altrimenti invia messaggio di errore
        if pos not in avalaible:
            messagebox.showerror('Tris', 'Cella già selezionata')
            return

        # scrivi il simbolo del giocatore sulla casella
        b['text'] = self.player.symbol

        # aggiorna il model
        self.table.update_pad(self.player.symbol, pos)

        # verifica lo stato del gioco
        self.game, winner, win_pos = self.table.check_gameover()

        # Game over
        if not self.game:
            self.game_over(winner, win_pos)
        else:
        # scambia il turno dei giocatori e aggiorna il puntatore
            self.player = self.p2 if self.player == self.p1 else self.p1
            pointer['text'] = self.player.symbol

# VIEW
# costruisce e posiziona i componenti della vista
    def build_grid(self) -> None:
        self.p1.symbol='X'
        self.p2.symbol='O'

        # labels
        # nomi dei giocatori
        l1 = Label(text=self.p1.name.get(), font=font.Font(family='calibre',
                                                           size=12, weight='bold', slant='roman'))
        l2 = Label(text=self.p2.name.get(), font=font.Font(family='calibre',
                                                           size=12, weight='bold', slant='roman'))
        # player One/Two
        L1 = Label(self.root, text="Player One", font=('calibre', 12, 'bold'))
        L2 = Label(self.root, text="Player Two", font=('calibre', 12, 'bold'))
        
        # puntatore del simbolo dei giocatori
        pointer = Label(text=self.player.symbol, font=font.Font(family='calibre',
                                                                size=24, weight='bold', slant='roman'), fg='#f00')
        
        # entries
        # input dei nomi dei giocatori
        E1 = Entry(self.root, textvariable=self.p1.name,
                   font=('calibre', 12, 'normal'))
        E2 = Entry(self.root, textvariable=self.p2.name,
                   font=('calibre', 12, 'normal'))

        # buttons
        # caselle di gioco
        # al click eseguono b_click
        b1 = Button(self.root, text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b1, (0, 0), pointer))
        b2 = Button(self.root, text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b2, (0, 1), pointer))
        b3 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b3, (0, 2), pointer))
        b4 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b4, (1, 0), pointer))
        b5 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b5, (1, 1), pointer))
        b6 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b6, (1, 2), pointer))
        b7 = Button(self.root,   text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b7, (2, 0), pointer))
        b8 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b8, (2, 1), pointer))
        b9 = Button(self.root,  text=' ', activeforeground='#5fb9f5', height=120,
                    width=120,  borderwidth=2,
                    font=font.Font(family='SignPainter',
                                   size=45, weight='bold', slant='roman'),
                    highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                    overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.b_click(b9, (2, 2), pointer))

        buttons = [b1,  b2,  b3,  b4,  b5,  b6,  b7,  b8,  b9]

        # set names
        # al click settano il nome del rispettivo utente
        set_name1 = Button(self.root, text='SET', activeforeground='#5fb9f5', height=18,
                           width=60,  borderwidth=2,
                           font=font.Font(family='calibre',
                                          size=16, weight='bold', slant='roman'),
                           highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                           overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.set_name(set_name1, 'p1', E1, l1, self.p1))
        set_name2 = Button(self.root, text='SET', activeforeground='#5fb9f5', height=18,
                           width=60,  borderwidth=2,
                           font=font.Font(family='calibre',
                                          size=16, weight='bold', slant='roman'),
                           highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                           overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.set_name(set_name2, 'p2', E2, l2, self.p2)) 
        
        # clear
        # al click esegue la funzione clear per azzerare e ricostruire la schermata
        b_clear = Button(self.root, text='CLEAR', activeforeground='#5fb9f5', height=30,
                         width=75,  borderwidth=2,
                         font=font.Font(family='calibre',
                                        size=18, weight='bold', slant='roman'),
                         highlightbackground='#5fb9f5', foreground='#575aff', background='#f7f4e1',
                         overbackground='#000000', overforeground='#575aff', activebackground=('#5fb9f5', '#D4D4D4'), borderless=1, command=lambda: self.clear([b_clear, pointer, E1, L1, E2, L2, set_name1, set_name2, l1, l2], buttons))
        
        self.components=[b_clear, pointer, E1, L1, E2, L2, set_name1, set_name2, l1, l2]
        i = 0
        for b in buttons:
            table = [
                (0, 0),
                (0, 1),
                (0, 2),
                (1, 0),
                (1, 1),
                (1, 2),
                (2, 0),
                (2, 1),
                (2, 2),
            ]
            r, c = table[i]
            b.grid(row=r, column=c)
            i += 1

        L1.grid(row=3, column=0, pady=10)
        E1.grid(row=3, column=1, pady=10)
        l1.grid(row=3, column=1)
        set_name1.grid(row=3, column=2, pady=10)

        L2.grid(row=4, column=0)
        E2.grid(row=4, column=1)
        l2.grid(row=4, column=1)
        set_name2.grid(row=4, column=2, pady=10)

        pointer.grid(row=5, column=0, pady=10)
        b_clear.grid(row=5, column=1)

        self.buttons = buttons

# VIEW
    def clear(self, components, buttons) -> None:
        # svuota il model
        self.table.clear()
        
        # rimuove i componenti dalla griglia
        components = components+buttons
        for component in components:
            component.grid_remove()

        # azzera i nomi dei giocatori 
        self.p1.name.set('')
        self.p2.name.set('')

        # ricostruisce la griglia
        self.build_grid()

# VIEW/ACTION
    def game_over(self, winner: str, win_pos: List[tuple]) -> None:

        # colora i bottoni
        table = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
        for ix, el in enumerate(table):
            if el in win_pos:
                b = self.buttons[ix]
                b.config(bg="#E69A8D")

        # invia messaggi
        user = {
            'p2': f'CONGRATS\n{str(self.p2.name.get()).upper()}',
            'p1': f'CONGRATS\n{str(self.p1.name.get()).upper()}',
            ' ': '       pair        '
        }

        messagebox.showinfo('tris', f'{user[winner]}')
        MsgBox = messagebox.askquestion(
            'Exit Application', 'Are you sure you want to exit the application', icon='warning')
        if MsgBox == 'yes':
            self.root.destroy()
        else:
        # ogni cella porta al refresh della schermata
            for b in self.buttons:
                b.config(command=lambda: self.clear(components=self.components,buttons=self.buttons))

# VIEW
    def set_name(self, B: Button, p: str, E: Entry, L: Label, player: Player) -> None:
        
        # elimina il bottone 'set'
        B.grid_remove()

        # rimuove l'entry 'nome player'
        E.grid_remove()

        # modifica la label sotto l'entry inserendo il nome scelto
        L['text'] = player.name.get()

# APP
    def run(self) -> None:
        self.root.title = ('Tris', 'Tris2')
        self.build_grid()
        self.root.mainloop()


if __name__ == '__main__':
    app = Tris()
    app.run()
