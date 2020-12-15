def cast_spell(hero_dic, name, mp, spell):
    if hero_dic[name][1] >= mp:
        hero_dic[name][1] -= mp
        return f"{name} has successfully cast {spell} and now has {hero_dic[name][1]} MP!"
    else:
        return f"{name} does not have enough MP to cast {spell}!"


def take_damage(hero_dic, name, damage, attacker):
    hero_dic[name][0] -= damage
    if hero_dic[name][0] > 0:
        return f"{name} was hit for {damage} HP by {attacker} and now has {hero_dic[name][0]} HP left!"
    else:
        hero_dic.pop(name)
        return f"{name} has been killed by {attacker}!"


def recharge(hero_dic, name, amount):
    hero_dic[name][1] += amount
    if hero_dic[name][1] >= 200:
        amount -= (hero_dic[name][1] - 200)
        hero_dic[name][1] = 200
    return f"{name} recharged for {amount} MP!"


def heal(hero_dic, name, amount):
    hero_dic[name][0] += amount
    if hero_dic[name][0] >= 100:
        amount -= (hero_dic[name][0] - 100)
        hero_dic[name][0] = 100
    return f"{name} healed for {amount} HP!"


num_heroes = int(input())
heroes = {}
for _ in range(num_heroes):
    hero = input()
    hero_name, hero_hp, hero_mp = hero.split()
    heroes[hero_name] = [int(hero_hp), int(hero_mp)]
cmd = input()
while not cmd == 'End':
    cmd = cmd.split(' - ')
    # name,amount,spell = cmd[1:]
    # name, amount = cmd[1:]
    if cmd[0] == 'CastSpell':
        print(cast_spell(heroes, cmd[1], int(cmd[2]), cmd[3]))
    elif cmd[0] == 'TakeDamage':
        print(take_damage(heroes, cmd[1], int(cmd[2]), cmd[3]))
    elif cmd[0] == 'Recharge':
        print(recharge(heroes, cmd[1], int(cmd[2])))
    elif cmd[0] == 'Heal':
        print(heal(heroes, cmd[1], int(cmd[2])))
    cmd = input()
heroes = dict(sorted(heroes.items(), reverse=False, key=lambda x: (-x[1][0], x[0])))
for hero, stats in heroes.items():
    print(f'{hero}\n  HP: {stats[0]}\n  MP: {stats[1]}')
