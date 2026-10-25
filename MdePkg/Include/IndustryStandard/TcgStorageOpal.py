# /** @file
#   Opal Specification defined values and structures.
# 
#   (TCG Storage Architecture Core Specification, Version 2.01, Revision 1.00,
#   https://trustedcomputinggroup.org/tcg-storage-architecture-core-specification/
# 
#   Storage Work Group Storage Security Subsystem Class: Pyrite, Version 1.00 Final, Revision 1.00,
#   https://trustedcomputinggroup.org/tcg-storage-security-subsystem-class-pyrite/
# 
#   Storage Work Group Storage Security Subsystem Class: Opal, Version 2.01 Final, Revision 1.00,
#   https://trustedcomputinggroup.org/storage-work-group-storage-security-subsystem-class-opal/
# 
#   TCG Storage Security Subsystem Class: Opalite Version 1.00 Revision 1.00,
#   https://trustedcomputinggroup.org/tcg-storage-security-subsystem-class-opalite/)
# 
#   Check http://trustedcomputinggroup.org for latest specification updates.
# 
# Copyright (c) 2016 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# TcgStorageOpal.py
#
# EfiPy2.MdePkg.IndustryStandard.TcgStorageOpal
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _TCG_STORAGE_OPAL_H_
# #define _TCG_STORAGE_OPAL_H_
# 
# #include <IndustryStandard/TcgStorageCore.h>
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import TcgStorageCore

# 
# #define OPAL_UID_ADMIN_SP             TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x01)
# #define OPAL_UID_ADMIN_SP_C_PIN_MSID  TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x84, 0x02)
# #define OPAL_UID_ADMIN_SP_C_PIN_SID   TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x01)
# #define OPAL_UID_LOCKING_SP           TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x02)
OPAL_UID_ADMIN_SP             = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x01)
OPAL_UID_ADMIN_SP_C_PIN_MSID  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x84, 0x02)
OPAL_UID_ADMIN_SP_C_PIN_SID   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x0B, 0x00, 0x00, 0x00, 0x01)
OPAL_UID_LOCKING_SP           = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x02, 0x05, 0x00, 0x00, 0x00, 0x02)

# 
# // ADMIN_SP
# // Authorities
# #define OPAL_ADMIN_SP_ANYBODY_AUTHORITY  TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
# #define OPAL_ADMIN_SP_ADMINS_AUTHORITY   TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
# #define OPAL_ADMIN_SP_MAKERS_AUTHORITY   TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x03)
# #define OPAL_ADMIN_SP_SID_AUTHORITY      TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x06)
# #define OPAL_ADMIN_SP_ADMIN1_AUTHORITY   TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x02, 0x01)
# #define OPAL_ADMIN_SP_PSID_AUTHORITY     TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0xFF, 0x01)
OPAL_ADMIN_SP_ANYBODY_AUTHORITY  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
OPAL_ADMIN_SP_ADMINS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
OPAL_ADMIN_SP_MAKERS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x03)
OPAL_ADMIN_SP_SID_AUTHORITY      = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x06)
OPAL_ADMIN_SP_ADMIN1_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x02, 0x01)
OPAL_ADMIN_SP_PSID_AUTHORITY     = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0xFF, 0x01)

# 
# #define OPAL_ADMIN_SP_ACTIVATE_METHOD  TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x03)
# #define OPAL_ADMIN_SP_REVERT_METHOD    TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x02)
OPAL_ADMIN_SP_ACTIVATE_METHOD  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x03)
OPAL_ADMIN_SP_REVERT_METHOD    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x02, 0x02)

# 
# // ADMIN_SP
# // Data Removal mechanism
# #define OPAL_UID_ADMIN_SP_DATA_REMOVAL_MECHANISM  TCG_TO_UID(0x00, 0x00, 0x11, 0x01, 0x00, 0x00, 0x00, 0x01)
OPAL_UID_ADMIN_SP_DATA_REMOVAL_MECHANISM  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x11, 0x01, 0x00, 0x00, 0x00, 0x01)

# 
# // LOCKING SP
# // Authorities
# #define OPAL_LOCKING_SP_ANYBODY_AUTHORITY  TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
# #define OPAL_LOCKING_SP_ADMINS_AUTHORITY   TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
# #define OPAL_LOCKING_SP_ADMIN1_AUTHORITY   TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0x00, 0x01)
# #define OPAL_LOCKING_SP_USERS_AUTHORITY    TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x00)
# #define OPAL_LOCKING_SP_USER1_AUTHORITY    TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x01)
OPAL_LOCKING_SP_ANYBODY_AUTHORITY  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x01)
OPAL_LOCKING_SP_ADMINS_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x02)
OPAL_LOCKING_SP_ADMIN1_AUTHORITY   = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x01, 0x00, 0x01)
OPAL_LOCKING_SP_USERS_AUTHORITY    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x00)
OPAL_LOCKING_SP_USER1_AUTHORITY    = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x09, 0x00, 0x03, 0x00, 0x01)

# 
# #define OPAL_LOCKING_SP_REVERTSP_METHOD  TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x11)
OPAL_LOCKING_SP_REVERTSP_METHOD  = TcgStorageCore.TCG_TO_UID(0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x11)

# 
# // C_PIN Table Rows
# #define OPAL_LOCKING_SP_C_PIN_ADMIN1  TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x01 )
# #define OPAL_LOCKING_SP_C_PIN_USER1   TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x03, 0x00, 0x01 )
OPAL_LOCKING_SP_C_PIN_ADMIN1  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x01, 0x00, 0x01 )
OPAL_LOCKING_SP_C_PIN_USER1   = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x0B, 0x00, 0x03, 0x00, 0x01 )

# 
# // Locking Table
# #define OPAL_LOCKING_SP_LOCKING_GLOBALRANGE  TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x00, 0x00, 0x01 )
# #define OPAL_LOCKING_SP_LOCKING_RANGE1       TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x03, 0x00, 0x01 )
OPAL_LOCKING_SP_LOCKING_GLOBALRANGE  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x00, 0x00, 0x01 )
OPAL_LOCKING_SP_LOCKING_RANGE1       = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x02, 0x00, 0x03, 0x00, 0x01 )

# 
# // LOCKING SP ACE Table Preconfiguration
# #define OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_GET_ALL       TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xD0, 0x00 )
# #define OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_RDLOCKED  TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE0, 0x00 )
# #define OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_WRLOCKED  TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE8, 0x00 )
OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_GET_ALL       = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xD0, 0x00 )
OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_RDLOCKED  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE0, 0x00 )
OPAL_LOCKING_SP_ACE_LOCKING_GLOBALRANGE_SET_WRLOCKED  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xE8, 0x00 )

# 
# #define OPAL_LOCKING_SP_ACE_K_AES_256_GLOBALRANGE_GENKEY  TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB8, 0x00 )
# #define OPAL_LOCKING_SP_ACE_K_AES_128_GLOBALRANGE_GENKEY  TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB0, 0x00 )
OPAL_LOCKING_SP_ACE_K_AES_256_GLOBALRANGE_GENKEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB8, 0x00 )
OPAL_LOCKING_SP_ACE_K_AES_128_GLOBALRANGE_GENKEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x00, 0x08, 0x00, 0x03, 0xB0, 0x00 )

# 
# // LOCKING SP LockingInfo Table Preconfiguration
# #define OPAL_LOCKING_SP_LOCKING_INFO  TCG_TO_UID( 0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x01 )
OPAL_LOCKING_SP_LOCKING_INFO  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x01, 0x00, 0x00, 0x00, 0x01 )
# 
# #define OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTREQUIRED_COL     0x7
# #define OPAL_LOCKING_SP_LOCKINGINFO_LOGICALBLOCKSIZE_COL      0x8
# #define OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTGRANULARITY_COL  0x9
# #define OPAL_LOCKING_SP_LOCKINGINFO_LOWESTALIGNEDLBA_COL      0xA
OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTREQUIRED_COL     = 0x7
OPAL_LOCKING_SP_LOCKINGINFO_LOGICALBLOCKSIZE_COL      = 0x8
OPAL_LOCKING_SP_LOCKINGINFO_ALIGNMENTGRANULARITY_COL  = 0x9
OPAL_LOCKING_SP_LOCKINGINFO_LOWESTALIGNEDLBA_COL      = 0xA

# 
# // K_AES_256 Table Preconfiguration
# #define OPAL_LOCKING_SP_K_AES_256_GLOBALRANGE_KEY  TCG_TO_UID( 0x00, 0x00, 0x08, 0x06, 0x00, 0x00, 0x00, 0x01 )
OPAL_LOCKING_SP_K_AES_256_GLOBALRANGE_KEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x06, 0x00, 0x00, 0x00, 0x01 )

# 
# // K_AES_128 Table Preconfiguration
# #define OPAL_LOCKING_SP_K_AES_128_GLOBALRANGE_KEY  TCG_TO_UID( 0x00, 0x00, 0x08, 0x05, 0x00, 0x00, 0x00, 0x01 )
OPAL_LOCKING_SP_K_AES_128_GLOBALRANGE_KEY  = TcgStorageCore.TCG_TO_UID( 0x00, 0x00, 0x08, 0x05, 0x00, 0x00, 0x00, 0x01 )

# 
# // Minimum Properties that an Opal Compliant SD Shall support
# #define OPAL_MIN_MAX_COM_PACKET_SIZE          2048
# #define OPAL_MIN_MAX_REPONSE_COM_PACKET_SIZE  2048
# #define OPAL_MIN_MAX_PACKET_SIZE              2028
# #define OPAL_MIN_MAX_IND_TOKEN_SIZE           1992
# #define OPAL_MIN_MAX_PACKETS                  1
# #define OPAL_MIN_MAX_SUBPACKETS               1
# #define OPAL_MIN_MAX_METHODS                  1
# #define OPAL_MIN_MAX_SESSIONS                 1
# #define OPAL_MIN_MAX_AUTHENTICATIONS          2
# #define OPAL_MIN_MAX_TRANSACTION_LIMIT        1
OPAL_MIN_MAX_COM_PACKET_SIZE          = 2048
OPAL_MIN_MAX_REPONSE_COM_PACKET_SIZE  = 2048
OPAL_MIN_MAX_PACKET_SIZE              = 2028
OPAL_MIN_MAX_IND_TOKEN_SIZE           = 1992
OPAL_MIN_MAX_PACKETS                  = 1
OPAL_MIN_MAX_SUBPACKETS               = 1
OPAL_MIN_MAX_METHODS                  = 1
OPAL_MIN_MAX_SESSIONS                 = 1
OPAL_MIN_MAX_AUTHENTICATIONS          = 2
OPAL_MIN_MAX_TRANSACTION_LIMIT        = 1

# 
# #define OPAL_ADMIN_SP_PIN_COL               3
# #define OPAL_LOCKING_SP_C_PIN_TRYLIMIT_COL  5
# #define OPAL_RANDOM_METHOD_MAX_COUNT_SIZE   32
OPAL_ADMIN_SP_PIN_COL               = 3
OPAL_LOCKING_SP_C_PIN_TRYLIMIT_COL  = 5
OPAL_RANDOM_METHOD_MAX_COUNT_SIZE   = 32

# 
# // Data Removal Mechanism column.
# #define OPAL_ADMIN_SP_ACTIVE_DATA_REMOVAL_MECHANISM_COL  1
OPAL_ADMIN_SP_ACTIVE_DATA_REMOVAL_MECHANISM_COL  = 1

# 
# //
# // Supported Data Removal Mechanism.
# // Detail see Pyrite SSC v2 spec.
# //
# typedef enum {
#   OverwriteDataErase = 0,
#   BlockErase,
#   CryptoErase,
#   Unmap,
#   ResetWritePointers,
#   VendorSpecificErase,
#   ResearvedMechanism
# } SUPPORTED_DATA_REMOVAL_MECHANISM;
OverwriteDataErase  = 0
BlockErase          = 1
CryptoErase         = 2
Unmap               = 3
ResetWritePointers  = 4
VendorSpecificErase = 5
ResearvedMechanism  = 6
SUPPORTED_DATA_REMOVAL_MECHANISM = ENUM

# 
# #pragma pack(1)
# 
# typedef struct _OPAL_GEOMETRY_REPORTING_FEATURE {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT8                                   Reserved[8];
#   UINT32                                  LogicalBlockSizeBE;
#   UINT64                                  AlignmentGranularityBE;
#   UINT64                                  LowestAlignedLBABE;
# } OPAL_GEOMETRY_REPORTING_FEATURE;
class OPAL_GEOMETRY_REPORTING_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",                UINT8 * 8),
    ("LogicalBlockSizeBE",      UINT32),
    ("AlignmentGranularityBE",  UINT64),
    ("LowestAlignedLBABE",      UINT64)
  ]

# 
# typedef struct _OPAL_SINGLE_USER_MODE_FEATURE  {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT32                                  NumLockingObjectsSupportedBE;
#   UINT8                                   Any      : 1;
#   UINT8                                   All      : 1;
#   UINT8                                   Policy   : 1;
#   UINT8                                   Reserved : 5;
#   UINT8                                   Reserved2[7];
# } OPAL_SINGLE_USER_MODE_FEATURE;
class OPAL_SINGLE_USER_MODE_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("NumLockingObjectsSupportedBE",  UINT32),
    ("Any",         UINT8, 1),
    ("All",         UINT8, 1),
    ("Policy",      UINT8, 1),
    ("Reserved",    UINT8, 5),
    ("Reserved2",   UINT8 * 7)
  ]

# 
# typedef struct _OPAL_DATASTORE_TABLE_FEATURE {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  Reserved;
#   UINT16                                  MaxNumTablesBE;
#   UINT32                                  MaxTotalSizeBE;
#   UINT32                                  SizeAlignmentBE;
# } OPAL_DATASTORE_TABLE_FEATURE;
class OPAL_DATASTORE_TABLE_FEATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",        UINT16),
    ("MaxNumTablesBE",  UINT16),
    ("MaxTotalSizeBE",  UINT32),
    ("SizeAlignmentBE", UINT32)
  ]

# 
# typedef struct _OPAL_SSCV1_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  BaseComdIdBE;
#   UINT16                                  NumComIdsBE;
#   UINT8                                   RangeCrossing : 1;
#   UINT8                                   Reserved      : 7;
#   UINT8                                   Future[11];
# } OPAL_SSCV1_FEATURE_DESCRIPTOR;
class OPAL_SSCV1_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",          TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",    UINT16),
    ("NumComIdsBE",     UINT16),
    ("RangeCrossing",   UINT8, 1),
    ("Reserved",        UINT8, 7),
    ("Future",          UINT8 * 11),
  ]

# 
# typedef struct _OPAL_SSCV2_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  BaseComdIdBE;
#   UINT16                                  NumComIdsBE;
#   UINT8                                   Reserved;
#   UINT16                                  NumLockingSpAdminAuthoritiesSupportedBE;
#   UINT16                                  NumLockingSpUserAuthoritiesSupportedBE;
#   UINT8                                   InitialCPINSIDPIN;
#   UINT8                                   CPINSIDPINRevertBehavior;
#   UINT8                                   Future[5];
# } OPAL_SSCV2_FEATURE_DESCRIPTOR;
class OPAL_SSCV2_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8),
    ("NumLockingSpAdminAuthoritiesSupportedBE", UINT16),
    ("NumLockingSpUserAuthoritiesSupportedBE",  UINT16),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

# 
# typedef struct _OPAL_SSCLITE_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  BaseComdIdBE;
#   UINT16                                  NumComIdsBE;
#   UINT8                                   Reserved[5];
#   UINT8                                   InitialCPINSIDPIN;
#   UINT8                                   CPINSIDPINRevertBehavior;
#   UINT8                                   Future[5];
# } OPAL_SSCLITE_FEATURE_DESCRIPTOR;
class OPAL_SSCLITE_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

# 
# typedef struct _PYRITE_SSC_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  BaseComdIdBE;
#   UINT16                                  NumComIdsBE;
#   UINT8                                   Reserved[5];
#   UINT8                                   InitialCPINSIDPIN;
#   UINT8                                   CPINSIDPINRevertBehavior;
#   UINT8                                   Future[5];
# } PYRITE_SSC_FEATURE_DESCRIPTOR;
class PYRITE_SSC_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

# 
# typedef struct _PYRITE_SSCV2_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT16                                  BaseComdIdBE;
#   UINT16                                  NumComIdsBE;
#   UINT8                                   Reserved[5];
#   UINT8                                   InitialCPINSIDPIN;
#   UINT8                                   CPINSIDPINRevertBehavior;
#   UINT8                                   Future[5];
# } PYRITE_SSCV2_FEATURE_DESCRIPTOR;
class PYRITE_SSCV2_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                                  TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("BaseComdIdBE",                            UINT16),
    ("NumComIdsBE",                             UINT16),
    ("Reserved",                                UINT8 * 5),
    ("InitialCPINSIDPIN",                       UINT8),
    ("CPINSIDPINRevertBehavior",                UINT8),
    ("Future",                                  UINT8 * 5)
  ]

# 
# typedef struct _DATA_REMOVAL_FEATURE_DESCRIPTOR {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    Header;
#   UINT8                                   Reserved;
#   UINT8                                   OperationProcessing : 1;
#   UINT8                                   Reserved2           : 7;
#   UINT8                                   RemovalMechanism;
#   UINT8                                   FormatBit0          : 1; // Data Removal Time Format for Bit 0
#   UINT8                                   FormatBit1          : 1; // Data Removal Time Format for Bit 1
#   UINT8                                   FormatBit2          : 1; // Data Removal Time Format for Bit 2
#   UINT8                                   FormatBit3          : 1; // Data Removal Time Format for Bit 3
#   UINT8                                   FormatBit4          : 1; // Data Removal Time Format for Bit 4
#   UINT8                                   FormatBit5          : 1; // Data Removal Time Format for Bit 5
#   UINT8                                   Reserved3           : 2;
#   UINT16                                  TimeBit0;      // Data Removal Time for Supported Data Removal Mechanism Bit 0
#   UINT16                                  TimeBit1;      // Data Removal Time for Supported Data Removal Mechanism Bit 1
#   UINT16                                  TimeBit2;      // Data Removal Time for Supported Data Removal Mechanism Bit 2
#   UINT16                                  TimeBit3;      // Data Removal Time for Supported Data Removal Mechanism Bit 3
#   UINT16                                  TimeBit4;      // Data Removal Time for Supported Data Removal Mechanism Bit 4
#   UINT16                                  TimeBit5;      // Data Removal Time for Supported Data Removal Mechanism Bit 5
#   UINT8                                   Future[16];
# } DATA_REMOVAL_FEATURE_DESCRIPTOR;
class DATA_REMOVAL_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Reserved",            UINT8),
    ("OperationProcessing", UINT8, 1),
    ("Reserved2",           UINT8, 7),
    ("RemovalMechanism",    UINT8),
    ("FormatBit0",          UINT8, 1),
    ("FormatBit1",          UINT8, 1),
    ("FormatBit2",          UINT8, 1),
    ("FormatBit3",          UINT8, 1),
    ("FormatBit4",          UINT8, 1),
    ("FormatBit5",          UINT8, 1),
    ("Reserved3",           UINT8, 2),
    ("TimeBit0",            UINT16),
    ("TimeBit1",            UINT16),
    ("TimeBit2",            UINT16),
    ("TimeBit3",            UINT16),
    ("TimeBit4",            UINT16),
    ("TimeBit5",            UINT16),
    ("Future",              UINT8 * 16)
  ]

# 
# typedef union {
#   TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER    CommonHeader;
#   TCG_TPER_FEATURE_DESCRIPTOR             Tper;
#   TCG_LOCKING_FEATURE_DESCRIPTOR          Locking;
#   OPAL_GEOMETRY_REPORTING_FEATURE         Geometry;
#   OPAL_SINGLE_USER_MODE_FEATURE           SingleUser;
#   OPAL_DATASTORE_TABLE_FEATURE            DataStore;
#   OPAL_SSCV1_FEATURE_DESCRIPTOR           OpalSscV1;
#   OPAL_SSCV2_FEATURE_DESCRIPTOR           OpalSscV2;
#   OPAL_SSCLITE_FEATURE_DESCRIPTOR         OpalSscLite;
#   PYRITE_SSC_FEATURE_DESCRIPTOR           PyriteSsc;
#   PYRITE_SSCV2_FEATURE_DESCRIPTOR         PyriteSscV2;
#   TCG_BLOCK_SID_FEATURE_DESCRIPTOR        BlockSid;
#   DATA_REMOVAL_FEATURE_DESCRIPTOR         DataRemoval;
# } OPAL_LEVEL0_FEATURE_DESCRIPTOR;
class OPAL_LEVEL0_FEATURE_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("CommonHeader",    TcgStorageCore.TCG_LEVEL0_FEATURE_DESCRIPTOR_HEADER),
    ("Tper",            TcgStorageCore.TCG_TPER_FEATURE_DESCRIPTOR),
    ("Locking",         TcgStorageCore.TCG_LOCKING_FEATURE_DESCRIPTOR),
    ("Geometry",        OPAL_GEOMETRY_REPORTING_FEATURE),
    ("SingleUser",      OPAL_SINGLE_USER_MODE_FEATURE),
    ("DataStore",       OPAL_DATASTORE_TABLE_FEATURE),
    ("OpalSscV1",       OPAL_SSCV1_FEATURE_DESCRIPTOR),
    ("OpalSscV2",       OPAL_SSCV2_FEATURE_DESCRIPTOR),
    ("OpalSscLite",     OPAL_SSCLITE_FEATURE_DESCRIPTOR),
    ("PyriteSsc",       PYRITE_SSC_FEATURE_DESCRIPTOR),
    ("PyriteSscV2",     PYRITE_SSCV2_FEATURE_DESCRIPTOR),
    ("BlockSid",        TcgStorageCore.TCG_BLOCK_SID_FEATURE_DESCRIPTOR),
    ("DataRemoval",     DATA_REMOVAL_FEATURE_DESCRIPTOR)
  ]

# 
# #pragma pack()
# 
# #endif // _OPAL_H_
# 