# /** @file
#   Legacy Master Boot Record Format Definition.
# 
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# Mbr.py
#
# EfiPy2.MdePkg.IndustryStandard.Mbr
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _MBR_H_
# #define _MBR_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #define MBR_SIGNATURE  0xaa55
MBR_SIGNATURE               = 0xaa55

# 
# #define EXTENDED_DOS_PARTITION      0x05
# #define EXTENDED_WINDOWS_PARTITION  0x0F
EXTENDED_DOS_PARTITION      = 0x05
EXTENDED_WINDOWS_PARTITION  = 0x0F

# 
# #define MAX_MBR_PARTITIONS  4
MAX_MBR_PARTITIONS          = 4

# 
# #define PMBR_GPT_PARTITION  0xEE
# #define EFI_PARTITION       0xEF
PMBR_GPT_PARTITION          = 0xEE
EFI_PARTITION               = 0xEF

# 
# #define MBR_SIZE  512
MBR_SIZE                    = 512

# 
# #pragma pack(1)
# ///
# /// MBR Partition Entry
# ///
# typedef struct {
#   UINT8    BootIndicator;
#   UINT8    StartHead;
#   UINT8    StartSector;
#   UINT8    StartTrack;
#   UINT8    OSIndicator;
#   UINT8    EndHead;
#   UINT8    EndSector;
#   UINT8    EndTrack;
#   UINT8    StartingLBA[4];
#   UINT8    SizeInLBA[4];
# } MBR_PARTITION_RECORD;
class MBR_PARTITION_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootIndicator", UINT8),
    ("StartHead",     UINT8),
    ("StartSector",   UINT8),
    ("StartTrack",    UINT8),
    ("OSIndicator",   UINT8),
    ("EndHead",       UINT8),
    ("EndSector",     UINT8),
    ("EndTrack",      UINT8),
    ("StartingLBA",   UINT8 * 4),
    ("SizeInLBA",     UINT8 * 4)
  ]

# 
# ///
# /// MBR Partition Table
# ///
# typedef struct {
#   UINT8                   BootStrapCode[440];
#   UINT8                   UniqueMbrSignature[4];
#   UINT8                   Unknown[2];
#   MBR_PARTITION_RECORD    Partition[MAX_MBR_PARTITIONS];
#   UINT16                  Signature;
# } MASTER_BOOT_RECORD;
class MASTER_BOOT_RECORD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BootStrapCode",       UINT8 * 440),
    ("UniqueMbrSignature",  UINT8 * 4),
    ("Unknown",             UINT8 * 2),
    ("Partition",           MBR_PARTITION_RECORD * MAX_MBR_PARTITIONS),
    ("Signature",           UINT16)
  ]

# 
# #pragma pack()
# 
# #endif
# 