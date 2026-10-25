# /** @file
#   TCPA ACPI table definition.
# 
# Copyright (c) 2013, Intel Corporation. All rights reserved. <BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# TcpaAcpi.py
#
# EfiPy2.MdePkg.IndustryStandard.TcpaAcpi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _TCPA_ACPI_H_
# #define _TCPA_ACPI_H_
# 
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack (1)
# 
# typedef struct _EFI_TCG_CLIENT_ACPI_TABLE {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT16                         PlatformClass;
#   UINT32                         Laml;
#   UINT64                         Lasa;
# } EFI_TCG_CLIENT_ACPI_TABLE;
class EFI_TCG_CLIENT_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",        Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass", UINT16),
    ("Laml",          UINT32),
    ("Lasa",          UINT64)
  ]

# 
# typedef struct _EFI_TCG_SERVER_ACPI_TABLE {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   UINT16                                    PlatformClass;
#   UINT16                                    Reserved0;
#   UINT64                                    Laml;
#   UINT64                                    Lasa;
#   UINT16                                    SpecRev;
#   UINT8                                     DeviceFlags;
#   UINT8                                     InterruptFlags;
#   UINT8                                     Gpe;
#   UINT8                                     Reserved1[3];
#   UINT32                                    GlobalSysInt;
#   EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE    BaseAddress;
#   UINT32                                    Reserved2;
#   EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE    ConfigAddress;
#   UINT8                                     PciSegNum;
#   UINT8                                     PciBusNum;
#   UINT8                                     PciDevNum;
#   UINT8                                     PciFuncNum;
# } EFI_TCG_SERVER_ACPI_TABLE;
class EFI_TCG_SERVER_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",          Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("PlatformClass",   UINT16),
    ("Reserved0",       UINT16),
    ("Laml",            UINT64),
    ("Lasa",            UINT64),
    ("SpecRev",         UINT16),
    ("DeviceFlags",     UINT8),
    ("InterruptFlags",  UINT8),
    ("Gpe",             UINT8),
    ("Reserved1",       UINT8 * 3),
    ("GlobalSysInt",    UINT32),
    ("BaseAddress",     Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("Reserved2",       UINT32),
    ("ConfigAddress",   Acpi.EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE),
    ("PciSegNum",       UINT8),
    ("PciBusNum",       UINT8),
    ("PciDevNum",       UINT8),
    ("PciFuncNum",      UINT8)
  ]

# 
# //
# // TCG Platform Type based on TCG ACPI Specification Version 1.00
# //
# #define TCG_PLATFORM_TYPE_CLIENT  0
# #define TCG_PLATFORM_TYPE_SERVER  1
TCG_PLATFORM_TYPE_CLIENT   = 0
TCG_PLATFORM_TYPE_SERVER   = 1

# 
# #pragma pack ()
# 
# #endif
# 