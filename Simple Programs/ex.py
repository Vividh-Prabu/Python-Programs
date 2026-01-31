def compress_ranges(nums):
    if not nums:
        return []

    result = []
    start = nums[0]
    prev = nums[0]

    for n in nums[1:]:
        if n == prev + 1:
            # still consecutive
            prev = n
        else:
            # range ended
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = n
            prev = n

    # add the final range
    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")

    return result


# Example Input
nums = [1, 2, 3, 5, 6, 8]
print(compress_ranges(nums))
