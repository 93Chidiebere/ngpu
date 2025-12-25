from ngpu import Index


def test_states_not_empty():
    states = Index.states()
    assert isinstance(states, list)
    assert len(states) > 0


def test_lgas_returns_list():
    states = Index.states()
    lgas = Index.lgas(states[0])
    assert isinstance(lgas, list)