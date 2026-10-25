# /** @file
#   ACPI high precision event timer table definition, at www.intel.com
#   Specification name is IA-PC HPET (High Precision Event Timers) Specification.
# 
#   Copyright (c) 2007 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# 
# #ifndef _HIGH_PRECISION_EVENT_TIMER_TABLE_H_
# #define _HIGH_PRECISION_EVENT_TIMER_TABLE_H_
#
# HighPrecisionEventTimerTable.py
#
# EfiPy2.MdePkg.IndustryStandard.HighPrecisionEventTimerTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
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
# /// HPET Event Timer Block ID described in IA-PC HPET Specification, 3.2.4.
# ///
# typedef union {
#   struct {
#     UINT32    Revision       : 8;
#     UINT32    NumberOfTimers : 5;
#     UINT32    CounterSize    : 1;
#     UINT32    Reserved       : 1;
#     UINT32    LegacyRoute    : 1;
#     UINT32    VendorId       : 16;
#   }      Bits;
#   UINT32    Uint32;
# } EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID;
class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",        UINT32, 8),
    ("NumberOfTimers",  UINT32, 5),
    ("CounterSize",     UINT32, 1),
    ("Reserved",        UINT32, 1),
    ("LegacyRoute",     UINT32, 1),
    ("VendorId",        UINT32, 16)
  ]

class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_BLOCK_ID_Bits),
    ("Uint32",          UINT32)
  ]

# 
# ///
# /// High Precision Event Timer Table header definition.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   UINT32                                    EventTimerBlockId;
#   EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE    BaseAddressLower32Bit;
#   UINT8                                     HpetNumber;
#   UINT16                                    MainCounterMinimumClockTickInPeriodicMode;
#   UINT8                                     PageProtectionAndOemAttribute;
# } EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER;
class EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                    Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("EventTimerBlockId",                         UINT32),
    ("BaseAddressLower32Bit",                     Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("HpetNumber",                                UINT8),
    ("MainCounterMinimumClockTickInPeriodicMode", UINT16),
    ("PageProtectionAndOemAttribute",             UINT8)
  ]

# 
# ///
# /// HPET Revision (defined in spec)
# ///
# #define EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_REVISION  0x01
EFI_ACPI_HIGH_PRECISION_EVENT_TIMER_TABLE_REVISION  = 0x01

# 
# //
# // Page protection setting
# // Values 3 through 15 are reserved for use by the specification
# //
# #define EFI_ACPI_NO_PAGE_PROTECTION    0
# #define EFI_ACPI_4KB_PAGE_PROTECTION   1
# #define EFI_ACPI_64KB_PAGE_PROTECTION  2
# 
EFI_ACPI_NO_PAGE_PROTECTION    = 0
EFI_ACPI_4KB_PAGE_PROTECTION   = 1
EFI_ACPI_64KB_PAGE_PROTECTION  = 2

# #pragma pack()
# 
# #endif
# 