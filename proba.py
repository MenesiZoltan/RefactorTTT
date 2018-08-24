import os


def request_input():
    #x és o-t valtogatja, + bekeri az inputot.
    selection = int(input("selection?: "))
    os.system("clear")
    return selection


def add_input_to_table(table, selection, player):    
    #beolvassa az inputot, és az adott érték alapján tölti be a table-be x vagy o-t.
    for y in range(len(table)):
        for x in range(len(table)):
            if table[y][x] == selection:
                table[y][x] = player
                round_cnt += 1
            return table   


def join_table_and_track(table, track):
    #trackben kicsereli a szoközöket a table megfelelő értékeire, akkor ha a table megfelelő értéke = string. különben meghagyja az adott pozicioban levő spacet.
    for y in range(len(table)):
        for x in range(len(table)):
            if isinstance(table[y][x],str):
                track[y*2+1][x*2+1] = table[y][x]      
            return track


def print_game_boards(track):    
    #Kinyomtatja az egészet tracket
    for y in range(len(track)):
        for x in range(len(track)):
            print(track[y][x],end="")
        print("")


def win_condition_check():
    pass


def draw_check():
    pass


def restart_game():
    pass


def exit_game():
    pass


def main():
    selection = 0
    table =[[7,8,9],[4,5,6],[1,2,3]]
    round_cnt = 1
    player = 'X' if round_cnt % 2 == 1 else 'O'
    track = [   ["\u250F","\u2501","\u2533","\u2501","\u2533","\u2501","\u2513"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2523","\u2501","\u254B","\u2501","\u254B","\u2501","\u252B"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2523","\u2501","\u254B","\u2501","\u254B","\u2501","\u252B"],
            ["\u2503"," ","\u2503"," ","\u2503"," ","\u2503"],
            ["\u2517","\u2501","\u253B","\u2501","\u253B","\u2501","\u251B"]]
    win = True
    while win == True:
        selection = request_input()
        add_input_to_table(table, selection, player)
        join_table_and_track(table, track)
        print_game_boards(track)
        win_condition_check()
        draw_check()
        restart_game()
    exit_game()

if __name__ == '__main__':
    main()