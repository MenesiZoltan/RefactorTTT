import os

def request_input():
    player = 'X' if round_cnt % 2 == 1 else 'O'
    selection = int(input("selection?: "))
    os.system("clear")

def add_input_to_table():
#beolvassa az inputot, és az adott érték alapján tölti be a table-be x vagy o-t.
    for y in range(len(table)):
        for x in range(len(table)):
            if table[y][x] == selection:
                table[y][x] = player
                round_cnt += 1

def join_table_and_tracker():
#trackben kicsereli a szoközöket a table megfelelő értékeire, akkor ha a table megfelelő értéke = string. különben meghagyja az adott pozicioban levő spacet.
    for y in range(len(table)):
        for x in range(len(table)):
            if isinstance(table[y][x],str):
                track[y*2+1][x*2+1] = table[y][x]

print_game_board():
#Kinyomtatja az egészet tracket
    for y in range(len(track)):
        for x in range(len(track)):
            print(track[y][x],end="")
        print("")

def win_c_check():
    pass

def draw_check():
    pass

def restart_game():
    pass

def exit_game():
    pass

def main():
    table =[[7,8,9],[4,5,6],[1,2,3]]
    round_cnt = 1
    track = [   ["\u250F","\u2501","\u2533","\u2501","\u2533","\u2501","\u2513"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2523","\u2501","\u254B","\u2501","\u254B","\u2501","\u252B"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2523","\u2501","\u254B","\u2501","\u254B","\u2501","\u252B"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2517","\u2501","\u253B","\u2501","\u253B","\u2501","\u251B"]]
    win = True
    while win == True:
        request_input()
        add_input_to_table()
        join_table_and_tracker()
        print_game_board()
        win_c_check()
        draw_check()
        restart_game()
    exit_game()

if __name__ == '__main__':
    main()