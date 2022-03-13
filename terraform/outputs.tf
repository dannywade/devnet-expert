output "aci_tenant_dn" {
  description = "ID of the new Villains ACI tenant"
  value       = aci_tenant.Villains.id
}

output "aci_tenant_name" {
  description = "ID of the new Villains ACI tenant"
  value       = aci_tenant.Villains.name
}

output "aci_vrf_dn" {
  description = "Name of the new VRF within the Villains tenant"
  value       = aci_vrf.blue_vrf.id
}

output "aci_vrf_name" {
  description = "Name of the new VRF within the Villains tenant"
  value       = aci_vrf.blue_vrf.name
}
