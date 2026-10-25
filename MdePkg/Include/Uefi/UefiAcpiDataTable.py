# /** @file
#   UEFI ACPI Data Table Definition.
# 
# Copyright (c) 2011 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# UefiAcpiDataTable.py
#
# EfiPy2.MdePkg.Uefi.UefiAcpiDataTable
#   part of EfiPy2
#
# Copyright (C) 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __UEFI_ACPI_DATA_TABLE_H__
# #define __UEFI_ACPI_DATA_TABLE_H__
import EfiPy2 as EfiPy

# 
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE

# 
# #pragma pack(1)
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   GUID                           Identifier;
#   UINT16                         DataOffset;
# } EFI_ACPI_DATA_TABLE;
class EFI_ACPI_DATA_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Identifier",          EfiPy.GUID),
    ("DataOffset",          EfiPy.UINT16),
  ]

# #pragma pack()
# 
# #endif
# 