from typing import Optional

import utils


def dfs(
    graph: dict[str, set[str]],
    visited: Optional[dict[str, int]] = None,
    way: Optional[list[str]] = None,
    current_vertex: str = "start",
) -> int:
    if visited is None:
        visited = {}
        for key in graph.keys():
            visited[key] = 0
    if way is None:
        way = []

    visited[current_vertex] += 1
    way.append(current_vertex)
    if current_vertex == "end":
        print(",".join(way))
        return 1

    result = 0
    for vertex in graph[current_vertex]:
        has_twice_visited_small_cave = max(
            value
            for key, value in visited.items()
            if key.upper() != key and key not in ("start", "end")
        ) > 1

        if (
            vertex.upper() == vertex
            or (vertex not in ("start", "end") and not has_twice_visited_small_cave and visited[vertex] < 2)
            or visited[vertex] < 1
        ):
            result += dfs(graph, visited, way, vertex)
            way.pop()
            visited[vertex] -= 1

    return result


def main():
    graph = {}
    with utils.open_input_file(day=12) as stdin:
        while True:
            tokens = [*utils.read_tokens(stdin, str, separator="[ \n-]+")]
            if not tokens:
                break

            graph[tokens[0]] = (
                set() if graph.get(tokens[0]) is None else graph.get(tokens[0])
            )
            graph[tokens[1]] = (
                set() if graph.get(tokens[0]) is None else graph.get(tokens[1])
            )

            if not graph.get(tokens[1]):
                graph[tokens[1]] = set()

            graph[tokens[0]].add(tokens[1])
            graph[tokens[1]].add(tokens[0])

    result = dfs(graph)
    print(result)


main()
