import pytest
import active_lab

def test_state_router():
    routing_graph = {
        "START": ["GET_INPUT"],
        "GET_INPUT": ["VALIDATE", "ERROR"],
        "VALIDATE": ["EXECUTE", "GET_INPUT"],
        "EXECUTE": ["END"],
        "ERROR": ["GET_INPUT"]
    }
    assert active_lab.is_transition_legal(routing_graph, "START", "GET_INPUT") == True
    assert active_lab.is_transition_legal(routing_graph, "START", "VALIDATE") == False
