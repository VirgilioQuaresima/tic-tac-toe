from typing import List

# Model
class Game:

    def __init__(self) -> None:

        self.table = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

# svuota le celle del campo
    def clear(self)->None:
        self.table = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

# aggiorna il campo
    def update_pad(self, symbol: str, pos: tuple)-> bool:
        if self.table[int(pos[0])-1][int(pos[1])-1] != 0:
            return True
        legend={
            'X':1,
            'O':-1,
            '':0
        }
        self.table[int(pos[0])-1][int(pos[1])-1] = legend[symbol]
        return False

# restituisce le celle disponibili
    def available(self)-> List[tuple]:
        available_pos = []
        j = 1
        for row in self.table:
            i = 1
            for el in row:
                if el == 0:
                    available_pos.append((j, i))
                i += 1
            j += 1
        return available_pos

# verifica lo stato del gioco
# -> stato, vincitore, posizione celle
    def check_gameover(self)-> tuple:

        tab = self.table
        aval = self.available()
        r = [0, 0, 0]

        for  r_ix,row in enumerate(tab):
            if sum(row) == 3:
                winner = 'p1'
                return False, winner,[(r_ix,0),(r_ix,1),(r_ix,2)]
            elif sum(row) == -3:
                winner = 'p2'
                return False, winner,[(r_ix,0),(r_ix,1),(r_ix,2)]

            i = 0
            for el in row:
                r[i] += el
                i += 1
        for c_ix, c in enumerate(r):
            if c == 3:
                winner = 'p1'
                return False, winner,[(0,c_ix),(1,c_ix),(2,c_ix)]
            elif c == -3:
                winner = 'p2'
                return False, winner,[(0,c_ix),(1,c_ix),(2,c_ix)]

        somma = tab[0][0]+tab[1][1]+tab[2][2]

        if somma == 3:
            winner = 'p1'
            return False, winner,[(0,0),(1,1),(2,2)]
        elif somma == -3:
            winner = 'p2'
            return False, winner,[(0,0),(1,1),(2,2)]

        somma = tab[0][2]+tab[1][1]+tab[2][0]
        if somma == 3:
            winner = 'p1'
            return False, winner,[(0,2),(1,1),(2,0)]
        elif somma == -3:
            winner = 'p2'
            return False, winner,[(0,2),(1,1),(2,0)]

        if len(aval)==0:
            return False,' ',[(),(),()]

        return True, '',[(0,0),(0,0),(0,0)]
