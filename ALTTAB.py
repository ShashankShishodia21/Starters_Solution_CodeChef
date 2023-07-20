def get_alt_tab_order(programs):
    active_programs = set()
    order = ""

    for program in reversed(programs):
        if program not in active_programs:
            active_programs.add(program)
            order += program[-2:]

    return order

# Read input
N = int(input())
programs = []
for _ in range(N):
    program = input().strip()
    programs.append(program)

# Get the alt + tab order
alt_tab_order = get_alt_tab_order(programs)

# Print the result in reverse order
print(alt_tab_order)