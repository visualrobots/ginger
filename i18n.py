#
# Projact Ginger
#
# Copyright IBM Corp, 2014-2016
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext


_ = gettext.gettext


messages = {
    "GINNET0001E": _("Failed to read /etc/resolv.conf because %(reason)s"),
    "GINNET0002E": _("Failed to write /etc/resolv.conf because %(reason)s"),
    "GINNET0005E": _("Invalid parameter for DNS servers"),
    "GINNET0006E": _("Invalid parameter for interface ip address"),
    "GINNET0007E": _("Invalid parameter for interface netmask"),
    "GINNET0008E": _("Invalid parameter for network gateway"),
    "GINNET0009E": _("Unable to get default gateway: %(err)s"),
    "GINNET0010E": _("Unable to delete default gateway: %(err)s"),
    "GINNET0011E": _("Unable to set default gateway: %(err)s"),
    "GINNET0014E": _("%(name)s is not valid network interface"),
    "GINNET0015E": _("Error getting information from ifcfg file: '%(error)s'."),
    "GINNET0016E": _("Unable to activate the interface on '%(name)s', '%(error)s'."),
    "GINNET0017E": _("Unable to deactivate the interface on '%(name)s', '%(error)s'."),
    "GINNET0018E": _("Invalid ipv4 address '%(ip)s', '%(error)s'."),
    "GINNET0019E": _("Invalid prefix '%(PREFIX)s', '%(error)s'."),
    "GINNET0020E": _("IP address is missing."),
    "GINNET0021E": _("PREFIX missing."),
    "GINNET0022E": _("Invalid boot protocol '%(mode)s', "),
    "GINNET0023E": _("Boot protocol is missing for ipv4 settings."),
    "GINNET0024E": _("Basic information of interface is missing."),
    "GINNET0025E": _("Device name of interface is missing or invalid."),
    "GINNET0026E": _("Missing ipv4 initialization key."),
    "GINNET0027E": _("Missing ipv6 initialization key."),
    "GINNET0028E": _("Invalid ipv6 address '%(ip)s', '%(error)s'."),
    "GINNET0029E": _("Missing ipv6 address information."),
    "GINNET0030E": _("Exception getting route information: %(err)s"),
    "GINNET0032E": _("Bond info is missing."),
    "GINNET0033E": _("Allowed values for BONDING_MASTER are 'yes' or 'no'"),
    "GINNET0034E": _("Bonding master is missing."),
    "GINNET0036E": _("Slave(s) is missing."),
    "GINNET0037E": _("Minimum one slave has to be given for the bond interface."),
    "GINNET0038E": _("Type is missing."),
    "GINNET0040E": _("Invalid bonding option parameter."),
    "GINNET0041E": _("'yes' or 'no' are the allowed values for the VLAN."),
    "GINNET0042E": _("Vlan info is missing."),
    "GINNET0043E": _("Vlan is missing."),
    "GINNET0044E": _("Vlan id is missing."),
    "GINNET0045E": _("Physical device name is missing."),
    "GINNET0046E": _("A VLAN slave cannot be configured on a bond with the fail_over_mac=follow option."),
    "GINNET0047E": _("For vlan creation over bond, slaves has to be up."),
    "GINNET0048E": _("Module 802q is not loaded into kernel."),
    "GINNET0049E": _("Failed to delete ifcfg file, Error: '%(error)s'"),
    "GINNET0050E": _("VLAN id exceeds the ranges from '0' to '4095'."),
    "GINNET0051E": _("Parent interface of type 'Bond' is not active."),
    "GINNET0052E": _("Type is unknown."),
    "GINNET0053E": _("Persistent file for slave '%(slave)s' is missing."),
    "GINNET0055E": _("Interface '%(name)s' is neither Vlan nor Bond to perform delete operation."),
    "GINNET0056E": _("Failed to identify the type of interface."),
    "GINNET0057E": _("Persistent file is not available for an interface, '%(name)s'."),
    "GINNET0058E": _("Failed to a delete token from ifcfg file, Error: '%(error)s'."),
    "GINNET0059E": _("Unable to bring up the interface '%(name)s', '%(error)s'."),
    "GINNET0060E": _("Unable to bring down the interface '%(name)s', '%(error)s'."),
    "GINNET0061E": _("Missing IPV4 addresses information."),
    "GINNET0062E": _("The prefix value %(PREFIX)s is not in range 1-32."),
    "GINNET0063E": _("Exception updating the interface settings: %(err)s"),
    "GINNET0064E": _("Boot protocol is missing for ipv6 settings."),
    "GINNET0065E": _("The prefix value %(PREFIX)s is not in range 1-128."),
    "GINNET0066E": _("Given vlan id is not an integer type, Error: '%(error)s'."),
    "GINNET0067E": _("Maximum length of device name is 15 characters only."),
    "GINNET0068E": _("Device name is invalid."),
    "GINNET0070E": _("Gateway information is missing."),
    "GINNET0071E": _("Invalid prefix '%(PREFIX)s'."),
    "GINNET0072E": _("Interface with the name '%(iface)s' already exists ."),
    "GINNET0073E": _("'%(key)s' value is missing."),
    "GINNET0074E": _("Exception updating/creating the ifcfg file."),
    "GINNET0075E": _("At least one slave is "
                     "required for the bond interface"),
    "GINNET0076E": _("Interface %(name)s loaded with driver %(module)s does not support SR-IOV."),
    "GINNET0077E": _("SR-IOV action of mlx5 module requires 'num_vfs' argument."),
    "GINNET0078E": _("SR-IOV enablement failed: required files under /sys directory not found."),
    "GINNET0079E": _("SR-IOV enablement failed: num_vfs must be an integer."),
    "GINNET0080E": _("Interface '%(name)s' doesn't exist. Please refresh the network list to fetch the latest list of interfaces"),
    "GINNET0081E": _("Unable to create a new network script file for the interface %(name)s."),
    "GINNET0082E": _("SR-IOV is not enabled in the firmware of the interface %(name)s."),
    "GINNET0083E": _("Unable to set %(num_vf)s virtual functions for interface %(name)s. Maximum allowed in the firmware is %(max_vf)s."),
    "GINNET0084E": _("SR-IOV is already configured in interface %(name)s with %(num_vf)s virtual functions."),
    "GINNET0085E": _("Error in the mlx5_SRIOV_enable task: %(err)s"),
    "GINNET0086E": _("Unable to read or update SR-IOV boot script file. Error: %(err)s"),
    "GINNET0087E": _("Unable to read or update openib.conf file. Error: %(err)s"),
    "GINNET0088E": _("Error: openib.conf file does not exist in the host. Unable to set SR-IOV boot script."),
    "GINNET0089W": _("Warning: Recent changes has been rolled back, due to operation fail"),
    "GINNET0090E": _("Activation of interface %(name)s failed. Physical cable is disconnected for the device '%(name)s'."),
    "GINNET0091E": _("Run time information is not available for the interface on '%(name)s'. Activation of the interface on '%(name)s' went wrong."),
    "GINNET0092E": _("%(mac)s is not a valid mac address."),
    "GINNET0093E": _("SR-IOV is already disabled (no virtual functions enabled) in interface %(name)s."),
    "GINNET0094E": _("Activation of vlan/bond interface '%(name)s' failed. Please "
                     "refresh and try again. "),
    "GINNET0095E": _("Activation of vlan interface '%(name)s' failed. "
                     "Try disabling the DHCP option in IPv4 settings tab."),

    "GINUSER0001E": _("Specify name, password, group and profile for the new "
                      "user."),
    "GINUSER0002E": _("User name is a required string."),
    "GINUSER0003E": _("User password is a required string."),
    "GINUSER0004E": _("User group should be non-empty string."),
    "GINUSER0005E": _("User profile should be one among regularuser, virtuser or admin."),
    "GINUSER0006E": _("Could not add user '%(user)s' to kvm group."),
    "GINUSER0007E": _("Could not add user '%(user)s' to sudoers list, error: '%(err)s'."),
    "GINUSER0008E": _("User/Login '%(user)s' already in use."),
    "GINUSER0009E": _("There was a problem while creating user '%(user)s', error: user name is empty."),
    "GINUSER0010E": _("There was a problem while deleting user '%(user)s', error: user name is empty."),
    "GINUSER0011E": _("User '%(user)s' does not exist."),
    "GINUSER0012E": _("There was a problem while deleting group '%(group)s'. Group name is an empty string."),
    "GINUSER0013E": _("Failed to remove user '%(user)s' from sudoers list"),
    "GINUSER0014E": _("There was a problem while creating group '%(group)s'. Group name is an empty string."),
    "GINUSER0015E": _("User 'no_login' should be boolean."),
    'GINUSER0016E': _("Deletion is not supported for users found in '/etc/sudoers' file. User: %(user)s"),
    'GINUSER0017E': _("Deletion is not supported for group found in '/etc/sudoers' file. Group: %(group)s"),
    "GINUSER0018E": _("Group name '%(group)s' is already in use'."),
    "GINUSER0019E": _("Failed to parse '/etc/sudoers' file. Error: %(error)s"),
    "GINUSER0020E": _("System users are not supported"),
    "GINUSER0021E": _("Failed to remove user '%(user)s' from group '%(group)s'. Error: '%(err)s'"),
    "GINUSER0022E": _("There was a problem while reading users details, see log for details"),
    "GINUSER0023E": _("There was a problem while fetching user profile, see log for details"),
    "GINUSER0024E": _("Failed to change password for user '%(user)s', error: '%(err)s'."),
    "GINUSER0025E": _("There was a problem while creating user '%(user)s', error: group id %(gid)s is not of integer type."),
    "GINUSER0026E": _("There was a problem while creating user '%(user)s', error: no_login id %(no_login)s is not of boolean type."),
    "GINUSER0027E": _("Failed to remove user '%(user)s' from group '%(group)s'. Error: group name is an empty string."),

    "GINFW0001E": _("Cannot update system firmware while running VMs."),
    "GINFW0002E": _("Firmware image unpack failed: rc = %(rc)s. "
                    "Details: %(err)s"),
    "GINFW0003E": _("FW update failed: "
                    "No image file found in the package file."),
    "GINFW0004E": _("Error flashing firmware: %(error)s"),
    "GINFW0005E": _("Error commiting firmware. rc = %(rc)s. Ensure you are booted to the temporary side."),
    "GINFW0006E": _("Error rejecting firmware. rc = %(rc)s. Ensure you are booted to the permanent side."),
    "GINFW0007I": _("Firmware update is initializing. System will reboot in order to flash the firmware."),
    "GINFW0008E": _("Internal error: %(error)s"),

    "GINHBK0001E": _('Failed to create tar archive "%(name)s", cmd: '
                     '"%(cmd)s". Inspect error log for more information.'),
    "GINHBK0002E": _('Failed to delete archive file "%(name)s".'),
    "GINHBK0003E": _('Failed to create archive dir "%(dir)s". '
                     'Inspect error log for more information.'),
    "GINHBK0004E": _('Description too long.'),
    "GINHBK0005E": _('Please check the uniqueness of the paths or patterns.'),
    "GINHBK0006E": _('Path or pattern is too long or too short.'),
    "GINHBK0007E": _('Invalid days_ago number.'),
    "GINHBK0008E": _('Invalid counts_ago number.'),
    "GINHBK0009E": _('Failed to create archive "%(identity)s". '
                     'Inspect error log for more information.'),
    "GINHBK0010E": _('Unable to create backup, file %(file)s changed as we read it'),
    "GINHBK0011E": _('Archive creation task failed. "%(err)s".'),
    "GINHBK0012E": _('Unable to include default backup dir (%(dir)s) to a backup file'),

    "GINADAP0001E": _("SAN adapter '%(adapter)s' does not exist in the system."
                      ),

    "GINSEP0001E": _("Provide required parameters: hostname, port, community."
                     ),
    "GINSEP0002E": _("System hostname must be a valid string."),
    "GINSEP0003E": _("System port number must be an integer between 1 and 65535."),
    "GINSEP0004E": _("SNMP community name must be a single word."),
    "GINSEP0005E": _("Error retrieving SEP subscribers data: '%(error)s'."),
    "GINSEP0006E": _("Hostname %(hostname)s not found."),
    "GINSEP0007E": _("Error loading SEP subscriptions data from server."),
    "GINSEP0008E": _("Error starting SEP service: '%(error)s'."),
    "GINSEP0009E": _("Error stopping SEP service: '%(error)s'."),
    "GINSEP0010E": _("Error subscribing SEP data to server: '%(error)s'."),
    "GINSEP0011E": _("Error deleting subscription: '%(error)s'."),

    "GINPOWER0001E": _("Error activating power saving profile %(profile)s, error: %(err)s."),
    "GINPOWER0002E": _("Failed to retrieve power management profiles: Daemon 'tuned-adm' is not active."),

    "GINFS00001E": _("Failed to retrieve details of the %(name)s filesystem."),
    "GINFS00002E": _("Failed to unmount filesystem %(name)s, error: %(err)s"),
    "GINFS00003E": _("Parsing df output failed."),
    "GINFS00004E": _("error in filesystem get list util"),
    "GINFS00005E": _("error in filesystem info fetch util"),
    "GINFS00006E": _("Error in executing 'df -hT' command"),
    "GINFS00007E": _("Failed to mount the filesystem, error: %(err)s"),
    "GINFS00008E": _("error in unmount util"),
    "GINFS00009E": _("Require block dev to mount a filesystem"),
    "GINFS00010E": _("Require mount point to mount a filesystem"),

    "GINFS00011E": _("Unable to open fstab"),
    "GINFS00012E": _("Unable to write fstab"),
    "GINFS00013E": _("Failed to retrieve list of filesystems. Error: %(err)s"),
    "GINFS00014E": _("required server ip addr"),
    "GINFS00015E": _("required remote share location"),
    "GINFS00016E": _("required type as local or nfs"),
    "GINFS00017E": _("Invalid type needs to be either local or nfs"),
    "GINFS00018E": _("NFS mount failed, %(err)s"),
    "GINFS00019E": _("Filesystem %(name)s already mounted in fstab."),

    "GINSP00001E": _("File location required for creating a swap device."),
    "GINSP00002E": _("Type required for creating a swap device."),
    "GINSP00003E": _("Size is mandatory while creating file type swap device."),
    "GINSP00004E": _("Incorrect swap type, only 'device' and 'file' are allowed."),
    "GINSP00005E": _("Error creating a swap device. %(err)s "),
    "GINSP00006E": _("Error deleting a swap file: %(err)s"),
    "GINSP00007E": _("Error deleting a swap device. %(err)s"),
    "GINSP00008E": _("Swap device not found. %(name)s"),
    "GINSP00009E": _("Error deleting a swap device. %(err)s"),
    "GINSP00010E": _("Error parsing /proc/swaps file. %(err)s"),
    "GINSP00011E": _("Error creating a flat file. %(err)s"),
    "GINSP00012E": _("Unable to format swap device. %(err)s"),
    "GINSP00013E": _("Unable to activate swap device. %(err)s"),
    "GINSP00014E": _("Unable to parse 'swapon -s' output. %(err)s"),
    "GINSP00015E": _("Unable to get single swap device info. %(err)s"),
    "GINSP00016E": _("Unable to deactivate swap device. %(err)s"),
    "GINSP00017E": _("No partitions found for disk %(disk)s"),
    "GINSP00018E": _("Single swap device %(swap)s not found."),
    "GINSP00019E": _("Unable to get single swap device info: directory /proc/swaps not found."),
    "GINSP00020E": _("File %(file)s already in use."),
    "GINSP00021E": _("Unable to change the partition type. Error: %(err)s"),
    "GINSP00022E": _("File path cannot be an existing directory"),

    "GINPART00001E": _("Fetching list of partitions failed. Error: %(err)s"),
    "GINPART00002E": _("Create partition failed. Error: %(err)s"),
    "GINPART00003E": _("Error retrieving information of partition %(name)s : %(err)s"),
    "GINPART00004E": _("Partition already mounted"),
    "GINPART00005E": _("Format partition failed"),
    "GINPART00006E": _("Change type for partition failed. Error: %(err)s"),
    "GINPART00007E": _("Delete partition failed. Error: %(err)s"),
    "GINPART00008E": _("Required parameter device name"),
    "GINPART00009E": _("Required parameter partition size"),
    "GINPART00011E": _("fdisk command failed"),
    "GINPART00012E": _("mkfs command failed"),
    "GINPART00013E": _("No partitions found"),
    "GINPART00014E": _("Partition %(name)s not found."),

    "GINLVM0001E": _("Error parsing output of 'lvm version' command: %(err)s"),
    "GINLVM0002E": _("Error executing 'lvm version' command. %(err)s"),
    "GINLVM0003E": _("Incompatible output from 'lvm version' command. %(err)s"),

    "GINPV00001E": _("Required pv_name parameter."),
    "GINPV00002E": _("Failed to create PV %(name)s."),
    "GINPV00003E": _("Failed to fetch PV list. Error: %(err)s"),
    "GINPV00004E": _("Failed to fetch PV %(name)s details."),
    "GINPV00005E": _("Failed to delete PV, error: %(err)s"),
    "GINPV00006E": _("pvs command failed"),
    "GINPV00007E": _("Unable to get information of device %(dev)s, error: %(err)s"),
    "GINPV00008E": _("pvcreate command failed"),
    "GINPV00009E": _("Remove failed: error: %(err)s"),
    "GINPV00010E": _("Remove failed: device %(dev)s not found."),
    "GINPV00011E": _("Unable to find device %(dev)s ."),

    "GINVG00001E": _("Failed to create VG %(name)s. Error: %(err)s"),
    "GINVG00002E": _("Failed to list VGs. Error: %(err)s"),
    "GINVG00003E": _("Failed to fetch VG %(name)s details."),
    "GINVG00004E": _("Failed to delete VG %(name)s."),
    "GINVG00005E": _("Failed to extend VG %(name)s."),
    "GINVG00006E": _("Failed to reduce VG %(name)s."),
    "GINVG00007E": _("vgs command failed"),
    "GINVG00008E": _("vgs command for given VG failed"),
    "GINVG00009E": _("vgcreate command failed"),
    "GINVG00010E": _("vgremove command failed"),
    "GINVG00011E": _("vgextend command failed"),
    "GINVG00012E": _("vgreduce command failed : %(err)s"),
    "GINVG00013E": _("Required vg_name parameter"),
    "GINVG00014E": _("Required pv_paths parameter"),
    "GINVG00015E": _("Invalid input to extend VG: error: %(err)s"),
    "GINVG00016E": _("Error reducing volume group : %(err)s"),
    "GINVG00017E": _("VG %(name)s contains logical volumes."),

    "GINLV00001E": _("Required vg_name parameter"),
    "GINLV00002E": _("Required size parameter"),
    "GINLV00003E": _("Failed to create LV"),
    "GINLV00004E": _("Failed to list LVs"),
    "GINLV00005E": _("Failed to fetch LV details"),
    "GINLV00006E": _("Failed to delete LV"),
    "GINLV00007E": _("lvcreate command failed"),
    "GINLV00008E": _("lvs command failed"),
    "GINLV00009E": _("lvdisplay command failed"),
    "GINLV00010E": _("lvremove command failed"),

    "GINDASD0001E": _("Error in executing 'lsdasd -l' command: %(err)s"),
    "GINDASD0002E": _("Error in executing 'lsdasd -l bus_id' command: %(err)s"),
    "GINDASD0003E": _("Parsing lsdasd output failed"),
    "GINDASD0004E": _("Failed to format %(name)s. Either format currently going on or device not available for format. Please try again later."),
    "GINDASD0005E": _("Failed to retrieve list of DASD devices, error: %(err)s"),
    "GINDASD0006E": _("Failed to retrieve details of DASD device %(name)s, error: %(err)s"),
    "GINDASD0007E": _("Failed to find specified DASD device"),
    "GINDASD0008E": _("Failed to format %(name)s. Either format currently going on or device not available for format"),
    "GINDASD0009E": _("Require DASD device name to be formatted"),
    "GINDASD0010E": _("Require block size for formatting DASD device"),
    "GINDASD0011E": _("Invalid bus ID, %(bus_id)s"),
    "GINDASD0012E": _("Error in executing 'lscss -d' command : %(err)s"),
    "GINDASD0013E": _("Error in parsing 'lscss -d' command : %(err)s"),
    "GINDASD0014E": _("No more than %(max_dasd_fmt)s concurrent DASD format operations are permitted."),
    "GINDASD0015E": _("Header is empty for given pattern."),

    "GINDASDPAR0005E": _("Require name to create DASD device partition"),
    "GINDASDPAR0006E": _("Require partition size to create DASD device partition"),
    "GINDASDPAR0007E": _("Failed to create partition %(name)s, error: %(err)s"),
    "GINDASDPAR0008E": _("Failed to retrieve list of DASD partitions. Error: %(err)s"),
    "GINDASDPAR0009E": _("Failed to retrieve details of DASD partition %(name)s."),
    "GINDASDPAR0010E": _("Failed to delete partition %(name)s, error: %(err)s"),
    "GINDASDPAR0011E": _("Invalid DASD partition, %(name)s"),
    "GINDASDPAR0012E": _("DASD device %(name)s not found"),
    "GINDASDPAR0013E": _("Size must be of type integer"),
    "GINDASDPAR0014E": _("Unable to change dasd type, error: %(err)s"),
    "GINDASDPAR0015E": _("Partition size exceeds device size"),
    "GINDASDPAR0016E": _("No more free partitions left. Please remove one partition first."),

    "GINSYSMOD00001E": _("Error getting loaded module list: %(err)s"),
    "GINSYSMOD00002E": _("Module %(module)s not found."),
    "GINSYSMOD00003E": _("Error fetching info of module %(module)s, reason: %(err)s"),
    "GINSYSMOD00004E": _("Error loading module %(module)s, reason: %(err)s"),
    "GINSYSMOD00005E": _("Error unloading module %(module)s, reason: %(err)s"),
    "GINSYSMOD00006E": _("Module %(module)s is already loaded in the kernel."),

    "GINOVS00001E": _("Error executing OVS command. Please check if 'openvswitch' service is running."),
    "GINOVS00002E": _("Error executing OVS command: %(err)s"),
    "GINOVS00003E": _("Error creating OVS bridge %(name)s. OVS bridge already exists."),
    "GINOVS00004E": _("Error retrieving OVS bridge %(name)s. OVS bridge does not exist."),
    "GINOVS00005E": _("Error adding port %(port)s in bridge %(name)s. Port already exists."),
    "GINOVS00006E": _("Unable to create bond with less than two interfaces."),
    "GINOVS00007E": _("Bridge %(bridge)s does not have a bond named %(bond)s."),
    "GINOVS00008E": _("Interface %(iface)s not found in openvswitch database."),

    "GINSD00001E": _("Error executing 'ls -l /dev/disk/by-id, %(err)s"),
    "GINSD00002E": _("Error executing 'lsblk -Po, %(err)s"),
    "GINSD00003E": _("Error parsing 'ls -l /dev/disk/by-id', %(err)s"),
    "GINSD00004E": _("Error parsing 'lsblk -Po', %(err)s"),
    "GINSD00005E": _("Error getting list of storage devices, %(err)s"),
    "GINSD00006E": _("Error getting bus id of DASD device, %(err)s"),

    "GINSERV00001E": _("Error executing SystemD command %(cmd)s, reason: %(err)s"),
    "GINSERV00002E": _("Service name %(name)s not found."),
    "GINSTG00001E": _("Invalid URI, please use /stgserver/%(ipaddr)s/nfsshares"),
    "GINSTG00002E": _("Invalid URI, no list of storage servers available"),
    "GINNFS00001E": _("Error fetching NFS shares for server %(name)s."),
    "GINNFS00002E": _("Invalid server or no NFS exports found on server."),

    "GINISCSI001E": _("No valid iSCSI Targets found for IP Address - %(ip_address)s"),
    "GINISCSI002E": _("Error executing iSCSI target discovery command - %(err)s"),
    "GINISCSI003E": _("Error parsing iSCSI target discovery command - %(err)s"),
    "GINISCSI004E": _("Unable to get iSCSI targets of host %(host)s: Connection timed out"),
    "GINISCSI005E": _("Error in listing pre-discovered iSCSI targets - %(err)s"),
    "GINISCSI006E": _("Error in determining iSCSI QN %(iqn)s logged in status - %(err)s"),
    "GINISCSI007E": _("Error in logging onto iSCSI QN %(iqn)s - %(err)s"),
    "GINISCSI008E": _("Error in logging out of iSCSI QN %(iqn)s - %(err)s"),
    "GINISCSI009E": _("Error in deleting iSCSI QN %(iqn)s from iscsiadm db - %(err)s"),
    "GINISCSI010E": _("Error parsing the output of iscsiadm discovery cmd - %(err)s. iscsiadm discovery Output - %(output)s"),
    "GINISCSI011E": _("Error updating iscsiadm db key %(db_key)s for IQN %(iqn)s with error - %(err)s"),
    "GINISCSI012E": _("Invalid authentication type - %(auth_type)s"),
    "GINISCSI013E": _("Error parsing session directory name %(session)s - %(err)s"),
    "GINISCSI014E": _("Error while searching the active session for IQN %(iqn)s - %(err)s"),
    "GINISCSI015E": _("Error executing command to rescan the IQN %(iqn)s - %(err)s"),
    "GINISCSI016E": _("IQN %(iqn)s is not logged onto the target"),
    "GINISCSI017E": _("Error in modifying iSCSI parameter %(parameter)s with value %(value)s - %(err)s"),
    "GINISCSI018E": _("Error getting the global iSCSI auth info - %(err)s"),
    "GINISCSI019E": _("Error getting the auth info for IQN %(iqn)s - %(err)s"),
    "GINISCSI020E": _("Invalid IQN. Given IQN not found in added IQNs"),

    "GINAUD0001E": _("Failed to get the list of persisted rules '%(error)s'."),
    "GINAUD0002E": _("Error in executing auditctl command '%(name)s'."),
    "GINAUD0003E": _("Creation of a rule failed. '%(error)s'."),
    "GINAUD0004E": _("Missing rule info."),
    "GINAUD0005E": _("Error occurred while writing rule into audit.rules: %(err)s"),
    "GINAUD0006E": _("Error occurred  while deleting the rule. %(err)s"),
    "GINAUD0007E": _("Error occurred in fetching audit rule info. %(error)s"),
    "GINAUD0008E": _("Error occurred in fetching system rule info. %(error)s"),
    "GINAUD0009E": _("Error occurred in fetching filesystem rule info. %(error)s"),
    "GINAUD0010E": _("Rule '%(name)s' is not persisted in the rules file."),
    "GINAUD0011E": _("Error occurred in modifying the rule '%(name)s'."),
    "GINAUD0012E": _("The rule '%(name)s' cannot be deleted. "),
    "GINAUD0013E": _("Error occurred in unload operation of rule '%(name)s' ."),
    "GINAUD0014E": _("Error occurred in getting the filtered logs."),
    "GINAUD0015E": _("Error occurred in getting the unfiltered logs."),
    "GINAUD0016E": _("Error occurred in fetching the logs."),
    "GINAUD0017E": _("Error occurred in getting the reports."),
    "GINAUD0018E": _("Loading the rule '%(name)s' failed."),
    "GINAUD0019E": _("Error occurred in loading predefined rules."),
    "GINAUD0020E": _("Error occurred in persisting the rules."
                     " The rule '%(name)s' already exists."),
    "GINAUD0021E": _("The predefined rules files doesn't exist."),
    "GINAUD0022E": _("Execution on auditctl command failed with error '%(error)s'"),
    "GINAUD0023E": _("Error in retrieving the audit conf file details. "),
    "GINAUD0024E": _("Error in enabling the audit dispatcher. "),
    "GINAUD0025E": _("Error in disabling the audit dispatcher. "),
    "GINAUD0026E": _("Error in updating the audit conf file details. "),
    "GINAUD0027E": _("Error occurred in rendering the graph. "),
    "GINAUD0028E": _("Error occurred in graph creation: '%(error)s"),
    "GINAUD0029E": _("Invalid parameters to create a report graph."),
    "GINAUD0030E": _("Failed to create the graph: Package 'Graphviz' is not installed."),
    "GINSE00001E": _("Missing Input Parameters"),
    "GINSE00002E": _("Server with name %(name)s is already added"),
    "GINSE00003E": _("Error while getting the status of server with name %(name)s and IP address or Host Name %(ipaddr)s. Please check the server details and retry the operation."),
    "GINSE00004E": _("Server with IP address or Host Name %(ipaddr)s is already added"),
    "GINSE00005E": _("Server with name %(name)s is not found"),
    "GINSE00006E": _("Power on server %(name)s failed"),
    "GINSE00007E": _("Power off server %(name)s failed"),
    "GINSE00008E": _("Password parameter is required"),
    "GINSE00009E": _("Invalid parameter, only username and password updates are allowed"),

    "GINSEL00001E": _("Unable to get System Event Log information for server %(name)s. IPMI Command error %(err)s. rc = %(rc)s"),
    "GINSEL00002E": _("Unable to get details of server %(name)s"),
    "GINSEL00003E": _("System Event Log %(sel_id)s is not present in System Event Log information for server %(name)s"),
    "GINSEL00004E": _("Unable to delete System Event Log %(sel_id)s for server %(name)s. IPMI Command error %(err)s. rc =%(rc)s"),
    "GINSEL00005E": _("Cannot process System Event Log entry %(selString)s"),

    "GINSDR00001E": _("Unable to get SDR information for server %(name)s. IPMI Command error %(err)s , rc = %(rc)s"),
    "GINSDR00002E": _("Cannot process SDR entry %(sdrString)s"),
    "GINSDR00003E": _("%(sensor_type)s is not a valid sensor type"),

    # These messages (ending with L) are for user log purposes
    "GINAUD0001L": _("Create audit rule '%(rule)s' type '%(type)s'"),
    "GINAUD0002L": _("Delete audit rule '%(ident)s'"),
    "GINAUD0003L": _("Persist audit rule '%(ident)s'"),
    "GINAUD0004L": _("Load audit rule '%(ident)s'"),
    "GINAUD0005L": _("Created the rule '%(name)s'"),
    "GINAUD0006L": _("Disabled audit dispatcher in conf file '%(ident)s'"),
    "GINAUD0007L": _("Persist the rule '%(ident)s'"),
    "GINAUD0008L": _("Load the rule '%(ident)s'"),
    "GINAUD0009L": _("Unload  the rule '%(ident)s'"),
    "GINDASD0001L": _("Format DASD device '%(ident)s' with block size %(blk_size)s"),
    "GINDASDPAR0001L": _("Create DASD partition on '%(dev_name)s' with size %(size)s"),
    "GINDASDPAR0002L": _("Remove DASD partition '%(ident)s'"),
    "GINFW0001L": _("Upgrade host firmware with '%(path)s'"),
    "GINFW0002L": _("Commit host firmware image from temp side to perm side"),
    "GINFW0003L": _("Reject host firmware image on temp side"),
    "GINFS0001L": _("Mount %(type)s filesystem at '%(mount_point)s'"),
    "GINFS0002L": _("Unmount filesystem '%(ident)s'"),
    "GINHBK0001L": _("Discard old archives"),
    "GINHBK0002L": _("Create archive with description '%(description)s'"),
    "GINHBK0003L": _("Remove archive '%(ident)s'"),
    "GINISCSIATH001L": _("Set initiator CHAP credentials in iscsid.conf '%(ident)s'"),
    "GINISCSIATH002L": _("Set targets CHAP credentials in iscsid.conf '%(ident)s'"),
    "GINISCSIATH003L": _("Set initiator discovery session CHAP credentials in iscsid.conf '%(ident)s'"),
    "GINISCSIATH004L": _("Set targets discovery session CHAP credentials in iscsid.conf '%(ident)s'"),
    "GINISCSI0001L": _("Delete IQN '%(ident)s'"),
    "GINISCSI0002L": _("Login onto IQN '%(ident)s'"),
    "GINISCSI0003L": _("Logout from IQN '%(ident)s'"),
    "GINISCSI0004L": _("Rescan IQN '%(ident)s'"),
    "GINISCSI0005L": _("Set initiator CHAP credentials for IQN '%(ident)s'"),
    "GINISCSI0006L": _("Set targets CHAP credentials for IQN '%(ident)s'"),
    "GINLV0001L": _("Create logical volume at volume group '%(vg_name)s'"),
    "GINLV0002L": _("Remove logical volume '%(ident)s'"),
    "GINNET0001L": _("Create configuration file for network interface"),
    "GINNET0002L": _("Remove configuration file for network interface '%(ident)s'"),
    "GINNET0003L": _("Update configuration file for network interface '%(ident)s'"),
    "GINNET0004L": _("Redefine host network interface '%(ident)s'"),
    "GINNET0005L": _("Activate host network interface '%(ident)s'"),
    "GINNET0006L": _("Deactivate host network interface '%(ident)s'"),
    "GINNET0007L": _("Enable SR-IOV feature for network interface '%(ident)s'"),
    "GINNET0008L": _("Update host network configuration"),
    "GINNET0009L": _("Confirm changes on host network configuration"),
    "GINOVS0001L": _("Create OVS bridge '%(name)s'"),
    "GINOVS0002L": _("Remove OVS bridge '%(ident)s'"),
    "GINOVS0003L": _("Add interface '%(interface)s' to OVS bridge '%(ident)s'"),
    "GINOVS0004L": _("Remove interface '%(interface)s' from OVS bridge '%(ident)s'"),
    "GINOVS0005L": _("Add bonded port '%(bond)s' in OVS bridge '%(ident)s'"),
    "GINOVS0006L": _("Remove bonded port '%(bond)s' from OVS bridge '%(ident)s'"),
    "GINOVS0007L": _("Modify bonded port '%(bond)s' to replace interface '%(interface_del)s' with interface '%(interface_add)s' in OVS bridge '%(ident)s'"),
    "GINPART0001L": _("Create disk partition at '%(devname)s' with size %(partsize)s"),
    "GINPART0002L": _("Remove disk partition '%(ident)s'"),
    "GINPART0003L": _("Update disk partition '%(ident)s' to type '%(type)s'"),
    "GINPART0004L": _("Format disk partition '%(ident)s' with filesystem '%(fstype)s'"),
    "GINPOWER0001L": _("Activate power saving profile '%(ident)s'"),
    "GINPV0001L": _("Add physical volume '%(pv_name)s'"),
    "GINPV0002L": _("Remove physical volume '%(ident)s'"),
    "GINSE0001L": _("Add managed server '%(name)s'"),
    "GINSE0002L": _("Remove managed server '%(ident)s'"),
    "GINSE0003L": _("Power on managed server '%(ident)s'"),
    "GINSE0004L": _("Power off managed server '%(ident)s'"),
    "GINSE0005L": _("Update Credentials of managed server '%(ident)s'"),
    "GINSEL0001L": _("Delete System Event Log entry '%(ident)s'"),
    "GINSEP0001L": _("Start IBM Serviceable Event Provider (SEP)"),
    "GINSEP0002L": _("Stop IBM Serviceable Event Provider (SEP)"),
    "GINSEP0003L": _("Subscribe '%(hostname)s' with IBM SEP"),
    "GINSEP0004L": _("Unsubscribe '%(ident)s' with IBM SEP"),
    "GINSEP0005L": _("Update '%(ident)s' subscription with IBM SEP"),
    "GINSERV0001L": _("Enabled autostart of service '%(ident)s'"),
    "GINSERV0002L": _("Disabled autostart of service '%(ident)s'"),
    "GINSERV0003L": _("Started service '%(ident)s'"),
    "GINSERV0004L": _("Stopped service '%(ident)s'"),
    "GINSERV0005L": _("Restarted service '%(ident)s'"),
    "GINSP0001L": _("Create swap device '%(file_loc)s'"),
    "GINSP0002L": _("Delete swap device '%(ident)s'"),
    "GINSYSMOD0001L": _("Load kernel module '%(name)s'"),
    "GINSYSMOD0002L": _("Unload kernel module '%(ident)s'"),
    "GINUSER0001L": _("Create user '%(name)s'"),
    "GINUSER0002L": _("Delete user '%(ident)s'"),
    "GINUSER0003L": _("Change password for user '%(ident)s'"),
    "GINVG0001L": _("Create host volume group '%(vg_name)s'"),
    "GINVG0002L": _("Remove host volume group '%(ident)s'"),
    "GINVG0003L": _("Extend host volume group '%(ident)s'"),
    "GINVG0004L": _("Reduce host volume group '%(ident)s'"),
}
