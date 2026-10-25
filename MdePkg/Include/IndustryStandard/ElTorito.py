# /** @file
#   ElTorito Partitions Format Definition.
#   This file includes some definitions from
#   1. "El Torito" Bootable CD-ROM Format Specification, Version 1.0.
#   2. Volume and File Structure of CDROM for Information Interchange,
#      Standard ECMA-119. (IS0 9660)
# 
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
#
# ElTorito.py
#
# EfiPy2.MdePkg.IndustryStandard.ElTorito
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _ELTORITO_H_
# #define _ELTORITO_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# //
# // CDROM_VOLUME_DESCRIPTOR.Types, defined in ISO 9660
# //
# #define CDVOL_TYPE_STANDARD  0x0
# #define CDVOL_TYPE_CODED     0x1
# #define CDVOL_TYPE_END       0xFF
CDVOL_TYPE_STANDARD = 0x0
CDVOL_TYPE_CODED    = 0x1
CDVOL_TYPE_END      = 0xFF

# 
# ///
# /// CDROM_VOLUME_DESCRIPTOR.Id
# ///
# #define CDVOL_ID  "CD001"
CDVOL_ID  = "CD001"

# 
# ///
# /// CDROM_VOLUME_DESCRIPTOR.SystemId
# ///
# #define CDVOL_ELTORITO_ID  "EL TORITO SPECIFICATION"
CDVOL_ELTORITO_ID = "EL TORITO SPECIFICATION"

# 
# //
# // Indicator types
# //
# #define ELTORITO_ID_CATALOG               0x01
# #define ELTORITO_ID_SECTION_BOOTABLE      0x88
# #define ELTORITO_ID_SECTION_NOT_BOOTABLE  0x00
# #define ELTORITO_ID_SECTION_HEADER        0x90
# #define ELTORITO_ID_SECTION_HEADER_FINAL  0x91
ELTORITO_ID_CATALOG               = 0x01
ELTORITO_ID_SECTION_BOOTABLE      = 0x88
ELTORITO_ID_SECTION_NOT_BOOTABLE  = 0x00
ELTORITO_ID_SECTION_HEADER        = 0x90
ELTORITO_ID_SECTION_HEADER_FINAL  = 0x91

# 
# //
# // ELTORITO_CATALOG.Boot.MediaTypes
# //
# #define ELTORITO_NO_EMULATION  0x00
# #define ELTORITO_12_DISKETTE   0x01
# #define ELTORITO_14_DISKETTE   0x02
# #define ELTORITO_28_DISKETTE   0x03
# #define ELTORITO_HARD_DISK     0x04
ELTORITO_NO_EMULATION = 0x00
ELTORITO_12_DISKETTE  = 0x01
ELTORITO_14_DISKETTE  = 0x02
ELTORITO_28_DISKETTE  = 0x03
ELTORITO_HARD_DISK    = 0x04

# 
# #pragma pack(1)
# 
# ///
# /// CD-ROM Volume Descriptor
# ///
# typedef union {
#   struct {
#     UINT8    Type;
#     CHAR8    Id[5];          ///< "CD001"
#     CHAR8    Reserved[82];
#   } Unknown;
# 
#   ///
#   /// Boot Record Volume Descriptor, defined in "El Torito" Specification.
#   ///
#   struct {
#     UINT8    Type;           ///< Must be 0
#     CHAR8    Id[5];          ///< "CD001"
#     UINT8    Version;        ///< Must be 1
#     CHAR8    SystemId[32];   ///< "EL TORITO SPECIFICATION"
#     CHAR8    Unused[32];     ///< Must be 0
#     UINT8    EltCatalog[4];  ///< Absolute pointer to first sector of Boot Catalog
#     CHAR8    Unused2[13];    ///< Must be 0
#   } BootRecordVolume;
# 
#   ///
#   /// Primary Volume Descriptor, defined in ISO 9660.
#   ///
#   struct {
#     UINT8     Type;
#     CHAR8     Id[5];         ///< "CD001"
#     UINT8     Version;
#     UINT8     Unused;        ///< Must be 0
#     CHAR8     SystemId[32];
#     CHAR8     VolumeId[32];
#     UINT8     Unused2[8];      ///< Must be 0
#     UINT32    VolSpaceSize[2]; ///< the number of Logical Blocks
#   } PrimaryVolume;
# } CDROM_VOLUME_DESCRIPTOR;
class CDROM_VOLUME_DESCRIPTOR_Unknown (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",      UINT8),
    ("Id",        CHAR8 * 5),
    ("Version",   CHAR8 * 82)
  ]

class CDROM_VOLUME_DESCRIPTOR_BootRecordVolume (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        UINT8),
    ("Id",          CHAR8 * 5),
    ("Version",     UINT8),
    ("SystemId",    CHAR8 * 32),
    ("Unused",      CHAR8 * 32),
    ("EltCatalog",  UINT8 * 4),
    ("Unused2",     CHAR8 * 13)
  ]

class CDROM_VOLUME_DESCRIPTOR_PrimaryVolume (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",          UINT8),
    ("Id",            CHAR8  * 5),
    ("Version",       UINT8),
    ("Unused",        UINT8),
    ("SystemId",      CHAR8  * 32),
    ("VolumeId",      CHAR8  * 32),
    ("Unused2",       UINT8  * 8),
    ("VolSpaceSize",  UINT32 * 2)
  ]

class CDROM_VOLUME_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unknown",           CDROM_VOLUME_DESCRIPTOR_Unknown),
    ("BootRecordVolume",  CDROM_VOLUME_DESCRIPTOR_BootRecordVolume),
    ("PrimaryVolume",     CDROM_VOLUME_DESCRIPTOR_PrimaryVolume)
  ]

# 
# ///
# /// Catalog Entry
# ///
# typedef union {
#   struct {
#     CHAR8    Reserved[0x20];
#   } Unknown;
# 
#   ///
#   /// Catalog validation entry (Catalog header)
#   ///
#   struct {
#     UINT8     Indicator;     ///< Must be 01
#     UINT8     PlatformId;
#     UINT16    Reserved;
#     CHAR8     ManufacId[24];
#     UINT16    Checksum;
#     UINT16    Id55AA;
#   } Catalog;
# 
#   ///
#   /// Initial/Default Entry or Section Entry
#   ///
#   struct {
#     UINT8     Indicator;     ///< 88 = Bootable, 00 = Not Bootable
#     UINT8     MediaType : 4;
#     UINT8     Reserved1 : 4; ///< Must be 0
#     UINT16    LoadSegment;
#     UINT8     SystemType;
#     UINT8     Reserved2;     ///< Must be 0
#     UINT16    SectorCount;
#     UINT32    Lba;
#   } Boot;
# 
#   ///
#   /// Section Header Entry
#   ///
#   struct {
#     UINT8     Indicator;     ///< 90 - Header, more header follw, 91 - Final Header
#     UINT8     PlatformId;
#     UINT16    SectionEntries; ///< Number of section entries following this header
#     CHAR8     Id[28];
#   } Section;
# } ELTORITO_CATALOG;
class ELTORITO_CATALOG_Unknown (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",  CHAR8 * 0x20)
  ]

class ELTORITO_CATALOG_Catalog (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",   UINT8),
    ("PlatformId",  UINT8),
    ("Reserved",    UINT16),
    ("ManufacId",   UINT8 * 24),
    ("Checksum",    UINT16),
    ("Id55AA",      UINT16)
  ]

class ELTORITO_CATALOG_Boot (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",   UINT8),
    ("MediaType",   UINT8, 4),
    ("Reserved1",   UINT8, 4),
    ("LoadSegment", UINT16),
    ("SystemType",  UINT8),
    ("Reserved2",   UINT8),
    ("SectorCount", UINT16),
    ("Lba",         UINT32)
  ]

class ELTORITO_CATALOG_Section (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Indicator",       UINT8),
    ("PlatformId",      UINT8),
    ("SectionEntries",  UINT16),
    ("Id",              UINT8 * 28)
  ]

class ELTORITO_CATALOG (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unknown", ELTORITO_CATALOG_Unknown),
    ("Catalog", ELTORITO_CATALOG_Catalog),
    ("Boot",    ELTORITO_CATALOG_Boot),
    ("Section", ELTORITO_CATALOG_Section)
  ]

# 
# #pragma pack()
# 
# #endif
# 