def remove_duplicates(data_list):
    seen = set()
    unique_data = []

    for item in data_list:
        # Convert the dictionary to a frozenset of its items (makes it hashable)
        item_frozen = frozenset(item.items())
        if item_frozen not in seen:
            seen.add(item_frozen)
            unique_data.append(item)

    return unique_data
if __name__ == "__main__":
    sample_data = [
        { "name": "Vijay", "email": "Vijayananthperumal123@gmail.com" },
        { "name": "Bala", "email": "balablast@example.com" },
        { "name": "Lakshmi", "email": "lakshmi@gmail.com" },
        { "name": "Naveen", "email": "naveensec@gmail.com" },
        { "name": "Poornima", "email": "pooja@123" }, 
        { "name": "Vijay", "email": "Vijayananthperumal123@gmail.com" }
    ]

    result = remove_duplicates(sample_data)
    print("Cleaned Data:", result)
