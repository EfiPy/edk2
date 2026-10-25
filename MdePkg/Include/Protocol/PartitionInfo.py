# /** @file
#   This file defines the EFI Partition Information Protocol.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol is introduced in UEFI Specification 2.7
# 
# **/
# PartitionInfo.py
#
# EfiPy2.MdePkg.Protocol.PartitionInfo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __PARTITION_INFO_PROTOCOL_H__
# #define __PARTITION_INFO_PROTOCOL_H__
from EfiPy2 import *

# 
# #include <IndustryStandard/Mbr.h>
from EfiPy2.MdePkg.IndustryStandard.Mbr import MBR_PARTITION_RECORD

# #include <Uefi/UefiGpt.h>
from EfiPy2.MdePkg.Uefi.UefiGpt         import EFI_PARTITION_ENTRY

# 
# //
# // EFI Partition Information Protocol GUID value
# //
# #define EFI_PARTITION_INFO_PROTOCOL_GUID \
#   { 0x8cf2f62c, 0xbc9b, 0x4821, { 0x80, 0x8d, 0xec, 0x9e, 0xc4, 0x21, 0xa1, 0xa0 }};
gEfiPartitionInfoProtocolGuid           = \
  EFI_GUID (0x8cf2f62c, 0xbc9b, 0x4821, ( 0x80, 0x8d, 0xec, 0x9e, 0xc4, 0x21, 0xa1, 0xa0 ))

# 
# #define EFI_PARTITION_INFO_PROTOCOL_REVISION  0x0001000
# #define PARTITION_TYPE_OTHER                  0x00
# #define PARTITION_TYPE_MBR                    0x01
# #define PARTITION_TYPE_GPT                    0x02
EFI_PARTITION_INFO_PROTOCOL_REVISION  = 0x0001000
PARTITION_TYPE_OTHER                  = 0x00
PARTITION_TYPE_MBR                    = 0x01
PARTITION_TYPE_GPT                    = 0x02

# 
# #pragma pack(1)
# 
# ///
# /// Partition Information Protocol structure.
# ///
# typedef struct {
#   //
#   // Set to EFI_PARTITION_INFO_PROTOCOL_REVISION.
#   //
#   UINT32    Revision;
#   //
#   // Partition info type (PARTITION_TYPE_MBR, PARTITION_TYPE_GPT, or PARTITION_TYPE_OTHER).
#   //
#   UINT32    Type;
#   //
#   // If 1, partition describes an EFI System Partition.
#   //
#   UINT8     System;
#   UINT8     Reserved[7];
#   union {
#     ///
#     /// MBR data
#     ///
#     MBR_PARTITION_RECORD    Mbr;
#     ///
#     /// GPT data
#     ///
#     EFI_PARTITION_ENTRY     Gpt;
#   } Info;
# } EFI_PARTITION_INFO_PROTOCOL;
class EFI_PARTITION_INFO_PROTOCOL_Info (Union):
  _pack_   = 1
  _fields_  = [
    ("Mbr", MBR_PARTITION_RECORD),
    ("Gpt", EFI_PARTITION_ENTRY),
  ]

class EFI_PARTITION_INFO_PROTOCOL (Structure):
  _pack_   = 1
  _fields_  = [
    ("Revision",    UINT32),
    ("Type",        UINT32),
    ("System",      UINT8),
    ("Reserved",    UINT8 * 7),
    ("Info",        EFI_PARTITION_INFO_PROTOCOL_Info)
  ]

# 
# #pragma pack()
# 
# ///
# /// Partition Information Protocol GUID variable.
# ///
# extern EFI_GUID  gEfiPartitionInfoProtocolGuid;
# 
# #endif
# 