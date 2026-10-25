# /** @file
# Support for the PCI Express 4.0 standard.
# 
# This header file may not define all structures.  Please extend as required.
# 
# Copyright (c) 2018, American Megatrends, Inc. All rights reserved.<BR>
# Copyright (c) 2020, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# PciExpress40.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress40
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _PCIEXPRESS40_H_
# #define _PCIEXPRESS40_H_
# 
# #include <IndustryStandard/PciExpress31.h>
from EfiPy2.MdePkg.IndustryStandard.PciExpress31 import *

# 
# #pragma pack(1)
# 
# /// The Physical Layer PCI Express Extended Capability definitions.
# ///
# /// Based on section 7.7.5 of PCI Express Base Specification 4.0.
# ///@{
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_ID    0x0026
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_VER1  0x1
# 
PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_ID    = 0x0026
PCI_EXPRESS_EXTENDED_CAPABILITY_PHYSICAL_LAYER_16_0_VER1  = 0x1

# // Register offsets from Physical Layer PCI-E Ext Cap Header
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_OFFSET                       0x04
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_OFFSET                            0x08
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_OFFSET                             0x0C
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LOCAL_DATA_PARITY_STATUS_OFFSET           0x10
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_FIRST_RETIMER_DATA_PARITY_STATUS_OFFSET   0x14
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_SECOND_RETIMER_DATA_PARITY_STATUS_OFFSET  0x18
# #define PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_OFFSET          0x20
# 
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_OFFSET                       = 0x04
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_OFFSET                            = 0x08
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_OFFSET                             = 0x0C
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LOCAL_DATA_PARITY_STATUS_OFFSET           = 0x10
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_FIRST_RETIMER_DATA_PARITY_STATUS_OFFSET   = 0x14
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_SECOND_RETIMER_DATA_PARITY_STATUS_OFFSET  = 0x18
PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_OFFSET          = 0x20

# typedef union {
#   struct {
#     UINT32    Reserved : 32;               // Reserved bit 0:31
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES;
class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    Reserved : 32;               // Reserved bit 0:31
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL;
class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT32, 32)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    EqualizationComplete      : 1;  // bit 0
#     UINT32    EqualizationPhase1Success : 1;  // bit 1
#     UINT32    EqualizationPhase2Success : 1;  // bit 2
#     UINT32    EqualizationPhase3Success : 1;  // bit 3
#     UINT32    LinkEqualizationRequest   : 1;  // bit 4
#     UINT32    Reserved                  : 27; // Reserved bit 5:31
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS;
class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EqualizationComplete",        UINT32, 1),
    ("EqualizationPhase1Success",   UINT32, 1),
    ("EqualizationPhase2Success",   UINT32, 1),
    ("EqualizationPhase3Success",   UINT32, 1),
    ("LinkEqualizationRequest",     UINT32, 1),
    ("Reserved",                    UINT32, 27)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DownstreamPortTransmitterPreset : 4; // bit 0..3
#     UINT8    UpstreamPortTransmitterPreset   : 4; // bit 4..7
#   } Bits;
#   UINT8    Uint8;
# } PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL;
class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset", UINT8, 4),
    ("UpstreamPortTransmitterPreset",   UINT8, 4)
  ]

class PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint8",           UINT8)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                         Header;
#   PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES                 Capablities;
#   PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL                      Control;
#   PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS                       Status;
#   UINT32                                                           LocalDataParityMismatchStatus;
#   UINT32                                                           FirstRetimerDataParityMismatchStatus;
#   UINT32                                                           SecondRetimerDataParityMismatchStatus;
#   UINT32                                                           Reserved;
#   PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL    LaneEqualizationControl[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_PHYSICAL_LAYER_16_0;
# ///@}
class PCI_EXPRESS_EXTENDED_CAPABILITIES_PHYSICAL_LAYER_16_0 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                         ),
    ("Capablities",                             PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CAPABILITIES                 ),
    ("Control",                                 PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_CONTROL                      ),
    ("Status",                                  PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_STATUS                       ),
    ("LocalDataParityMismatchStatus",           UINT32                                                           ),
    ("FirstRetimerDataParityMismatchStatus",    UINT32                                                           ),
    ("SecondRetimerDataParityMismatchStatus",   UINT32                                                           ),
    ("Reserved",                                UINT32                                                           ),
    ("LaneEqualizationControl",                 PCI_EXPRESS_REG_PHYSICAL_LAYER_16_0_LANE_EQUALIZATION_CONTROL * 1)
  ]

# 
# /// The Designated Vendor Specific Capability definitions
# /// Based on section 7.9.6 of PCI Express Base Specification 4.0.
# ///@{
# typedef union {
#   struct {
#     UINT32    DvsecVendorId : 16;                                     // bit 0..15
#     UINT32    DvsecRevision : 4;                                      // bit 16..19
#     UINT32    DvsecLength   : 12;                                     // bit 20..31
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1;
class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DvsecVendorId",   UINT32, 16),
    ("DvsecRevision",   UINT32, 4),
    ("DvsecLength",     UINT32, 12)
  ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT16    DvsecId : 16;                                           // bit 0..15
#   } Bits;
#   UINT16    Uint16;
# } PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2;
class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DvsecId",         UINT16, 16)
  ]

class PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER           Header;
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1    DesignatedVendorSpecificHeader1;
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2    DesignatedVendorSpecificHeader2;
#   UINT8                                              DesignatedVendorSpecific[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_DESIGNATED_VENDOR_SPECIFIC;
# ///@}
class PCI_EXPRESS_EXTENDED_CAPABILITIES_DESIGNATED_VENDOR_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("DesignatedVendorSpecific",        UINT8 * 1)
  ]

# 
# #pragma pack()
# 
# #endif
# 