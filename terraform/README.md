# Terraform with ACI provider
## Examples of Terraform plans using the ACI provider to stand up resources in APIC.

### Loop control
- `for_each` - map or set of strings that must be known
    ```
    # Map example (dict)
    resource "azurerm_resource_group" "rg" {
        for_each = {
            a_group = "eastus"
            b_group = "westus2"
        }
        name = each.key         # a_group
        location = each.value   # eastus
    }
    
    # Set example (list)
    resource "aws_iam_user" "user_account" {
        for_each = toset(["John", "Jim", "Alice, "Betsy"])
        name = each.key
    }
    
    # Accessing the instances (use key): azurerm_resource_group.rg["a_group"] / aws_iam_user.user_account["John"]
    
    # toset() - converts a list to a set that can be iterated over
    ```

- `count` - creates specific number of instances. Good for when instances are identical.
    ```
    resource "aws_instance" "server" {
        count = 4
        ami = "ami-abcdefg1"
        instance_type = "t2.micro"
    }
    
    Accessing the instances (use index): aws_instance.server[0]
    
    Get specific items from list: slice(var.dhcp_servers, 0, 2)
    ```

### Resource Graphs
- Builds dependency graph and walks the graph to generate TF plans

    `terraform graph`

**Graph building process:**
1. Resource nodes are added based on the configuration
2. Resources are mapped to provisioners (if defined)
3. Edges between resource are created if `depends_on` meta-parameter is defined
4. "Orphan" resources are present in the graph - nodes no longer in the config, but in the .tfstate file
5. Resources are mapped to providers and provider configuration nodes are created
6. Interpolations are parsed in resource and provider configs to determine dependencies
7. Root node created - points to all resources and is ignored when TF traverses graph
8. If a diff is present, traverse all the resource nodes. If a resource is being destroyed, two nodes are created: one being destroyed, and the new one being added
9. Validate the graph has no cycles (loops) and only one root node

### Variables
Variable order precedence (starting with highest precedence):
1. `-var` or `-var-file` in command-line
2. `*.auto.tfvars` or `*.auto.tfvars.json`
3. `terraform.tfvars` or `terraform.tfvars.json`
4. Env vars (starting with `TF_VAR_`)

`variables.tf` holds all variables used in `main.tf`
```
variable "aws_region" {
    description = "AWS region"
    type = string
    default = "us-east-1"
}

# sensitive variables
variable "db_username" {
    description = "Database username
    type = string
    sensitive = true    # Values are redacted from 'terraform apply' output
}

############################################
Usage:

provider "aws" {
    region = var.aws_region
}

resource "aws_db_resource" "mydb" {
    engine = "mysql"
    username.db_username
}
```
**Sensitive data is still shown in plaintext in the `.tfstate` file**