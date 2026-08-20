from pharma_interactions.engine import check

def test_order_independent_lookup():
    assert len(check("warfarin", "aspirin")) == 1
    assert len(check("aspirin", "warfarin")) == 1

def test_unknown_pair():
    assert check("drug-x", "drug-y") == []
