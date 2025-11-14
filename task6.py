 # Load JSON as dictionary and sort two lists of films by the 'year' field

import json

def main():
    # Read input data from file and process
    movies_data = read_input("input.txt")
    if movies_data is None:
        return

    merged_list = join_sorted_movie_lists(movies_data)
    if merged_list is not None:
        print(json.dumps(merged_list, ensure_ascii=False, indent=2))

# Reads JSON input from file, check, convert into dict
def read_input(filename):
    error = None
    data = None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data_str = file.read()
        data = json.loads(data_str)
    except json.JSONDecodeError:
        error = "Err: Input is not a valid JSON"

    if error is None:
        if "list1" not in data or "list2" not in data:
            error = "Err: no 'list1' or 'list2'"

    if error is None:
        list1 = data["list1"]
        list2 = data["list2"]

        for movie in list1 + list2:
            if not isinstance(movie, dict) or "year" not in movie:
                error = "Err: Movies must have 'year' field"
                break

    if error is not None:
        print(error)
        data = None

    return data

# Merges two sorted lists by the 'year'
def join_sorted_movie_lists(data):
    list1 = data["list1"]
    list2 = data["list2"]
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i]["year"] <= list2[j]["year"]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

if __name__ == "__main__":
    main()

