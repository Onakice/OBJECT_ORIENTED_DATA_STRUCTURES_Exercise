def climb_tree(total_steps, obstacles, total_energy, energy_per_step):
    def find_ways(current_step, current_energy, path):
        nonlocal ways
        if current_step == total_steps:
            ways.append(path)
            return

        for i in range(1, 4):
            next_step = current_step + i
            if next_step <= total_steps:
                if next_step not in obstacles:
                    next_energy = current_energy - energy_per_step[i - 1]
                    if next_energy >= 0:
                        find_ways(next_step, next_energy, path + [next_step])

    ways = []
    find_ways(0, total_energy, [0])
    return ways

input_data = input("Creating a simulated hell scenario: ").strip().split('/')
total_steps = int(input_data[0])
obstacles = list(map(int, input_data[1].split(','))) if input_data[1] != '0' else [0]
total_energy = float(input_data[2])
energy_per_step = list(map(float, input_data[3].split(',')))

if len(energy_per_step) == 1:
    energy_per_step = [energy_per_step[0]] * 3
elif len(energy_per_step) == 2:
    energy_per_step.append(0)

ways_to_escape = climb_tree(total_steps, obstacles, total_energy, energy_per_step)

print(f"Height: {total_steps}")
print(f"thorn At: {[str(obstacle) for obstacle in obstacles]}")
print(f"Max Tiredness: {total_energy}")
print(f"Tiredness Values: {{1: {energy_per_step[0]}, 2: {energy_per_step[1]}, 3: {energy_per_step[2]}}}")
print("--------------------------------------------------")
print(f"The ways to escape is/are {len(ways_to_escape)} ways")
