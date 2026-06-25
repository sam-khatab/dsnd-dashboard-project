from .base_component import BaseComponent
from fasthtml.common import Input, Label, Div

class Radio(BaseComponent):

    def __init__(self, values, name, hx_get="", hx_target="", selected=""):
        self.values = values
        self.name = name
        self.hx_get=hx_get
        self.hx_target=hx_target
        self.selected=selected


    def build_component(self, entity_id, model):

        children = []
        print(f"Rebuilding Radio component for model: {model.name}, entity_id: {entity_id}, selected: {self.selected}")
        print(f"Available values: {self.values}")
        for value in self.values:
            is_selected = value == model.name.title()
            print(f"Building option: {model.name}, text={value}, value={value}, is_selected={is_selected}")            
            input_child = Input(type="radio", id=value.lower(), name=self.name, value=value, hx_get=self.hx_get, hx_target=self.hx_target, checked=is_selected)
            label_child = Label(value, _for=value.lower())
            children.append(input_child)
            children.append(label_child)

        return children
    
    def outer_div(self, component):
        return Div(
            *component
        )