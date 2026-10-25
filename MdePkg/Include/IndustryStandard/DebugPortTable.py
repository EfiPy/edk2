# /** @file
#   ACPI debug port table definition, defined at
#   Microsoft DebugPortSpecification.
# 
#   Copyright (c) 2012 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# DebugPortTable.py
#
# EfiPy2.MdePkg.IndustryStandard.DebugPortTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _DEBUG_PORT_TABLE_H_
# #define _DEBUG_PORT_TABLE_H_
# 
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

# 
# //
# // Ensure proper structure formats
# //
# #pragma pack(1)
# 
# //
# // Debug Port Table definition.
# //
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   UINT8                                     InterfaceType;
#   UINT8                                     Reserved_37[3];
#   EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE    BaseAddress;
# } EFI_ACPI_DEBUG_PORT_DESCRIPTION_TABLE;
class EFI_ACPI_DEBUG_PORT_DESCRIPTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("InterfaceType",     UINT8),
    ("Reserved_37",       UINT8 * 3),
    ("BaseAddress",       Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE)
  ]

# 
# #pragma pack()
# 
# //
# // DBGP Revision (defined in spec)
# //
# #define EFI_ACPI_DEBUG_PORT_TABLE_REVISION  0x01
EFI_ACPI_DEBUG_PORT_TABLE_REVISION      = 0x01

# 
# //
# // Interface Type
# //
# #define EFI_ACPI_DBGP_INTERFACE_TYPE_FULL_16550                                 0
# #define EFI_ACPI_DBGP_INTERFACE_TYPE_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC  1
EFI_ACPI_DBGP_INTERFACE_TYPE_FULL_16550                                 = 0
EFI_ACPI_DBGP_INTERFACE_TYPE_16550_SUBSET_COMPATIBLE_WITH_MS_DBGP_SPEC  = 1

# 
# #endif
# 