# clean + use LXML cleaner
tree = tree_cleaning(tree, inc_tables, inc_images)

# convert tags, the rest does not work without conversion
tree = convert_tags(tree, inc_formatting, inc_tables, inc_images, inc_links)

# comments first, then remove
if inc_comments is True:
    tree = extract_comments(tree, deduplicate, config)
else:
    if favor_precision is True:
        tree = prune_unwanted_nodes(tree, REMOVE_COMMENTS_XPATH)