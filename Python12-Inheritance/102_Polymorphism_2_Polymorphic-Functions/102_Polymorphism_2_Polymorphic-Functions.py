# 03-131: Polymorphic Functions

class Heading:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<h1>{self.content}</h1>'
    
class P:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<p>{self.content}</p>'

class Div:
    def __init__(self, *content):
        self.content = content

    def render(self):
        div_content = ''.join(
            [div_item.render() if hasattr(div_item, 'render') else str(div_item) for div_item in self.content]
            )
        
        return f'<div>{div_content}</div>'


heading = Heading('A big Heading')
div_one = Div(Heading('Another heading but div-tagged'))
div_two = Div(P('Content from another Div tag'))

def html_render(tag_object):
    print(tag_object.render())

html_render(heading)
html_render(div_one)
html_render(div_two)