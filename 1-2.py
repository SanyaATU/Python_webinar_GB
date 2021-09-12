cube_list = []
n_cube_list = []
nn_cube_list = []

for i in range(1, 1001, 2):
    i = i ** 3
    cube_list.append(i)
print(f"cube_list = {cube_list}")

for i in range(0, len(cube_list)):
    i_sum = 0
    while cube_list[i] > 0:
        i_sum += cube_list[i] % 10
        cube_list[i] = cube_list[i] // 10
    cube_list[i] = i_sum
    all_sum = 0
    if cube_list[i] % 7 == 0:
        n_cube_list.append(cube_list[i])
        all_sum += cube_list[i]
    cube_list[i] = all_sum

for i in range(len(n_cube_list)):
    n_cube_list[i] = n_cube_list[i] + 17
print(f"n_cube_list = {n_cube_list}")

for i in range(0, len(n_cube_list)):
    i_sum = 0
    while n_cube_list[i] > 0:
        i_sum += n_cube_list[i] % 10
        n_cube_list[i] = n_cube_list[i] // 10
    n_cube_list[i] = i_sum
    all_sum = 0
    if n_cube_list[i] % 7 == 0:
        nn_cube_list.append(n_cube_list[i])
        all_sum += n_cube_list[i]
    n_cube_list[i] = all_sum
print(f"nn_cube_list = {nn_cube_list}")
