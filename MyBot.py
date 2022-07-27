def do_turn(pw):
    if len(pw.enemy_fleets()) > 0:
        dest = get_planet_of_ships(pw.enemy_fleets(), max(get_ships(pw.enemy_fleets()))).source_planet()
        num_ships = dest.num_ships() + 90
    else:
        return
    source = get_planet_of_ships(pw.my_planets(), max(get_ships(pw.my_fleets())))
    num_ships = source.num_ships()
    pw.debug('Num ships: ' + str(num_ships))
    pw.issue_order(source, dest, num_ships)
    pass

def get_ships(all):
    all_ships = []
    for i in all:
        all_ships += all.num_ships()
    return all_ships

def get_planet_of_ships(all, num_ships):
    for i in all:
        if i.num_ships() == num_ships:
            return all[i]
