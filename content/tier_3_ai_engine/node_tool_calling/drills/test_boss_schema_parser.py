import pytest
import active_lab
def get_weather(location: str, fahrenheit: bool = True) -> str:
    '''Get the weather.'''
    pass
def test_function_to_schema():
    schema = active_lab.function_to_schema(get_weather)
    assert schema['type'] == 'function'
    assert schema['function']['name'] == 'get_weather'
    params = schema['function']['parameters']
    assert params['properties']['location']['type'] == 'string'
    assert 'location' in params['required']
