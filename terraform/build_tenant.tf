terraform {
  required_providers {
      aci = {
          source = "ciscodevnet/aci"
          version = "0.7"
      }
  }
}

# Configure ACI provider
provider "aci" {
    username = "admin"
    password = "ACI_PASSWORD"
    url = "https://10.10.20.14"
    insecure = true
}

resource "aci_tenant" "Villains" {
    name = "Villains"
    description = "Configured via Terraform"
}