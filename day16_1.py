from abc import ABC

import utils

hex_to_binary_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

binary_to_hex_map = {v: k for k, v in hex_to_binary_map.items()}


class Package(ABC):
    def __init__(self, version: int, type: int):
        self.version = version
        self.type = type

    def version_sum(self) -> int:
        ...


class ValuePackage(Package):
    def __init__(self, version: int, type: int, value: str):
        super().__init__(version, type)
        self.value = value

    def __str__(self):
        return f"ValuePackage, version={self.version}, value={self.value} ({int(self.value, 2)})"

    def version_sum(self) -> int:
        return self.version


class CompositePackage(Package):
    def __init__(self, version: int, type: int, packages: list[Package]):
        super().__init__(version, type)
        self.packages = packages

    def __str__(self):
        return f"CompositePackage, version={self.version} value=({','.join([str(x) for x in self.packages])})"

    def version_sum(self) -> int:
        return sum([x.version_sum() for x in self.packages]) + self.version


def parse_package(binary_value: str, index: int) -> tuple[Package, int]:
    package_version = int(binary_value[index : index + 3], 2)
    package_type = int(binary_value[index + 3 : index + 6], 2)
    current_index = index + 6
    if package_type == 4:

        value = ""
        while True:
            value = value + binary_value[current_index + 1 : current_index + 5]
            current_index += 5
            if binary_value[current_index - 5] == "0":
                break
        return (
            ValuePackage(version=package_version, type=package_type, value=value),
            current_index,
        )
    else:
        length_type_id = binary_value[current_index]
        current_index += 1
        if length_type_id == "0":
            total_length = int(binary_value[current_index : current_index + 15], 2)
            current_index += 15
            initial_position = current_index
            packages = []
            while True:
                child, current_index = parse_package(binary_value, current_index)
                packages.append(child)
                if current_index - initial_position == total_length:
                    break
            return (
                CompositePackage(package_version, package_type, packages),
                current_index,
            )
        else:
            total_count = int(binary_value[current_index : current_index + 11], 2)
            current_index += 11
            packages = []
            while True:
                child, current_index = parse_package(binary_value, current_index)
                packages.append(child)
                if len(packages) == total_count:
                    break
            return (
                CompositePackage(package_version, package_type, packages),
                current_index,
            )


def hex_to_binary(value: str) -> str:
    return "".join([hex_to_binary_map[x] for x in value])


def main():
    with utils.open_input_file(day=16, example=True) as stdin:
        while True:
            tokens = [*utils.read_tokens(stdin, str)]
            if not tokens:
                break
            hex_value = tokens[0]
            binary_value = hex_to_binary(hex_value)
            package = parse_package(binary_value, 0)[0]
            print(package.version_sum())


main()
