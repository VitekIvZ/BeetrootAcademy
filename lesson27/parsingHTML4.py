from bs4 import BeautifulSoup

class DOMTree:
    def __init__(self, tag=None, text=None):
        self.tag = tag  
        self.text = text  
        self.children = []  

    def add_child(self, child):
        self.children.append(child)

    def find_text_by_tag(self, tag):
        if self.tag == tag:
            return self.text
        for child in self.children:
            result = child.find_text_by_tag(tag)
            if result:
                return result
        return None

    def __str__(self, indent=0):
        result = " " * indent + f"Tag: {self.tag}, Text: {self.text}\n"
        for child in self.children:
            result += child.__str__(indent + 4)
        return result


def parse_html_to_dom(html):
    soup = BeautifulSoup(html, 'html.parser')
    root = DOMTree(tag=soup.name, text=soup.string)

    def build_dom_tree(element, dom_node):
        for child in element.children:
            if child.name: 
                child_node = DOMTree(tag=child.name, text=child.string)
                dom_node.add_child(child_node)
                build_dom_tree(child, child_node)
            elif child.strip(): 
                text_node = DOMTree(tag=None, text=child.strip())
                dom_node.add_child(text_node)

    build_dom_tree(soup, root)
    return root


if __name__ == '__main__':
    html_doc = """
    <html>
        <head>
            <title>Sample Page</title>
        </head>
        <body>
            <h1>This is a heading</h1>
            <p>This is a paragraph.</p>
            <div>
                <p>This is another paragraph.</p>
            </div>
        </body>
    </html>
    """

    # Парсимо HTML-документ і будуємо DOM-дерево
    dom_tree = parse_html_to_dom(html_doc)

    # Виводимо DOM-дерево
    print("DOM-дерево:")
    print(dom_tree)

    # Пошук тексту за тегом
    tag_to_find = "title"
    text = dom_tree.find_text_by_tag(tag_to_find)
    print(f"\nТекст за тегом '{tag_to_find}': {text}")

    tag_to_find = "p"
    text = dom_tree.find_text_by_tag(tag_to_find)
    print(f"Текст за тегом '{tag_to_find}': {text}")
