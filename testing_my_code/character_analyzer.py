def how_many_times(path, search):
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if search.lower() in line.lower():
                matches.append({
                    "line_number": line_number,
                    "text": line.strip()
                })
    return matches
