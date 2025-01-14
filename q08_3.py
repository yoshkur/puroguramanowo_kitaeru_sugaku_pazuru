# P.41


from pydantic import BaseModel


IDO_KAISU = 12


class Position(BaseModel):
    tate: int
    yoko: int

    def get_up_position(self):
        return Position(tate=self.tate + 1, yoko=self.yoko)

    def get_down_position(self):
        return Position(tate=self.tate - 1, yoko=self.yoko)

    def get_right_position(self):
        return Position(tate=self.tate, yoko=self.yoko + 1)

    def get_left_position(self):
        return Position(tate=self.tate, yoko=self.yoko - 1)


def move(log: list) -> int:
    if len(log) == IDO_KAISU + 1:
        return 1

    count = 0
    current_position = log[-1]
    next_position_up = current_position.get_up_position()
    if next_position_up not in log:
        count += move(log=log + [next_position_up])
    next_position_down = current_position.get_down_position()
    if next_position_down not in log:
        count += move(log=log + [next_position_down])
    next_position_right = current_position.get_right_position()
    if next_position_right not in log:
        count += move(log=log + [next_position_right])
    next_position_left = current_position.get_left_position()
    if next_position_left not in log:
        count += move(log=log + [next_position_left])
    return count


if __name__ == '__main__':
    print(move(log=[Position(tate=0, yoko=0)]))
