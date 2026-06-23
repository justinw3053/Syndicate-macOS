import pytest
import ex_error_02 as active_lab

def test_finally_block():
    assert active_lab.audit_log == ["SUCCESS", "CLEANUP_RUN"] or active_lab.audit_log == ["ERROR_CAUGHT", "CLEANUP_RUN"], "The finally block did not execute. It must run regardless of success or failure."
