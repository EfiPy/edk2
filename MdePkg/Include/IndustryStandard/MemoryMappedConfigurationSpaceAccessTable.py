# /** @file
#   ACPI memory mapped configuration space access table definition, defined at
#   in the PCI Firmware Specification, version 3.0.
#   Specification is available at http://www.pcisig.com.
# 
#   Copyright (c) 2007 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
#
# MemoryMappedConfigurationSpaceAccessTable.py
#
# EfiPy2.MdePkg.IndustryStandard.MemoryMappedConfigurationSpaceAccessTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_H_
# #define _MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_H_
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
# ///
# /// Memory Mapped Configuration Space Access Table (MCFG)
# /// This table is a basic description table header followed by
# /// a number of base address allocation structures.
# ///
# typedef struct {
#   UINT64    BaseAddress;
#   UINT16    PciSegmentGroupNumber;
#   UINT8     StartBusNumber;
#   UINT8     EndBusNumber;
#   UINT32    Reserved;
# } EFI_ACPI_MEMORY_MAPPED_ENHANCED_CONFIGURATION_SPACE_BASE_ADDRESS_ALLOCATION_STRUCTURE;
class EFI_ACPI_MEMORY_MAPPED_ENHANCED_CONFIGURATION_SPACE_BASE_ADDRESS_ALLOCATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BaseAddress",           UINT64),
    ("PciSegmentGroupNumber", UINT16),
    ("StartBusNumber",        UINT8),
    ("EndBusNumber",          UINT8),
    ("Reserved",              UINT32)
  ]

# 
# ///
# /// MCFG Table header definition.  The rest of the table
# /// must be defined in a platform specific manner.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT64                         Reserved;
# } EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_HEADER;
class EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_BASE_ADDRESS_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT64)
  ]

# 
# ///
# /// MCFG Revision (defined in spec)
# ///
# #define EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_REVISION  0x01
EFI_ACPI_MEMORY_MAPPED_CONFIGURATION_SPACE_ACCESS_TABLE_REVISION  = 0x01

# 
# #pragma pack()
# 
# #endif
# 