# 03-079: Merging sets, as Symbols

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

# 1 - Union operator "|" -  As union()

merged_tags = tags_one | tags_two
print(merged_tags)      # {'ruby', 'tutorials', 'coding', 'python', 'development'}



# 2- Difference Operator "-" - As difference() 

# Tags present in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two

# Tags present in tags_two but not in tags_one
exclusive_to_tag_two = tags_two - tags_one

print('\nTags One: ', tags_one)
print('\nTags Two: ', tags_two)

print('\nExclusive tags from tags_one:  ', exclusive_to_tag_one)
print('\nExclusive tags from tags_two:  ', exclusive_to_tag_two)




# 3 Intersection operator - "&"" - As intersection()

universal_tags = tags_one & tags_two
print('\nUniversal Tags:  ', universal_tags)



