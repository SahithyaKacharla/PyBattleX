import random

class Player:
    def __init__(self, name, hp, attack_power, ability_name):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.ability_name = ability_name

    def attack(self):
        return self.attack_power + random.randint(-3, 5)

    def ability(self):
        return int((self.attack_power + random.randint(0, 5)) * 2)

    def heal(self):
        heal_amount = random.randint(8, 15)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        return heal_amount


class BattleGame:
    def __init__(self):
        self.players = {
            "Wonder women": Player("Wonderwoman", 100, 15, "Celestial Strike"),
            "SpiderMan": Player("Flashman", 110, 13, "Flame Burst"),
            "Hulk": Player("Hulk", 120, 18, "Volt Crash"),
            "Flashman": Player("Spiderman", 105, 12, "Earthquake"),
            "Superman": Player("Superman", 115, 14, "Nightshade")
        }

    def choose_player(self):
        print("\nAvailable players:", ", ".join(self.players.keys()))
        choice = input("Select your Hero: ").strip().title()

        if choice not in self.players:
            print("Custom hero created!")
            self.players[choice] = Player(choice, 100, 15, "Mystic Blast")

        return self.players[choice]

    def create_enemy(self):
        names = ["Dark Knight", "Shadow Beast", "Cyber Titan"]
        return Player(random.choice(names), 110, 14, "Dark Fury")

    def start(self):
        print("\n--- GAME STARTS ---")
        user = self.choose_player()
        enemy = self.create_enemy()

        # Reset HP for replay safety
        user.hp = user.max_hp

        print(f"\n⚔️ BATTLE: {user.name} vs {enemy.name} ⚔️")

        while user.hp > 0 and enemy.hp > 0:
            print(f"\n{user.name}: {user.hp} HP | {enemy.name}: {enemy.hp} HP")

            print("\nChoose Action:")
            print("1. Attack")
            print("2. Use Ability")
            print("3. Heal")

            choice = input("Enter choice (1/2/3): ")

            if choice == "1":
                damage = user.attack()
                print(f"You attacked and dealt {damage} damage!")

            elif choice == "2":
                if random.random() < 0.4:
                    damage = user.ability()
                    print(f"🔥 {user.ability_name} activated! {damage} damage!")
                else:
                    damage = 0
                    print("❌ Ability missed!")

            elif choice == "3":
                healed = user.heal()
                print(f"💚 You healed {healed} HP!")
                damage = 0

            else:
                print("Invalid choice! Turn skipped.")
                damage = 0

            enemy.hp -= damage

            if enemy.hp <= 0:
                print(f"\n🏆 VICTORY! {user.name} wins!")
                break

            # Enemy turn
            comp_damage = enemy.attack()
            user.hp -= comp_damage
            print(f"{enemy.name} attacks and deals {comp_damage} damage!")

            if user.hp <= 0:
                print(f"\n💀 DEFEAT! {user.name} was defeated.")

# Start game
BattleGame().start()