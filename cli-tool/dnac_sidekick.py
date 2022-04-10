#!/usr/bin/env python

from ast import Pass
import click
import requests
from requests.auth import HTTPBasicAuth
from rich.console import Console
from rich.table import Table
import os

requests.packages.urllib3.disable_warnings()

@click.group()
def dnac_cli():
    pass

@dnac_cli.group()
def get():
    """ Action for read-only tasks and gathering information. """
    click.echo("Getting information...")
    pass

@get.group()
def inventory():
    """ Gathers information related to device inventory in DNAC """
    pass

@get.group()
def health():
    """ Gathers health information for network devices and clients in DNAC """
    pass

@dnac_cli.command()
@click.option("--dnac_url", default="https://sandboxdnac.cisco.com", show_default=True, help="IP/hostname to the DNA Center appliance")
@click.option("--username", default="", help="User for login account")
@click.password_option(help="Password for login account")
def login(dnac_url, username, password):
    """ Use username and password to authenticate to DNAC. """
    click.echo("Attempting to login to DNAC...")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    dnac_token_url = f"{dnac_url}/dna/system/api/v1/auth/token"
    token = requests.post(url=dnac_token_url, headers=headers, auth=HTTPBasicAuth(username=username, password=password), verify=False)
    if token.status_code == 200:
        actual_token = token.json()["Token"]
        click.echo("Token generated successfully!")
        click.echo(f"COPY THIS TOKEN: {actual_token}")
    else:
        click.echo("Token not generated. Please try again...")

@inventory.command()
@click.option("--dnac_url", default=lambda: os.environ.get('DNAC_URL', ''), help=" Reads 'DNAC_URL' environment variable. If not set, please provide the IP/hostname to the DNA Center appliance")
@click.option("--token", required=True, hide_input=True, default=lambda: os.environ.get('DNAC_TOKEN', ''), help="Reads 'DNAC_TOKEN' environment variable. If not set, please provide the token string.")
@click.option("--hostname", default="", help="Specify a device's hostname to retrieve from inventory")
def devices(dnac_url, token, hostname):
    """ Retrieve all devices from DNAC inventory """
    click.echo("Attempting to login to DNAC...")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": token,
    }
    if hostname:
        dnac_devices_url = f"{dnac_url}/dna/intent/api/v1/network-device?hostname={hostname}"
    else:
        dnac_devices_url = f"{dnac_url}/dna/intent/api/v1/network-device"
    response = requests.get(url=dnac_devices_url, headers=headers, verify=False)
    device_list = response.json()["response"]
    if response.status_code == 200:
        table = Table(title="DNAC Network Devices")
        table.add_column("Hostname", justify="left", style="purple")
        table.add_column("Device Type", justify="left", style="cyan")
        table.add_column("Serial Number", justify="center", style="green")
        table.add_column("Software Version", justify="right", style="red")
        
        for device in device_list:
            table.add_row(device["hostname"], device["type"], device["serialNumber"], device["softwareVersion"])
        
        console = Console()
        console.print(table)
        # click.echo(f"Here's a list of devices: {console.print(table)}")
    elif response.status_code == 401:
        click.echo("Unauthorized. Please verify your token is valid.")
    else:
        click.echo("Could not retrieve list of network devices from DNAC.")


@health.command()
@click.option("--dnac_url", default=lambda: os.environ.get('DNAC_URL', ''), help=" Reads 'DNAC_URL' environment variable. If not set, please provide the IP/hostname to the DNA Center appliance")
@click.option("--token", required=True, hide_input=True, default=lambda: os.environ.get('DNAC_TOKEN', ''), help="Reads 'DNAC_TOKEN' environment variable. If not set, please provide the token string.")
def devices(dnac_url, token):
    """ Retrieve device health for all devices in DNAC inventory """
    click.echo("Attempting to login to DNAC...")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": token,
    }
    dnac_device_health = f"{dnac_url}/dna/intent/api/v1/device-health"
    response = requests.get(url=dnac_device_health, headers=headers, verify=False)
    device_list = response.json()["response"]
    if response.status_code == 200:
        table = Table(title="DNAC Network Health")
        table.add_column("Hostname", justify="left", style="purple")
        table.add_column("Overall Health", justify="left", style="cyan")
        table.add_column("CPU Util (%)", justify="center", style="green")
        table.add_column("Memory Util (%)", justify="right", style="red")
        
        for device in device_list:
            if device.get("overallHealth", -1) < 0:
                device_overall = "N/A"
            else:
                device_overall = str(device.get("overallHealth", "N/A"))
            device_cpu_util = str(device.get("cpuUlitilization", "N/A"))
            device_mem_util = str(device.get("memoryUtilization", "N/A"))
            table.add_row(device["name"], device_overall, device_cpu_util, device_mem_util)
        
        console = Console()
        console.print(table)
    elif response.status_code == 401:
        click.echo("Unauthorized. Please verify your token is valid.")
    else:
        click.echo("Could not retrieve list of network devices from DNAC.")

@health.command()
@click.option("--dnac_url", default=lambda: os.environ.get('DNAC_URL', ''), help=" Reads 'DNAC_URL' environment variable. If not set, please provide the IP/hostname to the DNA Center appliance")
@click.option("--token", required=True, hide_input=True, default=lambda: os.environ.get('DNAC_TOKEN', ''), help="Reads 'DNAC_TOKEN' environment variable. If not set, please provide the token string.")
@click.option("--mac", default="", help="Specify a client's MAC address for more details")
def clients(dnac_url, token, mac):
    """ Retrieve client health for all tracked clients in DNAC """
    click.echo("Attempting to login to DNAC...")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": token,
    }
    if mac:
        dnac_client_health = f"{dnac_url}/dna/intent/api/v1/client-health?macAddress={mac}"
    else:
        dnac_client_health = f"{dnac_url}/dna/intent/api/v1/client-health"
    response = requests.get(url=dnac_client_health, headers=headers, verify=False)
    device_list = response.json()["response"]
    if response.status_code == 200:
        table = Table(title="DNAC Client Health")
        table.add_column("Client Type", justify="left", style="purple")
        table.add_column("Client Count", justify="center", style="cyan")
        table.add_column("Client Health Score", justify="right", style="green")
        
        for device in device_list:
            if device.get("siteId") == "global":
                for score in device.get("scoreDetail"):
                    client_type = score["scoreCategory"]["value"]
                    client_count = str(score["clientCount"]) if score["clientCount"] > 0 else "0"
                    client_score = str(score["scoreValue"]) if score["scoreValue"] > 0 else "0"

                    table.add_row(client_type, client_count, client_score)
        
        console = Console()
        console.print(table)
    elif response.status_code == 401:
        click.echo("Unauthorized. Please verify your token is valid.")
    else:
        click.echo("Could not retrieve list of network devices from DNAC.")

if __name__ == "__main__":
    dnac_cli()