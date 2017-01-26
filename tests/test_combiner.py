from mock import patch

from src.combiner import Combiner


@patch('src.combiner.NameAPI')
@patch('src.combiner.GeolocationAPI')
@patch('src.combiner.CategorizationAPI')
def test_if_name_confidence_is_low_we_always_return_none(
    CategorizationAPI,
    GeolocationAPI,
    NameAPI):
    """
    Suppose the NameAPI returns this data:
    {confidence: .5, value: "Chipotle"}

    and the CategorizationAPI returns this data:
    {confidence: .99, value: "Guacamole"}

    and the GeoLocationAPI returns this data:
    {confidence: .88, city: "New York", state: "NY"}

    then....the combiner should return this data:
    None
    """
    NameAPI.return_value.process.return_value = {
        "confidence": .5, "value": "Chipotle"
    }

    CategorizationAPI.return_value.process.return_value = {
        "confidence": .88, "value": "Guacamole"
    }

    GeolocationAPI.return_value.process.return_value = {
        "confidence": .99,
        "city": "New York",
        "state": "NY"
    }

    result = Combiner("SOME DIRTY STRING").combine()
    assert result == None

    NameAPI.assert_called_once_with("SOME DIRTY STRING")
    NameAPI.return_value.process.assert_called_once_with()

    assert GeolocationAPI.called == False
    assert CategorizationAPI.called == False


@patch('src.combiner.NameAPI')
@patch('src.combiner.GeolocationAPI')
@patch('src.combiner.CategorizationAPI')
def test_dont_include_geo(
    CategorizationAPI,
    GeolocationAPI,
    NameAPI):
    NameAPI.return_value.process.return_value = {
        "confidence": .8, "value": "Chipotle"
    }

    CategorizationAPI.return_value.process.return_value = {
        "confidence": .88, "value": "Guacamole"
    }

    GeolocationAPI.return_value.process.return_value = {
        "confidence": .4,
        "city": "New York",
        "state": "NY"
    }

    result = Combiner("SOME DIRTY STRING").combine()
    expected_result = {
        "name": {"confidence": .8, "value": "Chipotle"},
        "category": {"confidence": .88, "value": "Guacamole"}
    }
    assert result == expected_result

    NameAPI.assert_called_once_with("SOME DIRTY STRING")
    NameAPI.return_value.process.assert_called_once_with()

    GeolocationAPI.assert_called_once_with("SOME DIRTY STRING")
    GeolocationAPI.return_value.process.assert_called_once_with()

    CategorizationAPI.assert_called_once_with("SOME DIRTY STRING")
    CategorizationAPI.return_value.process.assert_called_once_with()
