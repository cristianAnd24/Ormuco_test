def compare_versions(version1, version2):
    v1_components = [int(x) for x in version1.split(".")]
    v2_components = [int(x) for x in version2.split(".")]

    max_length = max(len(v1_components), len(v2_components))
    
    # If the lengths of version lists are not equal, append zeros to the shorter one
    v1_components += [0] * (max_length - len(v1_components))
    v2_components += [0] * (max_length - len(v2_components))

    for i in range(max_length):
        if v1_components[i] > v2_components[i]:
            return 1
        elif v1_components[i] < v2_components[i]:
            return -1

    return 0

def test():
    test_cases = [
        ("1.0", "1.0", 0),
        ("1.2", "1.1", 1),
        ("1.0.1", "1.0", 1),
        ("1.0", "1.0.1", -1),
        ("1.0", "1.0.0", 0),
        ("1.0.0.0.1", "1.0.0", 1),
        ("2.0", "10.0", -1),
        ("10.0", "2.0", 1),
        ("2.1", "2.0.5", 1),
        ("2.0.0.0.0", "2.0", 0),
        ("1.2.3.4.5.6.7.8", "1.2.3.4.5.6.7.8", 0)
    ]

    for v1, v2, expected in test_cases:
        result = compare_versions(v1, v2)
        assert result == expected, f"Expected {expected} for {v1} vs {v2}, but got {result}"

    print("All tests passed!")

test()
