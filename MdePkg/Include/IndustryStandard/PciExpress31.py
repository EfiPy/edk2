# /** @file
# Support for the PCI Express 3.1 standard.
# 
# This header file may not define all structures.  Please extend as required.
# 
# Copyright (c) 2016, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# PciExpress31.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress31
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _PCIEXPRESS31_H_
# #define _PCIEXPRESS31_H_
# 
# #include <IndustryStandard/PciExpress30.h>
from EfiPy2.MdePkg.IndustryStandard.PciExpress30 import *

# 
# #pragma pack(1)
# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_ID    0x001E
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_VER1  0x1
# 
PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_ID    = 0x001E
PCI_EXPRESS_EXTENDED_CAPABILITY_L1_PM_SUBSTATES_VER1  = 0x1

# typedef union {
#   struct {
#     UINT32    PciPmL12              : 1;
#     UINT32    PciPmL11              : 1;
#     UINT32    AspmL12               : 1;
#     UINT32    AspmL11               : 1;
#     UINT32    L1PmSubstates         : 1;
#     UINT32    Reserved              : 3;
#     UINT32    CommonModeRestoreTime : 8;
#     UINT32    TPowerOnScale         : 2;
#     UINT32    Reserved2             : 1;
#     UINT32    TPowerOnValue         : 5;
#     UINT32    Reserved3             : 8;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY;
class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PciPmL12",                UINT32, 1),
    ("PciPmL11",                UINT32, 1),
    ("AspmL12",                 UINT32, 1),
    ("AspmL11",                 UINT32, 1),
    ("L1PmSubstates",           UINT32, 1),
    ("Reserved",                UINT32, 3),
    ("CommonModeRestoreTime",   UINT32, 8),
    ("TPowerOnScale",           UINT32, 2),
    ("Reserved2",               UINT32, 1),
    ("TPowerOnValue",           UINT32, 5),
    ("Reserved3",               UINT32, 8)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    PciPmL12              : 1;
#     UINT32    PciPmL11              : 1;
#     UINT32    AspmL12               : 1;
#     UINT32    AspmL11               : 1;
#     UINT32    Reserved              : 4;
#     UINT32    CommonModeRestoreTime : 8;
#     UINT32    LtrL12ThresholdValue  : 10;
#     UINT32    Reserved2             : 3;
#     UINT32    LtrL12ThresholdScale  : 3;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1;
class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PciPmL12",                UINT32, 1),
    ("PciPmL11",                UINT32, 1),
    ("AspmL12",                 UINT32, 1),
    ("AspmL11",                 UINT32, 1),
    ("Reserved",                UINT32, 4),
    ("CommonModeRestoreTime",   UINT32, 8),
    ("LtrL12ThresholdValue",    UINT32, 10),
    ("Reserved2",               UINT32, 3),
    ("LtrL12ThresholdScale",    UINT32, 3)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    TPowerOnScale : 2;
#     UINT32    Reserved      : 1;
#     UINT32    TPowerOnValue : 5;
#     UINT32    Reserved2     : 24;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2;
class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TPowerOnScale",   UINT32, 2),
    ("Reserved",        UINT32, 1),
    ("TPowerOnValue",   UINT32, 5),
    ("Reserved2",       UINT32, 24)
  ]

class PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER      Header;
#   PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY    Capability;
#   PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1      Control1;
#   PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2      Control2;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_L1_PM_SUBSTATES;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_L1_PM_SUBSTATES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("Capability",  PCI_EXPRESS_REG_L1_PM_SUBSTATES_CAPABILITY),
    ("Control1",    PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL1),
    ("Control2",    PCI_EXPRESS_REG_L1_PM_SUBSTATES_CONTROL2)
  ]

# 
# #pragma pack()
# 
# #endif
# 