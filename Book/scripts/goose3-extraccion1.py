def calculate_best_node(self, doc):
    nodes_to_check = self.nodes_to_check(doc)

    for node in nodes_to_check:
        text_node = self.parser.getText(node)
        word_stats = self.stopwords_class(...get_stopword_count(text_node))
        high_link_density = self.is_highlink_density(node)
        if word_stats.get_stopword_count() > 2 and not high_link_density:
            nodes_with_text.append(node)