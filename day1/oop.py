import math

class Vector2D:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

class Player:
    def __init__(self, name:str, position: Vector2D, direction: Vector2D, fov: int) -> None:
        self.name : str = name
        self.position: Vector2D = position
        self.direction: Vector2D = direction
        self.fov: int = fov

    def get_position_x(self) -> int:
        return self.position.x

    def get_position_y(self) -> int:
        return self.position.y

    def get_direction_x(self) -> int:
        return self.direction.x

    def get_direction_y(self) -> int:
        return self.direction.y

    def calculate_distance(self, other: Player) -> float:
        return math.sqrt((other.position.x - self.position.x) ** 2 + (other.position.y - self.position.y) ** 2)

    def is_visible(self, player: Player) -> bool:
        dx = player.position.x - self.position.x
        dy = player.position.y - self.position.y

        AB: float = (self.direction.x * dx) + (self.direction.y * dy)

        if AB == 0.0:
            return False
        elif AB > 0.0:
            return True
        elif AB < 0.0:
            return False

    def area_visible(self, players: list[Player]) -> list:
        players_are_visible: list = []

        for player in players:
            if self.is_visible(player):
                players_are_visible.append(player)

        return players_are_visible

    def area_fov_visible(self, players: list[Player]) -> list:
        players_are_visible: list = []

        for player in players:
            if self.is_visible(player) and self.fov > self.calculate_distance(player):
                players_are_visible.append(player)

        return players_are_visible