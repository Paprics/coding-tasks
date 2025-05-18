from HW20_testing.utils import formatted_name

fn = 'jon'
ln = 'die'
mn = 'mortimer'

def test_formatted_name_valid():
    assert formatted_name(fn, ln) == f'{fn.title()} {ln.title()}', f'value - {fn=} {ln=}'

def test_formatted_name_valid_mn():
    assert formatted_name(fn, ln, mn) == f'{fn.title()} {mn.title()} {ln.title()}', f'value - {fn=} {ln=} {mn}'