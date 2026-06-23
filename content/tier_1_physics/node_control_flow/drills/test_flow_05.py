import pytest
import active_lab

def test_dispatcher_routing():
    assert active_lab.route_query('code', True) == 'compiler_agent', "Safe code intents should route to compiler_agent."
    assert active_lab.route_query('chat', True) == 'conversational_agent', "Safe chat intents should route to conversational_agent."
    assert active_lab.route_query('code', False) == 'quarantine', "Unsafe intents MUST route to quarantine."
    assert active_lab.route_query('random', True) == 'unknown', "Unrecognized intents should route to unknown."
