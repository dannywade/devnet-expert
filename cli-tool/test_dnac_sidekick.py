import requests
from click.testing import CliRunner
from dnac_sidekick import dnac_cli

"""
Tests for DNAC Sidekick CLI tool. Must have the following environment variables set:
- DNAC_URL
- DNAC_TOKEN
"""

def test_dnac_login():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['login', '--username', 'devnetuser', '--password', 'Cisco123!'])
    assert result.exit_code == 0

def test_dnac_get_devices():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['get', 'inventory', 'devices'])
    assert result.exit_code == 0

def test_dnac_get_device_by_hostname():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['get', 'inventory', 'devices', '--hostname', 'leaf1.abc.inc'])
    assert result.exit_code == 0

def test_dnac_get_device_health():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['get', 'health', 'devices'])
    assert result.exit_code == 0

def test_dnac_get_client_health():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['get', 'health', 'clients'])
    assert result.exit_code == 0

# TODO: Still needs tested. No client data available on always-on DevNet sandbox
def test_dnac_get_client_by_mac():
    requests.packages.urllib3.disable_warnings()
    runner = CliRunner()
    result = runner.invoke(dnac_cli, ['get', 'health', 'clients', '--mac', '0000.0000.0000'])
    assert result.exit_code == 0