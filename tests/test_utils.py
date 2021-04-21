import pytest

from app.utils import extractor, get_element_value, get_value, search_value


@pytest.mark.parametrize("attr,data,index", [("key", {}, None), ("key", [], 0)])
def test_get_element_value_returns_none(attr, data, index):
    nested_value = get_element_value(attr, data, index)
    assert nested_value is None


def test_search_value_with_no_data_returns_none():
    value = search_value("attr_1", None)
    assert value is None


def test_search_value_with_list_element():
    value = search_value("attr_1[0]", {"attr_1": ["foo", "bar"]})
    assert value == "foo"


def test_search_value_with_dict_element():
    value = search_value("attr_1", {"attr_1": ["foo", "bar"]})
    assert value == ["foo", "bar"]


@pytest.mark.parametrize(
    "attr,value", [("foo", {"bar": [1]}), ("foo.bar", [1]), ("foo.bar[0]", 1)]
)
def test_get_value(attr, value):
    data = {"foo": {"bar": [1]}}
    result = get_value(attr, data)
    assert result == value


def test_extractor_raise_if_no_dict_data():
    with pytest.raises(AssertionError):
        extractor("[]", [])


def test_extractor_returns_ok():
    raw_data = '{"foo": {"bar": [1]}}'
    attributes = ["foo", "foo.bar", "foo[1]", "foo.bar[0]"]
    result = extractor(raw_data, attributes)
    assert len(result) == 3
    assert result["foo"] == {"bar": [1]}
    assert result["foo.bar"] == [1]
    assert result["foo.bar[0]"] == 1
