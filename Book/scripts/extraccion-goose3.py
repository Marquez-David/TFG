def childNodesWithText(cls, node):
    root = node
    if root.text:
        elm = lxml.html.HtmlElement()
        elm.text = root.text
        elm.tag = 'text'
        root.text = None
        root.insert(0, elm)
    for _, elm in enumerate(list(root)):
        idx = root.index(elm)
        if elm.tag == 'text':
            continue
        if elm.tail:
            tmp = cls.createElement(tag='text', text=elm.tail, tail=None)
            root.insert(idx + 1, tmp)
    return list(root)