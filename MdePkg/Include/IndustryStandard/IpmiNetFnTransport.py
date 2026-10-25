# /** @file
#   IPMI 2.0 definitions from the IPMI Specification Version 2.0, Revision 1.1.
# 
#   This file contains all NetFn Transport commands, including:
#     IPM LAN Commands (Chapter 23)
#     IPMI Serial/Modem Commands (Chapter 25)
#     SOL Commands (Chapter 26)
#     Command Forwarding Commands (Chapter 35b)
# 
#   See IPMI specification, Appendix G, Command Assignments
#   and Appendix H, Sub-function Assignments.
# 
#   Copyright (c) 1999 - 2018, Intel Corporation. All rights reserved.<BR>
#   Copyright (C) 2023 Advanced Micro Devices, Inc. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# IpmiNetFnTransport.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnTransport
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _IPMI_NET_FN_TRANSPORT_H_
# #define _IPMI_NET_FN_TRANSPORT_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack(1)
# //
# // Net function definition for Transport command
# //
# #define IPMI_NETFN_TRANSPORT  0x0C
IPMI_NETFN_TRANSPORT  = 0x0C

# 
# //
# //  Below is Definitions for IPM LAN Commands (Chapter 23)
# //
# 
# //
# //  Definitions for Set Lan Configuration Parameters command
# //
# #define IPMI_TRANSPORT_SET_LAN_CONFIG_PARAMETERS  0x01
IPMI_TRANSPORT_SET_LAN_CONFIG_PARAMETERS = 0x01

# 
# //
# //  Constants and Structure definitions for "Set Lan Configuration Parameters" command to follow here
# //
# 
# //
# // LAN Management Structure
# //
# typedef enum {
#   IpmiLanReserved1,
#   IpmiLanReserved2,
#   IpmiLanAuthType,
#   IpmiLanIpAddress,
#   IpmiLanIpAddressSource,
#   IpmiLanMacAddress,
#   IpmiLanSubnetMask,
#   IpmiLanIpv4HeaderParam,
#   IpmiLanPrimaryRcmpPort,
#   IpmiLanSecondaryRcmpPort,
#   IpmiLanBmcGeneratedArpCtrl,
#   IpmiLanArpInterval,
#   IpmiLanDefaultGateway,
#   IpmiLanDefaultGatewayMac,
#   IpmiLanBackupGateway,
#   IpmiLanBackupGatewayMac,
#   IpmiLanCommunityString,
#   IpmiLanReserved3,
#   IpmiLanDestinationType,
#   IpmiLanDestinationAddress,
#   IpmiLanVlanId         = 0x14,
#   IpmiIpv4OrIpv6Support = 0x32,
#   IpmiIpv4OrIpv6AddressEnable,
#   IpmiIpv6HdrStatTrafficClass,
#   IpmiIpv6HdrStatHopLimit,
#   IpmiIpv6HdrFlowLabel,
#   IpmiIpv6Status,
#   IpmiIpv6StaticAddress,
#   IpmiIpv6DhcpStaticDuidLen,
#   IpmiIpv6DhcpStaticDuid,
#   IpmiIpv6DhcpAddress,
#   IpmiIpv6DhcpDynamicDuidLen,
#   IpmiIpv6DhcpDynamicDuid,
#   IpmiIpv6RouterConfig = 0x40,
#   IpmiIpv6StaticRouter1IpAddr,
#   IpmiIpv6DynamicRouterIpAddr = 0x4a
# } IPMI_LAN_OPTION_TYPE;
IpmiLanReserved1              =  0
IpmiLanReserved2              =  1
IpmiLanAuthType               =  2
IpmiLanIpAddress              =  3
IpmiLanIpAddressSource        =  4
IpmiLanMacAddress             =  5
IpmiLanSubnetMask             =  6
IpmiLanIpv4HeaderParam        =  7
IpmiLanPrimaryRcmpPort        =  8
IpmiLanSecondaryRcmpPort      =  9
IpmiLanBmcGeneratedArpCtrl    = 10
IpmiLanArpInterval            = 11
IpmiLanDefaultGateway         = 12
IpmiLanDefaultGatewayMac      = 13
IpmiLanBackupGateway          = 14
IpmiLanBackupGatewayMac       = 15
IpmiLanCommunityString        = 16
IpmiLanReserved3              = 17
IpmiLanDestinationType        = 18
IpmiLanDestinationAddress     = 19
IpmiLanVlanId                 = 0x14
IpmiIpv4OrIpv6Support         = 0x32
IpmiIpv4OrIpv6AddressEnable   = 0x33
IpmiIpv6HdrStatTrafficClass   = 0x34
IpmiIpv6HdrStatHopLimit       = 0x35
IpmiIpv6HdrFlowLabel          = 0x36
IpmiIpv6Status                = 0x37
IpmiIpv6StaticAddress         = 0x38
IpmiIpv6DhcpStaticDuidLen     = 0x39
IpmiIpv6DhcpStaticDuid        = 0x3A
IpmiIpv6DhcpAddress           = 0x3B
IpmiIpv6DhcpDynamicDuidLen    = 0x3C
IpmiIpv6DhcpDynamicDuid       = 0x3D
IpmiIpv6RouterConfig          = 0x40
IpmiIpv6StaticRouter1IpAddr   = 0x41
IpmiIpv6DynamicRouterIpAddr   = 0x4a
IPMI_LAN_OPTION_TYPE          = UINTN

# 
# //
# // IP Address Source
# //
# typedef enum {
#   IpmiUnspecified,
#   IpmiStaticAddrsss,
#   IpmiDynamicAddressBmcDhcp,
#   IpmiDynamicAddressBiosDhcp,
#   IpmiDynamicAddressBmcNonDhcp
# } IPMI_IP_ADDRESS_SRC;
IpmiUnspecified               = 0
IpmiStaticAddrsss             = 1
IpmiDynamicAddressBmcDhcp     = 2
IpmiDynamicAddressBiosDhcp    = 3
IpmiDynamicAddressBmcNonDhcp  = 4
IPMI_IP_ADDRESS_SRC           = UINTN

# 
# //
# // Destination Type
# //
# typedef enum {
#   IpmiPetTrapDestination,
#   IpmiDirectedEventDestination,
#   IpmiReserved1,
#   IpmiReserved2,
#   IpmiReserved3,
#   IpmiReserved4,
#   IpmiReserved5,
#   IpmiOem1,
#   IpmiOem2
# } IPMI_LAN_DEST_TYPE_DEST_TYPE;
IpmiPetTrapDestination          = 0
IpmiDirectedEventDestination    = 1
IpmiReserved1                   = 2
IpmiReserved2                   = 3
IpmiReserved3                   = 4
IpmiReserved4                   = 5
IpmiReserved5                   = 6
IpmiOem1                        = 7
IpmiOem2                        = 8
IPMI_LAN_DEST_TYPE_DEST_TYPE    = UINTN

# 
# //
# // Destination address format
# //
# typedef enum {
#   IpmiDestinationAddressVersion4,
#   IpmiDestinationAddressVersion6
# } IPMI_LAN_DEST_ADDRESS_VERSION;
IpmiDestinationAddressVersion4 = 0x0
IpmiDestinationAddressVersion6 = 0x1
IPMI_LAN_DEST_ADDRESS_VERSION  = ENUM

# 
# typedef union {
#   struct {
#     UINT8    NoAuth       : 1;
#     UINT8    MD2Auth      : 1;
#     UINT8    MD5Auth      : 1;
#     UINT8    Reserved1    : 1;
#     UINT8    StraightPswd : 1;
#     UINT8    OemType      : 1;
#     UINT8    Reserved2    : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_AUTH_TYPE;
class IPMI_LAN_AUTH_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NoAuth",        UINT8, 1),
    ("MD2Auth",       UINT8, 1),
    ("MD5Auth",       UINT8, 1),
    ("Reserved1",     UINT8, 1),
    ("StraightPswd",  UINT8, 1),
    ("OemType",       UINT8, 1),
    ("Reserved2",     UINT8, 2)
  ]

class IPMI_LAN_AUTH_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_AUTH_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    IpAddress[4];
# } IPMI_LAN_IP_ADDRESS;
class IPMI_LAN_IP_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddress", UINT8 * 4)
    ]

# 
# typedef union {
#   struct {
#     UINT8    AddressSrc : 4;
#     UINT8    Reserved   : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_IP_ADDRESS_SRC;
class IPMI_LAN_IP_ADDRESS_SRC_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressSrc",  UINT8, 4),
    ("Reserved",    UINT8, 4)
  ]

class IPMI_LAN_IP_ADDRESS_SRC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_IP_ADDRESS_SRC_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    MacAddress[6];
# } IPMI_LAN_MAC_ADDRESS;
class IPMI_LAN_MAC_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MacAddress", UINT8 * 6)
    ]

# 
# typedef struct {
#   UINT8    IpAddress[4];
# } IPMI_LAN_SUBNET_MASK;
class IPMI_LAN_SUBNET_MASK (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddress", UINT8 * 4)
    ]

# 
# typedef union {
#   struct {
#     UINT8    IpFlag   : 3;
#     UINT8    Reserved : 5;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_IPV4_HDR_PARAM_DATA_2;
class IPMI_LAN_IPV4_HDR_PARAM_DATA_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpFlag",        UINT8, 3),
    ("Reserved",      UINT8, 5)
  ]

class IPMI_LAN_IPV4_HDR_PARAM_DATA_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_IPV4_HDR_PARAM_DATA_2_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Precedence  : 3;
#     UINT8    Reserved    : 1;
#     UINT8    ServiceType : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_IPV4_HDR_PARAM_DATA_3;
class IPMI_LAN_IPV4_HDR_PARAM_DATA_3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Precedence",  UINT8, 3),
    ("Reserved",    UINT8, 1),
    ("ServiceType", UINT8, 4)
  ]

class IPMI_LAN_IPV4_HDR_PARAM_DATA_3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_IPV4_HDR_PARAM_DATA_3_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                             TimeToLive;
#   IPMI_LAN_IPV4_HDR_PARAM_DATA_2    Data2;
#   IPMI_LAN_IPV4_HDR_PARAM_DATA_3    Data3;
# } IPMI_LAN_IPV4_HDR_PARAM;
class IPMI_LAN_IPV4_HDR_PARAM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimeToLive",  UINT8),
    ("Data2",       IPMI_LAN_IPV4_HDR_PARAM_DATA_2),
    ("Data3",       IPMI_LAN_IPV4_HDR_PARAM_DATA_3)
    ]

# 
# typedef struct {
#   UINT8    RcmpPortMsb;
#   UINT8    RcmpPortLsb;
# } IPMI_LAN_RCMP_PORT;
class IPMI_LAN_RCMP_PORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcmpPortMsb",  UINT8),
    ("RcmpPortLsb",  UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    EnableBmcArpResponse   : 1;
#     UINT8    EnableBmcGratuitousArp : 1;
#     UINT8    Reserved               : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_BMC_GENERATED_ARP_CONTROL;
class IPMI_LAN_BMC_GENERATED_ARP_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EnableBmcArpResponse",    UINT8, 1),
    ("EnableBmcGratuitousArp",  UINT8, 1),
    ("Reserved",                UINT8, 6)
    ]

class IPMI_LAN_BMC_GENERATED_ARP_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_BMC_GENERATED_ARP_CONTROL_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    ArpInterval;
# } IPMI_LAN_ARP_INTERVAL;
class IPMI_LAN_ARP_INTERVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ArpInterval", UINT8)
    ]

# 
# typedef struct {
#   UINT8    IpAddress[4];
# } IPMI_LAN_DEFAULT_GATEWAY;
class IPMI_LAN_DEFAULT_GATEWAY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddress", UINT8 * 4)
    ]

# 
# typedef struct {
#   UINT8    Data[18];
# } IPMI_LAN_COMMUNITY_STRING;
class IPMI_LAN_COMMUNITY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    UINT8 * 18)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DestinationSelector : 4;
#     UINT8    Reserved            : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_SET_SELECTOR;
class IPMI_LAN_SET_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector", UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_LAN_SET_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_SET_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DestinationType   : 3;
#     UINT8    Reserved          : 4;
#     UINT8    AlertAcknowledged : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_DEST_TYPE_DESTINATION_TYPE;
class IPMI_LAN_DEST_TYPE_DESTINATION_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationType",     UINT8, 3),
    ("Reserved",            UINT8, 4),
    ("AlertAcknowledged",   UINT8, 1)
    ]

class IPMI_LAN_DEST_TYPE_DESTINATION_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_DEST_TYPE_DESTINATION_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_LAN_SET_SELECTOR                  SetSelector;
#   IPMI_LAN_DEST_TYPE_DESTINATION_TYPE    DestinationType;
# } IPMI_LAN_DEST_TYPE;
class IPMI_LAN_DEST_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector",     IPMI_LAN_SET_SELECTOR),
    ("DestinationType", IPMI_LAN_DEST_TYPE_DESTINATION_TYPE)
    ]

# 
# typedef union {
#   struct {
#     UINT8    AlertingIpAddressSelector : 4;
#     UINT8    AddressFormat             : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_ADDRESS_FORMAT;
class IPMI_LAN_ADDRESS_FORMAT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AlertingIpAddressSelector",   UINT8, 4),
    ("AddressFormat",               UINT8, 4)
    ]

class IPMI_LAN_ADDRESS_FORMAT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_ADDRESS_FORMAT_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    UseDefaultGateway : 1;
#     UINT8    Reserved2         : 7;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_GATEWAY_SELECTOR;
class IPMI_LAN_GATEWAY_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UseDefaultGateway",   UINT8, 1),
    ("Reserved2",           UINT8, 7)
    ]

class IPMI_LAN_GATEWAY_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_GATEWAY_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_LAN_SET_SELECTOR        SetSelector;
#   IPMI_LAN_ADDRESS_FORMAT      AddressFormat;
#   IPMI_LAN_GATEWAY_SELECTOR    GatewaySelector;
#   IPMI_LAN_IP_ADDRESS          AlertingIpAddress;
#   IPMI_LAN_MAC_ADDRESS         AlertingMacAddress;
# } IPMI_LAN_DEST_ADDRESS;
class IPMI_LAN_DEST_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector",         IPMI_LAN_SET_SELECTOR    ),
    ("AddressFormat",       IPMI_LAN_ADDRESS_FORMAT  ),
    ("GatewaySelector",     IPMI_LAN_GATEWAY_SELECTOR),
    ("AlertingIpAddress",   IPMI_LAN_IP_ADDRESS      ),
    ("AlertingMacAddress",  IPMI_LAN_MAC_ADDRESS     )
    ]

# 
# typedef struct {
#   UINT8    VanIdLowByte;
# } IPMI_LAN_VLAN_ID_DATA1;
class IPMI_LAN_VLAN_ID_DATA1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VanIdLowByte",         UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    VanIdHighByte : 4;
#     UINT8    Reserved      : 3;
#     UINT8    Enabled       : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_VLAN_ID_DATA2;
class IPMI_LAN_VLAN_ID_DATA2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VanIdHighByte",   UINT8, 4),
    ("Reserved",        UINT8, 3),
    ("Enabled",         UINT8, 1)
    ]

class IPMI_LAN_VLAN_ID_DATA2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_VLAN_ID_DATA2_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_LAN_VLAN_ID_DATA1    Data1;
#   IPMI_LAN_VLAN_ID_DATA2    Data2;
# } IPMI_LAN_VLAN_ID;
class IPMI_LAN_VLAN_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data1",   IPMI_LAN_VLAN_ID_DATA1),
    ("Data2",   IPMI_LAN_VLAN_ID_DATA2)
    ]

# 
# typedef union {
#   IPMI_LAN_AUTH_TYPE                    IpmiLanAuthType;
#   IPMI_LAN_IP_ADDRESS                   IpmiLanIpAddress;
#   IPMI_LAN_IP_ADDRESS_SRC               IpmiLanIpAddressSrc;
#   IPMI_LAN_MAC_ADDRESS                  IpmiLanMacAddress;
#   IPMI_LAN_SUBNET_MASK                  IpmiLanSubnetMask;
#   IPMI_LAN_IPV4_HDR_PARAM               IpmiLanIpv4HdrParam;
#   IPMI_LAN_RCMP_PORT                    IpmiLanPrimaryRcmpPort;
#   IPMI_LAN_BMC_GENERATED_ARP_CONTROL    IpmiLanArpControl;
#   IPMI_LAN_ARP_INTERVAL                 IpmiLanArpInterval;
#   IPMI_LAN_COMMUNITY_STRING             IpmiLanCommunityString;
#   IPMI_LAN_DEST_TYPE                    IpmiLanDestType;
#   IPMI_LAN_DEST_ADDRESS                 IpmiLanDestAddress;
# } IPMI_LAN_OPTIONS;
class IPMI_LAN_OPTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("IpmiLanAuthType",         IPMI_LAN_AUTH_TYPE                ),
    ("IpmiLanIpAddress",        IPMI_LAN_IP_ADDRESS               ),
    ("IpmiLanIpAddressSrc",     IPMI_LAN_IP_ADDRESS_SRC           ),
    ("IpmiLanMacAddress",       IPMI_LAN_MAC_ADDRESS              ),
    ("IpmiLanSubnetMask",       IPMI_LAN_SUBNET_MASK              ),
    ("IpmiLanIpv4HdrParam",     IPMI_LAN_IPV4_HDR_PARAM           ),
    ("IpmiLanPrimaryRcmpPort",  IPMI_LAN_RCMP_PORT                ),
    ("IpmiLanArpControl",       IPMI_LAN_BMC_GENERATED_ARP_CONTROL),
    ("IpmiLanArpInterval",      IPMI_LAN_ARP_INTERVAL             ),
    ("IpmiLanCommunityString",  IPMI_LAN_COMMUNITY_STRING         ),
    ("IpmiLanDestType",         IPMI_LAN_DEST_TYPE                ),
    ("IpmiLanDestAddress",      IPMI_LAN_DEST_ADDRESS             )
    ]

# 
# typedef union {
#   struct {
#     UINT8    AddressSourceType : 4;
#     UINT8    Reserved          : 3;
#     UINT8    EnableStatus      : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE;
class IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressSourceType",   UINT8, 4),
    ("Reserved",            UINT8, 3),
    ("EnableStatus",        UINT8, 1)
    ]

class IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                SetSelector;
#   IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE    AddressSourceType;
#   UINT8                                Ipv6Address[16];
#   UINT8                                AddressPrefixLen;
#   UINT8                                AddressStatus;
# } IPMI_LAN_IPV6_STATIC_ADDRESS;
class IPMI_LAN_IPV6_STATIC_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector",         UINT8                            ),
    ("AddressSourceType",   IPMI_LAN_IPV6_ADDRESS_SOURCE_TYPE),
    ("Ipv6Address;",        UINT8 * 16                       ),
    ("AddressPrefixLen",    UINT8                            ),
    ("AddressStatus",       UINT8                            )
    ]

# 
# //
# //  Set in progress parameter
# //
# typedef union {
#   struct {
#     UINT8    SetInProgress : 2;
#     UINT8    Reserved      : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_LAN_SET_IN_PROGRESS;
class IPMI_LAN_SET_IN_PROGRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetInProgress",   UINT8, 2),
    ("Reserved",        UINT8, 6)
    ]

class IPMI_LAN_SET_IN_PROGRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_LAN_SET_IN_PROGRESS_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChannelNo : 4;
#     UINT8    Reserved  : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SET_LAN_CONFIG_CHANNEL_NUM;
class IPMI_SET_LAN_CONFIG_CHANNEL_NUM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_SET_LAN_CONFIG_CHANNEL_NUM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_LAN_CONFIG_CHANNEL_NUM_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_SET_LAN_CONFIG_CHANNEL_NUM    ChannelNumber;
#   UINT8                              ParameterSelector;
#   UINT8                              ParameterData[0];
# } IPMI_SET_LAN_CONFIGURATION_PARAMETERS_COMMAND_REQUEST;
class IPMI_SET_LAN_CONFIGURATION_PARAMETERS_COMMAND_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_SET_LAN_CONFIG_CHANNEL_NUM),
    ("ParameterSelector",   UINT8),
    ("ParameterData;",      UINT8 * 0)
    ]

# 
# //
# //  Definitions for Get Lan Configuration Parameters command
# //
# #define IPMI_TRANSPORT_GET_LAN_CONFIG_PARAMETERS  0x02
IPMI_TRANSPORT_GET_LAN_CONFIG_PARAMETERS  = 0x02

# 
# //
# //  Constants and Structure definitions for "Get Lan Configuration Parameters" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChannelNo    : 4;
#     UINT8    Reserved     : 3;
#     UINT8    GetParameter : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_LAN_CONFIG_CHANNEL_NUM;
class IPMI_GET_LAN_CONFIG_CHANNEL_NUM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 3),
    ("GetParameter",UINT8, 1),
    ]

class IPMI_GET_LAN_CONFIG_CHANNEL_NUM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_LAN_CONFIG_CHANNEL_NUM_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_GET_LAN_CONFIG_CHANNEL_NUM    ChannelNumber;
#   UINT8                              ParameterSelector;
#   UINT8                              SetSelector;
#   UINT8                              BlockSelector;
# } IPMI_GET_LAN_CONFIGURATION_PARAMETERS_REQUEST;
class IPMI_GET_LAN_CONFIGURATION_PARAMETERS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_GET_LAN_CONFIG_CHANNEL_NUM),
    ("ParameterSelector",   UINT8),
    ("SetSelector",         UINT8),
    ("BlockSelector",       UINT8)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    ParameterRevision;
#   UINT8    ParameterData[0];
# } IPMI_GET_LAN_CONFIGURATION_PARAMETERS_RESPONSE;
class IPMI_GET_LAN_CONFIGURATION_PARAMETERS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8),
    ("ParameterRevision",   UINT8),
    ("ParameterData",       UINT8 * 0)
    ]

# 
# //
# //  Definitions for Suspend BMC ARPs command
# //
# #define IPMI_TRANSPORT_SUSPEND_BMC_ARPS  0x03
IPMI_TRANSPORT_SUSPEND_BMC_ARPS  = 0x03

# 
# //
# //  Constants and Structure definitions for "Suspend BMC ARPs" command to follow here
# //
# 
# //
# //  Definitions for Get IP-UDP-RMCP Statistics command
# //
# #define IPMI_TRANSPORT_GET_PACKET_STATISTICS  0x04
IPMI_TRANSPORT_GET_PACKET_STATISTICS  = 0x04

# 
# //
# //  Constants and Structure definitions for "Get IP-UDP-RMCP Statistics" command to follow here
# //
# 
# //
# //  Below is Definitions for IPMI Serial/Modem Commands (Chapter 25)
# //
# 
# //
# //  Definitions for Set Serial/Modem Configuration command
# //
# #define IPMI_TRANSPORT_SET_SERIAL_CONFIGURATION  0x10
IPMI_TRANSPORT_SET_SERIAL_CONFIGURATION  = 0x10

# 
# //
# //  Constants and Structure definitions for "Set Serial/Modem Configuration" command to follow here
# //
# 
# //
# // EMP OPTION DATA
# //
# typedef union {
#   struct {
#     UINT8    NoAuthentication  : 1;
#     UINT8    MD2Authentication : 1;
#     UINT8    MD5Authentication : 1;
#     UINT8    Reserved1         : 1;
#     UINT8    StraightPassword  : 1;
#     UINT8    OemProprietary    : 1;
#     UINT8    Reservd2          : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_AUTH_TYPE;
class IPMI_EMP_AUTH_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NoAuthentication",    UINT8, 1),
    ("MD2Authentication",   UINT8, 1),
    ("MD5Authentication",   UINT8, 1),
    ("Reserved1",           UINT8, 1),
    ("StraightPassword",    UINT8, 1),
    ("OemProprietary",      UINT8, 1),
    ("Reservd2",            UINT8, 2),
    ]

class IPMI_EMP_AUTH_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_AUTH_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    EnableBasicMode       : 1;
#     UINT8    EnablePPPMode         : 1;
#     UINT8    EnableTerminalMode    : 1;
#     UINT8    Reserved1             : 2;
#     UINT8    SnoopOsPPPNegotiation : 1;
#     UINT8    Reserved2             : 1;
#     UINT8    DirectConnect         : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_CONNECTION_TYPE;
class IPMI_EMP_CONNECTION_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EnableBasicMode",         UINT8, 1),
    ("EnablePPPMode",           UINT8, 1),
    ("EnableTerminalMode",      UINT8, 1),
    ("Reserved1",               UINT8, 2),
    ("SnoopOsPPPNegotiation",   UINT8, 1),
    ("Reserved2",               UINT8, 1),
    ("DirectConnect",           UINT8, 1)
    ]

class IPMI_EMP_CONNECTION_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_CONNECTION_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    InactivityTimeout : 4;
#     UINT8    Reserved          : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_INACTIVITY_TIMEOUT;
class IPMI_EMP_INACTIVITY_TIMEOUT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InactivityTimeout",   UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_EMP_INACTIVITY_TIMEOUT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_INACTIVITY_TIMEOUT_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    IpmiCallback : 1;
#     UINT8    CBCPCallback : 1;
#     UINT8    Reserved     : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE;
class IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpmiCallback",    UINT8, 1),
    ("CBCPCallback",    UINT8, 1),
    ("Reserved",        UINT8, 6)
    ]

class IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    CbcpEnableNoCallback          : 1;
#     UINT8    CbcpEnablePreSpecifiedNumber  : 1;
#     UINT8    CbcpEnableUserSpecifiedNumber : 1;
#     UINT8    CbcpEnableCallbackFromList    : 1;
#     UINT8    Reserved                      : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_CALLBACK_CONTROL_CBCP;
class IPMI_CHANNEL_CALLBACK_CONTROL_CBCP_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CbcpEnableNoCallback",            UINT8, 1),
    ("CbcpEnablePreSpecifiedNumber",    UINT8, 1),
    ("CbcpEnableUserSpecifiedNumber",   UINT8, 1),
    ("CbcpEnableCallbackFromList",      UINT8, 1),
    ("Reserved",                        UINT8, 4)
    ]

class IPMI_CHANNEL_CALLBACK_CONTROL_CBCP (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_CALLBACK_CONTROL_CBCP_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE    CallbackEnable;
#   IPMI_CHANNEL_CALLBACK_CONTROL_CBCP      CBCPNegotiation;
#   UINT8                                   CallbackDestination1;
#   UINT8                                   CallbackDestination2;
#   UINT8                                   CallbackDestination3;
# } IPMI_EMP_CHANNEL_CALLBACK_CONTROL;
class IPMI_EMP_CHANNEL_CALLBACK_CONTROL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CallbackEnable",          IPMI_CHANNEL_CALLBACK_CONTROL_ENABLE),
    ("CBCPNegotiation",         IPMI_CHANNEL_CALLBACK_CONTROL_CBCP  ),
    ("CallbackDestination1",    UINT8                               ),
    ("CallbackDestination2",    UINT8                               ),
    ("CallbackDestination3",    UINT8                               )
    ]

# 
# typedef union {
#   struct {
#     UINT8    CloseSessionOnDCDLoss          : 1;
#     UINT8    EnableSessionInactivityTimeout : 1;
#     UINT8    Reserved                       : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_SESSION_TERMINATION;
class IPMI_EMP_SESSION_TERMINATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CloseSessionOnDCDLoss",           UINT8, 1),
    ("EnableSessionInactivityTimeout",  UINT8, 1),
    ("Reserved",                        UINT8, 6)
    ]

class IPMI_EMP_SESSION_TERMINATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_SESSION_TERMINATION_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved1       : 5;
#     UINT8    EnableDtrHangup : 1;
#     UINT8    FlowControl     : 2;
#     UINT8    BitRate         : 4;
#     UINT8    Reserved2       : 4;
#     UINT8    SaveSetting     : 1;
#     UINT8    SetComPort      : 1;
#     UINT8    Reserved3       : 6;
#   } Bits;
#   UINT8     Uint8;
#   UINT16    Uint16;
# } IPMI_EMP_MESSAGING_COM_SETTING;
class IPMI_EMP_MESSAGING_COM_SETTING_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",       UINT8, 5),
    ("EnableDtrHangup", UINT8, 1),
    ("FlowControl",     UINT8, 2),
    ("BitRate",         UINT8, 4),
    ("Reserved2",       UINT8, 4),
    ("SaveSetting",     UINT8, 1),
    ("SetComPort",      UINT8, 1),
    ("Reserved3",       UINT8, 6)
    ]

class IPMI_EMP_MESSAGING_COM_SETTING (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_MESSAGING_COM_SETTING_Bits),
    ("Uint8",   UINT8),
    ("Uint16",  UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RingDurationInterval : 6;
#     UINT8    Reserved1            : 2;
#     UINT8    RingDeadTime         : 4;
#     UINT8    Reserved2            : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_MODEM_RING_TIME;
class IPMI_EMP_MODEM_RING_TIME_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RingDurationInterval",    UINT8, 6),
    ("Reserved1",               UINT8, 2),
    ("RingDeadTime",            UINT8, 4),
    ("Reserved2",               UINT8, 4)
    ]

class IPMI_EMP_MODEM_RING_TIME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_MODEM_RING_TIME_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    Reserved;
#   UINT8    InitString[48];
# } IPMI_EMP_MODEM_INIT_STRING;
class IPMI_EMP_MODEM_INIT_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8),
    ("InitString",  UINT8 * 48)
    ]

# 
# typedef struct {
#   UINT8    EscapeSequence[5];
# } IPMI_EMP_MODEM_ESC_SEQUENCE;
class IPMI_EMP_MODEM_ESC_SEQUENCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EscapeSequence",  UINT8 * 5)
    ]

# 
# typedef struct {
#   UINT8    HangupSequence[8];
# } IPMI_EMP_MODEM_HANGUP_SEQUENCE;
class IPMI_EMP_MODEM_HANGUP_SEQUENCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HangupSequence",  UINT8 * 8)
    ]

# 
# typedef struct {
#   UINT8    ModelDialCommend[8];
# } IPMI_MODEM_DIALUP_COMMAND;
class IPMI_MODEM_DIALUP_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModelDialCommend",  UINT8 * 8)
    ]

# 
# typedef struct {
#   UINT8    PageBlackoutInterval;
# } IPMI_PAGE_BLACKOUT_INTERVAL;
class IPMI_PAGE_BLACKOUT_INTERVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PageBlackoutInterval",UINT8)
    ]

# 
# typedef struct {
#   UINT8    CommunityString[18];
# } IPMI_EMP_COMMUNITY_STRING;
class IPMI_EMP_COMMUNITY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CommunityString", UINT8 * 18)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved           : 4;
#     UINT8    DialStringSelector : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_DIAL_PAGE_DESTINATION;
class IPMI_DIAL_PAGE_DESTINATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 4),
    ("DialStringSelector",  UINT8, 4)
    ]

class IPMI_DIAL_PAGE_DESTINATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_DIAL_PAGE_DESTINATION_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    TapAccountSelector : 4;
#     UINT8    Reserved           : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_TAP_PAGE_DESTINATION;
class IPMI_TAP_PAGE_DESTINATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapAccountSelector",  UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_TAP_PAGE_DESTINATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_TAP_PAGE_DESTINATION_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    PPPAccountSetSelector;
#   UINT8    DialStringSelector;
# } IPMI_PPP_ALERT_DESTINATION;
class IPMI_PPP_ALERT_DESTINATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PPPAccountSetSelector",   UINT8),
    ("DialStringSelector",      UINT8)
    ]

# 
# typedef union {
#   IPMI_DIAL_PAGE_DESTINATION    DialPageDestination;
#   IPMI_TAP_PAGE_DESTINATION     TapPageDestination;
#   IPMI_PPP_ALERT_DESTINATION    PppAlertDestination;
# } IPMI_DEST_TYPE_SPECIFIC;
class IPMI_DEST_TYPE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("DialPageDestination", IPMI_DIAL_PAGE_DESTINATION),
    ("TapPageDestination",  IPMI_TAP_PAGE_DESTINATION ),
    ("PppAlertDestination", IPMI_PPP_ALERT_DESTINATION)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DestinationSelector : 4;
#     UINT8    Reserved            : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_DESTINATION_SELECTOR;
class IPMI_EMP_DESTINATION_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector", UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_EMP_DESTINATION_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_DESTINATION_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DestinationType  : 4;
#     UINT8    Reserved         : 3;
#     UINT8    AlertAckRequired : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_DESTINATION_TYPE;
class IPMI_EMP_DESTINATION_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationType",     UINT8, 4),
    ("Reserved",            UINT8, 3),
    ("AlertAckRequired",    UINT8, 1)
    ]

class IPMI_EMP_DESTINATION_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_DESTINATION_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    NumRetriesCall : 3;
#     UINT8    Reserved1      : 1;
#     UINT8    NumRetryAlert  : 3;
#     UINT8    Reserved2      : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_RETRIES;
class IPMI_EMP_RETRIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NumRetriesCall",  UINT8, 3),
    ("Reserved1",       UINT8, 1),
    ("NumRetryAlert",   UINT8, 3),
    ("Reserved2",       UINT8, 1)
    ]

class IPMI_EMP_RETRIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_RETRIES_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_EMP_DESTINATION_SELECTOR    DestinationSelector;
#   IPMI_EMP_DESTINATION_TYPE        DestinationType;
#   UINT8                            AlertAckTimeoutSeconds;
#   IPMI_EMP_RETRIES                 Retries;
#   IPMI_DEST_TYPE_SPECIFIC          DestinationTypeSpecific;
# } IPMI_EMP_DESTINATION_INFO;
class IPMI_EMP_DESTINATION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector",     IPMI_EMP_DESTINATION_SELECTOR),
    ("DestinationType",         IPMI_EMP_DESTINATION_TYPE    ),
    ("AlertAckTimeoutSeconds",  UINT8                        ),
    ("Retries",                 IPMI_EMP_RETRIES             ),
    ("DestinationTypeSpecific", IPMI_DEST_TYPE_SPECIFIC      )
    ]

# 
# typedef union {
#   struct {
#     UINT8    Parity        : 3;
#     UINT8    CharacterSize : 1;
#     UINT8    StopBit       : 1;
#     UINT8    DtrHangup     : 1;
#     UINT8    FlowControl   : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_DESTINATION_COM_SETTING_DATA_2;
class IPMI_EMP_DESTINATION_COM_SETTING_DATA_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Parity",          UINT8, 3),
    ("CharacterSize",   UINT8, 1),
    ("StopBit",         UINT8, 1),
    ("DtrHangup",       UINT8, 1),
    ("FlowControl",     UINT8, 2)
    ]

class IPMI_EMP_DESTINATION_COM_SETTING_DATA_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_DESTINATION_COM_SETTING_DATA_2_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    BitRate  : 4;
#     UINT8    Reserved : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_EMP_BIT_RATE;
class IPMI_EMP_BIT_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BitRate",     UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_EMP_BIT_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_EMP_BIT_RATE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_EMP_DESTINATION_SELECTOR              DestinationSelector;
#   IPMI_EMP_DESTINATION_COM_SETTING_DATA_2    Data2;
#   IPMI_EMP_BIT_RATE                          BitRate;
# } IPMI_EMP_DESTINATION_COM_SETTING;
class IPMI_EMP_DESTINATION_COM_SETTING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector", IPMI_EMP_DESTINATION_SELECTOR),
    ("Data2",               IPMI_EMP_DESTINATION_COM_SETTING_DATA_2),
    ("BitRate",             IPMI_EMP_BIT_RATE)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DialStringSelector : 4;
#     UINT8    Reserved           : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_DIAL_STRING_SELECTOR;
class IPMI_DIAL_STRING_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DialStringSelector",  UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_DIAL_STRING_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_DIAL_STRING_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_DIAL_STRING_SELECTOR    DestinationSelector;
#   UINT8                        Reserved;
#   UINT8                        DialString[48];
# } IPMI_DESTINATION_DIAL_STRING;
class IPMI_DESTINATION_DIAL_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector", IPMI_DIAL_STRING_SELECTOR),
    ("Reserved",            UINT8),
    ("DialString",          UINT8 * 48)
    ]

# 
# typedef union {
#   UINT32    IpAddressLong;
#   UINT8     IpAddress[4];
# } IPMI_PPP_IP_ADDRESS;
class IPMI_PPP_IP_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("IpAddressLong",   UINT32),
    ("IpAddress",       UINT8 * 4)
    ]

# 
# typedef union {
#   struct {
#     UINT8    IpAddressSelector : 4;
#     UINT8    Reserved          : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_DESTINATION_IP_ADDRESS_SELECTOR;
class IPMI_DESTINATION_IP_ADDRESS_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IpAddressSelector",   UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_DESTINATION_IP_ADDRESS_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_DESTINATION_IP_ADDRESS_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_DESTINATION_IP_ADDRESS_SELECTOR    DestinationSelector;
#   IPMI_PPP_IP_ADDRESS                     PppIpAddress;
# } IPMI_DESTINATION_IP_ADDRESS;
class IPMI_DESTINATION_IP_ADDRESS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DestinationSelector", IPMI_DESTINATION_IP_ADDRESS_SELECTOR),
    ("PppIpAddress",        IPMI_PPP_IP_ADDRESS)
    ]

# 
# typedef union {
#   struct {
#     UINT8    TapServiceSelector    : 4;
#     UINT8    TapDialStringSelector : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR;
class IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapServiceSelector",      UINT8, 4),
    ("TapDialStringSelector",   UINT8, 4)
    ]

class IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                    TapSelector;
#   IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR    TapDialStringServiceSelector;
# } IPMI_DESTINATION_TAP_ACCOUNT;
class IPMI_DESTINATION_TAP_ACCOUNT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapSelector",                     UINT8),
    ("TapDialStringServiceSelector",    IPMI_TAP_DIAL_STRING_SERVICE_SELECTOR)
    ]

# 
# typedef struct {
#   UINT8    TapSelector;
#   UINT8    PagerIdString[16];
# } IPMI_TAP_PAGER_ID_STRING;
class IPMI_TAP_PAGER_ID_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TapSelector",     UINT8),
    ("PagerIdString",   UINT8 * 16)
    ]

# 
# typedef union {
#   UINT8                                OptionData;
#   IPMI_EMP_AUTH_TYPE                   EmpAuthType;
#   IPMI_EMP_CONNECTION_TYPE             EmpConnectionType;
#   IPMI_EMP_INACTIVITY_TIMEOUT          EmpInactivityTimeout;
#   IPMI_EMP_CHANNEL_CALLBACK_CONTROL    EmpCallbackControl;
#   IPMI_EMP_SESSION_TERMINATION         EmpSessionTermination;
#   IPMI_EMP_MESSAGING_COM_SETTING       EmpMessagingComSetting;
#   IPMI_EMP_MODEM_RING_TIME             EmpModemRingTime;
#   IPMI_EMP_MODEM_INIT_STRING           EmpModemInitString;
#   IPMI_EMP_MODEM_ESC_SEQUENCE          EmpModemEscSequence;
#   IPMI_EMP_MODEM_HANGUP_SEQUENCE       EmpModemHangupSequence;
#   IPMI_MODEM_DIALUP_COMMAND            EmpModemDialupCommand;
#   IPMI_PAGE_BLACKOUT_INTERVAL          EmpPageBlackoutInterval;
#   IPMI_EMP_COMMUNITY_STRING            EmpCommunityString;
#   IPMI_EMP_DESTINATION_INFO            EmpDestinationInfo;
#   IPMI_EMP_DESTINATION_COM_SETTING     EmpDestinationComSetting;
#   UINT8                                CallRetryBusySignalInterval;
#   IPMI_DESTINATION_DIAL_STRING         DestinationDialString;
#   IPMI_DESTINATION_IP_ADDRESS          DestinationIpAddress;
#   IPMI_DESTINATION_TAP_ACCOUNT         DestinationTapAccount;
#   IPMI_TAP_PAGER_ID_STRING             TapPagerIdString;
# } IPMI_EMP_OPTIONS;
class IPMI_EMP_OPTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("OptionData",                  UINT8                            ),
    ("EmpAuthType",                 IPMI_EMP_AUTH_TYPE               ),
    ("EmpConnectionType",           IPMI_EMP_CONNECTION_TYPE         ),
    ("EmpInactivityTimeout",        IPMI_EMP_INACTIVITY_TIMEOUT      ),
    ("EmpCallbackControl",          IPMI_EMP_CHANNEL_CALLBACK_CONTROL),
    ("EmpSessionTermination",       IPMI_EMP_SESSION_TERMINATION     ),
    ("EmpMessagingComSetting",      IPMI_EMP_MESSAGING_COM_SETTING   ),
    ("EmpModemRingTime",            IPMI_EMP_MODEM_RING_TIME         ),
    ("EmpModemInitString",          IPMI_EMP_MODEM_INIT_STRING       ),
    ("EmpModemEscSequence",         IPMI_EMP_MODEM_ESC_SEQUENCE      ),
    ("EmpModemHangupSequence",      IPMI_EMP_MODEM_HANGUP_SEQUENCE   ),
    ("EmpModemDialupCommand",       IPMI_MODEM_DIALUP_COMMAND        ),
    ("EmpPageBlackoutInterval",     IPMI_PAGE_BLACKOUT_INTERVAL      ),
    ("EmpCommunityString",          IPMI_EMP_COMMUNITY_STRING        ),
    ("EmpDestinationInfo",          IPMI_EMP_DESTINATION_INFO        ),
    ("EmpDestinationComSetting",    IPMI_EMP_DESTINATION_COM_SETTING ),
    ("CallRetryBusySignalInterval", UINT8                            ),
    ("DestinationDialString",       IPMI_DESTINATION_DIAL_STRING     ),
    ("DestinationIpAddress",        IPMI_DESTINATION_IP_ADDRESS      ),
    ("DestinationTapAccount",       IPMI_DESTINATION_TAP_ACCOUNT     ),
    ("TapPagerIdString",            IPMI_TAP_PAGER_ID_STRING         )
    ]

# 
# //
# //  Definitions for Get Serial/Modem Configuration command
# //
# #define IPMI_TRANSPORT_GET_SERIAL_CONFIGURATION  0x11
IPMI_TRANSPORT_GET_SERIAL_CONFIGURATION  = 0x11

# 
# //
# //  Constants and Structure definitions for "Get Serial/Modem Configuration" command to follow here
# //
# 
# //
# //  Definitions for Set Serial/Modem Mux command
# //
# #define IPMI_TRANSPORT_SET_SERIAL_MUX  0x12
IPMI_TRANSPORT_SET_SERIAL_MUX  = 0x12

# 
# //
# //  Constants and Structure definitions for "Set Serial/Modem Mux" command to follow here
# //
# 
# //
# // Set Serial/Modem Mux command request return status
# //
# #define IPMI_MUX_SETTING_REQUEST_REJECTED  0x00
# #define IPMI_MUX_SETTING_REQUEST_ACCEPTED  0x01
IPMI_MUX_SETTING_REQUEST_REJECTED  = 0x00
IPMI_MUX_SETTING_REQUEST_ACCEPTED  = 0x01

# 
# //
# //  Definitions for serial multiplex settings
# //
# #define IPMI_MUX_SETTING_GET_MUX_SETTING              0x0
# #define IPMI_MUX_SETTING_REQUEST_MUX_TO_SYSTEM        0x1
# #define IPMI_MUX_SETTING_REQUEST_MUX_TO_BMC           0x2
# #define IPMI_MUX_SETTING_FORCE_MUX_TO_SYSTEM          0x3
# #define IPMI_MUX_SETTING_FORCE_MUX_TO_BMC             0x4
# #define IPMI_MUX_SETTING_BLOCK_REQUEST_MUX_TO_SYSTEM  0x5
# #define IPMI_MUX_SETTING_ALLOW_REQUEST_MUX_TO_SYSTEM  0x6
# #define IPMI_MUX_SETTING_BLOCK_REQUEST_MUX_TO_BMC     0x7
# #define IPMI_MUX_SETTING_ALLOW_REQUEST_MUX_TO_BMC     0x8
IPMI_MUX_SETTING_GET_MUX_SETTING              = 0x0
IPMI_MUX_SETTING_REQUEST_MUX_TO_SYSTEM        = 0x1
IPMI_MUX_SETTING_REQUEST_MUX_TO_BMC           = 0x2
IPMI_MUX_SETTING_FORCE_MUX_TO_SYSTEM          = 0x3
IPMI_MUX_SETTING_FORCE_MUX_TO_BMC             = 0x4
IPMI_MUX_SETTING_BLOCK_REQUEST_MUX_TO_SYSTEM  = 0x5
IPMI_MUX_SETTING_ALLOW_REQUEST_MUX_TO_SYSTEM  = 0x6
IPMI_MUX_SETTING_BLOCK_REQUEST_MUX_TO_BMC     = 0x7
IPMI_MUX_SETTING_ALLOW_REQUEST_MUX_TO_BMC     = 0x8

# 
# typedef union {
#   struct {
#     UINT8    ChannelNo : 4;
#     UINT8    Reserved  : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_MUX_CHANNEL_NUM;
class IPMI_MUX_CHANNEL_NUM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_MUX_CHANNEL_NUM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_MUX_CHANNEL_NUM_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MuxSetting : 4;
#     UINT8    Reserved   : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_MUX_SETTING_REQUEST;
class IPMI_MUX_SETTING_REQUEST_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MuxSetting",  UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_MUX_SETTING_REQUEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_MUX_SETTING_REQUEST_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_MUX_CHANNEL_NUM        ChannelNumber;
#   IPMI_MUX_SETTING_REQUEST    MuxSetting;
# } IPMI_SET_SERIAL_MODEM_MUX_COMMAND_REQUEST;
class IPMI_SET_SERIAL_MODEM_MUX_COMMAND_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_MUX_CHANNEL_NUM),
    ("MuxSetting",      IPMI_MUX_SETTING_REQUEST)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MuxSetToBmc            : 1;
#     UINT8    CommandStatus          : 1;
#     UINT8    MessagingSessionActive : 1;
#     UINT8    AlertInProgress        : 1;
#     UINT8    Reserved               : 2;
#     UINT8    MuxToBmcAllowed        : 1;
#     UINT8    MuxToSystemBlocked     : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_MUX_SETTING_PRESENT_STATE;
class IPMI_MUX_SETTING_PRESENT_STATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MuxSetToBmc",             UINT8, 1),
    ("CommandStatus",           UINT8, 1),
    ("MessagingSessionActive",  UINT8, 1),
    ("AlertInProgress",         UINT8, 1),
    ("Reserved",                UINT8, 2),
    ("MuxToBmcAllowed",         UINT8, 1),
    ("MuxToSystemBlocked",      UINT8, 1)
    ]

class IPMI_MUX_SETTING_PRESENT_STATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_MUX_SETTING_PRESENT_STATE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                             CompletionCode;
#   IPMI_MUX_SETTING_PRESENT_STATE    MuxSetting;
# } IPMI_SET_SERIAL_MODEM_MUX_COMMAND_RESPONSE;
class IPMI_SET_SERIAL_MODEM_MUX_COMMAND_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("MuxSetting",      IPMI_MUX_SETTING_PRESENT_STATE)
    ]

# 
# //
# //  Definitions for Get TAP Response Code command
# //
# #define IPMI_TRANSPORT_GET_TAP_RESPONSE_CODE  0x13
IPMI_TRANSPORT_GET_TAP_RESPONSE_CODE  = 0x13

# 
# //
# //  Constants and Structure definitions for "Get TAP Response Code" command to follow here
# //
# 
# //
# //  Definitions for Set PPP UDP Proxy Transmit Data command
# //
# #define IPMI_TRANSPORT_SET_PPP_UDP_PROXY_TXDATA  0x14
IPMI_TRANSPORT_SET_PPP_UDP_PROXY_TXDATA  = 0x14

# 
# //
# //  Constants and Structure definitions for "Set PPP UDP Proxy Transmit Data" command to follow here
# //
# 
# //
# //  Definitions for Get PPP UDP Proxy Transmit Data command
# //
# #define IPMI_TRANSPORT_GET_PPP_UDP_PROXY_TXDATA  0x15
IPMI_TRANSPORT_GET_PPP_UDP_PROXY_TXDATA  = 0x15

# 
# //
# //  Constants and Structure definitions for "Get PPP UDP Proxy Transmit Data" command to follow here
# //
# 
# //
# //  Definitions for Send PPP UDP Proxy Packet command
# //
# #define IPMI_TRANSPORT_SEND_PPP_UDP_PROXY_PACKET  0x16
IPMI_TRANSPORT_SEND_PPP_UDP_PROXY_PACKET  = 0x16

# 
# //
# //  Constants and Structure definitions for "Send PPP UDP Proxy Packet" command to follow here
# //
# 
# //
# //  Definitions for Get PPP UDP Proxy Receive Data command
# //
# #define IPMI_TRANSPORT_GET_PPP_UDP_PROXY_RX  0x17
IPMI_TRANSPORT_GET_PPP_UDP_PROXY_RX  = 0x17

# 
# //
# //  Constants and Structure definitions for "Get PPP UDP Proxy Receive Data" command to follow here
# //
# 
# //
# //  Definitions for Serial/Modem connection active command
# //
# #define IPMI_TRANSPORT_SERIAL_CONNECTION_ACTIVE  0x18
IPMI_TRANSPORT_SERIAL_CONNECTION_ACTIVE  = 0x18

# 
# //
# //  Constants and Structure definitions for "Serial/Modem connection active" command to follow here
# //
# 
# //
# //  Definitions for Callback command
# //
# #define IPMI_TRANSPORT_CALLBACK  0x19
IPMI_TRANSPORT_CALLBACK  = 0x19

# 
# //
# //  Constants and Structure definitions for "Callback" command to follow here
# //
# 
# //
# //  Definitions for Set user Callback Options command
# //
# #define IPMI_TRANSPORT_SET_USER_CALLBACK_OPTIONS  0x1A
IPMI_TRANSPORT_SET_USER_CALLBACK_OPTIONS  = 0x1A

# 
# //
# //  Constants and Structure definitions for "Set user Callback Options" command to follow here
# //
# 
# //
# //  Definitions for Get user Callback Options command
# //
# #define IPMI_TRANSPORT_GET_USER_CALLBACK_OPTIONS  0x1B
IPMI_TRANSPORT_GET_USER_CALLBACK_OPTIONS  = 0x1B

# 
# //
# //  Constants and Structure definitions for "Get user Callback Options" command to follow here
# //
# 
# //
# //  Below is Definitions for SOL Commands (Chapter 26)
# //
# 
# //
# //  Definitions for SOL activating command
# //
# #define IPMI_TRANSPORT_SOL_ACTIVATING  0x20
IPMI_TRANSPORT_SOL_ACTIVATING  = 0x20

# 
# //
# //  Constants and Structure definitions for "SOL activating" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    SessionState : 4;
#     UINT8    Reserved     : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SOL_SESSION_STATE;
class IPMI_SOL_SESSION_STATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SessionState",    UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_SOL_SESSION_STATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SOL_SESSION_STATE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_SOL_SESSION_STATE    SessionState;
#   UINT8                     PayloadInstance;
#   UINT8                     FormatVersionMajor; // 1
#   UINT8                     FormatVersionMinor; // 0
# } IPMI_SOL_ACTIVATING_REQUEST;
class IPMI_SOL_ACTIVATING_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SessionState",        IPMI_SOL_SESSION_STATE),
    ("PayloadInstance",     UINT8),
    ("FormatVersionMajor",  UINT8),
    ("FormatVersionMinor",  UINT8)
    ]

# 
# //
# //  Definitions for Set SOL Configuration Parameters command
# //
# #define IPMI_TRANSPORT_SET_SOL_CONFIG_PARAM  0x21
IPMI_TRANSPORT_SET_SOL_CONFIG_PARAM  = 0x21

# 
# //
# //  Constants and Structure definitions for "Set SOL Configuration Parameters" command to follow here
# //
# 
# //
# // SOL Configuration Parameters selector
# //
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SET_IN_PROGRESS        0
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_ENABLE             1
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_AUTHENTICATION     2
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_CHARACTER_PARAM    3
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_RETRY              4
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_NV_BIT_RATE        5
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_VOLATILE_BIT_RATE  6
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_PAYLOAD_CHANNEL    7
# #define IPMI_SOL_CONFIGURATION_PARAMETER_SOL_PAYLOAD_PORT       8
IPMI_SOL_CONFIGURATION_PARAMETER_SET_IN_PROGRESS        = 0
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_ENABLE             = 1
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_AUTHENTICATION     = 2
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_CHARACTER_PARAM    = 3
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_RETRY              = 4
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_NV_BIT_RATE        = 5
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_VOLATILE_BIT_RATE  = 6
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_PAYLOAD_CHANNEL    = 7
IPMI_SOL_CONFIGURATION_PARAMETER_SOL_PAYLOAD_PORT       = 8

# 
# typedef union {
#   struct {
#     UINT8    ChannelNumber : 4;
#     UINT8    Reserved      : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM;
class IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM    ChannelNumber;
#   UINT8                                    ParameterSelector;
#   UINT8                                    ParameterData[0];
# } IPMI_SET_SOL_CONFIGURATION_PARAMETERS_REQUEST;
class IPMI_SET_SOL_CONFIGURATION_PARAMETERS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_SET_SOL_CONFIG_PARAM_CHANNEL_NUM),
    ("ParameterSelector",   UINT8),
    ("ParameterData",       UINT8 * 0)
    ]

# 
# //
# //  Definitions for Get SOL Configuration Parameters command
# //
# #define IPMI_TRANSPORT_GET_SOL_CONFIG_PARAM  0x22
IPMI_TRANSPORT_GET_SOL_CONFIG_PARAM  = 0x22

# 
# //
# //  Constants and Structure definitions for "Get SOL Configuration Parameters" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChannelNumber : 4;
#     UINT8    Reserved      : 3;
#     UINT8    GetParameter  : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM;
class IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Reserved",        UINT8, 3),
    ("GetParameter",    UINT8, 1)
    ]

class IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM    ChannelNumber;
#   UINT8                                    ParameterSelector;
#   UINT8                                    SetSelector;
#   UINT8                                    BlockSelector;
# } IPMI_GET_SOL_CONFIGURATION_PARAMETERS_REQUEST;
class IPMI_GET_SOL_CONFIGURATION_PARAMETERS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_GET_SOL_CONFIG_PARAM_CHANNEL_NUM),
    ("ParameterSelector",   UINT8),
    ("SetSelector",         UINT8),
    ("BlockSelector",       UINT8)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    ParameterRevision;
#   UINT8    ParameterData[0];
# } IPMI_GET_SOL_CONFIGURATION_PARAMETERS_RESPONSE;
class IPMI_GET_SOL_CONFIGURATION_PARAMETERS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8),
    ("ParameterRevision",   UINT8),
    ("ParameterData",       UINT8 * 0)
    ]

# 
# #pragma pack()
# #endif
# 