import json
import re
from typing import Any, Dict, List, Tuple

NESTED = "."
REG_INDEX = r"(\[\d+\])"
regex = re.compile(REG_INDEX)


def get_element_value(element: str, data: Any, index=None) -> str:
    """Returns an element's value."""

    if index is None:
        try:
            value = data[element]
        except (KeyError, TypeError):
            value = None
    else:
        try:
            value = data[element][index]
        except (IndexError, KeyError, TypeError):
            value = None

    return value


def get_element_and_index_position(regex_result: Any, element: str) -> Tuple[str, int]:

    index_position = regex_result.group()
    index = int(index_position[1:-1])
    element_position = regex_result.span()[0]
    element = element[:element_position]

    return element, index


def search_value(element: str, data: Any) -> Any:
    """Get the element's value if exists."""

    index_exist = regex.search(element)

    if index_exist:
        element, index = get_element_and_index_position(index_exist, element)
        value = get_element_value(element, data, index)
    else:
        value = get_element_value(element, data)

    return value


def get_value(attribute: str, data: Dict) -> Tuple[str, Any]:
    """Iterate over the atrributes and get its value if exist."""

    if NESTED not in attribute:
        return search_value(attribute, data)

    attribute_list = attribute.split(".")
    sub_attribute = attribute_list.pop(0)
    remaining_attribute_string = ".".join(attribute_list)
    remaining_data = search_value(sub_attribute, data)

    return get_value(remaining_attribute_string, remaining_data)


def extractor(raw_data: str, attributes: List[str]) -> Dict:
    """Extract the wanted attributes from raw_data."""

    data = json.loads(raw_data)
    assert isinstance(data, dict)

    raw_attributes = [(attr, get_value(attr, data)) for attr in attributes]

    # filter attributes with valid values
    result = filter(lambda x: x[1], raw_attributes)

    return dict(result)
