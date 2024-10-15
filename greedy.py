import random
import os
import argparse

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        tasks = []
        for _ in range(n):
            p, d = map(int, file.readline().strip().split())
            tasks.append((p, d))
        
        # Read the setup times (S)
        setup_times = []
        for _ in range(n):
            setup_times.append(list(map(int, file.readline().strip().split())))
    
    return n, tasks, setup_times

def write_output(filename, total_delay, order):
    with open(filename, 'w') as file:
        file.write(f"{total_delay}\n")
        file.write(" ".join(map(str, order)) + "\n")

def schedule_tasks(n, tasks, setup_times):
    # Sort tasks by due date (d)
    tasks_with_index = [(i, tasks[i][0], tasks[i][1]) for i in range(n)]  # (index, p, d)
    #tasks_with_index.sort(key=lambda x: (x[2], x[1]))  # x[2] to d, x[1] to p
    tasks_with_index.sort(key=lambda x: (x[1] / x[2], x[2]))  # x[1] to p, x[2] to d

    current_time = 0
    total_delay = 0
    order = []

    for index, p, d in tasks_with_index:
        order.append(index + 1)  # Indeks zadania (1-based)
        current_time += p  # Dodaj czas trwania
        if current_time > d:
            total_delay += min(p, max(0, current_time - d))  # Oblicz opóźnienie
        
        if len(order) > 1:  #  dodaj czas przezbrojenia jesli to nie 1 zad
            current_time += setup_times[order[-2] - 1][index]  # S[last_task][current_task]

    return total_delay, order

def process_files(input_directory):
    results_directory = os.path.join(input_directory, '../results')
    os.makedirs(results_directory, exist_ok=True)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.in'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(results_directory, f'151600_{filename[:-3]}.txt')
            
            n, tasks, setup_times = read_input(input_file)
            total_delay, order = schedule_tasks(n, tasks, setup_times)
            write_output(output_file, total_delay, order)
            
            print(f"Processed {filename}: Total delay = {total_delay}")


def main():
    parser = argparse.ArgumentParser(description='Process scheduling input files.')
    parser.add_argument('input_directory', type=str, help='Directory containing input .in files')
    args = parser.parse_args()

    process_files(args.input_directory)

if __name__ == "__main__":
    main()