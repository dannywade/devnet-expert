terraform {
  required_providers {
    aci = {
      source  = "ciscodevnet/aci"
      version = "0.7"
    }
  }
}

# Configure ACI provider
provider "aci" {
  username = "admin"
  password = "C1sco12345"
  url      = var.apic_url
  insecure = true
}

resource "aci_tenant" "Villains" {
  name        = "Villains"
  description = "Configured via Terraform"
}

# NETWORK RESOURCES
# VRF
resource "aci_vrf" "blue_vrf" {
  tenant_dn = aci_tenant.Villains.id
  name      = "blue_vrf"
}

# Bridge domains
resource "aci_bridge_domain" "bd_netsvcs" {
  tenant_dn   = aci_tenant.Villains.id
  description = "bridge domain for network services"
  name        = "bd_netsvcs"
}

resource "aci_bridge_domain" "bd_apps" {
  tenant_dn   = aci_tenant.Villains.id
  description = "bridge domain for applications"
  name        = "bd_apps"
}

# Subnets
resource "aci_subnet" "subnet_netsvcs" {
  parent_dn   = aci_bridge_domain.bd_netsvcs.id
  description = "subnet for network services BD"
  ip          = "10.10.250.1/24"
}

resource "aci_subnet" "subnet_app1" {
  parent_dn   = aci_bridge_domain.bd_apps.id
  description = "subnet for app group 1"
  ip          = "10.10.1.1/24"
}

resource "aci_subnet" "subnet_app2" {
  parent_dn   = aci_bridge_domain.bd_apps.id
  description = "subnet for app group 2"
  ip          = "10.10.2.1/24"
}


# POLICY RESOURCES
resource "aci_application_profile" "dw_ap" {
  tenant_dn = aci_tenant.Villains.id
  name      = "dw_ap"
}

resource "aci_application_epg" "ll_app_epg" {
  application_profile_dn = aci_application_profile.dw_ap.id
  name                   = "ll_app_epg"
  description            = "EPG for low-latency apps"
}
