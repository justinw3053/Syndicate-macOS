import pytest
import active_lab
import os
import json

def test_boss_document_scraper(tmp_path):
    workspace = os.path.join(tmp_path, "source_docs")
    os.makedirs(workspace, exist_ok=True)
    
    doc1 = os.path.join(workspace, "doc1.txt")
    with open(doc1, "w") as f:
        f.write("   Hello from text doc 1\nNewline characters should be removed!   ")
        
    doc2 = os.path.join(workspace, "sub", "doc2.txt")
    os.makedirs(os.path.dirname(doc2), exist_ok=True)
    with open(doc2, "w") as f:
        f.write("Doc 2 metrics log   ")
        
    out_json = os.path.join(tmp_path, "output", "db.json")
    
    count = active_lab.compile_document_database(workspace, "http://mock.api", out_json)
    
    assert count == 2
    assert os.path.exists(out_json)
    
    with open(out_json, "r") as f:
        data = json.load(f)
        
    assert len(data) == 2
    assert data[0]["file_name"] == "doc1.txt"
    assert "removed!" in data[0]["content"]
    assert not data[0]["content"].startswith(" ")
    assert data[0]["meta"]["source_api"] == "http://mock.api"
