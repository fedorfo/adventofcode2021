import heapq
from collections import OrderedDict
from typing import Optional

import utils


#    "#01.2.3.4.56#" - hall cells
#    "###0#1#2#3###" - rooms

distance_from_room_to_hall = [
    [2, 1, 1, 3, 5, 7, 8],
    [4, 3, 1, 1, 3, 5, 6],
    [6, 5, 3, 1, 1, 3, 4],
    [8, 7, 5, 3, 1, 1, 2],
]
nearest_left_hall = [1, 2, 3, 4]
nearest_right_hall = [2, 3, 4, 5]
infinity = 10 ** 9


best_score = 11340


class Position:
    def __init__(self, rooms: list[list[int]], hall: list[Optional[int]], room_depth: int):
        self.rooms = [[fish for fish in room] for room in rooms]
        self.hall = [hall_cell for hall_cell in hall]
        self.room_depth = room_depth
        self._id = None

    def is_final(self) -> bool:
        for room_id, room in enumerate(self.rooms):
            if any((x != room_id for x in room)):
                return False
        if any(x is not None for x in self.hall):
            return False
        return True

    def get_id(self) -> int:
        if not self._id:
            result = 0
            for hall_cell in self.hall:
                result *= 5
                result += hall_cell if hall_cell is not None else 4
            for room in self.rooms:
                for i in range(self.room_depth):
                    result *= 5
                    if len(room) > i:
                        result += room[i]
                    else:
                        result += 4
            self._id = result
        return self._id

    def get_next_positions(self) -> list[tuple["Position", int]]:
        result = []
        for room_id, room in enumerate(self.rooms):
            if any((x != room_id for x in room)):
                new_room = [*room]
                new_rooms = [x if i != room_id else new_room for i, x in enumerate(self.rooms)]
                current_fish = new_room.pop()
                new_hall = [*self.hall]
                hall_cell_candidates = []
                for hall_cell_id in range(nearest_left_hall[room_id], -1, -1):
                    if self.hall[hall_cell_id] is not None:
                        break
                    hall_cell_candidates.append(hall_cell_id)
                for hall_cell_id in range(nearest_right_hall[room_id], len(self.hall)):
                    if self.hall[hall_cell_id] is not None:
                        break
                    hall_cell_candidates.append(hall_cell_id)

                for hall_cell_id in hall_cell_candidates:
                    new_hall[hall_cell_id] = current_fish
                    result.append(
                        (
                            Position(new_rooms, new_hall, self.room_depth),
                            (distance_from_room_to_hall[room_id][hall_cell_id] + self.room_depth + 1 - len(room))
                            * (10 ** current_fish),
                        )
                    )
                    new_hall[hall_cell_id] = None

        for room_id, room in enumerate(self.rooms):
            if all((x == room_id for x in room)) and len(room) < self.room_depth:
                hall_cell_candidates = []
                for hall_cell_id in range(nearest_left_hall[room_id], -1, -1):
                    if self.hall[hall_cell_id] is not None:
                        if self.hall[hall_cell_id] == room_id:
                            hall_cell_candidates.append(hall_cell_id)
                        break
                for hall_cell_id in range(nearest_right_hall[room_id], len(self.hall)):
                    if self.hall[hall_cell_id] is not None:
                        if self.hall[hall_cell_id] == room_id:
                            hall_cell_candidates.append(hall_cell_id)
                        break

                new_room = [*room]
                new_rooms = [x if i != room_id else new_room for i, x in enumerate(self.rooms)]
                new_hall = [*self.hall]
                for hall_cell_id in hall_cell_candidates:
                    new_room.append(self.hall[hall_cell_id])
                    new_hall[hall_cell_id] = None
                    result.append(
                        (
                            Position(new_rooms, new_hall, self.room_depth),
                            (distance_from_room_to_hall[room_id][hall_cell_id] + self.room_depth - len(room))
                            * (10 ** room_id),
                        )
                    )
                    new_room.pop()
                    new_hall[hall_cell_id] = self.hall[hall_cell_id]
        return result

    def __str__(self):
        result = f"id: {self.get_id()}"
        result += f"\nrooms: {self.rooms}"
        result += f"\nhall: {self.hall}"
        result += "\n#############"
        letters = ["A", "B", "C", "D"]
        result += (
            "\n#"
            f"{letters[self.hall[0]] if self.hall[0] is not None else '.'}"
            f"{letters[self.hall[1]] if self.hall[1] is not None else '.'}."
            f"{letters[self.hall[2]] if self.hall[2] is not None else '.'}."
            f"{letters[self.hall[3]] if self.hall[3] is not None else '.'}."
            f"{letters[self.hall[4]] if self.hall[4] is not None else '.'}."
            f"{letters[self.hall[5]] if self.hall[5] is not None else '.'}"
            f"{letters[self.hall[6]] if self.hall[6] is not None else '.'}"
            "#"
        )
        for x in range(self.room_depth - 1, -1, -1):
            result += (
                f"\n  "
                f"#{letters[self.rooms[0][x]] if len(self.rooms[0]) > x else '.'}"
                f"#{letters[self.rooms[1][x]] if len(self.rooms[1]) > x else '.'}"
                f"#{letters[self.rooms[2][x]] if len(self.rooms[2]) > x else '.'}"
                f"#{letters[self.rooms[3][x]] if len(self.rooms[3]) > x else '.'}#"
            )
        result += "\n  #########"
        return result


def main():
    fishes = []
    with utils.open_input_file(day=23, example=False) as stdin:
        stdin.readline()
        stdin.readline()

    depth = len(fishes)
    rooms = [[ord(fishes[depth - j - 1][i]) - ord("A") for j in range(depth)] for i in range(4)]
    initial_position = Position(rooms, [None] * 7, depth)
    print(initial_position)

    dist = {initial_position.get_id(): 0}
    positions = {initial_position.get_id(): initial_position}
    marked = {initial_position.get_id(): False}
    heap = []
    heapq.heappush(heap, (0, initial_position.get_id()))

    while True:
        if len(heap) == 0:
            raise RuntimeError("BUG")
        current_dist, current_position_id = heapq.heappop(heap)
        if marked[current_position_id]:
            continue
        current_position = positions[current_position_id]
        print(f"Process distance {dist[current_position.get_id()]}")
        if current_position.is_final():
            print(f"{dist[current_position.get_id()]}")
            return
        for next_position, delta in current_position.get_next_positions():
            if (
                next_position.get_id() not in dist
                or dist[next_position.get_id()] > dist[current_position.get_id()] + delta
            ):
                dist[next_position.get_id()] = dist[current_position.get_id()] + delta
                heapq.heappush(heap, (dist[next_position.get_id()], next_position.get_id()))
                if next_position.get_id() not in marked:
                    positions[next_position.get_id()] = next_position
                    marked[next_position.get_id()] = False

        marked[current_position.get_id()] = True


main()
