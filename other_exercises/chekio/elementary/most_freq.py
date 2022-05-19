import re


def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    num_data = []
    for i in data:
        num_data.append(data.count(i))  
    dic = dict(zip(data, num_data))
    sorted_tuple = sorted(dic.items(), key=lambda x: x[1])
    return sorted_tuple[-1][0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")