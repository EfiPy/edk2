# /** @file
#   Support for the PCI Express 3.0 standard.
# 
#   This header file may not define all structures.  Please extend as required.
# 
#   Copyright (c) 2014 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# PciExpress30.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _PCIEXPRESS30_H_
# #define _PCIEXPRESS30_H_
# 
# #include <IndustryStandard/PciExpress21.h>
from EfiPy2.MdePkg.IndustryStandard.PciExpress21 import *

# 
# #pragma pack(1)
# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_ID    0x0019
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_ID    = 0x0019
PCI_EXPRESS_EXTENDED_CAPABILITY_SECONDARY_PCIE_VER1  = 0x1   

# 
# typedef union {
#   struct {
#     UINT32    PerformEqualization                    : 1;
#     UINT32    LinkEqualizationRequestInterruptEnable : 1;
#     UINT32    Reserved                               : 30;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_LINK_CONTROL3;
class PCI_EXPRESS_REG_LINK_CONTROL3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PerformEqualization",                     UINT32, 1),
    ("LinkEqualizationRequestInterruptEnable",  UINT32, 1),
    ("Reserved",                                UINT32, 30)
  ]

class PCI_EXPRESS_REG_LINK_CONTROL3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_LINK_CONTROL3_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT16    DownstreamPortTransmitterPreset  : 4;
#     UINT16    DownstreamPortReceiverPresetHint : 3;
#     UINT16    Reserved                         : 1;
#     UINT16    UpstreamPortTransmitterPreset    : 4;
#     UINT16    UpstreamPortReceiverPresetHint   : 3;
#     UINT16    Reserved2                        : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL;
class PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DownstreamPortTransmitterPreset",     UINT16, 4),
    ("DownstreamPortReceiverPresetHint",    UINT16, 3),
    ("Reserved",                            UINT16, 1),
    ("UpstreamPortTransmitterPreset",       UINT16, 4),
    ("UpstreamPortReceiverPresetHint",      UINT16, 3),
    ("Reserved2",                           UINT16, 1)
  ]

class PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER     Header;
#   PCI_EXPRESS_REG_LINK_CONTROL3                LinkControl3;
#   UINT32                                       LaneErrorStatus;
#   PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL    EqualizationControl[2];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_SECONDARY_PCIE;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_SECONDARY_PCIE (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("LinkControl3",        PCI_EXPRESS_REG_LINK_CONTROL3),
    ("LaneErrorStatus",     UINT32),
    ("EqualizationControl", PCI_EXPRESS_REG_LANE_EQUALIZATION_CONTROL * 2)
    ]

# 
# #pragma pack()
# 
# #endif
# 