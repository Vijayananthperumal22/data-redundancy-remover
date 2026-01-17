def remove_duplicates(data_list):
    seen = set()
    unique_data = []

    for item in data_list:
        # Convert dictionary to a hashable form
        item_frozen = frozenset(item.items())
        if item_frozen not in seen:
            seen.add(item_frozen)
            unique_data.append(item)

    return unique_data


if __name__ == "__main__":
    sample_data = [
        {"name": "Vijay", "email": "Vijayananthperumal123@gmail.com"},
        {"name": "Bala", "email": "bala@example.com"},
        {"name": "surya", "email": "suryaremo3@gmail.com"},
        {"name": "gowsalya", "email": "gowsalyaperumal@gmail.com"},
        {"name": "Naveen", "email": "naveensec@gmail.com"},
        {"name": "Poornima", "email": "pooja@2022"},
        {"name": "Vijay", "email": "Vijayananthperumal22@gmail.com"}
    ]

    result = remove_duplicates(sample_data)
    print("Cleaned Data:", result)
