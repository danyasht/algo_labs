def read_input():
    tribes = {}
    girls = set()
    boys = set()

    with open("input.txt", "r") as file:
        num_pairs = int(file.readline().strip())

        for _ in range(num_pairs):
            pair = file.readline().strip().split()
            num1, num2 = map(int, pair)

            if num1 % 2 == 0:
                girls.add(num1)
            else:
                boys.add(num1)

            if num2 % 2 == 0:
                girls.add(num2)
            else:
                boys.add(num2)

            if not tribes:
                tribes[num1] = tribes[num2] = 0
            else:
                if num1 in tribes:
                    tribes[num2] = tribes[num1]
                elif num2 in tribes:
                    tribes[num1] = tribes[num2]
                else:
                    tribes[num1] = tribes[num2] = max(tribes.values()) + 1

    return tribes, boys, girls


def group_tribes(tribes, boys, girls):
    tribe_groups = {"boys": {}, "girls": {}}

    for person_set, group_type in [(boys, "boys"), (girls, "girls")]:
        for person in person_set:
            tribe = tribes.get(person)
            if tribe is not None:
                tribe_groups[group_type].setdefault(tribe, []).append(person)

    return tribe_groups


def count_pairs(tribe_groups):
    count = 0
    pairs = []

    for boys_tribe in tribe_groups["boys"]:
        for girls_tribe in tribe_groups["girls"]:
            if boys_tribe != girls_tribe:
                count += len(tribe_groups["boys"][boys_tribe]) * len(
                    tribe_groups["girls"][girls_tribe]
                )
                pairs.extend(
                    [
                        (b, g)
                        for b in tribe_groups["boys"][boys_tribe]
                        for g in tribe_groups["girls"][girls_tribe]
                    ]
                )

    return count, pairs


def write_output(count, pairs):
    with open("output.txt", "w") as file:
        file.write(f"Result: {count}\n")
        file.write("All pairs:\n")
        for pair in pairs:
            file.write(f"({pair[0]} / {pair[1]})\n")


if __name__ == "__main__":
    tribes, boys, girls = read_input()
    tribe_groups = group_tribes(tribes, boys, girls)
    count, pairs = count_pairs(tribe_groups)
    write_output(count, pairs)
