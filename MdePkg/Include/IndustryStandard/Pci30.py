# /** @file
#   Support for PCI 3.0 standard.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Pci30.py
#
# EfiPy2.MdePkg.IndustryStandard.Pci30
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __PCI30_H__
# #define __PCI30_H__
# 
# #include <IndustryStandard/Pci23.h>
from EfiPy2.MdePkg.IndustryStandard.Pci23 import *

# 
# ///
# /// PCI_CLASS_MASS_STORAGE, Base Class 01h.
# ///
# ///@{
# #define PCI_CLASS_MASS_STORAGE_SATADPA  0x06
# #define   PCI_IF_MASS_STORAGE_SATA      0x00
# #define   PCI_IF_MASS_STORAGE_AHCI      0x01
PCI_CLASS_MASS_STORAGE_SATADPA   = 0x06
PCI_IF_MASS_STORAGE_SATA         = 0x00
PCI_IF_MASS_STORAGE_AHCI         = 0x01

# ///@}
# 
# ///
# /// PCI_CLASS_WIRELESS, Base Class 0Dh.
# ///
# ///@{
# #define PCI_SUBCLASS_ETHERNET_80211A  0x20
# #define PCI_SUBCLASS_ETHERNET_80211B  0x21
PCI_SUBCLASS_ETHERNET_80211A    = 0x20
PCI_SUBCLASS_ETHERNET_80211B    = 0x21

# ///@}
# 
# /**
#   Macro that checks whether device is a SATA controller.
# 
#   @param  _p      Specified device.
# 
#   @retval TRUE    Device is a SATA controller.
#   @retval FALSE   Device is not a SATA controller.
# 
# **/
# #define IS_PCI_SATADPA(_p)  IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_SATADPA)
def IS_PCI_SATADPA(_p):
  return IS_CLASS2 (_p, PCI_CLASS_MASS_STORAGE, PCI_CLASS_MASS_STORAGE_SATADPA)

# 
# ///
# /// PCI Capability List IDs and records
# ///
# #define EFI_PCI_CAPABILITY_ID_PCIEXP  0x10
EFI_PCI_CAPABILITY_ID_PCIEXP  = 0x10

# 
# #pragma pack(1)
# 
# ///
# /// PCI Data Structure Format
# /// Section 5.1.2, PCI Firmware Specification, Revision 3.0
# ///
# typedef struct {
#   UINT32    Signature;  ///< "PCIR"
#   UINT16    VendorId;
#   UINT16    DeviceId;
#   UINT16    DeviceListOffset;
#   UINT16    Length;
#   UINT8     Revision;
#   UINT8     ClassCode[3];
#   UINT16    ImageLength;
#   UINT16    CodeRevision;
#   UINT8     CodeType;
#   UINT8     Indicator;
#   UINT16    MaxRuntimeImageLength;
#   UINT16    ConfigUtilityCodeHeaderOffset;
#   UINT16    DMTFCLPEntryPointOffset;
# } PCI_3_0_DATA_STRUCTURE;
class PCI_3_0_DATA_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",                     UINT32),
    ("VendorId",                      UINT16),
    ("DeviceId",                      UINT16),
    ("DeviceListOffset",              UINT16),
    ("Length",                        UINT16),
    ("Revision",                      UINT8),
    ("ClassCode",                     UINT8 * 3),
    ("ImageLength",                   UINT16),
    ("CodeRevision",                  UINT16),
    ("CodeType",                      UINT8),
    ("Indicator",                     UINT8),
    ("MaxRuntimeImageLength",         UINT16),
    ("ConfigUtilityCodeHeaderOffset", UINT16),
    ("DMTFCLPEntryPointOffset",       UINT16)
    ]

# 
# #pragma pack()
# 
# #endif
# 