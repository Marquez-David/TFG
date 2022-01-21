    for itm in parent_nodes:
        score = self.get_score(itm)
        if score > top_node_score:
            top_node = itm
            top_node_score = score
        if top_node is None:
            top_node = itm
    return top_node