import pytest
import active_lab

def test_auditor():
    ILLEGAL = [("START", "WRITE_DB")]
    MANDATORY = ["AUTH_CHECK"]
    
    clean = ["START", "AUTH_CHECK", "WRITE_DB", "END"]
    assert len(active_lab.audit_trajectory(clean, ILLEGAL, MANDATORY)) == 0
    
    malicious = ["START", "WRITE_DB", "END"]
    errs = active_lab.audit_trajectory(malicious, ILLEGAL, MANDATORY)
    assert len(errs) == 2 # Missing check + Illegal jump
