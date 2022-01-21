text_node_parents = HtmlTree.execute_xpath_expression('/path/to/text()/..')

for node in text_node_parents:
    partitions = []
    for child in node.children:
        partitions.insert( TextSplitter().split( child ))
    node.children = partitions

histogram = {}
for node in text_node_parents:
    histogram[node.parent.path] = node.children.count

max_path = argmax(histogram)
main_text_nodes = [node for node in text_node_parents if max_path in node.path]