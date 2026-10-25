# /** @file
#   ACPI Watchdog Resource Table (WDRT) as defined at
#   Microsoft Windows Hardware Developer Central.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
#
# WatchdogResourceTable.py
#
# EfiPy2.MdePkg.IndustryStandard.WatchdogResourceTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _WATCHDOG_RESOURCE_TABLE_H_
# #define _WATCHDOG_RESOURCE_TABLE_H_
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
# /// Watchdog Resource Table definition.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE    ControlRegisterAddress;
#   EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE    CountRegisterAddress;
#   UINT16                                    PCIDeviceID;
#   UINT16                                    PCIVendorID;
#   UINT8                                     PCIBusNumber;
#   UINT8                                     PCIDeviceNumber;
#   UINT8                                     PCIFunctionNumber;
#   UINT8                                     PCISegment;
#   UINT16                                    MaxCount;
#   UINT8                                     Units;
# } EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE;
class EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("ControlRegisterAddress",  Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("CountRegisterAddress",    Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("PCIDeviceID",             UINT16),
    ("PCIVendorID",             UINT16),
    ("PCIBusNumber",            UINT8),
    ("PCIDeviceNumber",         UINT8),
    ("PCIFunctionNumber",       UINT8),
    ("PCISegment",              UINT8),
    ("MaxCount",                UINT16),
    ("Units",                   UINT8)
  ]

# 
# #pragma pack()
# 
# //
# // WDRT Revision (defined in spec)
# //
# #define EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE_REVISION  0x01
EFI_ACPI_WATCHDOG_RESOURCE_1_0_TABLE_REVISION  = 0x01

# 
# //
# // WDRT 1.0 Count Unit
# //
# #define EFI_ACPI_WDRT_1_0_COUNT_UNIT_1_SEC_PER_COUNT         1
# #define EFI_ACPI_WDRT_1_0_COUNT_UNIT_100_MILLISEC_PER_COUNT  2
# #define EFI_ACPI_WDRT_1_0_COUNT_UNIT_10_MILLISEC_PER_COUNT   3
EFI_ACPI_WDRT_1_0_COUNT_UNIT_1_SEC_PER_COUNT        = 1
EFI_ACPI_WDRT_1_0_COUNT_UNIT_100_MILLISEC_PER_COUNT = 2
EFI_ACPI_WDRT_1_0_COUNT_UNIT_10_MILLISEC_PER_COUNT  = 3

# 
# #endif
# 