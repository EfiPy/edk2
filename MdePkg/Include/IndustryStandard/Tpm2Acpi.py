# /** @file
#   TPM2 ACPI table definition.
# 
# Copyright (c) 2013 - 2019, Intel Corporation. All rights reserved. <BR>
# Copyright (c) 2021, Ampere Computing LLC. All rights reserved. <BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Tpm2Acpi.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm2Acpi
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _TPM2_ACPI_H_
# #define _TPM2_ACPI_H_
# 
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack (1)
# 
# #define EFI_TPM2_ACPI_TABLE_REVISION_3  3
# #define EFI_TPM2_ACPI_TABLE_REVISION_4  4
# #define EFI_TPM2_ACPI_TABLE_REVISION    EFI_TPM2_ACPI_TABLE_REVISION_4
# 
EFI_TPM2_ACPI_TABLE_REVISION_3  = 3
EFI_TPM2_ACPI_TABLE_REVISION_4  = 4
EFI_TPM2_ACPI_TABLE_REVISION  = EFI_TPM2_ACPI_TABLE_REVISION_4  

# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   // Flags field is replaced in version 4 and above
#   //    BIT0~15:  PlatformClass      This field is only valid for version 4 and above
#   //    BIT16~31: Reserved
#   UINT32                         Flags;
#   UINT64                         AddressOfControlArea;
#   UINT32                         StartMethod;
#   // UINT8                       PlatformSpecificParameters[];  // size up to 12
#   // UINT32                      Laml;                          // Optional
#   // UINT64                      Lasa;                          // Optional
# } EFI_TPM2_ACPI_TABLE;
class EFI_TPM2_ACPI_TABLE (Structure):
  _fields_ = [
    ("Header",                      Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("Flags",                       UINT32),
    ("AddressOfControlArea",        UINT64),
    ("StartMethod",                 UINT32)
    # ("PlatformSpecificParameters",  UINT8 * N),
    # ("Laml",                        UINT32),
    # ("Lasa",                        UINT64),
  ]

# 
# #define EFI_TPM2_ACPI_TABLE_START_METHOD_ACPI                                         2
# #define EFI_TPM2_ACPI_TABLE_START_METHOD_TIS                                          6
# #define EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE            7
# #define EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_ACPI  8
# #define EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_SMC   11
EFI_TPM2_ACPI_TABLE_START_METHOD_ACPI                                          = 2
EFI_TPM2_ACPI_TABLE_START_METHOD_TIS                                           = 6
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE             = 7
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_ACPI   = 8
EFI_TPM2_ACPI_TABLE_START_METHOD_COMMAND_RESPONSE_BUFFER_INTERFACE_WITH_SMC   = 11

# 
# typedef struct {
#   UINT32    Reserved;
#   UINT32    Error;
#   UINT32    Cancel;
#   UINT32    Start;
#   UINT64    InterruptControl;
#   UINT32    CommandSize;
#   UINT64    Command;
#   UINT32    ResponseSize;
#   UINT64    Response;
# } EFI_TPM2_ACPI_CONTROL_AREA;
class EFI_TPM2_ACPI_CONTROL_AREA (Structure):
  _fields_ = [
    ("Reserved",          UINT32),
    ("Error",             UINT32),
    ("Cancel",            UINT32),
    ("Start",             UINT32),
    ("InterruptControl",  UINT64),
    ("CommandSize",       UINT32),
    ("Command",           UINT64),
    ("ResponseSize",      UINT32),
    ("Response",          UINT64)
  ]

# 
# //
# // Start Method Specific Parameters for ARM SMC Start Method (11)
# // Refer to Table 9: Start Method Specific Parameters for ARM SMC
# //
# typedef struct {
#   UINT32    Interrupt;
#   UINT8     Flags;
#   UINT8     OperationFlags;
#   UINT8     Reserved[2];
#   UINT32    SmcFunctionId;
# } EFI_TPM2_ACPI_START_METHOD_SPECIFIC_PARAMETERS_ARM_SMC;
class EFI_TPM2_ACPI_START_METHOD_SPECIFIC_PARAMETERS_ARM_SMC (Structure):
  _fields_ = [
    ("Interrupt",       UINT32),
    ("Flags",           UINT8),
    ("OperationFlags",  UINT8),
    ("Reserved",        UINT8 * 2),
    ("SmcFunctionId",   UINT32)
  ]

# 
# #pragma pack ()
# 
# #endif
# 