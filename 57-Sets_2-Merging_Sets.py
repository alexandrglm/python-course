# 03-079: Merging sets

tags_one = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

tags_two = {
    'ruby',
    'coding',
    'tutorials',
    'development'
}

# 1 - "|" -  Merged tags with pipes |

merged_tags = tags_one | tags_two
print(merged_tags)      # {'ruby', 'tutorials', 'coding', 'python', 'development'}



# 2- "-" -  tags in tags_one but not in tags_two

exclusive_to_tag_one = tags_one - tags_two
exclusive_to_tag_two = tags_two - tags_one

print('\nTags One: ', tags_one)
print('\nTags Two: ', tags_two)

print('\nExclusive tags from tags_one:  ', exclusive_to_tag_one)
print('\nExclusive tags from tags_two:  ', exclusive_to_tag_two)


# 3 - "&"" - Matches found in both sets

universal_tags = tags_one & tags_two
print('\nUniversal Tags:  ', universal_tags)