#
# Project Ginger
# Copyright IBM Corp, 2016
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#


import ethtool
import glob
import os

from nw_cfginterfaces_utils import IFACE_VLAN
from nw_cfginterfaces_utils import IFACE_BOND
from nw_cfginterfaces_utils import IFACE_ETHERNET

from sysmodules import get_loaded_modules_list
from wok.utils import encode_value

NET_PATH = '/sys/class/net'
NIC_PATH = '/sys/class/net/*/device'
BRIDGE_PATH = '/sys/class/net/*/bridge'
BONDING_PATH = '/sys/class/net/*/bonding'
WLAN_PATH = '/sys/class/net/*/wireless'
NET_BRPORT = '/sys/class/net/%s/brport'
NET_MASTER = '/sys/class/net/%s/master'
NET_STATE = '/sys/class/net/%s/operstate'
PROC_NET_VLAN = '/proc/net/vlan/'
BONDING_SLAVES = '/sys/class/net/%s/bonding/slaves'
BRIDGE_PORTS = '/sys/class/net/%s/brif'
MAC_ADDRESS = '/sys/class/net/%s/address'
KERNEL_MODULE_LINK = '/sys/class/net/%s/device/driver/module'


def wlans():
    return [b.split('/')[-2] for b in glob.glob(WLAN_PATH)]


def is_wlan(iface):
    return encode_value(iface) in map(encode_value, wlans())


# FIXME if we do not want to list usb nic
def nics():
    return list(set([b.split('/')[-2] for b in glob.glob(NIC_PATH)]) -
                set(wlans()))


def is_nic(iface):
    return encode_value(iface) in map(encode_value, nics())


def bondings():
    return [b.split('/')[-2] for b in glob.glob(BONDING_PATH)]


def is_bonding(iface):
    return encode_value(iface) in map(encode_value, bondings())


def vlans():
    return list(set([b.split('/')[-1]
                     for b in glob.glob(NET_PATH + '/*')]) &
                set([b.split('/')[-1]
                     for b in glob.glob(PROC_NET_VLAN + '*')]))


def is_vlan(iface):
    return encode_value(iface) in map(encode_value, vlans())


def bridges():
    return [b.split('/')[-2] for b in glob.glob(BRIDGE_PATH)]


def is_bridge(iface):
    return encode_value(iface) in map(encode_value, bridges())


def all_interfaces():
    """
    This interface will return all the interfaces as seen by the ethtool.
    This is equivalent to cat /proc/net/dev or ip addr show
    :return:
    """
    return ethtool.get_devices()


def slaves(bonding):
    with open(BONDING_SLAVES % bonding) as bonding_file:
        res = bonding_file.readline().split()
    return res


def ports(bridge):
    return os.listdir(BRIDGE_PORTS % bridge)


def is_brport(nic):
    return os.path.exists(NET_BRPORT % nic)


def is_bondlave(nic):
    return os.path.exists(NET_MASTER % nic)


def operstate(dev):
    link_status = link_detected(dev)
    return "up" if link_status == "up" else "down"


def macaddr(dev):
    try:
        with open(MAC_ADDRESS % dev) as dev_file:
            hwaddr = dev_file.readline().strip()
            return hwaddr
    except IOError:
        return "n/a"


def link_detected(dev):
    # try to read interface operstate (link) status
    try:
        with open(NET_STATE % dev) as dev_file:
            return dev_file.readline().strip()
    # when IOError is raised, interface is down
    except IOError:
        return "down"


def get_vlan_device(vlan):
    """ Return the device of the given VLAN. """
    dev = None

    if os.path.exists(PROC_NET_VLAN + vlan):
        with open(PROC_NET_VLAN + vlan) as vlan_file:
            for line in vlan_file:
                if "Device:" in line:
                    dummy, dev = line.split()
                    break
    return dev


def get_bridge_port_device(bridge):
    """Return the nics list that belongs to bridge."""
    #   br  --- v  --- bond --- nic1
    if encode_value(bridge) not in map(encode_value, bridges()):
        raise ValueError('unknown bridge %s' % bridge)
    nics = []
    for port in ports(bridge):
        if encode_value(port) in map(encode_value, vlans()):
            device = get_vlan_device(port)
            if encode_value(device) in map(encode_value, bondings()):
                nics.extend(slaves(device))
            else:
                nics.append(device)
        if encode_value(port) in map(encode_value, bondings()):
            nics.extend(slaves(port))
        else:
            nics.append(port)
    return nics


def aggregated_bridges():
    return [bridge for bridge in bridges() if
            (set(get_bridge_port_device(bridge)) & set(nics()))]


def bare_nics():
    "The nic is not a port of a bridge or a slave of bond."
    return [nic for nic in nics() if not (is_brport(nic) or is_bondlave(nic))]


def is_bare_nic(iface):
    return encode_value(iface) in map(encode_value, bare_nics())


#  The nic will not be exposed when it is a port of a bridge or
#  a slave of bond.
#  The bridge will not be exposed when all it's port are tap.
def all_favored_interfaces():
    return aggregated_bridges() + bare_nics() + bondings()


def get_interface_type(iface):
    # FIXME if we want to get more device type
    # just support nic, bridge, bondings and vlan, for we just
    # want to expose this 4 kinds of interface
    try:
        if is_nic(iface):
            return IFACE_ETHERNET
        if is_bonding(iface):
            return IFACE_BOND
        if is_bridge(iface):
            return "Bridge"
        if is_vlan(iface):
            return IFACE_VLAN
        return 'unknown'
    except IOError:
        return 'unknown'


def get_interface_kernel_module(iface):
    link_path = KERNEL_MODULE_LINK % iface
    try:
        link_target = os.readlink(link_path)
    except OSError:
        return 'unknown'
    module = link_target.split('/')[-1]
    if encode_value(module) in map(encode_value,
                                   get_loaded_modules_list()):
        return module
    else:
        return 'unknown'


def get_interface_info(iface):
    if encode_value(iface) not in map(encode_value, ethtool.get_devices()):
        raise ValueError('unknown interface: %s' % iface)

    ipaddr = ''
    netmask = ''
    try:
        ipaddr = ethtool.get_ipaddr(encode_value(iface))
        netmask = ethtool.get_netmask(encode_value(iface))
    except IOError:
        pass
    return {'device': iface,
            'type': get_interface_type(iface),
            'status': link_detected(iface),
            'ipaddr': ipaddr,
            'netmask': netmask,
            'macaddr': macaddr(iface),
            'module': get_interface_kernel_module(iface)}
