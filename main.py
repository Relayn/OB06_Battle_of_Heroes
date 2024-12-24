import random

class Game:
    def __init__(self, player_name):
        """Инициализация игры с игроком и компьютером."""
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Основной цикл игры."""
        print("Игра началась!")
        turn = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n--- Ход {turn} ---")  # Вывод номера хода
            # Ход игрока
            player_damage = self.player.attack(self.computer)
            print(f"{self.player.name} нанёс {player_damage} урона {self.computer.name}.")
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            computer_damage = self.computer.attack(self.player)
            print(f"{self.computer.name} нанёс {computer_damage} урона {self.player.name}.")
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

            turn += 1

            # Вывод текущего состояния
            print(f"\nСостояние после хода:")
            print(f"{self.player.name}: {self.player.health} здоровья")
            print(f"{self.computer.name}: {self.computer.health} здоровья")
        print("Игра окончена.")

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        """Инициализация героя с именем, здоровьем и силой удара."""
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Наносит случайный урон другому герою."""
        damage = random.randint(5, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} на {damage} урона!")
        return damage # Возвращаем урон для информации

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

if __name__ == "__main__":
    game = Game(player_name="Игрок")
    game.start()



