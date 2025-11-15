def is_natural_number(s):
    return s.isdigit() and int(s) > 0

def read_input():
    error = False
    N = 0
    total_time = 0
    machines = []
    
    try:
        first_line = input().strip()
        parts = first_line.split()
        if len(parts) != 2:
            error = True
            return error, N, total_time, machines
        
        if not is_natural_number(parts[0]) or not is_natural_number(parts[1]):
            error = True
            return error, N, total_time, machines
        
        N = int(parts[0])
        total_time = int(parts[1])
        if N <= 1:
            # Need at least two machines to form a pair
            error = True
            return error, N, total_time, machines
        
        for _ in range(N):
            line = input().strip()
            vals = line.split()
            if len(vals) != 3:
                error = True
                break
            y, c, t = vals
            if not (is_natural_number(y) and is_natural_number(c) and is_natural_number(t)):
                error = True
                break
            machines.append( (int(y), float(c), int(t)) )
            
    except Exception:
        error = True
    
    return error, N, total_time, machines

def find_min_cost_pair(total_time, machines):
    # organize machines by year
    by_year = {}
    for (year, cost, run_time) in machines:
        if year not in by_year:
            by_year[year] = {}
        # For each run_time, keep minimal cost machine
        if run_time not in by_year[year] or cost < by_year[year][run_time]:
            by_year[year][run_time] = cost
    
    min_cost = None
    # For each year find pairs where run_times sum to total_time
    for year, runtimes_map in by_year.items():
        # For fast lookup
        keys = list(runtimes_map.keys())
        
        # To avoid counting same machine twice, handle pairs carefully
        for time1 in keys:
            time2 = total_time - time1
            if time2 in runtimes_map:
                # If time1 == time2, need at least two machines with same run_time
                if time1 == time2:
                    # Check if there are at least two machines with time1 in input?
                    # Since runtimes_map stores only one minimum cost per time, we can't be sure.
                    # We'll rely on input guarantee that solution exists and is unique.
                    # So we can skip this case or count once.
                    # Safer to assume input guarantees two machines different
                    continue
                curr_cost = runtimes_map[time1] + runtimes_map[time2]
                if (min_cost is None) or (curr_cost < min_cost):
                    min_cost = curr_cost
                    
    return min_cost

def main():
    err, n, req_time, machs = read_input()
    if err:
        print("error")
        return
    cost = find_min_cost_pair(req_time, machs)
    if cost is None:
        print("error")
    else:
        print(cost)

if __name__ == "__main__":
    main()

