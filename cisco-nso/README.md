## Intermediate
This folder contains examples of two YANG modules. `ip-access-list.yang` is the "main" module, which is a data model that describes an Access Control List (ACL). The `protocol-base.yang` file is used to supplement, and is imported into `ip-access-list.yang`.

I hope this provides an example of what an NSO data model may look like. Obviously, there are other pieces to the puzzle, but this will help you get started creating YANG data models in NSO.

**All code is from Cisco DevNet Learning Labs: YANG for NSO**

## Netdevopslive-python-and-template
Based on the long and overly verbose name, you can safely assume that the code found in this folder came from a NetDevOps Live! video (link [here](https://youtu.be/-QZfxASrZXw)). The reference code from the video is found [here](https://github.com/kecorbin/nso-service-development).

This example adds concepts to the Intermediate code examples by including some Python logic to create an NSO service package that deploys L2 VLANs with switchport configurations to IOS and NX-OS devices.

I decided to try it out myself by writing out the reference code from scratch. It definitely taught me some things along the way (including some XML and YANG errors :/ ). I highly encourage you to watch the YouTube video alongside trying out the code. Most of my code is identical to the reference code, but I added in some additional comments that helped me better understand why I was doing something. I hope you find it useful!

### Quick Setup
To get a skeleton of this code, use the following command from the root of your NSO instance directory:
```
ncs-make-package --dest packages/vlan --service-skeleton python-and-template vlan
```

The above command should create many of the directories and files for you. You'll just have to edit the existing files or add files to complete the service package.

**All code was copied from the reference link above. I do not claim to own any of this code. This is only for learning purposes**