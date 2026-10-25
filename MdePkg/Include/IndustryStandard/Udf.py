# /** @file
#   OSTA Universal Disk Format (UDF) definitions.
# 
#   Copyright (C) 2014-2017 Paulo Alcantara <pcacjr@zytor.com>
# 
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# 
# Udf.py
#
# EfiPy2.MdePkg.IndustryStandard.Udf
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __UDF_H__
# #define __UDF_H__
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #define UDF_BEA_IDENTIFIER   "BEA01"
# #define UDF_NSR2_IDENTIFIER  "NSR02"
# #define UDF_NSR3_IDENTIFIER  "NSR03"
# #define UDF_TEA_IDENTIFIER   "TEA01"
UDF_BEA_IDENTIFIER   = b"BEA01"
UDF_NSR2_IDENTIFIER  = b"NSR02"
UDF_NSR3_IDENTIFIER  = b"NSR03"
UDF_TEA_IDENTIFIER   = b"TEA01"

# 
# #define UDF_LOGICAL_SECTOR_SHIFT  11
# #define UDF_LOGICAL_SECTOR_SIZE   ((UINT64)(1ULL << UDF_LOGICAL_SECTOR_SHIFT))
# #define UDF_VRS_START_OFFSET      ((UINT64)(16ULL << UDF_LOGICAL_SECTOR_SHIFT))
UDF_LOGICAL_SECTOR_SHIFT  = 11
UDF_LOGICAL_SECTOR_SIZE   = (1  << UDF_LOGICAL_SECTOR_SHIFT)
UDF_VRS_START_OFFSET      = (16 << UDF_LOGICAL_SECTOR_SHIFT)

# 
# typedef enum {
#   UdfPrimaryVolumeDescriptor          = 1,
#   UdfAnchorVolumeDescriptorPointer    = 2,
#   UdfVolumeDescriptorPointer          = 3,
#   UdfImplemenationUseVolumeDescriptor = 4,
#   UdfPartitionDescriptor              = 5,
#   UdfLogicalVolumeDescriptor          = 6,
#   UdfUnallocatedSpaceDescriptor       = 7,
#   UdfTerminatingDescriptor            = 8,
#   UdfLogicalVolumeIntegrityDescriptor = 9,
#   UdfFileSetDescriptor                = 256,
#   UdfFileIdentifierDescriptor         = 257,
#   UdfAllocationExtentDescriptor       = 258,
#   UdfFileEntry                        = 261,
#   UdfExtendedFileEntry                = 266,
# } UDF_VOLUME_DESCRIPTOR_ID;
UdfPrimaryVolumeDescriptor          = 1
UdfAnchorVolumeDescriptorPointer    = 2
UdfVolumeDescriptorPointer          = 3
UdfImplemenationUseVolumeDescriptor = 4
UdfPartitionDescriptor              = 5
UdfLogicalVolumeDescriptor          = 6
UdfUnallocatedSpaceDescriptor       = 7
UdfTerminatingDescriptor            = 8
UdfLogicalVolumeIntegrityDescriptor = 9
UdfFileSetDescriptor                = 256
UdfFileIdentifierDescriptor         = 257
UdfAllocationExtentDescriptor       = 258
UdfFileEntry                        = 261
UdfExtendedFileEntry                = 266
UDF_VOLUME_DESCRIPTOR_ID            = ENUM

# 
# #pragma pack(1)
# 
# typedef struct {
#   UINT16    TagIdentifier;
#   UINT16    DescriptorVersion;
#   UINT8     TagChecksum;
#   UINT8     Reserved;
#   UINT16    TagSerialNumber;
#   UINT16    DescriptorCRC;
#   UINT16    DescriptorCRCLength;
#   UINT32    TagLocation;
# } UDF_DESCRIPTOR_TAG;
class UDF_DESCRIPTOR_TAG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TagIdentifier",       UINT16),
    ("DescriptorVersion",   UINT16),
    ("TagChecksum",         UINT8 ),
    ("Reserved",            UINT8 ),
    ("TagSerialNumber",     UINT16),
    ("DescriptorCRC",       UINT16),
    ("DescriptorCRCLength", UINT16),
    ("TagLocation",         UINT32)
  ]

# 
# typedef struct {
#   UINT32    ExtentLength;
#   UINT32    ExtentLocation;
# } UDF_EXTENT_AD;
class UDF_EXTENT_AD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtentLength",    UINT32),
    ("ExtentLocation",  UINT32)
  ]

# 
# typedef struct {
#   UINT8    CharacterSetType;
#   UINT8    CharacterSetInfo[63];
# } UDF_CHAR_SPEC;
class UDF_CHAR_SPEC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharacterSetType",    UINT8),
    ("CharacterSetInfo",    UINT8 * 63)
  ]

# 
# typedef struct {
#   UINT8    Flags;
#   UINT8    Identifier[23];
#   union {
#     //
#     // Domain Entity Identifier
#     //
#     struct {
#       UINT16    UdfRevision;
#       UINT8     DomainFlags;
#       UINT8     Reserved[5];
#     } Domain;
class UDF_ENTITY_ID_Suffix_Domain (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UdfRevision",    UINT16),
    ("DomainFlags",    UINT8),
    ("Reserved",       UINT8 * 5)
  ]

#     //
#     // UDF Entity Identifier
#     //
#     struct {
#       UINT16    UdfRevision;
#       UINT8     OSClass;
#       UINT8     OSIdentifier;
#       UINT8     Reserved[4];
#     } Entity;
#     //
#     // Implementation Entity Identifier
#     //
#     struct {
#       UINT8    OSClass;
#       UINT8    OSIdentifier;
#       UINT8    ImplementationUseArea[6];
#     } ImplementationEntity;
#     //
#     // Application Entity Identifier
#     //
#     struct {
#       UINT8    ApplicationUseArea[8];
#     } ApplicationEntity;
#     //
#     // Raw Identifier Suffix
#     //
#     struct {
#       UINT8    Data[8];
#     } Raw;
#   } Suffix;
# } UDF_ENTITY_ID;
class UDF_ENTITY_ID_Suffix_Entity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UdfRevision",     UINT16),
    ("OSClass",         UINT8 ),
    ("OSIdentifier",    UINT8 ),
    ("Reserved",        UINT8 * 4)
  ]

class UDF_ENTITY_ID_Suffix_ImplementationEntity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OSClass",                 UINT8),
    ("OSIdentifier",            UINT8),
    ("ImplementationUseArea",   UINT8 * 6)
  ]

class UDF_ENTITY_ID_Suffix_ApplicationEntity (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ApplicationUseArea",  UINT8 * 8)
  ]

class UDF_ENTITY_ID_Suffix_Raw (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data",    UINT8 * 8)
  ]

class UDF_ENTITY_ID_Suffix (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Entity",                  UDF_ENTITY_ID_Suffix_Entity),
    ("ImplementationEntity",    UDF_ENTITY_ID_Suffix_Entity),
    ("ApplicationEntity",       UDF_ENTITY_ID_Suffix_Entity),
    ("Raw",                     UDF_ENTITY_ID_Suffix_Raw)
  ]

class UDF_ENTITY_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Flags",       UINT8     ),
    ("Identifier",  UINT8 * 23),
    ("Suffix",      UDF_ENTITY_ID_Suffix)
  ]

# 
# typedef struct {
#   UINT32    LogicalBlockNumber;
#   UINT16    PartitionReferenceNumber;
# } UDF_LB_ADDR;
class UDF_LB_ADDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogicalBlockNumber",      UINT32),
    ("PartitionReferenceNumber",UINT16)
  ]

# 
# typedef struct {
#   UINT32         ExtentLength;
#   UDF_LB_ADDR    ExtentLocation;
#   UINT8          ImplementationUse[6];
# } UDF_LONG_ALLOCATION_DESCRIPTOR;
class UDF_LONG_ALLOCATION_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtentLength",        UINT32),
    ("ExtentLocation",      UDF_LB_ADDR),
    ("ImplementationUse",   UINT8 * 6)
  ]

# 
# typedef struct {
#   UDF_DESCRIPTOR_TAG    DescriptorTag;
#   UDF_EXTENT_AD         MainVolumeDescriptorSequenceExtent;
#   UDF_EXTENT_AD         ReserveVolumeDescriptorSequenceExtent;
#   UINT8                 Reserved[480];
# } UDF_ANCHOR_VOLUME_DESCRIPTOR_POINTER;
class UDF_ANCHOR_VOLUME_DESCRIPTOR_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorTag",                           UDF_DESCRIPTOR_TAG),
    ("MainVolumeDescriptorSequenceExtent",      UDF_EXTENT_AD     ),
    ("ReserveVolumeDescriptorSequenceExtent",   UDF_EXTENT_AD     ),
    ("Reserved",                                UINT8 * 480       )
  ]

# 
# typedef struct {
#   UDF_DESCRIPTOR_TAG                DescriptorTag;
#   UINT32                            VolumeDescriptorSequenceNumber;
#   UDF_CHAR_SPEC                     DescriptorCharacterSet;
#   UINT8                             LogicalVolumeIdentifier[128];
#   UINT32                            LogicalBlockSize;
#   UDF_ENTITY_ID                     DomainIdentifier;
#   UDF_LONG_ALLOCATION_DESCRIPTOR    LogicalVolumeContentsUse;
#   UINT32                            MapTableLength;
#   UINT32                            NumberOfPartitionMaps;
#   UDF_ENTITY_ID                     ImplementationIdentifier;
#   UINT8                             ImplementationUse[128];
#   UDF_EXTENT_AD                     IntegritySequenceExtent;
#   UINT8                             PartitionMaps[6];
# } UDF_LOGICAL_VOLUME_DESCRIPTOR;
class UDF_LOGICAL_VOLUME_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DescriptorTag",                   UDF_DESCRIPTOR_TAG            ),
    ("VolumeDescriptorSequenceNumber",  UINT32                        ),
    ("DescriptorCharacterSet",          UDF_CHAR_SPEC                 ),
    ("LogicalVolumeIdentifier",         UINT8 * 128                   ),
    ("LogicalBlockSize",                UINT32                        ),
    ("DomainIdentifier",                UDF_ENTITY_ID                 ),
    ("LogicalVolumeContentsUse",        UDF_LONG_ALLOCATION_DESCRIPTOR),
    ("MapTableLength",                  UINT32                        ),
    ("NumberOfPartitionMaps",           UINT32                        ),
    ("ImplementationIdentifier",        UDF_ENTITY_ID                 ),
    ("ImplementationUse",               UINT8 * 128                   ),
    ("IntegritySequenceExtent",         UDF_EXTENT_AD                 ),
    ("PartitionMaps",                   UINT8 * 6                     )
  ]

# 
# #pragma pack()
# 
# #endif
# 