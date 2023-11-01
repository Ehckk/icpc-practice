import sys


def input_process():
    enemy_attacks = []
    for attck in sys.stdin:
        [enemy_attacks.append(a) for a in attck if a != '\n']

    print(counter_attack(enemy_attacks))


def counter_attack(enemy_attack: list) -> str:
    combo_more_breaker, combo_breaker, move = (0, 3, 'C')
    rake, bite, laser = ['R', 'B', 'L']  # attaks
    slice, kick, shield = ['S', 'K', 'H']  # counter attacks

    counter_attack = []
    attack_combo = []

    for attack in enemy_attack:
        attack_combo.append(attack)
        if attack == rake:
            counter_attack.append(slice)
        elif attack == bite:
            counter_attack.append(kick)
        elif attack == laser:
            counter_attack.append(shield)

        if len(set(attack_combo)) == combo_breaker:
            for _ in range(combo_breaker):
                counter_attack.pop()

            counter_attack.append(move)
            attack_combo.clear()

        elif len(attack_combo) >= combo_breaker:
            attack_combo.pop(combo_more_breaker)

    return ''.join(counter_attack)


input_process()
