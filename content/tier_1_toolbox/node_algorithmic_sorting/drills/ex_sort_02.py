# PROBLEM: Sorting dictionaries by key value
#
# To sort complex dictionary lists, we use the `key` parameter with a lambda:
#    sorted_items = sorted(configs, key=lambda x: x["metric"])
#
# Your Task: Sort 'items' (list of dictionaries) by the key "metric" in descending order.

def sort_by_metric(items: list) -> list:
    # Step 1: Use sorted() with a lambda key pointing to the "metric" attribute
    sorted_list = sorted(items, key=lambda x: x["metric"], reverse=True)
    return sorted_list
