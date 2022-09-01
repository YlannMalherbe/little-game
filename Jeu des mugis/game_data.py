level_0 = {"node_pos": (220, 200), 'level': 1, 'level_content': 'This is the level 1', 'gravity': 0.8, 'unlock': 1,
           'LEVEL_MAP':
       ['                                                   X         V   ',
        '                                         XXXX      X         V   ',
        '                   M   XX                          X         V   ',
        '                XXXX           XX     XX        XXXX     XXXXX   ',
        '            P                     M XXXX        X        X       ',
        '         XXXXX         XX        XXXXXXXX             XXXX       ',
        '          XXXX       XX             XXXXXX               X       ',
        '          XX    X  XXXX    XX  XX    XXXXXX     XXXX     X       ',
        '                X  XXXX    XX  XXX    XXXXXX             X       ',
        '             XXXX  XXXXXX  XX  XXXX    XXXXXXX           X       ',
        '         XXXXXXXX  XXXXXX  XX  XXXX    XXXXXXX           X       ',
        '         XXXXXXXX  XXXXXX  XX  XXXX    XXXXXXX           X       ',
        '         XXXXXXXX  XXXXXX  XX  XXXX    XXXXXXX           X       ',
        'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']}
level_1 = {"node_pos": (640, 200), 'level': 2, 'level_content': 'This is the level 2', 'gravity': 0.8, 'unlock': 2,
           'LEVEL_MAP':
       ['                                                                 ',
        '                                                                 ',
        '                  XX   XXX                                       ',
        '            XXX               XX  XX         M                   ',
        '                                      XX    XXXX                 ',
        '                                                   XXX    C      ',
        '             V                                            C      ',
        '             V                                           XX      ',
        '             V                         M                         ',
        '            XX                       XXXXX    XX    XXX          ',
        '                                                                 ',
        '     P                     XX   XXX                              ',
        '   XXXXXX   XX   XX  XXX                                         ',
        '                                                                 ',
        '                                                                 ',
        'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']}
level_2 = {"node_pos": (1080, 200), 'level': 3, 'level_content': 'This is the level 3',  'gravity': 0.2, 'unlock': 3,
           'LEVEL_MAP':
       ['                                                                 ',
        '              P                                                  ',
        '            XXXXXXXXXX                                           ',
        '                                 D            D         D        ',
        '                                                                 ',
        '                       D           D                             ',
        '                                                                 ',
        '                                  D         D                    ',
        '                                                                 ',
        '                     D                                           ',
        '                                                     D           ',
        '                                                                 ',
        '                                    D                            ',
        '                                                                 ',
        '                 D                                               ',
        '                                                  D          DD  ',
        '                             D                                   ',
        '              D                                                  ',
        '                                D                                ',
        '                                                                 ',
        '                                                                 ',
        '                                       D                         ',
        '                                                                 ',
        '                                                                 ',
        '                D                                                ',
        '                                                    D            ',
        '                                                                 ',
        '                                         D                       ',
        '                            D                                    ',
        '                                                                 ',
        '          D                                                      ',
        '                                                   D             ',
        '                                    D                            ',
        '                                                                 ',
        '                    D                                            ',
        '                                           D                     ',
        '                                                                 ',
        '                                                                 ',
        '                                                  D              ',
        '   D                                                             ',
        '                                 D                               ',
        '                         D                                       ',
        '                                                                 ',
        '                        D        D                               ',
        '                                                                 ',
        '                        VVVVVVVVVVV                              ',
        'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']}
level_3 = {"node_pos": (450, 400), 'level': 4, 'level_content': 'This is the level 4',  'gravity': 0.8, 'unlock': 4,
           'LEVEL_MAP':
       ['                                                V                ',
        '                                                V                ',
        '                                         X    XXXXXX             ',
        '                                                                 ',
        '                                       X                         ',
        '                                                                 ',
        '                                         XX                      ',
        '                                               XX           C    ',
        '                                                     M      C    ',
        '                                                    XXX     C    ',
        '                                                           XX    ',
        '                                                                 ',
        '                                                      XX         ',
        '         P                                      XXX              ',
        '        XXXXX                             XX                     ',
        '                        M   XX     XX  X                         ',
        '               XXX  X  XXX                                       ',
        'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']}
level_4 = {"node_pos": (850, 400), 'level': 5, 'level_content': 'This is the level 5', 'gravity': 0.8, 'unlock': 5,
           'LEVEL_MAP':
       ['                                                                 ',
        '                                                     M           ',
        '                                                    XXXX       V ',
        '                X    X    X                    X          X    V ',
        '           MX                          X XX                   XX ',
        '           X                  X    X                             ',
        '          X                                                      ',
        '                                                                 ',
        '       X                                                         ',
        '       X  P                                                      ',
        '       XXXXX                                                     ',
        '                                                                 ',
        '                                                                 ',
        'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']}

shop_speed = {"node_pos": (120, 50), "Content": "speed upgrade", "upgrade": "speed"}
shop_cooldown = {"node_pos": (120, 200), "Content": "cooldown upgrade", "upgrade": "attack_cooldown"}
shop_damage = {"node_pos": (120, 350), "Content": "damage upgrade", "upgrade": "damage"}
shop_pv = {"node_pos": (120, 500), "Content": "pv upgrade", "upgrade": "pv"}

speed_stats_panel = [8, 9, 10]
cooldown_stats_panel = [75, 50, 30, 20, 10]
damage_stats_panel = [20, 30, 40, 50]
pv_stats_panel = [100, 125, 150, 175, 200]

speed_price_panel = [100, 250, 500]
cooldown_price_panel = [100, 150, 250, 350, 500]
damage_price_panel = [100, 275, 400, 500]
pv_price_panel = [100, 150, 250, 350, 500]

shop_info = {
 "0": {"info": shop_speed, "panel": speed_stats_panel, "price": speed_price_panel},
 "1": {"info": shop_cooldown, "panel": cooldown_stats_panel, "price": cooldown_price_panel},
 "2": {"info": shop_damage, "panel": damage_stats_panel, "price": damage_price_panel},
 "3": {"info": shop_pv, "panel": pv_stats_panel, "price": pv_price_panel}
}

levels = {
    0: level_0,
    1: level_1,
    2: level_2,
    3: level_3,
    4: level_4
}

end_level_sentence = {
 'win': ["Victory ! GG", "And that's a win ! GG", "You nailed it ! GG", "So easy for you ! GG"],
 'loose': ["You really leave ? coward ! ", "Tsss look, a Looser who give up !", "Raahhh it's not that hard, you're bad !", "Maybe it would work if you were better !"],
 'dead': ["Damn already 5 death ! You're a Looser !", "Raahhh it's not that hard, you're bad !", "Can you be better please ?", "Keep trying maybe one day..."]
}
