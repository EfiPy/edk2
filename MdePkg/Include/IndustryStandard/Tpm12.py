# /** @file
#   TPM Specification data structures (TCG TPM Specification Version 1.2 Revision 103)
#   See http://trustedcomputinggroup.org for latest specification updates
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# Tpm12.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm12
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _TPM12_H_
# #define _TPM12_H_
# 
from EfiPy2.MdePkg.IndustryStandard import *

class TPM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  pass

# /// The start of TPM return codes
# ///
# #define TPM_BASE  0
TPM_BASE                    = 0

# 
# //
# // All structures MUST be packed on a byte boundary.
# //
# 
# #pragma pack (1)
# 
# //
# // Part 2, section 2.2.3: Helper redefinitions
# //
# ///
# /// Indicates the conditions where it is required that authorization be presented
# ///
# typedef UINT8 TPM_AUTH_DATA_USAGE;
TPM_AUTH_DATA_USAGE                 = UINT8
# ///
# /// The information as to what the payload is in an encrypted structure
# ///
# typedef UINT8 TPM_PAYLOAD_TYPE;
TPM_PAYLOAD_TYPE                    = UINT8
# ///
# /// The version info breakdown
# ///
# typedef UINT8 TPM_VERSION_BYTE;
TPM_VERSION_BYTE                    = UINT8
# ///
# /// The state of the dictionary attack mitigation logic
# ///
# typedef UINT8 TPM_DA_STATE;
TPM_DA_STATE                        = UINT8
# ///
# /// The request or response authorization type
# ///
# typedef UINT16 TPM_TAG;
TPM_TAG                             = UINT16
# ///
# /// The protocol in use
# ///
# typedef UINT16 TPM_PROTOCOL_ID;
TPM_PROTOCOL_ID                     = UINT16
# ///
# /// Indicates the start state
# ///
# typedef UINT16 TPM_STARTUP_TYPE;
TPM_STARTUP_TYPE                    = UINT16
# ///
# /// The definition of the encryption scheme
# ///
# typedef UINT16 TPM_ENC_SCHEME;
TPM_ENC_SCHEME                      = UINT16
# ///
# /// The definition of the signature scheme
# ///
# typedef UINT16 TPM_SIG_SCHEME;
TPM_SIG_SCHEME                      = UINT16
# ///
# /// The definition of the migration scheme
# ///
# typedef UINT16 TPM_MIGRATE_SCHEME;
TPM_MIGRATE_SCHEME                  = UINT16
# ///
# /// Sets the state of the physical presence mechanism
# ///
# typedef UINT16 TPM_PHYSICAL_PRESENCE;
TPM_PHYSICAL_PRESENCE               = UINT16
# ///
# /// Indicates the types of entity that are supported by the TPM
# ///
# typedef UINT16 TPM_ENTITY_TYPE;
TPM_ENTITY_TYPE                     = UINT16
# ///
# /// Indicates the permitted usage of the key
# ///
# typedef UINT16 TPM_KEY_USAGE;
TPM_KEY_USAGE                       = UINT16
# ///
# /// The type of asymmetric encrypted structure in use by the endorsement key
# ///
# typedef UINT16 TPM_EK_TYPE;
TPM_EK_TYPE                         = UINT16
# ///
# /// The tag for the structure
# ///
# typedef UINT16 TPM_STRUCTURE_TAG;
TPM_STRUCTURE_TAG                   = UINT16
# ///
# /// The platform specific spec to which the information relates to
# ///
# typedef UINT16 TPM_PLATFORM_SPECIFIC;
TPM_PLATFORM_SPECIFIC               = UINT16
# ///
# /// The command ordinal
# ///
# typedef UINT32 TPM_COMMAND_CODE;
TPM_COMMAND_CODE                    = UINT32
# ///
# /// Identifies a TPM capability area
# ///
# typedef UINT32 TPM_CAPABILITY_AREA;
TPM_CAPABILITY_AREA                 = UINT32
# ///
# /// Indicates information regarding a key
# ///
# typedef UINT32 TPM_KEY_FLAGS;
TPM_KEY_FLAGS                       = UINT32
# ///
# /// Indicates the type of algorithm
# ///
# typedef UINT32 TPM_ALGORITHM_ID;
TPM_ALGORITHM_ID                    = UINT32
# ///
# /// The locality modifier
# ///
# typedef UINT32 TPM_MODIFIER_INDICATOR;
TPM_MODIFIER_INDICATOR              = UINT32
# ///
# /// The actual number of a counter
# ///
# typedef UINT32 TPM_ACTUAL_COUNT;
TPM_ACTUAL_COUNT                    = UINT32
# ///
# /// Attributes that define what options are in use for a transport session
# ///
# typedef UINT32 TPM_TRANSPORT_ATTRIBUTES;
TPM_TRANSPORT_ATTRIBUTES            = UINT32
# ///
# /// Handle to an authorization session
# ///
# typedef UINT32 TPM_AUTHHANDLE;
TPM_AUTHHANDLE                      = UINT32
# ///
# /// Index to a DIR register
# ///
# typedef UINT32 TPM_DIRINDEX;
TPM_DIRINDEX                        = UINT32
# ///
# /// The area where a key is held assigned by the TPM
# ///
# typedef UINT32 TPM_KEY_HANDLE;
TPM_KEY_HANDLE                      = UINT32
# ///
# /// Index to a PCR register
# ///
# typedef UINT32 TPM_PCRINDEX;
TPM_PCRINDEX                        = UINT32
# ///
# /// The return code from a function
# ///
# typedef UINT32 TPM_RESULT;
TPM_RESULT                          = UINT32
# ///
# /// The types of resources that a TPM may have using internal resources
# ///
# typedef UINT32 TPM_RESOURCE_TYPE;
TPM_RESOURCE_TYPE                   = UINT32
# ///
# /// Allows for controlling of the key when loaded and how to handle TPM_Startup issues
# ///
# typedef UINT32 TPM_KEY_CONTROL;
TPM_KEY_CONTROL                     = UINT32
# ///
# /// The index into the NV storage area
# ///
# typedef UINT32 TPM_NV_INDEX;
TPM_NV_INDEX                        = UINT32
# ///
# /// The family ID. Family IDs are automatically assigned a sequence number by the TPM.
# /// A trusted process can set the FamilyID value in an individual row to NULL, which
# /// invalidates that row. The family ID resets to NULL on each change of TPM Owner.
# ///
# typedef UINT32 TPM_FAMILY_ID;
TPM_FAMILY_ID                       = UINT32
# ///
# /// IA value used as a label for the most recent verification of this family. Set to zero when not in use.
# ///
# typedef UINT32 TPM_FAMILY_VERIFICATION;
TPM_FAMILY_VERIFICATION             = UINT32
# ///
# /// How the TPM handles var
# ///
# typedef UINT32 TPM_STARTUP_EFFECTS;
TPM_STARTUP_EFFECTS                 = UINT32
# ///
# /// The mode of a symmetric encryption
# ///
# typedef UINT32 TPM_SYM_MODE;
TPM_SYM_MODE                        = UINT32
# ///
# /// The family flags
# ///
# typedef UINT32 TPM_FAMILY_FLAGS;
TPM_FAMILY_FLAGS                    = UINT32
# ///
# /// The index value for the delegate NV table
# ///
# typedef UINT32 TPM_DELEGATE_INDEX;
TPM_DELEGATE_INDEX                  = UINT32
# ///
# /// The restrictions placed on delegation of CMK commands
# ///
# typedef UINT32 TPM_CMK_DELEGATE;
TPM_CMK_DELEGATE                    = UINT32
# ///
# /// The ID value of a monotonic counter
# ///
# typedef UINT32 TPM_COUNT_ID;
TPM_COUNT_ID                        = UINT32
# ///
# /// A command to execute
# ///
# typedef UINT32 TPM_REDIT_COMMAND;
TPM_REDIT_COMMAND                   = UINT32
# ///
# /// A transport session handle
# ///
# typedef UINT32 TPM_TRANSHANDLE;
TPM_TRANSHANDLE                     = UINT32
# ///
# /// A generic handle could be key, transport etc
# ///
# typedef UINT32 TPM_HANDLE;
TPM_HANDLE                          = UINT32
# ///
# /// What operation is happening
# ///
# typedef UINT32 TPM_FAMILY_OPERATION;
TPM_FAMILY_OPERATION                = UINT32

# 
# //
# // Part 2, section 2.2.4: Vendor specific
# // The following defines allow for the quick specification of a
# // vendor specific item.
# //
# #define TPM_Vendor_Specific32  ((UINT32) 0x00000400)
# #define TPM_Vendor_Specific8   ((UINT8) 0x80)
TPM_Vendor_Specific32       = 0x00000400
TPM_Vendor_Specific8        = 0x80

# 
# //
# // Part 2, section 3.1: TPM_STRUCTURE_TAG
# //
# #define TPM_TAG_CONTEXTBLOB          ((TPM_STRUCTURE_TAG) 0x0001)
# #define TPM_TAG_CONTEXT_SENSITIVE    ((TPM_STRUCTURE_TAG) 0x0002)
# #define TPM_TAG_CONTEXTPOINTER       ((TPM_STRUCTURE_TAG) 0x0003)
# #define TPM_TAG_CONTEXTLIST          ((TPM_STRUCTURE_TAG) 0x0004)
# #define TPM_TAG_SIGNINFO             ((TPM_STRUCTURE_TAG) 0x0005)
# #define TPM_TAG_PCR_INFO_LONG        ((TPM_STRUCTURE_TAG) 0x0006)
# #define TPM_TAG_PERSISTENT_FLAGS     ((TPM_STRUCTURE_TAG) 0x0007)
# #define TPM_TAG_VOLATILE_FLAGS       ((TPM_STRUCTURE_TAG) 0x0008)
# #define TPM_TAG_PERSISTENT_DATA      ((TPM_STRUCTURE_TAG) 0x0009)
# #define TPM_TAG_VOLATILE_DATA        ((TPM_STRUCTURE_TAG) 0x000A)
# #define TPM_TAG_SV_DATA              ((TPM_STRUCTURE_TAG) 0x000B)
# #define TPM_TAG_EK_BLOB              ((TPM_STRUCTURE_TAG) 0x000C)
# #define TPM_TAG_EK_BLOB_AUTH         ((TPM_STRUCTURE_TAG) 0x000D)
# #define TPM_TAG_COUNTER_VALUE        ((TPM_STRUCTURE_TAG) 0x000E)
# #define TPM_TAG_TRANSPORT_INTERNAL   ((TPM_STRUCTURE_TAG) 0x000F)
# #define TPM_TAG_TRANSPORT_LOG_IN     ((TPM_STRUCTURE_TAG) 0x0010)
# #define TPM_TAG_TRANSPORT_LOG_OUT    ((TPM_STRUCTURE_TAG) 0x0011)
# #define TPM_TAG_AUDIT_EVENT_IN       ((TPM_STRUCTURE_TAG) 0x0012)
# #define TPM_TAG_AUDIT_EVENT_OUT      ((TPM_STRUCTURE_TAG) 0x0013)
# #define TPM_TAG_CURRENT_TICKS        ((TPM_STRUCTURE_TAG) 0x0014)
# #define TPM_TAG_KEY                  ((TPM_STRUCTURE_TAG) 0x0015)
# #define TPM_TAG_STORED_DATA12        ((TPM_STRUCTURE_TAG) 0x0016)
# #define TPM_TAG_NV_ATTRIBUTES        ((TPM_STRUCTURE_TAG) 0x0017)
# #define TPM_TAG_NV_DATA_PUBLIC       ((TPM_STRUCTURE_TAG) 0x0018)
# #define TPM_TAG_NV_DATA_SENSITIVE    ((TPM_STRUCTURE_TAG) 0x0019)
# #define TPM_TAG_DELEGATIONS          ((TPM_STRUCTURE_TAG) 0x001A)
# #define TPM_TAG_DELEGATE_PUBLIC      ((TPM_STRUCTURE_TAG) 0x001B)
# #define TPM_TAG_DELEGATE_TABLE_ROW   ((TPM_STRUCTURE_TAG) 0x001C)
# #define TPM_TAG_TRANSPORT_AUTH       ((TPM_STRUCTURE_TAG) 0x001D)
# #define TPM_TAG_TRANSPORT_PUBLIC     ((TPM_STRUCTURE_TAG) 0x001E)
# #define TPM_TAG_PERMANENT_FLAGS      ((TPM_STRUCTURE_TAG) 0x001F)
# #define TPM_TAG_STCLEAR_FLAGS        ((TPM_STRUCTURE_TAG) 0x0020)
# #define TPM_TAG_STANY_FLAGS          ((TPM_STRUCTURE_TAG) 0x0021)
# #define TPM_TAG_PERMANENT_DATA       ((TPM_STRUCTURE_TAG) 0x0022)
# #define TPM_TAG_STCLEAR_DATA         ((TPM_STRUCTURE_TAG) 0x0023)
# #define TPM_TAG_STANY_DATA           ((TPM_STRUCTURE_TAG) 0x0024)
# #define TPM_TAG_FAMILY_TABLE_ENTRY   ((TPM_STRUCTURE_TAG) 0x0025)
# #define TPM_TAG_DELEGATE_SENSITIVE   ((TPM_STRUCTURE_TAG) 0x0026)
# #define TPM_TAG_DELG_KEY_BLOB        ((TPM_STRUCTURE_TAG) 0x0027)
# #define TPM_TAG_KEY12                ((TPM_STRUCTURE_TAG) 0x0028)
# #define TPM_TAG_CERTIFY_INFO2        ((TPM_STRUCTURE_TAG) 0x0029)
# #define TPM_TAG_DELEGATE_OWNER_BLOB  ((TPM_STRUCTURE_TAG) 0x002A)
# #define TPM_TAG_EK_BLOB_ACTIVATE     ((TPM_STRUCTURE_TAG) 0x002B)
# #define TPM_TAG_DAA_BLOB             ((TPM_STRUCTURE_TAG) 0x002C)
# #define TPM_TAG_DAA_CONTEXT          ((TPM_STRUCTURE_TAG) 0x002D)
# #define TPM_TAG_DAA_ENFORCE          ((TPM_STRUCTURE_TAG) 0x002E)
# #define TPM_TAG_DAA_ISSUER           ((TPM_STRUCTURE_TAG) 0x002F)
# #define TPM_TAG_CAP_VERSION_INFO     ((TPM_STRUCTURE_TAG) 0x0030)
# #define TPM_TAG_DAA_SENSITIVE        ((TPM_STRUCTURE_TAG) 0x0031)
# #define TPM_TAG_DAA_TPM              ((TPM_STRUCTURE_TAG) 0x0032)
# #define TPM_TAG_CMK_MIGAUTH          ((TPM_STRUCTURE_TAG) 0x0033)
# #define TPM_TAG_CMK_SIGTICKET        ((TPM_STRUCTURE_TAG) 0x0034)
# #define TPM_TAG_CMK_MA_APPROVAL      ((TPM_STRUCTURE_TAG) 0x0035)
# #define TPM_TAG_QUOTE_INFO2          ((TPM_STRUCTURE_TAG) 0x0036)
# #define TPM_TAG_DA_INFO              ((TPM_STRUCTURE_TAG) 0x0037)
# #define TPM_TAG_DA_LIMITED           ((TPM_STRUCTURE_TAG) 0x0038)
# #define TPM_TAG_DA_ACTION_TYPE       ((TPM_STRUCTURE_TAG) 0x0039)
TPM_TAG_CONTEXTBLOB         = 0x0001
TPM_TAG_CONTEXT_SENSITIVE   = 0x0002
TPM_TAG_CONTEXTPOINTER      = 0x0003
TPM_TAG_CONTEXTLIST         = 0x0004
TPM_TAG_SIGNINFO            = 0x0005
TPM_TAG_PCR_INFO_LONG       = 0x0006
TPM_TAG_PERSISTENT_FLAGS    = 0x0007
TPM_TAG_VOLATILE_FLAGS      = 0x0008
TPM_TAG_PERSISTENT_DATA     = 0x0009
TPM_TAG_VOLATILE_DATA       = 0x000A
TPM_TAG_SV_DATA             = 0x000B
TPM_TAG_EK_BLOB             = 0x000C
TPM_TAG_EK_BLOB_AUTH        = 0x000D
TPM_TAG_COUNTER_VALUE       = 0x000E
TPM_TAG_TRANSPORT_INTERNAL  = 0x000F
TPM_TAG_TRANSPORT_LOG_IN    = 0x0010
TPM_TAG_TRANSPORT_LOG_OUT   = 0x0011
TPM_TAG_AUDIT_EVENT_IN      = 0x0012
TPM_TAG_AUDIT_EVENT_OUT     = 0x0013
TPM_TAG_CURRENT_TICKS       = 0x0014
TPM_TAG_KEY                 = 0x0015
TPM_TAG_STORED_DATA12       = 0x0016
TPM_TAG_NV_ATTRIBUTES       = 0x0017
TPM_TAG_NV_DATA_PUBLIC      = 0x0018
TPM_TAG_NV_DATA_SENSITIVE   = 0x0019
TPM_TAG_DELEGATIONS         = 0x001A
TPM_TAG_DELEGATE_PUBLIC     = 0x001B
TPM_TAG_DELEGATE_TABLE_ROW  = 0x001C
TPM_TAG_TRANSPORT_AUTH      = 0x001D
TPM_TAG_TRANSPORT_PUBLIC    = 0x001E
TPM_TAG_PERMANENT_FLAGS     = 0x001F
TPM_TAG_STCLEAR_FLAGS       = 0x0020
TPM_TAG_STANY_FLAGS         = 0x0021
TPM_TAG_PERMANENT_DATA      = 0x0022
TPM_TAG_STCLEAR_DATA        = 0x0023
TPM_TAG_STANY_DATA          = 0x0024
TPM_TAG_FAMILY_TABLE_ENTRY  = 0x0025
TPM_TAG_DELEGATE_SENSITIVE  = 0x0026
TPM_TAG_DELG_KEY_BLOB       = 0x0027
TPM_TAG_KEY12               = 0x0028
TPM_TAG_CERTIFY_INFO2       = 0x0029
TPM_TAG_DELEGATE_OWNER_BLOB = 0x002A
TPM_TAG_EK_BLOB_ACTIVATE    = 0x002B
TPM_TAG_DAA_BLOB            = 0x002C
TPM_TAG_DAA_CONTEXT         = 0x002D
TPM_TAG_DAA_ENFORCE         = 0x002E
TPM_TAG_DAA_ISSUER          = 0x002F
TPM_TAG_CAP_VERSION_INFO    = 0x0030
TPM_TAG_DAA_SENSITIVE       = 0x0031
TPM_TAG_DAA_TPM             = 0x0032
TPM_TAG_CMK_MIGAUTH         = 0x0033
TPM_TAG_CMK_SIGTICKET       = 0x0034
TPM_TAG_CMK_MA_APPROVAL     = 0x0035
TPM_TAG_QUOTE_INFO2         = 0x0036
TPM_TAG_DA_INFO             = 0x0037
TPM_TAG_DA_LIMITED          = 0x0038
TPM_TAG_DA_ACTION_TYPE      = 0x0039

# 
# //
# // Part 2, section 4: TPM Types
# //
# 
# //
# // Part 2, section 4.1: TPM_RESOURCE_TYPE
# //
# #define TPM_RT_KEY       ((TPM_RESOURCE_TYPE) 0x00000001)            ///< The handle is a key handle and is the result of a LoadKey type operation
# #define TPM_RT_AUTH      ((TPM_RESOURCE_TYPE) 0x00000002)            ///< The handle is an authorization handle. Auth handles come from TPM_OIAP, TPM_OSAP and TPM_DSAP
# #define TPM_RT_HASH      ((TPM_RESOURCE_TYPE) 0x00000003)            ///< Reserved for hashes
# #define TPM_RT_TRANS     ((TPM_RESOURCE_TYPE) 0x00000004)            ///< The handle is for a transport session. Transport handles come from TPM_EstablishTransport
# #define TPM_RT_CONTEXT   ((TPM_RESOURCE_TYPE) 0x00000005)            ///< Resource wrapped and held outside the TPM using the context save/restore commands
# #define TPM_RT_COUNTER   ((TPM_RESOURCE_TYPE) 0x00000006)            ///< Reserved for counters
# #define TPM_RT_DELEGATE  ((TPM_RESOURCE_TYPE) 0x00000007)            ///< The handle is for a delegate row. These are the internal rows held in NV storage by the TPM
# #define TPM_RT_DAA_TPM   ((TPM_RESOURCE_TYPE) 0x00000008)            ///< The value is a DAA TPM specific blob
# #define TPM_RT_DAA_V0    ((TPM_RESOURCE_TYPE) 0x00000009)            ///< The value is a DAA V0 parameter
# #define TPM_RT_DAA_V1    ((TPM_RESOURCE_TYPE) 0x0000000A)            ///< The value is a DAA V1 parameter
TPM_RT_KEY                  = 0x00000001
TPM_RT_AUTH                 = 0x00000002
TPM_RT_HASH                 = 0x00000003
TPM_RT_TRANS                = 0x00000004
TPM_RT_CONTEXT              = 0x00000005
TPM_RT_COUNTER              = 0x00000006
TPM_RT_DELEGATE             = 0x00000007
TPM_RT_DAA_TPM              = 0x00000008
TPM_RT_DAA_V0               = 0x00000009
TPM_RT_DAA_V1               = 0x0000000A

# 
# //
# // Part 2, section 4.2: TPM_PAYLOAD_TYPE
# //
# #define TPM_PT_ASYM                ((TPM_PAYLOAD_TYPE) 0x01)  ///< The entity is an asymmetric key
# #define TPM_PT_BIND                ((TPM_PAYLOAD_TYPE) 0x02)  ///< The entity is bound data
# #define TPM_PT_MIGRATE             ((TPM_PAYLOAD_TYPE) 0x03)  ///< The entity is a migration blob
# #define TPM_PT_MAINT               ((TPM_PAYLOAD_TYPE) 0x04)  ///< The entity is a maintenance blob
# #define TPM_PT_SEAL                ((TPM_PAYLOAD_TYPE) 0x05)  ///< The entity is sealed data
# #define TPM_PT_MIGRATE_RESTRICTED  ((TPM_PAYLOAD_TYPE) 0x06)  ///< The entity is a restricted-migration asymmetric key
# #define TPM_PT_MIGRATE_EXTERNAL    ((TPM_PAYLOAD_TYPE) 0x07)  ///< The entity is a external migratable key
# #define TPM_PT_CMK_MIGRATE         ((TPM_PAYLOAD_TYPE) 0x08)  ///< The entity is a CMK migratable blob
# #define TPM_PT_VENDOR_SPECIFIC     ((TPM_PAYLOAD_TYPE) 0x80)  ///< 0x80 - 0xFF Vendor specific payloads
TPM_PT_ASYM                 = 0x01
TPM_PT_BIND                 = 0x02
TPM_PT_MIGRATE              = 0x03
TPM_PT_MAINT                = 0x04
TPM_PT_SEAL                 = 0x05
TPM_PT_MIGRATE_RESTRICTED   = 0x06
TPM_PT_MIGRATE_EXTERNAL     = 0x07
TPM_PT_CMK_MIGRATE          = 0x08
TPM_PT_VENDOR_SPECIFIC      = 0x80

# 
# //
# // Part 2, section 4.3: TPM_ENTITY_TYPE
# //
# #define TPM_ET_KEYHANDLE        ((UINT16) 0x0001)     ///< The entity is a keyHandle or key
# #define TPM_ET_OWNER            ((UINT16) 0x0002)     ///< The entity is the TPM Owner
# #define TPM_ET_DATA             ((UINT16) 0x0003)     ///< The entity is some data
# #define TPM_ET_SRK              ((UINT16) 0x0004)     ///< The entity is the SRK
# #define TPM_ET_KEY              ((UINT16) 0x0005)     ///< The entity is a key or keyHandle
# #define TPM_ET_REVOKE           ((UINT16) 0x0006)     ///< The entity is the RevokeTrust value
# #define TPM_ET_DEL_OWNER_BLOB   ((UINT16) 0x0007)     ///< The entity is a delegate owner blob
# #define TPM_ET_DEL_ROW          ((UINT16) 0x0008)     ///< The entity is a delegate row
# #define TPM_ET_DEL_KEY_BLOB     ((UINT16) 0x0009)     ///< The entity is a delegate key blob
# #define TPM_ET_COUNTER          ((UINT16) 0x000A)     ///< The entity is a counter
# #define TPM_ET_NV               ((UINT16) 0x000B)     ///< The entity is a NV index
# #define TPM_ET_OPERATOR         ((UINT16) 0x000C)     ///< The entity is the operator
# #define TPM_ET_RESERVED_HANDLE  ((UINT16) 0x0040)     ///< Reserved. This value avoids collisions with the handle MSB setting.
TPM_ET_KEYHANDLE            = 0x0001
TPM_ET_OWNER                = 0x0002
TPM_ET_DATA                 = 0x0003
TPM_ET_SRK                  = 0x0004
TPM_ET_KEY                  = 0x0005
TPM_ET_REVOKE               = 0x0006
TPM_ET_DEL_OWNER_BLOB       = 0x0007
TPM_ET_DEL_ROW              = 0x0008
TPM_ET_DEL_KEY_BLOB         = 0x0009
TPM_ET_COUNTER              = 0x000A
TPM_ET_NV                   = 0x000B
TPM_ET_OPERATOR             = 0x000C
TPM_ET_RESERVED_HANDLE      = 0x0040

# //
# // TPM_ENTITY_TYPE MSB Values: The MSB is used to indicate the ADIP encryption sheme when applicable
# //
# #define TPM_ET_XOR     ((UINT16) 0x0000)              ///< ADIP encryption scheme: XOR
# #define TPM_ET_AES128  ((UINT16) 0x0006)              ///< ADIP encryption scheme: AES 128 bits
TPM_ET_XOR                  = 0x0000
TPM_ET_AES128               = 0x0006

# 
# //
# // Part 2, section 4.4.1: Reserved Key Handles
# //
# #define TPM_KH_SRK        ((TPM_KEY_HANDLE) 0x40000000)           ///< The handle points to the SRK
# #define TPM_KH_OWNER      ((TPM_KEY_HANDLE) 0x40000001)           ///< The handle points to the TPM Owner
# #define TPM_KH_REVOKE     ((TPM_KEY_HANDLE) 0x40000002)           ///< The handle points to the RevokeTrust value
# #define TPM_KH_TRANSPORT  ((TPM_KEY_HANDLE) 0x40000003)           ///< The handle points to the EstablishTransport static authorization
# #define TPM_KH_OPERATOR   ((TPM_KEY_HANDLE) 0x40000004)           ///< The handle points to the Operator auth
# #define TPM_KH_ADMIN      ((TPM_KEY_HANDLE) 0x40000005)           ///< The handle points to the delegation administration auth
# #define TPM_KH_EK         ((TPM_KEY_HANDLE) 0x40000006)           ///< The handle points to the PUBEK, only usable with TPM_OwnerReadInternalPub
TPM_KH_SRK                  = 0x40000000
TPM_KH_OWNER                = 0x40000001
TPM_KH_REVOKE               = 0x40000002
TPM_KH_TRANSPORT            = 0x40000003
TPM_KH_OPERATOR             = 0x40000004
TPM_KH_ADMIN                = 0x40000005
TPM_KH_EK                   = 0x40000006

# 
# //
# // Part 2, section 4.5: TPM_STARTUP_TYPE
# //
# #define TPM_ST_CLEAR        ((TPM_STARTUP_TYPE) 0x0001)         ///< The TPM is starting up from a clean state
# #define TPM_ST_STATE        ((TPM_STARTUP_TYPE) 0x0002)         ///< The TPM is starting up from a saved state
# #define TPM_ST_DEACTIVATED  ((TPM_STARTUP_TYPE) 0x0003)         ///< The TPM is to startup and set the deactivated flag to TRUE
TPM_ST_CLEAR                = 0x0001
TPM_ST_STATE                = 0x0002
TPM_ST_DEACTIVATED          = 0x0003

# 
# //
# // Part 2, section 4.6: TPM_STATUP_EFFECTS
# // The table makeup is still an open issue.
# //
# 
# //
# // Part 2, section 4.7: TPM_PROTOCOL_ID
# //
# #define TPM_PID_OIAP       ((TPM_PROTOCOL_ID) 0x0001)          ///< The OIAP protocol.
# #define TPM_PID_OSAP       ((TPM_PROTOCOL_ID) 0x0002)          ///< The OSAP protocol.
# #define TPM_PID_ADIP       ((TPM_PROTOCOL_ID) 0x0003)          ///< The ADIP protocol.
# #define TPM_PID_ADCP       ((TPM_PROTOCOL_ID) 0x0004)          ///< The ADCP protocol.
# #define TPM_PID_OWNER      ((TPM_PROTOCOL_ID) 0x0005)          ///< The protocol for taking ownership of a TPM.
# #define TPM_PID_DSAP       ((TPM_PROTOCOL_ID) 0x0006)          ///< The DSAP protocol
# #define TPM_PID_TRANSPORT  ((TPM_PROTOCOL_ID) 0x0007)          ///< The transport protocol
TPM_PID_OIAP                = 0x0001
TPM_PID_OSAP                = 0x0002
TPM_PID_ADIP                = 0x0003
TPM_PID_ADCP                = 0x0004
TPM_PID_OWNER               = 0x0005
TPM_PID_DSAP                = 0x0006
TPM_PID_TRANSPORT           = 0x0007

# 
# //
# // Part 2, section 4.8: TPM_ALGORITHM_ID
# //   The TPM MUST support the algorithms TPM_ALG_RSA, TPM_ALG_SHA, TPM_ALG_HMAC,
# //   TPM_ALG_MGF1
# //
# #define TPM_ALG_RSA     ((TPM_ALGORITHM_ID) 0x00000001)             ///< The RSA algorithm.
# #define TPM_ALG_DES     ((TPM_ALGORITHM_ID) 0x00000002)             ///< The DES algorithm
# #define TPM_ALG_3DES    ((TPM_ALGORITHM_ID) 0x00000003)             ///< The 3DES algorithm in EDE mode
# #define TPM_ALG_SHA     ((TPM_ALGORITHM_ID) 0x00000004)             ///< The SHA1 algorithm
# #define TPM_ALG_HMAC    ((TPM_ALGORITHM_ID) 0x00000005)             ///< The RFC 2104 HMAC algorithm
# #define TPM_ALG_AES128  ((TPM_ALGORITHM_ID) 0x00000006)             ///< The AES algorithm, key size 128
# #define TPM_ALG_MGF1    ((TPM_ALGORITHM_ID) 0x00000007)             ///< The XOR algorithm using MGF1 to create a string the size of the encrypted block
# #define TPM_ALG_AES192  ((TPM_ALGORITHM_ID) 0x00000008)             ///< AES, key size 192
# #define TPM_ALG_AES256  ((TPM_ALGORITHM_ID) 0x00000009)             ///< AES, key size 256
# #define TPM_ALG_XOR     ((TPM_ALGORITHM_ID) 0x0000000A)             ///< XOR using the rolling nonces
TPM_ALG_RSA                 = 0x00000001
TPM_ALG_DES                 = 0x00000002
TPM_ALG_3DES                = 0x00000003
TPM_ALG_SHA                 = 0x00000004
TPM_ALG_HMAC                = 0x00000005
TPM_ALG_AES128              = 0x00000006
TPM_ALG_MGF1                = 0x00000007
TPM_ALG_AES192              = 0x00000008
TPM_ALG_AES256              = 0x00000009
TPM_ALG_XOR                 = 0x0000000A

# 
# //
# // Part 2, section 4.9: TPM_PHYSICAL_PRESENCE
# //
# #define TPM_PHYSICAL_PRESENCE_HW_DISABLE     ((TPM_PHYSICAL_PRESENCE) 0x0200) ///< Sets the physicalPresenceHWEnable to FALSE
# #define TPM_PHYSICAL_PRESENCE_CMD_DISABLE    ((TPM_PHYSICAL_PRESENCE) 0x0100) ///< Sets the physicalPresenceCMDEnable to FALSE
# #define TPM_PHYSICAL_PRESENCE_LIFETIME_LOCK  ((TPM_PHYSICAL_PRESENCE) 0x0080) ///< Sets the physicalPresenceLifetimeLock to TRUE
# #define TPM_PHYSICAL_PRESENCE_HW_ENABLE      ((TPM_PHYSICAL_PRESENCE) 0x0040) ///< Sets the physicalPresenceHWEnable to TRUE
# #define TPM_PHYSICAL_PRESENCE_CMD_ENABLE     ((TPM_PHYSICAL_PRESENCE) 0x0020) ///< Sets the physicalPresenceCMDEnable to TRUE
# #define TPM_PHYSICAL_PRESENCE_NOTPRESENT     ((TPM_PHYSICAL_PRESENCE) 0x0010) ///< Sets PhysicalPresence = FALSE
# #define TPM_PHYSICAL_PRESENCE_PRESENT        ((TPM_PHYSICAL_PRESENCE) 0x0008) ///< Sets PhysicalPresence = TRUE
# #define TPM_PHYSICAL_PRESENCE_LOCK           ((TPM_PHYSICAL_PRESENCE) 0x0004) ///< Sets PhysicalPresenceLock = TRUE
TPM_PHYSICAL_PRESENCE_HW_DISABLE    = 0x0200
TPM_PHYSICAL_PRESENCE_CMD_DISABLE   = 0x0100
TPM_PHYSICAL_PRESENCE_LIFETIME_LOCK = 0x0080
TPM_PHYSICAL_PRESENCE_HW_ENABLE     = 0x0040
TPM_PHYSICAL_PRESENCE_CMD_ENABLE    = 0x0020
TPM_PHYSICAL_PRESENCE_NOTPRESENT    = 0x0010
TPM_PHYSICAL_PRESENCE_PRESENT       = 0x0008
TPM_PHYSICAL_PRESENCE_LOCK          = 0x0004

# 
# //
# // Part 2, section 4.10: TPM_MIGRATE_SCHEME
# //
# #define TPM_MS_MIGRATE                  ((TPM_MIGRATE_SCHEME) 0x0001)     ///< A public key that can be used with all TPM migration commands other than 'ReWrap' mode.
# #define TPM_MS_REWRAP                   ((TPM_MIGRATE_SCHEME) 0x0002)     ///< A public key that can be used for the ReWrap mode of TPM_CreateMigrationBlob.
# #define TPM_MS_MAINT                    ((TPM_MIGRATE_SCHEME) 0x0003)     ///< A public key that can be used for the Maintenance commands
# #define TPM_MS_RESTRICT_MIGRATE         ((TPM_MIGRATE_SCHEME) 0x0004)     ///< The key is to be migrated to a Migration Authority.
# #define TPM_MS_RESTRICT_APPROVE_DOUBLE  ((TPM_MIGRATE_SCHEME) 0x0005)     ///< The key is to be migrated to an entity approved by a Migration Authority using double wrapping
TPM_MS_MIGRATE                      = 0x0001
TPM_MS_REWRAP                       = 0x0002
TPM_MS_MAINT                        = 0x0003
TPM_MS_RESTRICT_MIGRATE             = 0x0004
TPM_MS_RESTRICT_APPROVE_DOUBLE      = 0x0005

# 
# //
# // Part 2, section 4.11: TPM_EK_TYPE
# //
# #define TPM_EK_TYPE_ACTIVATE  ((TPM_EK_TYPE) 0x0001)       ///< The blob MUST be TPM_EK_BLOB_ACTIVATE
# #define TPM_EK_TYPE_AUTH      ((TPM_EK_TYPE) 0x0002)       ///< The blob MUST be TPM_EK_BLOB_AUTH
TPM_EK_TYPE_ACTIVATE        = 0x0001
TPM_EK_TYPE_AUTH            = 0x0002

# 
# //
# // Part 2, section 4.12: TPM_PLATFORM_SPECIFIC
# //
# #define TPM_PS_PC_11      ((TPM_PLATFORM_SPECIFIC) 0x0001)           ///< PC Specific version 1.1
# #define TPM_PS_PC_12      ((TPM_PLATFORM_SPECIFIC) 0x0002)           ///< PC Specific version 1.2
# #define TPM_PS_PDA_12     ((TPM_PLATFORM_SPECIFIC) 0x0003)           ///< PDA Specific version 1.2
# #define TPM_PS_Server_12  ((TPM_PLATFORM_SPECIFIC) 0x0004)           ///< Server Specific version 1.2
# #define TPM_PS_Mobile_12  ((TPM_PLATFORM_SPECIFIC) 0x0005)           ///< Mobil Specific version 1.2
TPM_PS_PC_11                = 0x0001
TPM_PS_PC_12                = 0x0002
TPM_PS_PDA_12               = 0x0003
TPM_PS_Server_12            = 0x0004
TPM_PS_Mobile_12            = 0x0005

# 
# //
# // Part 2, section 5: Basic Structures
# //
# 
# ///
# /// Part 2, section 5.1: TPM_STRUCT_VER
# ///
# typedef struct tdTPM_STRUCT_VER {
#   UINT8    major;
#   UINT8    minor;
#   UINT8    revMajor;
#   UINT8    revMinor;
# } TPM_STRUCT_VER;
class TPM_STRUCT_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     UINT8),
    ("minor",     UINT8),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

# 
# ///
# /// Part 2, section 5.3: TPM_VERSION
# ///
# typedef struct tdTPM_VERSION {
#   TPM_VERSION_BYTE    major;
#   TPM_VERSION_BYTE    minor;
#   UINT8               revMajor;
#   UINT8               revMinor;
# } TPM_VERSION;
class TPM_VERSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     TPM_VERSION_BYTE),
    ("minor",     TPM_VERSION_BYTE),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

# 
# #define TPM_SHA1_160_HASH_LEN    0x14
# #define TPM_SHA1BASED_NONCE_LEN  TPM_SHA1_160_HASH_LEN
TPM_SHA1_160_HASH_LEN       = 0x14
TPM_SHA1BASED_NONCE_LEN     = TPM_SHA1_160_HASH_LEN

# 
# ///
# /// Part 2, section 5.4: TPM_DIGEST
# ///
# typedef struct tdTPM_DIGEST {
#   UINT8    digest[TPM_SHA1_160_HASH_LEN];
# } TPM_DIGEST;
class TPM_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("digest",  UINT8 * TPM_SHA1_160_HASH_LEN)
  ]

# 
# ///
# /// This SHALL be the digest of the chosen identityLabel and privacyCA for a new TPM identity
# ///
# typedef TPM_DIGEST TPM_CHOSENID_HASH;
TPM_CHOSENID_HASH                   = TPM_DIGEST
# ///
# /// This SHALL be the hash of a list of PCR indexes and PCR values that a key or data is bound to
# ///
# typedef TPM_DIGEST TPM_COMPOSITE_HASH;
TPM_COMPOSITE_HASH                  = TPM_DIGEST
# ///
# /// This SHALL be the value of a DIR register
# ///
# typedef TPM_DIGEST TPM_DIRVALUE;
# 
# typedef TPM_DIGEST TPM_HMAC;
# ///
# /// The value inside of the PCR
# ///
# typedef TPM_DIGEST TPM_PCRVALUE;
# ///
# /// This SHALL be the value of the current internal audit state
# ///
# typedef TPM_DIGEST TPM_AUDITDIGEST;
TPM_DIRVALUE                        = TPM_DIGEST
TPM_HMAC                            = TPM_DIGEST
TPM_PCRVALUE                        = TPM_DIGEST
TPM_AUDITDIGEST                     = TPM_DIGEST

# 
# ///
# /// Part 2, section 5.5: TPM_NONCE
# ///
# typedef struct tdTPM_NONCE {
#   UINT8    nonce[20];
# } TPM_NONCE;
class TPM_NONCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",  UINT8 * 20)
  ]

# 
# ///
# /// This SHALL be a random value generated by a TPM immediately after the EK is installed
# /// in that TPM, whenever an EK is installed in that TPM
# ///
# typedef TPM_NONCE TPM_DAA_TPM_SEED;
# ///
# /// This SHALL be a random value
# ///
# typedef TPM_NONCE TPM_DAA_CONTEXT_SEED;
TPM_DAA_TPM_SEED                  = TPM_NONCE
TPM_DAA_CONTEXT_SEED              = TPM_NONCE

# 
# //
# // Part 2, section 5.6: TPM_AUTHDATA
# //
# ///
# /// The AuthData data is the information that is saved or passed to provide proof of ownership
# /// 296 of an entity
# ///
# typedef UINT8 tdTPM_AUTHDATA[20];
# 
# typedef tdTPM_AUTHDATA TPM_AUTHDATA;
# ///
# /// A secret plaintext value used in the authorization process
# ///
# typedef TPM_AUTHDATA TPM_SECRET;
# ///
# /// A ciphertext (encrypted) version of AuthData data. The encryption mechanism depends on the context
# ///
# typedef TPM_AUTHDATA TPM_ENCAUTH;
tdTPM_AUTHDATA                    = UINT8 * 20
TPM_AUTHDATA                      = tdTPM_AUTHDATA
TPM_SECRET                        = TPM_AUTHDATA
TPM_ENCAUTH                       = TPM_AUTHDATA

# 
# ///
# /// Part 2, section 5.7: TPM_KEY_HANDLE_LIST
# /// Size of handle is loaded * sizeof(TPM_KEY_HANDLE)
# ///
# typedef struct tdTPM_KEY_HANDLE_LIST {
#   UINT16            loaded;
#   TPM_KEY_HANDLE    handle[1];
# } TPM_KEY_HANDLE_LIST;
class TPM_KEY_HANDLE_LIST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("loaded",  UINT16),
    ("handle",  TPM_KEY_HANDLE * 1)
  ]

# 
# //
# // Part 2, section 5.8: TPM_KEY_USAGE values
# //
# ///
# /// TPM_KEY_SIGNING SHALL indicate a signing key. The [private] key SHALL be
# /// used for signing operations, only. This means that it MUST be a leaf of the
# /// Protected Storage key hierarchy.
# ///
# #define TPM_KEY_SIGNING  ((UINT16) 0x0010)
# ///
# /// TPM_KEY_STORAGE SHALL indicate a storage key. The key SHALL be used to wrap
# /// and unwrap other keys in the Protected Storage hierarchy
# ///
# #define TPM_KEY_STORAGE  ((UINT16) 0x0011)
# ///
# /// TPM_KEY_IDENTITY SHALL indicate an identity key. The key SHALL be used for
# /// operations that require a TPM identity, only.
# ///
# #define TPM_KEY_IDENTITY  ((UINT16) 0x0012)
# ///
# /// TPM_KEY_AUTHCHANGE SHALL indicate an ephemeral key that is in use during
# /// the ChangeAuthAsym process, only.
# ///
# #define TPM_KEY_AUTHCHANGE  ((UINT16) 0x0013)
# ///
# /// TPM_KEY_BIND SHALL indicate a key that can be used for TPM_Bind and
# /// TPM_Unbind operations only.
# ///
# #define TPM_KEY_BIND  ((UINT16) 0x0014)
# ///
# /// TPM_KEY_LEGACY SHALL indicate a key that can perform signing and binding
# /// operations. The key MAY be used for both signing and binding operations.
# /// The TPM_KEY_LEGACY key type is to allow for use by applications where both
# /// signing and encryption operations occur with the same key. The use of this
# /// key type is not recommended TPM_KEY_MIGRATE 0x0016 This SHALL indicate a
# /// key in use for TPM_MigrateKey
# ///
# #define TPM_KEY_LEGACY  ((UINT16) 0x0015)
# ///
# /// TPM_KEY_MIGRAGE SHALL indicate a key in use for TPM_MigrateKey
# ///
# #define TPM_KEY_MIGRATE  ((UINT16) 0x0016)
TPM_KEY_SIGNING             = 0x0010
TPM_KEY_STORAGE             = 0x0011
TPM_KEY_IDENTITY            = 0x0012
TPM_KEY_AUTHCHANGE          = 0x0013
TPM_KEY_BIND                = 0x0014
TPM_KEY_LEGACY              = 0x0015
TPM_KEY_MIGRATE             = 0x0016
# 
# //
# // Part 2, section 5.8.1: Mandatory Key Usage Schemes
# //
# 
# #define TPM_ES_NONE                 ((TPM_ENC_SCHEME) 0x0001)
# #define TPM_ES_RSAESPKCSv15         ((TPM_ENC_SCHEME) 0x0002)
# #define TPM_ES_RSAESOAEP_SHA1_MGF1  ((TPM_ENC_SCHEME) 0x0003)
# #define TPM_ES_SYM_CNT              ((TPM_ENC_SCHEME) 0x0004)  ///< rev94 defined
# #define TPM_ES_SYM_CTR              ((TPM_ENC_SCHEME) 0x0004)
# #define TPM_ES_SYM_OFB              ((TPM_ENC_SCHEME) 0x0005)
TPM_ES_NONE                 = 0x0001
TPM_ES_RSAESPKCSv15         = 0x0002
TPM_ES_RSAESOAEP_SHA1_MGF1  = 0x0003
TPM_ES_SYM_CNT              = 0x0004
TPM_ES_SYM_CTR              = 0x0004
TPM_ES_SYM_OFB              = 0x0005

# 
# #define TPM_SS_NONE                 ((TPM_SIG_SCHEME) 0x0001)
# #define TPM_SS_RSASSAPKCS1v15_SHA1  ((TPM_SIG_SCHEME) 0x0002)
# #define TPM_SS_RSASSAPKCS1v15_DER   ((TPM_SIG_SCHEME) 0x0003)
# #define TPM_SS_RSASSAPKCS1v15_INFO  ((TPM_SIG_SCHEME) 0x0004)
TPM_SS_NONE                 = 0x0001
TPM_SS_RSASSAPKCS1v15_SHA1  = 0x0002
TPM_SS_RSASSAPKCS1v15_DER   = 0x0003
TPM_SS_RSASSAPKCS1v15_INFO  = 0x0004

# 
# //
# // Part 2, section 5.9: TPM_AUTH_DATA_USAGE values
# //
# #define TPM_AUTH_NEVER          ((TPM_AUTH_DATA_USAGE) 0x00)
# #define TPM_AUTH_ALWAYS         ((TPM_AUTH_DATA_USAGE) 0x01)
# #define TPM_AUTH_PRIV_USE_ONLY  ((TPM_AUTH_DATA_USAGE) 0x03)
TPM_AUTH_NEVER              = 0x00
TPM_AUTH_ALWAYS             = 0x01
TPM_AUTH_PRIV_USE_ONLY      = 0x03

# 
# ///
# /// Part 2, section 5.10: TPM_KEY_FLAGS
# ///
# typedef enum tdTPM_KEY_FLAGS {
#   redirection      = 0x00000001,
#   migratable       = 0x00000002,
#   isVolatile       = 0x00000004,
#   pcrIgnoredOnRead = 0x00000008,
#   migrateAuthority = 0x00000010
# } TPM_KEY_FLAGS_BITS;
redirection                       = 0x00000001
migratable                        = 0x00000002
isVolatile                        = 0x00000004
pcrIgnoredOnRead                  = 0x00000008
migrateAuthority                  = 0x00000010
TPM_KEY_FLAGS_BITS = ENUM

# 
# ///
# /// Part 2, section 5.11: TPM_CHANGEAUTH_VALIDATE
# ///
# typedef struct tdTPM_CHANGEAUTH_VALIDATE {
#   TPM_SECRET    newAuthSecret;
#   TPM_NONCE     n1;
# } TPM_CHANGEAUTH_VALIDATE;
class TPM_CHANGEAUTH_VALIDATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("newAuthSecret", TPM_SECRET),
    ("n1",            TPM_NONCE)
  ]

# 
# ///
# /// Part 2, section 5.12: TPM_MIGRATIONKEYAUTH
# ///   declared after section 10 to catch declaration of TPM_PUBKEY
# ///
# /// Part 2 section 10.1: TPM_KEY_PARMS
# ///   [size_is(parmSize)] BYTE* parms;
# ///
# typedef struct tdTPM_KEY_PARMS {
#   TPM_ALGORITHM_ID    algorithmID;
#   TPM_ENC_SCHEME      encScheme;
#   TPM_SIG_SCHEME      sigScheme;
#   UINT32              parmSize;
#   UINT8               *parms;
# } TPM_KEY_PARMS;
class TPM_KEY_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmID", TPM_ALGORITHM_ID),
    ("encScheme",   TPM_ENC_SCHEME),
    ("sigScheme",   TPM_SIG_SCHEME),
    ("parmSize",    UINT32),
    ("parms",       POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 10.4: TPM_STORE_PUBKEY
# ///
# typedef struct tdTPM_STORE_PUBKEY {
#   UINT32    keyLength;
#   UINT8     key[1];
# } TPM_STORE_PUBKEY;
class TPM_STORE_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       UINT8 * 1)
  ]

# 
# ///
# /// Part 2, section 10.5: TPM_PUBKEY
# ///
# typedef struct tdTPM_PUBKEY {
#   TPM_KEY_PARMS       algorithmParms;
#   TPM_STORE_PUBKEY    pubKey;
# } TPM_PUBKEY;
class TPM_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubKey",          TPM_STORE_PUBKEY)
  ]

# 
# ///
# /// Part 2, section 5.12: TPM_MIGRATIONKEYAUTH
# ///
# typedef struct tdTPM_MIGRATIONKEYAUTH {
#   TPM_PUBKEY            migrationKey;
#   TPM_MIGRATE_SCHEME    migrationScheme;
#   TPM_DIGEST            digest;
# } TPM_MIGRATIONKEYAUTH;
class TPM_MIGRATIONKEYAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationKey",    TPM_PUBKEY),
    ("migrationScheme", TPM_MIGRATE_SCHEME),
    ("digest",          TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 5.13: TPM_COUNTER_VALUE
# ///
# typedef struct tdTPM_COUNTER_VALUE {
#   TPM_STRUCTURE_TAG    tag;
#   UINT8                label[4];
#   TPM_ACTUAL_COUNT     counter;
# } TPM_COUNTER_VALUE;
class TPM_COUNTER_VALUE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("label",   UINT8 * 4),
    ("counter", TPM_ACTUAL_COUNT)
  ]

# 
# ///
# /// Part 2, section 5.14: TPM_SIGN_INFO
# ///   Size of data indicated by dataLen
# ///
# typedef struct tdTPM_SIGN_INFO {
#   TPM_STRUCTURE_TAG    tag;
#   UINT8                fixed[4];
#   TPM_NONCE            replay;
#   UINT32               dataLen;
#   UINT8                *data;
# } TPM_SIGN_INFO;
class TPM_SIGN_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("fixed",   UINT8 * 4),
    ("replay",  TPM_NONCE),
    ("dataLen", UINT32),
    ("data",    POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 5.15: TPM_MSA_COMPOSITE
# ///   Number of migAuthDigest indicated by MSAlist
# ///
# typedef struct tdTPM_MSA_COMPOSITE {
#   UINT32        MSAlist;
#   TPM_DIGEST    migAuthDigest[1];
# } TPM_MSA_COMPOSITE;
class TPM_MSA_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MSAlist",       UINT32),
    ("migAuthDigest", TPM_DIGEST * 1)
  ]

# 
# ///
# /// Part 2, section 5.16: TPM_CMK_AUTH
# ///
# typedef struct tdTPM_CMK_AUTH {
#   TPM_DIGEST    migrationAuthorityDigest;
#   TPM_DIGEST    destinationKeyDigest;
#   TPM_DIGEST    sourceKeyDigest;
# } TPM_CMK_AUTH;
class TPM_CMK_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationAuthorityDigest",  TPM_DIGEST),
    ("destinationKeyDigest",      TPM_DIGEST),
    ("sourceKeyDigest",           TPM_DIGEST)
  ]

# 
# //
# // Part 2, section 5.17: TPM_CMK_DELEGATE
# //
# #define TPM_CMK_DELEGATE_SIGNING  ((TPM_CMK_DELEGATE) BIT31)
# #define TPM_CMK_DELEGATE_STORAGE  ((TPM_CMK_DELEGATE) BIT30)
# #define TPM_CMK_DELEGATE_BIND     ((TPM_CMK_DELEGATE) BIT29)
# #define TPM_CMK_DELEGATE_LEGACY   ((TPM_CMK_DELEGATE) BIT28)
# #define TPM_CMK_DELEGATE_MIGRATE  ((TPM_CMK_DELEGATE) BIT27)
TPM_CMK_DELEGATE_SIGNING    = BIT31
TPM_CMK_DELEGATE_STORAGE    = BIT30
TPM_CMK_DELEGATE_BIND       = BIT29
TPM_CMK_DELEGATE_LEGACY     = BIT28
TPM_CMK_DELEGATE_MIGRATE    = BIT27

# 
# ///
# /// Part 2, section 5.18: TPM_SELECT_SIZE
# ///
# typedef struct tdTPM_SELECT_SIZE {
#   UINT8     major;
#   UINT8     minor;
#   UINT16    reqSize;
# } TPM_SELECT_SIZE;
class TPM_SELECT_SIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",   UINT8),
    ("minor",   UINT8),
    ("reqSize", UINT16)
  ]

# 
# ///
# /// Part 2, section 5,19: TPM_CMK_MIGAUTH
# ///
# typedef struct tdTPM_CMK_MIGAUTH {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           msaDigest;
#   TPM_DIGEST           pubKeyDigest;
# } TPM_CMK_MIGAUTH;
class TPM_CMK_MIGAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("msaDigest",     TPM_DIGEST),
    ("pubKeyDigest",  TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 5.20: TPM_CMK_SIGTICKET
# ///
# typedef struct tdTPM_CMK_SIGTICKET {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           verKeyDigest;
#   TPM_DIGEST           signedData;
# } TPM_CMK_SIGTICKET;
class TPM_CMK_SIGTICKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("verKeyDigest",  TPM_DIGEST),
    ("signedData",    TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 5.21: TPM_CMK_MA_APPROVAL
# ///
# typedef struct tdTPM_CMK_MA_APPROVAL {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           migrationAuthorityDigest;
# } TPM_CMK_MA_APPROVAL;
class TPM_CMK_MA_APPROVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("migrationAuthorityDigest",  TPM_DIGEST)
  ]

# 
# //
# // Part 2, section 6: Command Tags
# //
# #define TPM_TAG_RQU_COMMAND        ((TPM_STRUCTURE_TAG) 0x00C1)
# #define TPM_TAG_RQU_AUTH1_COMMAND  ((TPM_STRUCTURE_TAG) 0x00C2)
# #define TPM_TAG_RQU_AUTH2_COMMAND  ((TPM_STRUCTURE_TAG) 0x00C3)
# #define TPM_TAG_RSP_COMMAND        ((TPM_STRUCTURE_TAG) 0x00C4)
# #define TPM_TAG_RSP_AUTH1_COMMAND  ((TPM_STRUCTURE_TAG) 0x00C5)
# #define TPM_TAG_RSP_AUTH2_COMMAND  ((TPM_STRUCTURE_TAG) 0x00C6)
TPM_TAG_RQU_COMMAND         = 0x00C1
TPM_TAG_RQU_AUTH1_COMMAND   = 0x00C2
TPM_TAG_RQU_AUTH2_COMMAND   = 0x00C3
TPM_TAG_RSP_COMMAND         = 0x00C4
TPM_TAG_RSP_AUTH1_COMMAND   = 0x00C5
TPM_TAG_RSP_AUTH2_COMMAND   = 0x00C6

# 
# ///
# /// Part 2, section 7.1: TPM_PERMANENT_FLAGS
# ///
# typedef struct tdTPM_PERMANENT_FLAGS {
#   TPM_STRUCTURE_TAG    tag;
#   BOOLEAN              disable;
#   BOOLEAN              ownership;
#   BOOLEAN              deactivated;
#   BOOLEAN              readPubek;
#   BOOLEAN              disableOwnerClear;
#   BOOLEAN              allowMaintenance;
#   BOOLEAN              physicalPresenceLifetimeLock;
#   BOOLEAN              physicalPresenceHWEnable;
#   BOOLEAN              physicalPresenceCMDEnable;
#   BOOLEAN              CEKPUsed;
#   BOOLEAN              TPMpost;
#   BOOLEAN              TPMpostLock;
#   BOOLEAN              FIPS;
#   BOOLEAN                           operator;
#   BOOLEAN                           enableRevokeEK;
#   BOOLEAN              nvLocked;
#   BOOLEAN              readSRKPub;
#   BOOLEAN              tpmEstablished;
#   BOOLEAN              maintenanceDone;
#   BOOLEAN              disableFullDALogicInfo;
# } TPM_PERMANENT_FLAGS;
class TPM_PERMANENT_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                           TPM_STRUCTURE_TAG),
    ("disable",                       BOOLEAN),
    ("ownership",                     BOOLEAN),
    ("deactivated",                   BOOLEAN),
    ("readPubek",                     BOOLEAN),
    ("disableOwnerClear",             BOOLEAN),
    ("allowMaintenance",              BOOLEAN),
    ("physicalPresenceLifetimeLock",  BOOLEAN),
    ("physicalPresenceHWEnable",      BOOLEAN),
    ("physicalPresenceCMDEnable",     BOOLEAN),
    ("CEKPUsed",                      BOOLEAN),
    ("TPMpost",                       BOOLEAN),
    ("TPMpostLock",                   BOOLEAN),
    ("FIPS",                          BOOLEAN),
    ("operator",                      BOOLEAN),
    ("enableRevokeEK",                BOOLEAN),
    ("nvLocked",                      BOOLEAN),
    ("readSRKPub",                    BOOLEAN),
    ("tpmEstablished",                BOOLEAN),
    ("maintenanceDone",               BOOLEAN),
    ("disableFullDALogicInfo",        BOOLEAN)
  ]

# 
# //
# // Part 2, section 7.1.1: Flag Restrictions (of TPM_PERMANENT_FLAGS)
# //
# #define TPM_PF_DISABLE                       ((TPM_CAPABILITY_AREA) 1)
# #define TPM_PF_OWNERSHIP                     ((TPM_CAPABILITY_AREA) 2)
# #define TPM_PF_DEACTIVATED                   ((TPM_CAPABILITY_AREA) 3)
# #define TPM_PF_READPUBEK                     ((TPM_CAPABILITY_AREA) 4)
# #define TPM_PF_DISABLEOWNERCLEAR             ((TPM_CAPABILITY_AREA) 5)
# #define TPM_PF_ALLOWMAINTENANCE              ((TPM_CAPABILITY_AREA) 6)
# #define TPM_PF_PHYSICALPRESENCELIFETIMELOCK  ((TPM_CAPABILITY_AREA) 7)
# #define TPM_PF_PHYSICALPRESENCEHWENABLE      ((TPM_CAPABILITY_AREA) 8)
# #define TPM_PF_PHYSICALPRESENCECMDENABLE     ((TPM_CAPABILITY_AREA) 9)
# #define TPM_PF_CEKPUSED                      ((TPM_CAPABILITY_AREA) 10)
# #define TPM_PF_TPMPOST                       ((TPM_CAPABILITY_AREA) 11)
# #define TPM_PF_TPMPOSTLOCK                   ((TPM_CAPABILITY_AREA) 12)
# #define TPM_PF_FIPS                          ((TPM_CAPABILITY_AREA) 13)
# #define TPM_PF_OPERATOR                      ((TPM_CAPABILITY_AREA) 14)
# #define TPM_PF_ENABLEREVOKEEK                ((TPM_CAPABILITY_AREA) 15)
# #define TPM_PF_NV_LOCKED                     ((TPM_CAPABILITY_AREA) 16)
# #define TPM_PF_READSRKPUB                    ((TPM_CAPABILITY_AREA) 17)
# #define TPM_PF_TPMESTABLISHED                ((TPM_CAPABILITY_AREA) 18)
# #define TPM_PF_MAINTENANCEDONE               ((TPM_CAPABILITY_AREA) 19)
# #define TPM_PF_DISABLEFULLDALOGICINFO        ((TPM_CAPABILITY_AREA) 20)
TPM_PF_DISABLE                      = 1
TPM_PF_OWNERSHIP                    = 2
TPM_PF_DEACTIVATED                  = 3
TPM_PF_READPUBEK                    = 4
TPM_PF_DISABLEOWNERCLEAR            = 5
TPM_PF_ALLOWMAINTENANCE             = 6
TPM_PF_PHYSICALPRESENCELIFETIMELOCK = 7
TPM_PF_PHYSICALPRESENCEHWENABLE     = 8
TPM_PF_PHYSICALPRESENCECMDENABLE    = 9
TPM_PF_CEKPUSED                     = 10
TPM_PF_TPMPOST                      = 11
TPM_PF_TPMPOSTLOCK                  = 12
TPM_PF_FIPS                         = 13
TPM_PF_OPERATOR                     = 14
TPM_PF_ENABLEREVOKEEK               = 15
TPM_PF_NV_LOCKED                    = 16
TPM_PF_READSRKPUB                   = 17
TPM_PF_TPMESTABLISHED               = 18
TPM_PF_MAINTENANCEDONE              = 19
TPM_PF_DISABLEFULLDALOGICINFO       = 20

# 
# ///
# /// Part 2, section 7.2: TPM_STCLEAR_FLAGS
# ///
# typedef struct tdTPM_STCLEAR_FLAGS {
#   TPM_STRUCTURE_TAG    tag;
#   BOOLEAN              deactivated;
#   BOOLEAN              disableForceClear;
#   BOOLEAN              physicalPresence;
#   BOOLEAN              physicalPresenceLock;
#   BOOLEAN              bGlobalLock;
# } TPM_STCLEAR_FLAGS;
class TPM_STCLEAR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("deactivated",           BOOLEAN),
    ("disableForceClear",     BOOLEAN),
    ("physicalPresence",      BOOLEAN),
    ("physicalPresenceLock",  BOOLEAN),
    ("bGlobalLock",           BOOLEAN)
  ]

# 
# //
# // Part 2, section 7.2.1: Flag Restrictions (of TPM_STCLEAR_FLAGS)
# //
# #define TPM_SF_DEACTIVATED           ((TPM_CAPABILITY_AREA) 1)
# #define TPM_SF_DISABLEFORCECLEAR     ((TPM_CAPABILITY_AREA) 2)
# #define TPM_SF_PHYSICALPRESENCE      ((TPM_CAPABILITY_AREA) 3)
# #define TPM_SF_PHYSICALPRESENCELOCK  ((TPM_CAPABILITY_AREA) 4)
# #define TPM_SF_BGLOBALLOCK           ((TPM_CAPABILITY_AREA) 5)
TPM_SF_DEACTIVATED          = 1
TPM_SF_DISABLEFORCECLEAR    = 2
TPM_SF_PHYSICALPRESENCE     = 3
TPM_SF_PHYSICALPRESENCELOCK = 4
TPM_SF_BGLOBALLOCK          = 5

# 
# ///
# /// Part 2, section 7.3: TPM_STANY_FLAGS
# ///
# typedef struct tdTPM_STANY_FLAGS {
#   TPM_STRUCTURE_TAG         tag;
#   BOOLEAN                   postInitialise;
#   TPM_MODIFIER_INDICATOR    localityModifier;
#   BOOLEAN                   transportExclusive;
#   BOOLEAN                   TOSPresent;
# } TPM_STANY_FLAGS;
class TPM_STANY_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("postInitialise",      BOOLEAN),
    ("localityModifier",    TPM_MODIFIER_INDICATOR),
    ("transportExclusive",  BOOLEAN),
    ("TOSPresent",          BOOLEAN)
  ]

# 
# //
# // Part 2, section 7.3.1: Flag Restrictions (of TPM_STANY_FLAGS)
# //
# #define TPM_AF_POSTINITIALISE      ((TPM_CAPABILITY_AREA) 1)
# #define TPM_AF_LOCALITYMODIFIER    ((TPM_CAPABILITY_AREA) 2)
# #define TPM_AF_TRANSPORTEXCLUSIVE  ((TPM_CAPABILITY_AREA) 3)
# #define TPM_AF_TOSPRESENT          ((TPM_CAPABILITY_AREA) 4)
TPM_AF_POSTINITIALISE       = 1
TPM_AF_LOCALITYMODIFIER     = 2
TPM_AF_TRANSPORTEXCLUSIVE   = 3
TPM_AF_TOSPRESENT           = 4

# 
# //
# // All those structures defined in section 7.4, 7.5, 7.6 are not normative and
# // thus no definitions here
# //
# // Part 2, section 7.4: TPM_PERMANENT_DATA
# //
# #define TPM_MIN_COUNTERS          4     ///< the minimum number of counters is 4
# #define TPM_DELEGATE_KEY          TPM_KEY
# #define TPM_NUM_PCR               16
# #define TPM_MAX_NV_WRITE_NOOWNER  64
TPM_MIN_COUNTERS            = 4
TPM_DELEGATE_KEY            = TPM_KEY
TPM_NUM_PCR                 = 16
TPM_MAX_NV_WRITE_NOOWNER    = 64

# 
# //
# // Part 2, section 7.4.1: PERMANENT_DATA Subcap for SetCapability
# //
# #define TPM_PD_REVMAJOR               ((TPM_CAPABILITY_AREA) 1)
# #define TPM_PD_REVMINOR               ((TPM_CAPABILITY_AREA) 2)
# #define TPM_PD_TPMPROOF               ((TPM_CAPABILITY_AREA) 3)
# #define TPM_PD_OWNERAUTH              ((TPM_CAPABILITY_AREA) 4)
# #define TPM_PD_OPERATORAUTH           ((TPM_CAPABILITY_AREA) 5)
# #define TPM_PD_MANUMAINTPUB           ((TPM_CAPABILITY_AREA) 6)
# #define TPM_PD_ENDORSEMENTKEY         ((TPM_CAPABILITY_AREA) 7)
# #define TPM_PD_SRK                    ((TPM_CAPABILITY_AREA) 8)
# #define TPM_PD_DELEGATEKEY            ((TPM_CAPABILITY_AREA) 9)
# #define TPM_PD_CONTEXTKEY             ((TPM_CAPABILITY_AREA) 10)
# #define TPM_PD_AUDITMONOTONICCOUNTER  ((TPM_CAPABILITY_AREA) 11)
# #define TPM_PD_MONOTONICCOUNTER       ((TPM_CAPABILITY_AREA) 12)
# #define TPM_PD_PCRATTRIB              ((TPM_CAPABILITY_AREA) 13)
# #define TPM_PD_ORDINALAUDITSTATUS     ((TPM_CAPABILITY_AREA) 14)
# #define TPM_PD_AUTHDIR                ((TPM_CAPABILITY_AREA) 15)
# #define TPM_PD_RNGSTATE               ((TPM_CAPABILITY_AREA) 16)
# #define TPM_PD_FAMILYTABLE            ((TPM_CAPABILITY_AREA) 17)
# #define TPM_DELEGATETABLE             ((TPM_CAPABILITY_AREA) 18)
# #define TPM_PD_EKRESET                ((TPM_CAPABILITY_AREA) 19)
# #define TPM_PD_MAXNVBUFSIZE           ((TPM_CAPABILITY_AREA) 20)
# #define TPM_PD_LASTFAMILYID           ((TPM_CAPABILITY_AREA) 21)
# #define TPM_PD_NOOWNERNVWRITE         ((TPM_CAPABILITY_AREA) 22)
# #define TPM_PD_RESTRICTDELEGATE       ((TPM_CAPABILITY_AREA) 23)
# #define TPM_PD_TPMDAASEED             ((TPM_CAPABILITY_AREA) 24)
# #define TPM_PD_DAAPROOF               ((TPM_CAPABILITY_AREA) 25)
TPM_PD_REVMAJOR               = 1
TPM_PD_REVMINOR               = 2
TPM_PD_TPMPROOF               = 3
TPM_PD_OWNERAUTH              = 4
TPM_PD_OPERATORAUTH           = 5
TPM_PD_MANUMAINTPUB           = 6
TPM_PD_ENDORSEMENTKEY         = 7
TPM_PD_SRK                    = 8
TPM_PD_DELEGATEKEY            = 9
TPM_PD_CONTEXTKEY             = 10
TPM_PD_AUDITMONOTONICCOUNTER  = 11
TPM_PD_MONOTONICCOUNTER       = 12
TPM_PD_PCRATTRIB              = 13
TPM_PD_ORDINALAUDITSTATUS     = 14
TPM_PD_AUTHDIR                = 15
TPM_PD_RNGSTATE               = 16
TPM_PD_FAMILYTABLE            = 17
TPM_DELEGATETABLE             = 18
TPM_PD_EKRESET                = 19
TPM_PD_MAXNVBUFSIZE           = 20
TPM_PD_LASTFAMILYID           = 21
TPM_PD_NOOWNERNVWRITE         = 22
TPM_PD_RESTRICTDELEGATE       = 23
TPM_PD_TPMDAASEED             = 24
TPM_PD_DAAPROOF               = 25

# 
# ///
# /// Part 2, section 7.5: TPM_STCLEAR_DATA
# ///   available inside TPM only
# ///
# typedef struct tdTPM_STCLEAR_DATA {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_NONCE            contextNonceKey;
#   TPM_COUNT_ID         countID;
#   UINT32               ownerReference;
#   BOOLEAN              disableResetLock;
#   TPM_PCRVALUE         PCR[TPM_NUM_PCR];
#   UINT32               deferredPhysicalPresence;
# } TPM_STCLEAR_DATA;
class TPM_STCLEAR_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("contextNonceKey",           TPM_NONCE),
    ("countID",                   TPM_COUNT_ID),
    ("ownerReference",            UINT32),
    ("disableResetLock",          BOOLEAN),
    ("PCR",                       TPM_PCRVALUE * TPM_NUM_PCR),
    ("deferredPhysicalPresence",  UINT32)
  ]

# 
# //
# // Part 2, section 7.5.1: STCLEAR_DATA Subcap for SetCapability
# //
# #define TPM_SD_CONTEXTNONCEKEY           ((TPM_CAPABILITY_AREA)0x00000001)
# #define TPM_SD_COUNTID                   ((TPM_CAPABILITY_AREA)0x00000002)
# #define TPM_SD_OWNERREFERENCE            ((TPM_CAPABILITY_AREA)0x00000003)
# #define TPM_SD_DISABLERESETLOCK          ((TPM_CAPABILITY_AREA)0x00000004)
# #define TPM_SD_PCR                       ((TPM_CAPABILITY_AREA)0x00000005)
# #define TPM_SD_DEFERREDPHYSICALPRESENCE  ((TPM_CAPABILITY_AREA)0x00000006)
TPM_SD_CONTEXTNONCEKEY            = 0x00000001
TPM_SD_COUNTID                    = 0x00000002
TPM_SD_OWNERREFERENCE             = 0x00000003
TPM_SD_DISABLERESETLOCK           = 0x00000004
TPM_SD_PCR                        = 0x00000005
TPM_SD_DEFERREDPHYSICALPRESENCE   = 0x00000006

# 
# //
# // Part 2, section 7.6.1: STANY_DATA Subcap for SetCapability
# //
# #define TPM_AD_CONTEXTNONCESESSION  ((TPM_CAPABILITY_AREA) 1)
# #define TPM_AD_AUDITDIGEST          ((TPM_CAPABILITY_AREA) 2)
# #define TPM_AD_CURRENTTICKS         ((TPM_CAPABILITY_AREA) 3)
# #define TPM_AD_CONTEXTCOUNT         ((TPM_CAPABILITY_AREA) 4)
# #define TPM_AD_CONTEXTLIST          ((TPM_CAPABILITY_AREA) 5)
# #define TPM_AD_SESSIONS             ((TPM_CAPABILITY_AREA) 6)
TPM_AD_CONTEXTNONCESESSION        = 1
TPM_AD_AUDITDIGEST                = 2
TPM_AD_CURRENTTICKS               = 3
TPM_AD_CONTEXTCOUNT               = 4
TPM_AD_CONTEXTLIST                = 5
TPM_AD_SESSIONS                   = 6

# 
# //
# // Part 2, section 8: PCR Structures
# //
# 
# ///
# /// Part 2, section 8.1: TPM_PCR_SELECTION
# ///   Size of pcrSelect[] indicated by sizeOfSelect
# ///
# typedef struct tdTPM_PCR_SELECTION {
#   UINT16    sizeOfSelect;
#   UINT8     pcrSelect[1];
# } TPM_PCR_SELECTION;
class TPM_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeOfSelect",  UINT16),
    ("pcrSelect",     UINT8 * 1)
  ]

# 
# ///
# /// Part 2, section 8.2: TPM_PCR_COMPOSITE
# ///   Size of pcrValue[] indicated by valueSize
# ///
# typedef struct tdTPM_PCR_COMPOSITE {
#   TPM_PCR_SELECTION    select;
#   UINT32               valueSize;
#   TPM_PCRVALUE         pcrValue[1];
# } TPM_PCR_COMPOSITE;
class TPM_PCR_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("select",    TPM_PCR_SELECTION),
    ("valueSize", UINT32),
    ("pcrValue",  TPM_PCRVALUE * 1)
  ]

# 
# ///
# /// Part 2, section 8.3: TPM_PCR_INFO
# ///
# typedef struct tdTPM_PCR_INFO {
#   TPM_PCR_SELECTION     pcrSelection;
#   TPM_COMPOSITE_HASH    digestAtRelease;
#   TPM_COMPOSITE_HASH    digestAtCreation;
# } TPM_PCR_INFO;
class TPM_PCR_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH),
    ("digestAtCreation",  TPM_COMPOSITE_HASH)
  ]

# 
# ///
# /// Part 2, section 8.6: TPM_LOCALITY_SELECTION
# ///
# typedef UINT8 TPM_LOCALITY_SELECTION;
TPM_LOCALITY_SELECTION = UINT8

# 
# #define TPM_LOC_FOUR   ((UINT8) 0x10)
# #define TPM_LOC_THREE  ((UINT8) 0x08)
# #define TPM_LOC_TWO    ((UINT8) 0x04)
# #define TPM_LOC_ONE    ((UINT8) 0x02)
# #define TPM_LOC_ZERO   ((UINT8) 0x01)
TPM_LOC_FOUR                = 0x10
TPM_LOC_THREE               = 0x08
TPM_LOC_TWO                 = 0x04
TPM_LOC_ONE                 = 0x02
TPM_LOC_ZERO                = 0x01

# 
# ///
# /// Part 2, section 8.4: TPM_PCR_INFO_LONG
# ///
# typedef struct tdTPM_PCR_INFO_LONG {
#   TPM_STRUCTURE_TAG         tag;
#   TPM_LOCALITY_SELECTION    localityAtCreation;
#   TPM_LOCALITY_SELECTION    localityAtRelease;
#   TPM_PCR_SELECTION         creationPCRSelection;
#   TPM_PCR_SELECTION         releasePCRSelection;
#   TPM_COMPOSITE_HASH        digestAtCreation;
#   TPM_COMPOSITE_HASH        digestAtRelease;
# } TPM_PCR_INFO_LONG;
class TPM_PCR_INFO_LONG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("localityAtCreation",    TPM_LOCALITY_SELECTION),
    ("localityAtRelease",     TPM_LOCALITY_SELECTION),
    ("creationPCRSelection",  TPM_PCR_SELECTION),
    ("releasePCRSelection",   TPM_PCR_SELECTION),
    ("digestAtCreation",      TPM_COMPOSITE_HASH),
    ("digestAtRelease",       TPM_COMPOSITE_HASH)
  ]

# 
# ///
# /// Part 2, section 8.5: TPM_PCR_INFO_SHORT
# ///
# typedef struct tdTPM_PCR_INFO_SHORT {
#   TPM_PCR_SELECTION         pcrSelection;
#   TPM_LOCALITY_SELECTION    localityAtRelease;
#   TPM_COMPOSITE_HASH        digestAtRelease;
# } TPM_PCR_INFO_SHORT;
class TPM_PCR_INFO_SHORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("localityAtRelease", TPM_LOCALITY_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH)
  ]

# 
# ///
# /// Part 2, section 8.8: TPM_PCR_ATTRIBUTES
# ///
# typedef struct tdTPM_PCR_ATTRIBUTES {
#   BOOLEAN                   pcrReset;
#   TPM_LOCALITY_SELECTION    pcrExtendLocal;
#   TPM_LOCALITY_SELECTION    pcrResetLocal;
# } TPM_PCR_ATTRIBUTES;
class TPM_PCR_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrReset",        BOOLEAN),
    ("pcrExtendLocal",  TPM_LOCALITY_SELECTION),
    ("pcrResetLocal",   TPM_LOCALITY_SELECTION)
  ]

# 
# //
# // Part 2, section 9: Storage Structures
# //
# 
# ///
# /// Part 2, section 9.1: TPM_STORED_DATA
# ///   [size_is(sealInfoSize)] BYTE* sealInfo;
# ///   [size_is(encDataSize)] BYTE* encData;
# ///
# typedef struct tdTPM_STORED_DATA {
#   TPM_STRUCT_VER    ver;
#   UINT32            sealInfoSize;
#   UINT8             *sealInfo;
#   UINT32            encDataSize;
#   UINT8             *encData;
# } TPM_STORED_DATA;
class TPM_STORED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",           TPM_STRUCT_VER),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 9.2: TPM_STORED_DATA12
# ///   [size_is(sealInfoSize)] BYTE* sealInfo;
# ///   [size_is(encDataSize)] BYTE* encData;
# ///
# typedef struct tdTPM_STORED_DATA12 {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_ENTITY_TYPE      et;
#   UINT32               sealInfoSize;
#   UINT8                *sealInfo;
#   UINT32               encDataSize;
#   UINT8                *encData;
# } TPM_STORED_DATA12;
class TPM_STORED_DATA12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("et",            TPM_ENTITY_TYPE),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 9.3: TPM_SEALED_DATA
# ///   [size_is(dataSize)] BYTE* data;
# ///
# typedef struct tdTPM_SEALED_DATA {
#   TPM_PAYLOAD_TYPE    payload;
#   TPM_SECRET          authData;
#   TPM_NONCE           tpmProof;
#   TPM_DIGEST          storedDigest;
#   UINT32              dataSize;
#   UINT8               *data;
# } TPM_SEALED_DATA;
class TPM_SEALED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("authData",      TPM_SECRET),
    ("tpmProof",      TPM_NONCE),
    ("storedDigest",  TPM_DIGEST),
    ("dataSize",      UINT32),
    ("data",          POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 9.4: TPM_SYMMETRIC_KEY
# ///   [size_is(size)] BYTE* data;
# ///
# typedef struct tdTPM_SYMMETRIC_KEY {
#   TPM_ALGORITHM_ID    algId;
#   TPM_ENC_SCHEME      encScheme;
#   UINT16              dataSize;
#   UINT8               *data;
# } TPM_SYMMETRIC_KEY;
class TPM_SYMMETRIC_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algId",     TPM_ALGORITHM_ID),
    ("encScheme", TPM_ENC_SCHEME),
    ("dataSize",  UINT16),
    ("data",      POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 9.5: TPM_BOUND_DATA
# ///
# typedef struct tdTPM_BOUND_DATA {
#   TPM_STRUCT_VER      ver;
#   TPM_PAYLOAD_TYPE    payload;
#   UINT8               payloadData[1];
# } TPM_BOUND_DATA;
class TPM_BOUND_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",         TPM_STRUCT_VER),
    ("payload",     TPM_PAYLOAD_TYPE),
    ("payloadData", UINT8 * 1)
  ]


# //
# // Part 2 section 10: TPM_KEY complex
# //
# 
# //
# // Section 10.1, 10.4, and 10.5 have been defined previously
# //
# 
# ///
# /// Part 2, section 10.2: TPM_KEY
# ///   [size_is(encDataSize)] BYTE* encData;
# ///
# typedef struct tdTPM_KEY {
#   TPM_STRUCT_VER         ver;
#   TPM_KEY_USAGE          keyUsage;
#   TPM_KEY_FLAGS          keyFlags;
#   TPM_AUTH_DATA_USAGE    authDataUsage;
#   TPM_KEY_PARMS          algorithmParms;
#   UINT32                 PCRInfoSize;
#   UINT8                  *PCRInfo;
#   TPM_STORE_PUBKEY       pubKey;
#   UINT32                 encDataSize;
#   UINT8                  *encData;
# } TPM_KEY;
TPM_KEY._fields_ = [
    ("ver",             TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 10.3: TPM_KEY12
# ///   [size_is(encDataSize)] BYTE* encData;
# ///
# typedef struct tdTPM_KEY12 {
#   TPM_STRUCTURE_TAG      tag;
#   UINT16                 fill;
#   TPM_KEY_USAGE          keyUsage;
#   TPM_KEY_FLAGS          keyFlags;
#   TPM_AUTH_DATA_USAGE    authDataUsage;
#   TPM_KEY_PARMS          algorithmParms;
#   UINT32                 PCRInfoSize;
#   UINT8                  *PCRInfo;
#   TPM_STORE_PUBKEY       pubKey;
#   UINT32                 encDataSize;
#   UINT8                  *encData;
# } TPM_KEY12;
class TPM_KEY12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("fill",            UINT16),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 10.7: TPM_STORE_PRIVKEY
# ///   [size_is(keyLength)] BYTE* key;
# ///
# typedef struct tdTPM_STORE_PRIVKEY {
#   UINT32    keyLength;
#   UINT8     *key;
# } TPM_STORE_PRIVKEY;
class TPM_STORE_PRIVKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 10.6: TPM_STORE_ASYMKEY
# ///
# typedef struct tdTPM_STORE_ASYMKEY {
#   // pos len total
#   TPM_PAYLOAD_TYPE     payload;                     // 0    1   1
#   TPM_SECRET           usageAuth;                   // 1    20  21
#   TPM_SECRET           migrationAuth;               // 21   20  41
#   TPM_DIGEST           pubDataDigest;               // 41   20  61
#   TPM_STORE_PRIVKEY    privKey;                     // 61 132-151 193-214
# } TPM_STORE_ASYMKEY;
class TPM_STORE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("usageAuth",     TPM_SECRET),
    ("migrationAuth", TPM_SECRET),
    ("pubDataDigest", TPM_DIGEST),
    ("privKey",       TPM_STORE_PRIVKEY)
  ]

# 
# ///
# /// Part 2, section 10.8: TPM_MIGRATE_ASYMKEY
# ///   [size_is(partPrivKeyLen)] BYTE* partPrivKey;
# ///
# typedef struct tdTPM_MIGRATE_ASYMKEY {
#   // pos  len  total
#   TPM_PAYLOAD_TYPE    payload;                      //   0    1       1
#   TPM_SECRET          usageAuth;                    //   1   20      21
#   TPM_DIGEST          pubDataDigest;                //  21   20      41
#   UINT32              partPrivKeyLen;               //  41    4      45
#   UINT8               *partPrivKey;                 //  45 112-127 157-172
# } TPM_MIGRATE_ASYMKEY;
class TPM_MIGRATE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",         TPM_PAYLOAD_TYPE),
    ("usageAuth",       TPM_SECRET),
    ("pubDataDigest",   TPM_DIGEST),
    ("partPrivKeyLen",  UINT32),
    ("partPrivKey",     POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 10.9: TPM_KEY_CONTROL
# ///
# #define TPM_KEY_CONTROL_OWNER_EVICT  ((UINT32) 0x00000001)
TPM_KEY_CONTROL_OWNER_EVICT = 0x00000001

# 
# //
# // Part 2, section 11: Signed Structures
# //
# 
# ///
# /// Part 2, section 11.1: TPM_CERTIFY_INFO Structure
# ///
# typedef struct tdTPM_CERTIFY_INFO {
#   TPM_STRUCT_VER         version;
#   TPM_KEY_USAGE          keyUsage;
#   TPM_KEY_FLAGS          keyFlags;
#   TPM_AUTH_DATA_USAGE    authDataUsage;
#   TPM_KEY_PARMS          algorithmParms;
#   TPM_DIGEST             pubkeyDigest;
#   TPM_NONCE              data;
#   BOOLEAN                parentPCRStatus;
#   UINT32                 PCRInfoSize;
#   UINT8                  *PCRInfo;
# } TPM_CERTIFY_INFO;
class TPM_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",         TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubkeyDigest",    TPM_DIGEST),
    ("data",            TPM_NONCE),
    ("parentPCRStatus", BOOLEAN),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 11.2: TPM_CERTIFY_INFO2 Structure
# ///
# typedef struct tdTPM_CERTIFY_INFO2 {
#   TPM_STRUCTURE_TAG      tag;
#   UINT8                  fill;
#   TPM_PAYLOAD_TYPE       payloadType;
#   TPM_KEY_USAGE          keyUsage;
#   TPM_KEY_FLAGS          keyFlags;
#   TPM_AUTH_DATA_USAGE    authDataUsage;
#   TPM_KEY_PARMS          algorithmParms;
#   TPM_DIGEST             pubkeyDigest;
#   TPM_NONCE              data;
#   BOOLEAN                parentPCRStatus;
#   UINT32                 PCRInfoSize;
#   UINT8                  *PCRInfo;
#   UINT32                 migrationAuthoritySize;
#   UINT8                  *migrationAuthority;
# } TPM_CERTIFY_INFO2;
class TPM_CERTIFY_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                     TPM_STRUCTURE_TAG),
    ("fill",                    UINT8),
    ("payloadType",             TPM_PAYLOAD_TYPE),
    ("keyUsage",                TPM_KEY_USAGE),
    ("keyFlags",                TPM_KEY_FLAGS),
    ("authDataUsage",           TPM_AUTH_DATA_USAGE),
    ("algorithmParms",          TPM_KEY_PARMS),
    ("pubkeyDigest",            TPM_DIGEST),
    ("data",                    TPM_NONCE),
    ("parentPCRStatus",         BOOLEAN),
    ("PCRInfoSize",             UINT32),
    ("PCRInfo",                 POINTER(UINT8)),
    ("migrationAuthoritySize",  UINT32),
    ("migrationAuthority",      POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 11.3 TPM_QUOTE_INFO Structure
# ///
# typedef struct tdTPM_QUOTE_INFO {
#   TPM_STRUCT_VER        version;
#   UINT8                 fixed[4];
#   TPM_COMPOSITE_HASH    digestValue;
#   TPM_NONCE             externalData;
# } TPM_QUOTE_INFO;
class TPM_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",       TPM_STRUCT_VER),
    ("fixed",         UINT8 * 4),
    ("digestValue",   TPM_COMPOSITE_HASH),
    ("externalData",  TPM_NONCE)
  ]

# 
# ///
# /// Part 2, section 11.4 TPM_QUOTE_INFO2 Structure
# ///
# typedef struct tdTPM_QUOTE_INFO2 {
#   TPM_STRUCTURE_TAG     tag;
#   UINT8                 fixed[4];
#   TPM_NONCE             externalData;
#   TPM_PCR_INFO_SHORT    infoShort;
# } TPM_QUOTE_INFO2;
class TPM_QUOTE_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("fixed",         UINT8 * 4),
    ("externalData",  TPM_NONCE),
    ("infoShort",     TPM_PCR_INFO_SHORT)
  ]

# 
# //
# // Part 2, section 12: Identity Structures
# //
# 
# ///
# /// Part 2, section 12.1 TPM_EK_BLOB
# ///
# typedef struct tdTPM_EK_BLOB {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_EK_TYPE          ekType;
#   UINT32               blobSize;
#   UINT8                *blob;
# } TPM_EK_BLOB;
class TPM_EK_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("ekType",    TPM_EK_TYPE),
    ("blobSize",  UINT32),
    ("blob",      POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 12.2 TPM_EK_BLOB_ACTIVATE
# ///
# typedef struct tdTPM_EK_BLOB_ACTIVATE {
#   TPM_STRUCTURE_TAG     tag;
#   TPM_SYMMETRIC_KEY     sessionKey;
#   TPM_DIGEST            idDigest;
#   TPM_PCR_INFO_SHORT    pcrInfo;
# } TPM_EK_BLOB_ACTIVATE;
class TPM_EK_BLOB_ACTIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST),
    ("pcrInfo",     TPM_PCR_INFO_SHORT)
  ]

# 
# ///
# /// Part 2, section 12.3 TPM_EK_BLOB_AUTH
# ///
# typedef struct tdTPM_EK_BLOB_AUTH {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_SECRET           authValue;
# } TPM_EK_BLOB_AUTH;
class TPM_EK_BLOB_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("authValue",   TPM_SECRET)
  ]

# 
# ///
# /// Part 2, section 12.5 TPM_IDENTITY_CONTENTS
# ///
# typedef struct tdTPM_IDENTITY_CONTENTS {
#   TPM_STRUCT_VER       ver;
#   UINT32               ordinal;
#   TPM_CHOSENID_HASH    labelPrivCADigest;
#   TPM_PUBKEY           identityPubKey;
# } TPM_IDENTITY_CONTENTS;
class TPM_IDENTITY_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",               TPM_STRUCT_VER),
    ("ordinal",           UINT32),
    ("labelPrivCADigest", TPM_CHOSENID_HASH),
    ("identityPubKey",    TPM_PUBKEY)
  ]

# 
# ///
# /// Part 2, section 12.6 TPM_IDENTITY_REQ
# ///
# typedef struct tdTPM_IDENTITY_REQ {
#   UINT32           asymSize;
#   UINT32           symSize;
#   TPM_KEY_PARMS    asymAlgorithm;
#   TPM_KEY_PARMS    symAlgorithm;
#   UINT8            *asymBlob;
#   UINT8            *symBlob;
# } TPM_IDENTITY_REQ;
class TPM_IDENTITY_REQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymSize",      UINT32),
    ("symSize",       UINT32),
    ("asymAlgorithm", TPM_KEY_PARMS),
    ("symAlgorithm",  TPM_KEY_PARMS),
    ("asymBlob",      POINTER (UINT8)),
    ("symBlob",       POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 12.7 TPM_IDENTITY_PROOF
# ///
# typedef struct tdTPM_IDENTITY_PROOF {
#   TPM_STRUCT_VER    ver;
#   UINT32            labelSize;
#   UINT32            identityBindingSize;
#   UINT32            endorsementSize;
#   UINT32            platformSize;
#   UINT32            conformanceSize;
#   TPM_PUBKEY        identityKey;
#   UINT8             *labelArea;
#   UINT8             *identityBinding;
#   UINT8             *endorsementCredential;
#   UINT8             *platformCredential;
#   UINT8             *conformanceCredential;
# } TPM_IDENTITY_PROOF;
class TPM_IDENTITY_PROOF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",                   TPM_STRUCT_VER),
    ("labelSize",             UINT32),
    ("identityBindingSize",   UINT32),
    ("endorsementSize",       UINT32),
    ("platformSize",          UINT32),
    ("conformanceSize",       UINT32),
    ("identityKey",           TPM_PUBKEY),
    ("labelArea",             POINTER (UINT8)),
    ("identityBinding",       POINTER (UINT8)),
    ("endorsementCredential", POINTER (UINT8)),
    ("platformCredential",    POINTER (UINT8)),
    ("conformanceCredential", POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 12.8 TPM_ASYM_CA_CONTENTS
# ///
# typedef struct tdTPM_ASYM_CA_CONTENTS {
#   TPM_SYMMETRIC_KEY    sessionKey;
#   TPM_DIGEST           idDigest;
# } TPM_ASYM_CA_CONTENTS;
class TPM_ASYM_CA_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 12.9 TPM_SYM_CA_ATTESTATION
# ///
# typedef struct tdTPM_SYM_CA_ATTESTATION {
#   UINT32           credSize;
#   TPM_KEY_PARMS    algorithm;
#   UINT8            *credential;
# } TPM_SYM_CA_ATTESTATION;
class TPM_SYM_CA_ATTESTATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("credSize",    UINT32),
    ("algorithm",   TPM_KEY_PARMS),
    ("credential",  POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 15: Tick Structures
# ///   Placed here out of order because definitions are used in section 13.
# ///
# typedef struct tdTPM_CURRENT_TICKS {
#   TPM_STRUCTURE_TAG    tag;
#   UINT64               currentTicks;
#   UINT16               tickRate;
#   TPM_NONCE            tickNonce;
# } TPM_CURRENT_TICKS;
class TPM_CURRENT_TICKS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("currentTicks",  UINT64),
    ("tickRate",      UINT16),
    ("tickNonce",     TPM_NONCE)
  ]

# 
# ///
# /// Part 2, section 13: Transport structures
# ///
# 
# ///
# /// Part 2, section 13.1: TPM _TRANSPORT_PUBLIC
# ///
# typedef struct tdTPM_TRANSPORT_PUBLIC {
#   TPM_STRUCTURE_TAG           tag;
#   TPM_TRANSPORT_ATTRIBUTES    transAttributes;
#   TPM_ALGORITHM_ID            algId;
#   TPM_ENC_SCHEME              encScheme;
# } TPM_TRANSPORT_PUBLIC;
class TPM_TRANSPORT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("transAttributes", TPM_TRANSPORT_ATTRIBUTES),
    ("algId",           TPM_ALGORITHM_ID),
    ("encScheme",       TPM_ENC_SCHEME)
  ]

# 
# //
# // Part 2, section 13.1.1 TPM_TRANSPORT_ATTRIBUTES Definitions
# //
# #define TPM_TRANSPORT_ENCRYPT    ((UINT32)BIT0)
# #define TPM_TRANSPORT_LOG        ((UINT32)BIT1)
# #define TPM_TRANSPORT_EXCLUSIVE  ((UINT32)BIT2)
TPM_TRANSPORT_ENCRYPT       = BIT0
TPM_TRANSPORT_LOG           = BIT1
TPM_TRANSPORT_EXCLUSIVE     = BIT2

# 
# ///
# /// Part 2, section 13.2 TPM_TRANSPORT_INTERNAL
# ///
# typedef struct tdTPM_TRANSPORT_INTERNAL {
#   TPM_STRUCTURE_TAG       tag;
#   TPM_AUTHDATA            authData;
#   TPM_TRANSPORT_PUBLIC    transPublic;
#   TPM_TRANSHANDLE         transHandle;
#   TPM_NONCE               transNonceEven;
#   TPM_DIGEST              transDigest;
# } TPM_TRANSPORT_INTERNAL;
class TPM_TRANSPORT_INTERNAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("authData",        TPM_AUTHDATA),
    ("transPublic",     TPM_TRANSPORT_PUBLIC),
    ("transHandle",     TPM_TRANSHANDLE),
    ("transNonceEven",  TPM_NONCE),
    ("transDigest",     TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 13.3 TPM_TRANSPORT_LOG_IN structure
# ///
# typedef struct tdTPM_TRANSPORT_LOG_IN {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           parameters;
#   TPM_DIGEST           pubKeyHash;
# } TPM_TRANSPORT_LOG_IN;
class TPM_TRANSPORT_LOG_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("parameters",      TPM_DIGEST),
    ("pubKeyHash",      TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 13.4 TPM_TRANSPORT_LOG_OUT structure
# ///
# typedef struct tdTPM_TRANSPORT_LOG_OUT {
#   TPM_STRUCTURE_TAG         tag;
#   TPM_CURRENT_TICKS         currentTicks;
#   TPM_DIGEST                parameters;
#   TPM_MODIFIER_INDICATOR    locality;
# } TPM_TRANSPORT_LOG_OUT;
class TPM_TRANSPORT_LOG_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("currentTicks",    TPM_CURRENT_TICKS),
    ("parameters",      TPM_DIGEST),
    ("locality",        TPM_MODIFIER_INDICATOR)
  ]

# 
# ///
# /// Part 2, section 13.5 TPM_TRANSPORT_AUTH structure
# ///
# typedef struct tdTPM_TRANSPORT_AUTH {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_AUTHDATA         authData;
# } TPM_TRANSPORT_AUTH;
class TPM_TRANSPORT_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authData",  TPM_AUTHDATA)
  ]

# 
# //
# // Part 2, section 14: Audit Structures
# //
# 
# ///
# /// Part 2, section 14.1 TPM_AUDIT_EVENT_IN structure
# ///
# typedef struct tdTPM_AUDIT_EVENT_IN {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           inputParms;
#   TPM_COUNTER_VALUE    auditCount;
# } TPM_AUDIT_EVENT_IN;
class TPM_AUDIT_EVENT_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("inputParms",  TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE)
  ]

# 
# ///
# /// Part 2, section 14.2 TPM_AUDIT_EVENT_OUT structure
# ///
# typedef struct tdTPM_AUDIT_EVENT_OUT {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_COMMAND_CODE     ordinal;
#   TPM_DIGEST           outputParms;
#   TPM_COUNTER_VALUE    auditCount;
#   TPM_RESULT           returnCode;
# } TPM_AUDIT_EVENT_OUT;
class TPM_AUDIT_EVENT_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("ordinal",     TPM_COMMAND_CODE),
    ("outputParms", TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE),
    ("returnCode",  TPM_RESULT)
  ]

# 
# //
# // Part 2, section 16: Return Codes
# //
# 
# #define TPM_VENDOR_ERROR  TPM_Vendor_Specific32
# #define TPM_NON_FATAL     0x00000800
TPM_VENDOR_ERROR            = TPM_Vendor_Specific32
TPM_NON_FATAL               = 0x00000800
# 
# #define TPM_SUCCESS                 ((TPM_RESULT) TPM_BASE)
# #define TPM_AUTHFAIL                ((TPM_RESULT) (TPM_BASE + 1))
# #define TPM_BADINDEX                ((TPM_RESULT) (TPM_BASE + 2))
# #define TPM_BAD_PARAMETER           ((TPM_RESULT) (TPM_BASE + 3))
# #define TPM_AUDITFAILURE            ((TPM_RESULT) (TPM_BASE + 4))
# #define TPM_CLEAR_DISABLED          ((TPM_RESULT) (TPM_BASE + 5))
# #define TPM_DEACTIVATED             ((TPM_RESULT) (TPM_BASE + 6))
# #define TPM_DISABLED                ((TPM_RESULT) (TPM_BASE + 7))
# #define TPM_DISABLED_CMD            ((TPM_RESULT) (TPM_BASE + 8))
# #define TPM_FAIL                    ((TPM_RESULT) (TPM_BASE + 9))
# #define TPM_BAD_ORDINAL             ((TPM_RESULT) (TPM_BASE + 10))
# #define TPM_INSTALL_DISABLED        ((TPM_RESULT) (TPM_BASE + 11))
# #define TPM_INVALID_KEYHANDLE       ((TPM_RESULT) (TPM_BASE + 12))
# #define TPM_KEYNOTFOUND             ((TPM_RESULT) (TPM_BASE + 13))
# #define TPM_INAPPROPRIATE_ENC       ((TPM_RESULT) (TPM_BASE + 14))
# #define TPM_MIGRATEFAIL             ((TPM_RESULT) (TPM_BASE + 15))
# #define TPM_INVALID_PCR_INFO        ((TPM_RESULT) (TPM_BASE + 16))
# #define TPM_NOSPACE                 ((TPM_RESULT) (TPM_BASE + 17))
# #define TPM_NOSRK                   ((TPM_RESULT) (TPM_BASE + 18))
# #define TPM_NOTSEALED_BLOB          ((TPM_RESULT) (TPM_BASE + 19))
# #define TPM_OWNER_SET               ((TPM_RESULT) (TPM_BASE + 20))
# #define TPM_RESOURCES               ((TPM_RESULT) (TPM_BASE + 21))
# #define TPM_SHORTRANDOM             ((TPM_RESULT) (TPM_BASE + 22))
# #define TPM_SIZE                    ((TPM_RESULT) (TPM_BASE + 23))
# #define TPM_WRONGPCRVAL             ((TPM_RESULT) (TPM_BASE + 24))
# #define TPM_BAD_PARAM_SIZE          ((TPM_RESULT) (TPM_BASE + 25))
# #define TPM_SHA_THREAD              ((TPM_RESULT) (TPM_BASE + 26))
# #define TPM_SHA_ERROR               ((TPM_RESULT) (TPM_BASE + 27))
# #define TPM_FAILEDSELFTEST          ((TPM_RESULT) (TPM_BASE + 28))
# #define TPM_AUTH2FAIL               ((TPM_RESULT) (TPM_BASE + 29))
# #define TPM_BADTAG                  ((TPM_RESULT) (TPM_BASE + 30))
# #define TPM_IOERROR                 ((TPM_RESULT) (TPM_BASE + 31))
# #define TPM_ENCRYPT_ERROR           ((TPM_RESULT) (TPM_BASE + 32))
# #define TPM_DECRYPT_ERROR           ((TPM_RESULT) (TPM_BASE + 33))
# #define TPM_INVALID_AUTHHANDLE      ((TPM_RESULT) (TPM_BASE + 34))
# #define TPM_NO_ENDORSEMENT          ((TPM_RESULT) (TPM_BASE + 35))
# #define TPM_INVALID_KEYUSAGE        ((TPM_RESULT) (TPM_BASE + 36))
# #define TPM_WRONG_ENTITYTYPE        ((TPM_RESULT) (TPM_BASE + 37))
# #define TPM_INVALID_POSTINIT        ((TPM_RESULT) (TPM_BASE + 38))
# #define TPM_INAPPROPRIATE_SIG       ((TPM_RESULT) (TPM_BASE + 39))
# #define TPM_BAD_KEY_PROPERTY        ((TPM_RESULT) (TPM_BASE + 40))
# #define TPM_BAD_MIGRATION           ((TPM_RESULT) (TPM_BASE + 41))
# #define TPM_BAD_SCHEME              ((TPM_RESULT) (TPM_BASE + 42))
# #define TPM_BAD_DATASIZE            ((TPM_RESULT) (TPM_BASE + 43))
# #define TPM_BAD_MODE                ((TPM_RESULT) (TPM_BASE + 44))
# #define TPM_BAD_PRESENCE            ((TPM_RESULT) (TPM_BASE + 45))
# #define TPM_BAD_VERSION             ((TPM_RESULT) (TPM_BASE + 46))
# #define TPM_NO_WRAP_TRANSPORT       ((TPM_RESULT) (TPM_BASE + 47))
# #define TPM_AUDITFAIL_UNSUCCESSFUL  ((TPM_RESULT) (TPM_BASE + 48))
# #define TPM_AUDITFAIL_SUCCESSFUL    ((TPM_RESULT) (TPM_BASE + 49))
# #define TPM_NOTRESETABLE            ((TPM_RESULT) (TPM_BASE + 50))
# #define TPM_NOTLOCAL                ((TPM_RESULT) (TPM_BASE + 51))
# #define TPM_BAD_TYPE                ((TPM_RESULT) (TPM_BASE + 52))
# #define TPM_INVALID_RESOURCE        ((TPM_RESULT) (TPM_BASE + 53))
# #define TPM_NOTFIPS                 ((TPM_RESULT) (TPM_BASE + 54))
# #define TPM_INVALID_FAMILY          ((TPM_RESULT) (TPM_BASE + 55))
# #define TPM_NO_NV_PERMISSION        ((TPM_RESULT) (TPM_BASE + 56))
# #define TPM_REQUIRES_SIGN           ((TPM_RESULT) (TPM_BASE + 57))
# #define TPM_KEY_NOTSUPPORTED        ((TPM_RESULT) (TPM_BASE + 58))
# #define TPM_AUTH_CONFLICT           ((TPM_RESULT) (TPM_BASE + 59))
# #define TPM_AREA_LOCKED             ((TPM_RESULT) (TPM_BASE + 60))
# #define TPM_BAD_LOCALITY            ((TPM_RESULT) (TPM_BASE + 61))
# #define TPM_READ_ONLY               ((TPM_RESULT) (TPM_BASE + 62))
# #define TPM_PER_NOWRITE             ((TPM_RESULT) (TPM_BASE + 63))
# #define TPM_FAMILYCOUNT             ((TPM_RESULT) (TPM_BASE + 64))
# #define TPM_WRITE_LOCKED            ((TPM_RESULT) (TPM_BASE + 65))
# #define TPM_BAD_ATTRIBUTES          ((TPM_RESULT) (TPM_BASE + 66))
# #define TPM_INVALID_STRUCTURE       ((TPM_RESULT) (TPM_BASE + 67))
# #define TPM_KEY_OWNER_CONTROL       ((TPM_RESULT) (TPM_BASE + 68))
# #define TPM_BAD_COUNTER             ((TPM_RESULT) (TPM_BASE + 69))
# #define TPM_NOT_FULLWRITE           ((TPM_RESULT) (TPM_BASE + 70))
# #define TPM_CONTEXT_GAP             ((TPM_RESULT) (TPM_BASE + 71))
# #define TPM_MAXNVWRITES             ((TPM_RESULT) (TPM_BASE + 72))
# #define TPM_NOOPERATOR              ((TPM_RESULT) (TPM_BASE + 73))
# #define TPM_RESOURCEMISSING         ((TPM_RESULT) (TPM_BASE + 74))
# #define TPM_DELEGATE_LOCK           ((TPM_RESULT) (TPM_BASE + 75))
# #define TPM_DELEGATE_FAMILY         ((TPM_RESULT) (TPM_BASE + 76))
# #define TPM_DELEGATE_ADMIN          ((TPM_RESULT) (TPM_BASE + 77))
# #define TPM_TRANSPORT_NOTEXCLUSIVE  ((TPM_RESULT) (TPM_BASE + 78))
# #define TPM_OWNER_CONTROL           ((TPM_RESULT) (TPM_BASE + 79))
# #define TPM_DAA_RESOURCES           ((TPM_RESULT) (TPM_BASE + 80))
# #define TPM_DAA_INPUT_DATA0         ((TPM_RESULT) (TPM_BASE + 81))
# #define TPM_DAA_INPUT_DATA1         ((TPM_RESULT) (TPM_BASE + 82))
# #define TPM_DAA_ISSUER_SETTINGS     ((TPM_RESULT) (TPM_BASE + 83))
# #define TPM_DAA_TPM_SETTINGS        ((TPM_RESULT) (TPM_BASE + 84))
# #define TPM_DAA_STAGE               ((TPM_RESULT) (TPM_BASE + 85))
# #define TPM_DAA_ISSUER_VALIDITY     ((TPM_RESULT) (TPM_BASE + 86))
# #define TPM_DAA_WRONG_W             ((TPM_RESULT) (TPM_BASE + 87))
# #define TPM_BAD_HANDLE              ((TPM_RESULT) (TPM_BASE + 88))
# #define TPM_BAD_DELEGATE            ((TPM_RESULT) (TPM_BASE + 89))
# #define TPM_BADCONTEXT              ((TPM_RESULT) (TPM_BASE + 90))
# #define TPM_TOOMANYCONTEXTS         ((TPM_RESULT) (TPM_BASE + 91))
# #define TPM_MA_TICKET_SIGNATURE     ((TPM_RESULT) (TPM_BASE + 92))
# #define TPM_MA_DESTINATION          ((TPM_RESULT) (TPM_BASE + 93))
# #define TPM_MA_SOURCE               ((TPM_RESULT) (TPM_BASE + 94))
# #define TPM_MA_AUTHORITY            ((TPM_RESULT) (TPM_BASE + 95))
# #define TPM_PERMANENTEK             ((TPM_RESULT) (TPM_BASE + 97))
# #define TPM_BAD_SIGNATURE           ((TPM_RESULT) (TPM_BASE + 98))
# #define TPM_NOCONTEXTSPACE          ((TPM_RESULT) (TPM_BASE + 99))
TPM_SUCCESS                 = TPM_BASE
TPM_AUTHFAIL                = TPM_BASE + 1
TPM_BADINDEX                = TPM_BASE + 2
TPM_BAD_PARAMETER           = TPM_BASE + 3
TPM_AUDITFAILURE            = TPM_BASE + 4
TPM_CLEAR_DISABLED          = TPM_BASE + 5
TPM_DEACTIVATED             = TPM_BASE + 6
TPM_DISABLED                = TPM_BASE + 7
TPM_DISABLED_CMD            = TPM_BASE + 8
TPM_FAIL                    = TPM_BASE + 9
TPM_BAD_ORDINAL             = TPM_BASE + 10
TPM_INSTALL_DISABLED        = TPM_BASE + 11
TPM_INVALID_KEYHANDLE       = TPM_BASE + 12
TPM_KEYNOTFOUND             = TPM_BASE + 13
TPM_INAPPROPRIATE_ENC       = TPM_BASE + 14
TPM_MIGRATEFAIL             = TPM_BASE + 15
TPM_INVALID_PCR_INFO        = TPM_BASE + 16
TPM_NOSPACE                 = TPM_BASE + 17
TPM_NOSRK                   = TPM_BASE + 18
TPM_NOTSEALED_BLOB          = TPM_BASE + 19
TPM_OWNER_SET               = TPM_BASE + 20
TPM_RESOURCES               = TPM_BASE + 21
TPM_SHORTRANDOM             = TPM_BASE + 22
TPM_SIZE                    = TPM_BASE + 23
TPM_WRONGPCRVAL             = TPM_BASE + 24
TPM_BAD_PARAM_SIZE          = TPM_BASE + 25
TPM_SHA_THREAD              = TPM_BASE + 26
TPM_SHA_ERROR               = TPM_BASE + 27
TPM_FAILEDSELFTEST          = TPM_BASE + 28
TPM_AUTH2FAIL               = TPM_BASE + 29
TPM_BADTAG                  = TPM_BASE + 30
TPM_IOERROR                 = TPM_BASE + 31
TPM_ENCRYPT_ERROR           = TPM_BASE + 32
TPM_DECRYPT_ERROR           = TPM_BASE + 33
TPM_INVALID_AUTHHANDLE      = TPM_BASE + 34
TPM_NO_ENDORSEMENT          = TPM_BASE + 35
TPM_INVALID_KEYUSAGE        = TPM_BASE + 36
TPM_WRONG_ENTITYTYPE        = TPM_BASE + 37
TPM_INVALID_POSTINIT        = TPM_BASE + 38
TPM_INAPPROPRIATE_SIG       = TPM_BASE + 39
TPM_BAD_KEY_PROPERTY        = TPM_BASE + 40
TPM_BAD_MIGRATION           = TPM_BASE + 41
TPM_BAD_SCHEME              = TPM_BASE + 42
TPM_BAD_DATASIZE            = TPM_BASE + 43
TPM_BAD_MODE                = TPM_BASE + 44
TPM_BAD_PRESENCE            = TPM_BASE + 45
TPM_BAD_VERSION             = TPM_BASE + 46
TPM_NO_WRAP_TRANSPORT       = TPM_BASE + 47
TPM_AUDITFAIL_UNSUCCESSFUL  = TPM_BASE + 48
TPM_AUDITFAIL_SUCCESSFUL    = TPM_BASE + 49
TPM_NOTRESETABLE            = TPM_BASE + 50
TPM_NOTLOCAL                = TPM_BASE + 51
TPM_BAD_TYPE                = TPM_BASE + 52
TPM_INVALID_RESOURCE        = TPM_BASE + 53
TPM_NOTFIPS                 = TPM_BASE + 54
TPM_INVALID_FAMILY          = TPM_BASE + 55
TPM_NO_NV_PERMISSION        = TPM_BASE + 56
TPM_REQUIRES_SIGN           = TPM_BASE + 57
TPM_KEY_NOTSUPPORTED        = TPM_BASE + 58
TPM_AUTH_CONFLICT           = TPM_BASE + 59
TPM_AREA_LOCKED             = TPM_BASE + 60
TPM_BAD_LOCALITY            = TPM_BASE + 61
TPM_READ_ONLY               = TPM_BASE + 62
TPM_PER_NOWRITE             = TPM_BASE + 63
TPM_FAMILYCOUNT             = TPM_BASE + 64
TPM_WRITE_LOCKED            = TPM_BASE + 65
TPM_BAD_ATTRIBUTES          = TPM_BASE + 66
TPM_INVALID_STRUCTURE       = TPM_BASE + 67
TPM_KEY_OWNER_CONTROL       = TPM_BASE + 68
TPM_BAD_COUNTER             = TPM_BASE + 69
TPM_NOT_FULLWRITE           = TPM_BASE + 70
TPM_CONTEXT_GAP             = TPM_BASE + 71
TPM_MAXNVWRITES             = TPM_BASE + 72
TPM_NOOPERATOR              = TPM_BASE + 73
TPM_RESOURCEMISSING         = TPM_BASE + 74
TPM_DELEGATE_LOCK           = TPM_BASE + 75
TPM_DELEGATE_FAMILY         = TPM_BASE + 76
TPM_DELEGATE_ADMIN          = TPM_BASE + 77
TPM_TRANSPORT_NOTEXCLUSIVE  = TPM_BASE + 78
TPM_OWNER_CONTROL           = TPM_BASE + 79
TPM_DAA_RESOURCES           = TPM_BASE + 80
TPM_DAA_INPUT_DATA0         = TPM_BASE + 81
TPM_DAA_INPUT_DATA1         = TPM_BASE + 82
TPM_DAA_ISSUER_SETTINGS     = TPM_BASE + 83
TPM_DAA_TPM_SETTINGS        = TPM_BASE + 84
TPM_DAA_STAGE               = TPM_BASE + 85
TPM_DAA_ISSUER_VALIDITY     = TPM_BASE + 86
TPM_DAA_WRONG_W             = TPM_BASE + 87
TPM_BAD_HANDLE              = TPM_BASE + 88
TPM_BAD_DELEGATE            = TPM_BASE + 89
TPM_BADCONTEXT              = TPM_BASE + 90
TPM_TOOMANYCONTEXTS         = TPM_BASE + 91
TPM_MA_TICKET_SIGNATURE     = TPM_BASE + 92
TPM_MA_DESTINATION          = TPM_BASE + 93
TPM_MA_SOURCE               = TPM_BASE + 94
TPM_MA_AUTHORITY            = TPM_BASE + 95
TPM_PERMANENTEK             = TPM_BASE + 97
TPM_BAD_SIGNATURE           = TPM_BASE + 98
TPM_NOCONTEXTSPACE          = TPM_BASE + 99

# 
# #define TPM_RETRY                ((TPM_RESULT) (TPM_BASE + TPM_NON_FATAL))
# #define TPM_NEEDS_SELFTEST       ((TPM_RESULT) (TPM_BASE + TPM_NON_FATAL + 1))
# #define TPM_DOING_SELFTEST       ((TPM_RESULT) (TPM_BASE + TPM_NON_FATAL + 2))
# #define TPM_DEFEND_LOCK_RUNNING  ((TPM_RESULT) (TPM_BASE + TPM_NON_FATAL + 3))
TPM_RETRY                   = TPM_BASE + TPM_NON_FATAL
TPM_NEEDS_SELFTEST          = TPM_BASE + TPM_NON_FATAL + 1
TPM_DOING_SELFTEST          = TPM_BASE + TPM_NON_FATAL + 2
TPM_DEFEND_LOCK_RUNNING     = TPM_BASE + TPM_NON_FATAL + 3

# 
# //
# // Part 2, section 17: Ordinals
# //
# // Ordinals are 32 bit values. The upper byte contains values that serve as
# // flag indicators, the next byte contains values indicating what committee
# // designated the ordinal, and the final two bytes contain the Command
# // Ordinal Index.
# //      3                   2                   1
# //    1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
# //   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# //   |P|C|V| Reserved| Purview |     Command Ordinal Index           |
# //   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# //
# //  Where:
# //
# //    * P is Protected/Unprotected command. When 0 the command is a Protected
# //      command, when 1 the command is an Unprotected command.
# //
# //    * C is Non-Connection/Connection related command. When 0 this command
# //      passes through to either the protected (TPM) or unprotected (TSS)
# //      components.
# //
# //    * V is TPM/Vendor command. When 0 the command is TPM defined, when 1 the
# //      command is vendor defined.
# //
# //    * All reserved area bits are set to 0.
# //
# 
# #define TPM_ORD_ActivateIdentity                ((TPM_COMMAND_CODE) 0x0000007A)
# #define TPM_ORD_AuthorizeMigrationKey           ((TPM_COMMAND_CODE) 0x0000002B)
# #define TPM_ORD_CertifyKey                      ((TPM_COMMAND_CODE) 0x00000032)
# #define TPM_ORD_CertifyKey2                     ((TPM_COMMAND_CODE) 0x00000033)
# #define TPM_ORD_CertifySelfTest                 ((TPM_COMMAND_CODE) 0x00000052)
# #define TPM_ORD_ChangeAuth                      ((TPM_COMMAND_CODE) 0x0000000C)
# #define TPM_ORD_ChangeAuthAsymFinish            ((TPM_COMMAND_CODE) 0x0000000F)
# #define TPM_ORD_ChangeAuthAsymStart             ((TPM_COMMAND_CODE) 0x0000000E)
# #define TPM_ORD_ChangeAuthOwner                 ((TPM_COMMAND_CODE) 0x00000010)
# #define TPM_ORD_CMK_ApproveMA                   ((TPM_COMMAND_CODE) 0x0000001D)
# #define TPM_ORD_CMK_ConvertMigration            ((TPM_COMMAND_CODE) 0x00000024)
# #define TPM_ORD_CMK_CreateBlob                  ((TPM_COMMAND_CODE) 0x0000001B)
# #define TPM_ORD_CMK_CreateKey                   ((TPM_COMMAND_CODE) 0x00000013)
# #define TPM_ORD_CMK_CreateTicket                ((TPM_COMMAND_CODE) 0x00000012)
# #define TPM_ORD_CMK_SetRestrictions             ((TPM_COMMAND_CODE) 0x0000001C)
# #define TPM_ORD_ContinueSelfTest                ((TPM_COMMAND_CODE) 0x00000053)
# #define TPM_ORD_ConvertMigrationBlob            ((TPM_COMMAND_CODE) 0x0000002A)
# #define TPM_ORD_CreateCounter                   ((TPM_COMMAND_CODE) 0x000000DC)
# #define TPM_ORD_CreateEndorsementKeyPair        ((TPM_COMMAND_CODE) 0x00000078)
# #define TPM_ORD_CreateMaintenanceArchive        ((TPM_COMMAND_CODE) 0x0000002C)
# #define TPM_ORD_CreateMigrationBlob             ((TPM_COMMAND_CODE) 0x00000028)
# #define TPM_ORD_CreateRevocableEK               ((TPM_COMMAND_CODE) 0x0000007F)
# #define TPM_ORD_CreateWrapKey                   ((TPM_COMMAND_CODE) 0x0000001F)
# #define TPM_ORD_DAA_JOIN                        ((TPM_COMMAND_CODE) 0x00000029)
# #define TPM_ORD_DAA_SIGN                        ((TPM_COMMAND_CODE) 0x00000031)
# #define TPM_ORD_Delegate_CreateKeyDelegation    ((TPM_COMMAND_CODE) 0x000000D4)
# #define TPM_ORD_Delegate_CreateOwnerDelegation  ((TPM_COMMAND_CODE) 0x000000D5)
# #define TPM_ORD_Delegate_LoadOwnerDelegation    ((TPM_COMMAND_CODE) 0x000000D8)
# #define TPM_ORD_Delegate_Manage                 ((TPM_COMMAND_CODE) 0x000000D2)
# #define TPM_ORD_Delegate_ReadTable              ((TPM_COMMAND_CODE) 0x000000DB)
# #define TPM_ORD_Delegate_UpdateVerification     ((TPM_COMMAND_CODE) 0x000000D1)
# #define TPM_ORD_Delegate_VerifyDelegation       ((TPM_COMMAND_CODE) 0x000000D6)
# #define TPM_ORD_DirRead                         ((TPM_COMMAND_CODE) 0x0000001A)
# #define TPM_ORD_DirWriteAuth                    ((TPM_COMMAND_CODE) 0x00000019)
# #define TPM_ORD_DisableForceClear               ((TPM_COMMAND_CODE) 0x0000005E)
# #define TPM_ORD_DisableOwnerClear               ((TPM_COMMAND_CODE) 0x0000005C)
# #define TPM_ORD_DisablePubekRead                ((TPM_COMMAND_CODE) 0x0000007E)
# #define TPM_ORD_DSAP                            ((TPM_COMMAND_CODE) 0x00000011)
# #define TPM_ORD_EstablishTransport              ((TPM_COMMAND_CODE) 0x000000E6)
# #define TPM_ORD_EvictKey                        ((TPM_COMMAND_CODE) 0x00000022)
# #define TPM_ORD_ExecuteTransport                ((TPM_COMMAND_CODE) 0x000000E7)
# #define TPM_ORD_Extend                          ((TPM_COMMAND_CODE) 0x00000014)
# #define TPM_ORD_FieldUpgrade                    ((TPM_COMMAND_CODE) 0x000000AA)
# #define TPM_ORD_FlushSpecific                   ((TPM_COMMAND_CODE) 0x000000BA)
# #define TPM_ORD_ForceClear                      ((TPM_COMMAND_CODE) 0x0000005D)
# #define TPM_ORD_GetAuditDigest                  ((TPM_COMMAND_CODE) 0x00000085)
# #define TPM_ORD_GetAuditDigestSigned            ((TPM_COMMAND_CODE) 0x00000086)
# #define TPM_ORD_GetAuditEvent                   ((TPM_COMMAND_CODE) 0x00000082)
# #define TPM_ORD_GetAuditEventSigned             ((TPM_COMMAND_CODE) 0x00000083)
# #define TPM_ORD_GetCapability                   ((TPM_COMMAND_CODE) 0x00000065)
# #define TPM_ORD_GetCapabilityOwner              ((TPM_COMMAND_CODE) 0x00000066)
# #define TPM_ORD_GetCapabilitySigned             ((TPM_COMMAND_CODE) 0x00000064)
# #define TPM_ORD_GetOrdinalAuditStatus           ((TPM_COMMAND_CODE) 0x0000008C)
# #define TPM_ORD_GetPubKey                       ((TPM_COMMAND_CODE) 0x00000021)
# #define TPM_ORD_GetRandom                       ((TPM_COMMAND_CODE) 0x00000046)
# #define TPM_ORD_GetTestResult                   ((TPM_COMMAND_CODE) 0x00000054)
# #define TPM_ORD_GetTicks                        ((TPM_COMMAND_CODE) 0x000000F1)
# #define TPM_ORD_IncrementCounter                ((TPM_COMMAND_CODE) 0x000000DD)
# #define TPM_ORD_Init                            ((TPM_COMMAND_CODE) 0x00000097)
# #define TPM_ORD_KeyControlOwner                 ((TPM_COMMAND_CODE) 0x00000023)
# #define TPM_ORD_KillMaintenanceFeature          ((TPM_COMMAND_CODE) 0x0000002E)
# #define TPM_ORD_LoadAuthContext                 ((TPM_COMMAND_CODE) 0x000000B7)
# #define TPM_ORD_LoadContext                     ((TPM_COMMAND_CODE) 0x000000B9)
# #define TPM_ORD_LoadKey                         ((TPM_COMMAND_CODE) 0x00000020)
# #define TPM_ORD_LoadKey2                        ((TPM_COMMAND_CODE) 0x00000041)
# #define TPM_ORD_LoadKeyContext                  ((TPM_COMMAND_CODE) 0x000000B5)
# #define TPM_ORD_LoadMaintenanceArchive          ((TPM_COMMAND_CODE) 0x0000002D)
# #define TPM_ORD_LoadManuMaintPub                ((TPM_COMMAND_CODE) 0x0000002F)
# #define TPM_ORD_MakeIdentity                    ((TPM_COMMAND_CODE) 0x00000079)
# #define TPM_ORD_MigrateKey                      ((TPM_COMMAND_CODE) 0x00000025)
# #define TPM_ORD_NV_DefineSpace                  ((TPM_COMMAND_CODE) 0x000000CC)
# #define TPM_ORD_NV_ReadValue                    ((TPM_COMMAND_CODE) 0x000000CF)
# #define TPM_ORD_NV_ReadValueAuth                ((TPM_COMMAND_CODE) 0x000000D0)
# #define TPM_ORD_NV_WriteValue                   ((TPM_COMMAND_CODE) 0x000000CD)
# #define TPM_ORD_NV_WriteValueAuth               ((TPM_COMMAND_CODE) 0x000000CE)
# #define TPM_ORD_OIAP                            ((TPM_COMMAND_CODE) 0x0000000A)
# #define TPM_ORD_OSAP                            ((TPM_COMMAND_CODE) 0x0000000B)
# #define TPM_ORD_OwnerClear                      ((TPM_COMMAND_CODE) 0x0000005B)
# #define TPM_ORD_OwnerReadInternalPub            ((TPM_COMMAND_CODE) 0x00000081)
# #define TPM_ORD_OwnerReadPubek                  ((TPM_COMMAND_CODE) 0x0000007D)
# #define TPM_ORD_OwnerSetDisable                 ((TPM_COMMAND_CODE) 0x0000006E)
# #define TPM_ORD_PCR_Reset                       ((TPM_COMMAND_CODE) 0x000000C8)
# #define TPM_ORD_PcrRead                         ((TPM_COMMAND_CODE) 0x00000015)
# #define TPM_ORD_PhysicalDisable                 ((TPM_COMMAND_CODE) 0x00000070)
# #define TPM_ORD_PhysicalEnable                  ((TPM_COMMAND_CODE) 0x0000006F)
# #define TPM_ORD_PhysicalSetDeactivated          ((TPM_COMMAND_CODE) 0x00000072)
# #define TPM_ORD_Quote                           ((TPM_COMMAND_CODE) 0x00000016)
# #define TPM_ORD_Quote2                          ((TPM_COMMAND_CODE) 0x0000003E)
# #define TPM_ORD_ReadCounter                     ((TPM_COMMAND_CODE) 0x000000DE)
# #define TPM_ORD_ReadManuMaintPub                ((TPM_COMMAND_CODE) 0x00000030)
# #define TPM_ORD_ReadPubek                       ((TPM_COMMAND_CODE) 0x0000007C)
# #define TPM_ORD_ReleaseCounter                  ((TPM_COMMAND_CODE) 0x000000DF)
# #define TPM_ORD_ReleaseCounterOwner             ((TPM_COMMAND_CODE) 0x000000E0)
# #define TPM_ORD_ReleaseTransportSigned          ((TPM_COMMAND_CODE) 0x000000E8)
# #define TPM_ORD_Reset                           ((TPM_COMMAND_CODE) 0x0000005A)
# #define TPM_ORD_ResetLockValue                  ((TPM_COMMAND_CODE) 0x00000040)
# #define TPM_ORD_RevokeTrust                     ((TPM_COMMAND_CODE) 0x00000080)
# #define TPM_ORD_SaveAuthContext                 ((TPM_COMMAND_CODE) 0x000000B6)
# #define TPM_ORD_SaveContext                     ((TPM_COMMAND_CODE) 0x000000B8)
# #define TPM_ORD_SaveKeyContext                  ((TPM_COMMAND_CODE) 0x000000B4)
# #define TPM_ORD_SaveState                       ((TPM_COMMAND_CODE) 0x00000098)
# #define TPM_ORD_Seal                            ((TPM_COMMAND_CODE) 0x00000017)
# #define TPM_ORD_Sealx                           ((TPM_COMMAND_CODE) 0x0000003D)
# #define TPM_ORD_SelfTestFull                    ((TPM_COMMAND_CODE) 0x00000050)
# #define TPM_ORD_SetCapability                   ((TPM_COMMAND_CODE) 0x0000003F)
# #define TPM_ORD_SetOperatorAuth                 ((TPM_COMMAND_CODE) 0x00000074)
# #define TPM_ORD_SetOrdinalAuditStatus           ((TPM_COMMAND_CODE) 0x0000008D)
# #define TPM_ORD_SetOwnerInstall                 ((TPM_COMMAND_CODE) 0x00000071)
# #define TPM_ORD_SetOwnerPointer                 ((TPM_COMMAND_CODE) 0x00000075)
# #define TPM_ORD_SetRedirection                  ((TPM_COMMAND_CODE) 0x0000009A)
# #define TPM_ORD_SetTempDeactivated              ((TPM_COMMAND_CODE) 0x00000073)
# #define TPM_ORD_SHA1Complete                    ((TPM_COMMAND_CODE) 0x000000A2)
# #define TPM_ORD_SHA1CompleteExtend              ((TPM_COMMAND_CODE) 0x000000A3)
# #define TPM_ORD_SHA1Start                       ((TPM_COMMAND_CODE) 0x000000A0)
# #define TPM_ORD_SHA1Update                      ((TPM_COMMAND_CODE) 0x000000A1)
# #define TPM_ORD_Sign                            ((TPM_COMMAND_CODE) 0x0000003C)
# #define TPM_ORD_Startup                         ((TPM_COMMAND_CODE) 0x00000099)
# #define TPM_ORD_StirRandom                      ((TPM_COMMAND_CODE) 0x00000047)
# #define TPM_ORD_TakeOwnership                   ((TPM_COMMAND_CODE) 0x0000000D)
# #define TPM_ORD_Terminate_Handle                ((TPM_COMMAND_CODE) 0x00000096)
# #define TPM_ORD_TickStampBlob                   ((TPM_COMMAND_CODE) 0x000000F2)
# #define TPM_ORD_UnBind                          ((TPM_COMMAND_CODE) 0x0000001E)
# #define TPM_ORD_Unseal                          ((TPM_COMMAND_CODE) 0x00000018)
# #define TSC_ORD_PhysicalPresence                ((TPM_COMMAND_CODE) 0x4000000A)
# #define TSC_ORD_ResetEstablishmentBit           ((TPM_COMMAND_CODE) 0x4000000B)
TPM_ORD_ActivateIdentity                  = 0x0000007A
TPM_ORD_AuthorizeMigrationKey             = 0x0000002B
TPM_ORD_CertifyKey                        = 0x00000032
TPM_ORD_CertifyKey2                       = 0x00000033
TPM_ORD_CertifySelfTest                   = 0x00000052
TPM_ORD_ChangeAuth                        = 0x0000000C
TPM_ORD_ChangeAuthAsymFinish              = 0x0000000F
TPM_ORD_ChangeAuthAsymStart               = 0x0000000E
TPM_ORD_ChangeAuthOwner                   = 0x00000010
TPM_ORD_CMK_ApproveMA                     = 0x0000001D
TPM_ORD_CMK_ConvertMigration              = 0x00000024
TPM_ORD_CMK_CreateBlob                    = 0x0000001B
TPM_ORD_CMK_CreateKey                     = 0x00000013
TPM_ORD_CMK_CreateTicket                  = 0x00000012
TPM_ORD_CMK_SetRestrictions               = 0x0000001C
TPM_ORD_ContinueSelfTest                  = 0x00000053
TPM_ORD_ConvertMigrationBlob              = 0x0000002A
TPM_ORD_CreateCounter                     = 0x000000DC
TPM_ORD_CreateEndorsementKeyPair          = 0x00000078
TPM_ORD_CreateMaintenanceArchive          = 0x0000002C
TPM_ORD_CreateMigrationBlob               = 0x00000028
TPM_ORD_CreateRevocableEK                 = 0x0000007F
TPM_ORD_CreateWrapKey                     = 0x0000001F
TPM_ORD_DAA_JOIN                          = 0x00000029
TPM_ORD_DAA_SIGN                          = 0x00000031
TPM_ORD_Delegate_CreateKeyDelegation      = 0x000000D4
TPM_ORD_Delegate_CreateOwnerDelegation    = 0x000000D5
TPM_ORD_Delegate_LoadOwnerDelegation      = 0x000000D8
TPM_ORD_Delegate_Manage                   = 0x000000D2
TPM_ORD_Delegate_ReadTable                = 0x000000DB
TPM_ORD_Delegate_UpdateVerification       = 0x000000D1
TPM_ORD_Delegate_VerifyDelegation         = 0x000000D6
TPM_ORD_DirRead                           = 0x0000001A
TPM_ORD_DirWriteAuth                      = 0x00000019
TPM_ORD_DisableForceClear                 = 0x0000005E
TPM_ORD_DisableOwnerClear                 = 0x0000005C
TPM_ORD_DisablePubekRead                  = 0x0000007E
TPM_ORD_DSAP                              = 0x00000011
TPM_ORD_EstablishTransport                = 0x000000E6
TPM_ORD_EvictKey                          = 0x00000022
TPM_ORD_ExecuteTransport                  = 0x000000E7
TPM_ORD_Extend                            = 0x00000014
TPM_ORD_FieldUpgrade                      = 0x000000AA
TPM_ORD_FlushSpecific                     = 0x000000BA
TPM_ORD_ForceClear                        = 0x0000005D
TPM_ORD_GetAuditDigest                    = 0x00000085
TPM_ORD_GetAuditDigestSigned              = 0x00000086
TPM_ORD_GetAuditEvent                     = 0x00000082
TPM_ORD_GetAuditEventSigned               = 0x00000083
TPM_ORD_GetCapability                     = 0x00000065
TPM_ORD_GetCapabilityOwner                = 0x00000066
TPM_ORD_GetCapabilitySigned               = 0x00000064
TPM_ORD_GetOrdinalAuditStatus             = 0x0000008C
TPM_ORD_GetPubKey                         = 0x00000021
TPM_ORD_GetRandom                         = 0x00000046
TPM_ORD_GetTestResult                     = 0x00000054
TPM_ORD_GetTicks                          = 0x000000F1
TPM_ORD_IncrementCounter                  = 0x000000DD
TPM_ORD_Init                              = 0x00000097
TPM_ORD_KeyControlOwner                   = 0x00000023
TPM_ORD_KillMaintenanceFeature            = 0x0000002E
TPM_ORD_LoadAuthContext                   = 0x000000B7
TPM_ORD_LoadContext                       = 0x000000B9
TPM_ORD_LoadKey                           = 0x00000020
TPM_ORD_LoadKey2                          = 0x00000041
TPM_ORD_LoadKeyContext                    = 0x000000B5
TPM_ORD_LoadMaintenanceArchive            = 0x0000002D
TPM_ORD_LoadManuMaintPub                  = 0x0000002F
TPM_ORD_MakeIdentity                      = 0x00000079
TPM_ORD_MigrateKey                        = 0x00000025
TPM_ORD_NV_DefineSpace                    = 0x000000CC
TPM_ORD_NV_ReadValue                      = 0x000000CF
TPM_ORD_NV_ReadValueAuth                  = 0x000000D0
TPM_ORD_NV_WriteValue                     = 0x000000CD
TPM_ORD_NV_WriteValueAuth                 = 0x000000CE
TPM_ORD_OIAP                              = 0x0000000A
TPM_ORD_OSAP                              = 0x0000000B
TPM_ORD_OwnerClear                        = 0x0000005B
TPM_ORD_OwnerReadInternalPub              = 0x00000081
TPM_ORD_OwnerReadPubek                    = 0x0000007D
TPM_ORD_OwnerSetDisable                   = 0x0000006E
TPM_ORD_PCR_Reset                         = 0x000000C8
TPM_ORD_PcrRead                           = 0x00000015
TPM_ORD_PhysicalDisable                   = 0x00000070
TPM_ORD_PhysicalEnable                    = 0x0000006F
TPM_ORD_PhysicalSetDeactivated            = 0x00000072
TPM_ORD_Quote                             = 0x00000016
TPM_ORD_Quote2                            = 0x0000003E
TPM_ORD_ReadCounter                       = 0x000000DE
TPM_ORD_ReadManuMaintPub                  = 0x00000030
TPM_ORD_ReadPubek                         = 0x0000007C
TPM_ORD_ReleaseCounter                    = 0x000000DF
TPM_ORD_ReleaseCounterOwner               = 0x000000E0
TPM_ORD_ReleaseTransportSigned            = 0x000000E8
TPM_ORD_Reset                             = 0x0000005A
TPM_ORD_ResetLockValue                    = 0x00000040
TPM_ORD_RevokeTrust                       = 0x00000080
TPM_ORD_SaveAuthContext                   = 0x000000B6
TPM_ORD_SaveContext                       = 0x000000B8
TPM_ORD_SaveKeyContext                    = 0x000000B4
TPM_ORD_SaveState                         = 0x00000098
TPM_ORD_Seal                              = 0x00000017
TPM_ORD_Sealx                             = 0x0000003D
TPM_ORD_SelfTestFull                      = 0x00000050
TPM_ORD_SetCapability                     = 0x0000003F
TPM_ORD_SetOperatorAuth                   = 0x00000074
TPM_ORD_SetOrdinalAuditStatus             = 0x0000008D
TPM_ORD_SetOwnerInstall                   = 0x00000071
TPM_ORD_SetOwnerPointer                   = 0x00000075
TPM_ORD_SetRedirection                    = 0x0000009A
TPM_ORD_SetTempDeactivated                = 0x00000073
TPM_ORD_SHA1Complete                      = 0x000000A2
TPM_ORD_SHA1CompleteExtend                = 0x000000A3
TPM_ORD_SHA1Start                         = 0x000000A0
TPM_ORD_SHA1Update                        = 0x000000A1
TPM_ORD_Sign                              = 0x0000003C
TPM_ORD_Startup                           = 0x00000099
TPM_ORD_StirRandom                        = 0x00000047
TPM_ORD_TakeOwnership                     = 0x0000000D
TPM_ORD_Terminate_Handle                  = 0x00000096
TPM_ORD_TickStampBlob                     = 0x000000F2
TPM_ORD_UnBind                            = 0x0000001E
TPM_ORD_Unseal                            = 0x00000018
TSC_ORD_PhysicalPresence                  = 0x4000000A
TSC_ORD_ResetEstablishmentBit             = 0x4000000B

# 
# //
# // Part 2, section 18: Context structures
# //
# 
# ///
# /// Part 2, section 18.1: TPM_CONTEXT_BLOB
# ///
# typedef struct tdTPM_CONTEXT_BLOB {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_RESOURCE_TYPE    resourceType;
#   TPM_HANDLE           handle;
#   UINT8                label[16];
#   UINT32               contextCount;
#   TPM_DIGEST           integrityDigest;
#   UINT32               additionalSize;
#   UINT8                *additionalData;
#   UINT32               sensitiveSize;
#   UINT8                *sensitiveData;
# } TPM_CONTEXT_BLOB;
class TPM_CONTEXT_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("handle",          TPM_HANDLE),
    ("label",           UINT8 * 16),
    ("contextCount",    UINT32),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 18.2 TPM_CONTEXT_SENSITIVE
# ///
# typedef struct tdTPM_CONTEXT_SENSITIVE {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_NONCE            contextNonce;
#   UINT32               internalSize;
#   UINT8                *internalData;
# } TPM_CONTEXT_SENSITIVE;
class TPM_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("contextNonce",  TPM_NONCE),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

# 
# //
# // Part 2, section 19: NV Structures
# //
# 
# //
# // Part 2, section 19.1.1: Required TPM_NV_INDEX values
# //
# #define TPM_NV_INDEX_LOCK          ((UINT32)0xffffffff)
# #define TPM_NV_INDEX0              ((UINT32)0x00000000)
# #define TPM_NV_INDEX_DIR           ((UINT32)0x10000001)
# #define TPM_NV_INDEX_EKCert        ((UINT32)0x0000f000)
# #define TPM_NV_INDEX_TPM_CC        ((UINT32)0x0000f001)
# #define TPM_NV_INDEX_PlatformCert  ((UINT32)0x0000f002)
# #define TPM_NV_INDEX_Platform_CC   ((UINT32)0x0000f003)
TPM_NV_INDEX_LOCK              = 0xffffffff
TPM_NV_INDEX0                  = 0x00000000
TPM_NV_INDEX_DIR               = 0x10000001
TPM_NV_INDEX_EKCert            = 0x0000f000
TPM_NV_INDEX_TPM_CC            = 0x0000f001
TPM_NV_INDEX_PlatformCert      = 0x0000f002
TPM_NV_INDEX_Platform_CC       = 0x0000f003

# //
# // Part 2, section 19.1.2: Reserved Index values
# //
# #define TPM_NV_INDEX_TSS_BASE         ((UINT32)0x00011100)
# #define TPM_NV_INDEX_PC_BASE          ((UINT32)0x00011200)
# #define TPM_NV_INDEX_SERVER_BASE      ((UINT32)0x00011300)
# #define TPM_NV_INDEX_MOBILE_BASE      ((UINT32)0x00011400)
# #define TPM_NV_INDEX_PERIPHERAL_BASE  ((UINT32)0x00011500)
# #define TPM_NV_INDEX_GROUP_RESV_BASE  ((UINT32)0x00010000)
TPM_NV_INDEX_TSS_BASE          = 0x00011100
TPM_NV_INDEX_PC_BASE           = 0x00011200
TPM_NV_INDEX_SERVER_BASE       = 0x00011300
TPM_NV_INDEX_MOBILE_BASE       = 0x00011400
TPM_NV_INDEX_PERIPHERAL_BASE   = 0x00011500
TPM_NV_INDEX_GROUP_RESV_BASE   = 0x00010000

# 
# ///
# /// Part 2, section 19.2: TPM_NV_ATTRIBUTES
# ///
# typedef struct tdTPM_NV_ATTRIBUTES {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               attributes;
# } TPM_NV_ATTRIBUTES;
class TPM_NV_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("attributes",  UINT32)
  ]

# 
# #define TPM_NV_PER_READ_STCLEAR   (BIT31)
# #define TPM_NV_PER_AUTHREAD       (BIT18)
# #define TPM_NV_PER_OWNERREAD      (BIT17)
# #define TPM_NV_PER_PPREAD         (BIT16)
# #define TPM_NV_PER_GLOBALLOCK     (BIT15)
# #define TPM_NV_PER_WRITE_STCLEAR  (BIT14)
# #define TPM_NV_PER_WRITEDEFINE    (BIT13)
# #define TPM_NV_PER_WRITEALL       (BIT12)
# #define TPM_NV_PER_AUTHWRITE      (BIT2)
# #define TPM_NV_PER_OWNERWRITE     (BIT1)
# #define TPM_NV_PER_PPWRITE        (BIT0)
TPM_NV_PER_READ_STCLEAR        = BIT31
TPM_NV_PER_AUTHREAD            = BIT18
TPM_NV_PER_OWNERREAD           = BIT17
TPM_NV_PER_PPREAD              = BIT16
TPM_NV_PER_GLOBALLOCK          = BIT15
TPM_NV_PER_WRITE_STCLEAR       = BIT14
TPM_NV_PER_WRITEDEFINE         = BIT13
TPM_NV_PER_WRITEALL            = BIT12
TPM_NV_PER_AUTHWRITE           = BIT2
TPM_NV_PER_OWNERWRITE          = BIT1
TPM_NV_PER_PPWRITE             = BIT0

# 
# ///
# /// Part 2, section 19.3: TPM_NV_DATA_PUBLIC
# ///
# typedef struct tdTPM_NV_DATA_PUBLIC {
#   TPM_STRUCTURE_TAG     tag;
#   TPM_NV_INDEX          nvIndex;
#   TPM_PCR_INFO_SHORT    pcrInfoRead;
#   TPM_PCR_INFO_SHORT    pcrInfoWrite;
#   TPM_NV_ATTRIBUTES     permission;
#   BOOLEAN               bReadSTClear;
#   BOOLEAN               bWriteSTClear;
#   BOOLEAN               bWriteDefine;
#   UINT32                dataSize;
# } TPM_NV_DATA_PUBLIC;
class TPM_NV_DATA_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("nvIndex",       TPM_NV_INDEX),
    ("pcrInfoRead",   TPM_PCR_INFO_SHORT),
    ("pcrInfoWrite",  TPM_PCR_INFO_SHORT),
    ("permission",    TPM_NV_ATTRIBUTES),
    ("bReadSTClear",  BOOLEAN),
    ("bWriteSTClear", BOOLEAN),
    ("bWriteDefine",  BOOLEAN),
    ("dataSize",      UINT32)
  ]

# 
# //
# // Part 2, section 20: Delegate Structures
# //
# 
# #define TPM_DEL_OWNER_BITS  ((UINT32)0x00000001)
# #define TPM_DEL_KEY_BITS    ((UINT32)0x00000002)
TPM_DEL_OWNER_BITS          = 0x00000001
TPM_DEL_KEY_BITS            = 0x00000002

# ///
# /// Part 2, section 20.2: Delegate Definitions
# ///
# typedef struct tdTPM_DELEGATIONS {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               delegateType;
#   UINT32               per1;
#   UINT32               per2;
# } TPM_DELEGATIONS;
class TPM_DELEGATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("delegateType",  UINT32),
    ("per1",          UINT32),
    ("per2",          UINT32)
  ]

# 
# //
# // Part 2, section 20.2.1: Owner Permission Settings
# //
# #define TPM_DELEGATE_SetOrdinalAuditStatus           (BIT30)
# #define TPM_DELEGATE_DirWriteAuth                    (BIT29)
# #define TPM_DELEGATE_CMK_ApproveMA                   (BIT28)
# #define TPM_DELEGATE_NV_WriteValue                   (BIT27)
# #define TPM_DELEGATE_CMK_CreateTicket                (BIT26)
# #define TPM_DELEGATE_NV_ReadValue                    (BIT25)
# #define TPM_DELEGATE_Delegate_LoadOwnerDelegation    (BIT24)
# #define TPM_DELEGATE_DAA_Join                        (BIT23)
# #define TPM_DELEGATE_AuthorizeMigrationKey           (BIT22)
# #define TPM_DELEGATE_CreateMaintenanceArchive        (BIT21)
# #define TPM_DELEGATE_LoadMaintenanceArchive          (BIT20)
# #define TPM_DELEGATE_KillMaintenanceFeature          (BIT19)
# #define TPM_DELEGATE_OwnerReadInteralPub             (BIT18)
# #define TPM_DELEGATE_ResetLockValue                  (BIT17)
# #define TPM_DELEGATE_OwnerClear                      (BIT16)
# #define TPM_DELEGATE_DisableOwnerClear               (BIT15)
# #define TPM_DELEGATE_NV_DefineSpace                  (BIT14)
# #define TPM_DELEGATE_OwnerSetDisable                 (BIT13)
# #define TPM_DELEGATE_SetCapability                   (BIT12)
# #define TPM_DELEGATE_MakeIdentity                    (BIT11)
# #define TPM_DELEGATE_ActivateIdentity                (BIT10)
# #define TPM_DELEGATE_OwnerReadPubek                  (BIT9)
# #define TPM_DELEGATE_DisablePubekRead                (BIT8)
# #define TPM_DELEGATE_SetRedirection                  (BIT7)
# #define TPM_DELEGATE_FieldUpgrade                    (BIT6)
# #define TPM_DELEGATE_Delegate_UpdateVerification     (BIT5)
# #define TPM_DELEGATE_CreateCounter                   (BIT4)
# #define TPM_DELEGATE_ReleaseCounterOwner             (BIT3)
# #define TPM_DELEGATE_DelegateManage                  (BIT2)
# #define TPM_DELEGATE_Delegate_CreateOwnerDelegation  (BIT1)
# #define TPM_DELEGATE_DAA_Sign                        (BIT0)
TPM_DELEGATE_SetOrdinalAuditStatus          = BIT30
TPM_DELEGATE_DirWriteAuth                   = BIT29
TPM_DELEGATE_CMK_ApproveMA                  = BIT28
TPM_DELEGATE_NV_WriteValue                  = BIT27
TPM_DELEGATE_CMK_CreateTicket               = BIT26
TPM_DELEGATE_NV_ReadValue                   = BIT25
TPM_DELEGATE_Delegate_LoadOwnerDelegation   = BIT24
TPM_DELEGATE_DAA_Join                       = BIT23
TPM_DELEGATE_AuthorizeMigrationKey          = BIT22
TPM_DELEGATE_CreateMaintenanceArchive       = BIT21
TPM_DELEGATE_LoadMaintenanceArchive         = BIT20
TPM_DELEGATE_KillMaintenanceFeature         = BIT19
TPM_DELEGATE_OwnerReadInteralPub            = BIT18
TPM_DELEGATE_ResetLockValue                 = BIT17
TPM_DELEGATE_OwnerClear                     = BIT16
TPM_DELEGATE_DisableOwnerClear              = BIT15
TPM_DELEGATE_NV_DefineSpace                 = BIT14
TPM_DELEGATE_OwnerSetDisable                = BIT13
TPM_DELEGATE_SetCapability                  = BIT12
TPM_DELEGATE_MakeIdentity                   = BIT11
TPM_DELEGATE_ActivateIdentity               = BIT10
TPM_DELEGATE_OwnerReadPubek                 = BIT9
TPM_DELEGATE_DisablePubekRead               = BIT8
TPM_DELEGATE_SetRedirection                 = BIT7
TPM_DELEGATE_FieldUpgrade                   = BIT6
TPM_DELEGATE_Delegate_UpdateVerification    = BIT5
TPM_DELEGATE_CreateCounter                  = BIT4
TPM_DELEGATE_ReleaseCounterOwner            = BIT3
TPM_DELEGATE_DelegateManage                 = BIT2
TPM_DELEGATE_Delegate_CreateOwnerDelegation = BIT1
TPM_DELEGATE_DAA_Sign                       = BIT0

# 
# //
# // Part 2, section 20.2.3: Key Permission settings
# //
# #define TPM_KEY_DELEGATE_CMK_ConvertMigration    (BIT28)
# #define TPM_KEY_DELEGATE_TickStampBlob           (BIT27)
# #define TPM_KEY_DELEGATE_ChangeAuthAsymStart     (BIT26)
# #define TPM_KEY_DELEGATE_ChangeAuthAsymFinish    (BIT25)
# #define TPM_KEY_DELEGATE_CMK_CreateKey           (BIT24)
# #define TPM_KEY_DELEGATE_MigrateKey              (BIT23)
# #define TPM_KEY_DELEGATE_LoadKey2                (BIT22)
# #define TPM_KEY_DELEGATE_EstablishTransport      (BIT21)
# #define TPM_KEY_DELEGATE_ReleaseTransportSigned  (BIT20)
# #define TPM_KEY_DELEGATE_Quote2                  (BIT19)
# #define TPM_KEY_DELEGATE_Sealx                   (BIT18)
# #define TPM_KEY_DELEGATE_MakeIdentity            (BIT17)
# #define TPM_KEY_DELEGATE_ActivateIdentity        (BIT16)
# #define TPM_KEY_DELEGATE_GetAuditDigestSigned    (BIT15)
# #define TPM_KEY_DELEGATE_Sign                    (BIT14)
# #define TPM_KEY_DELEGATE_CertifyKey2             (BIT13)
# #define TPM_KEY_DELEGATE_CertifyKey              (BIT12)
# #define TPM_KEY_DELEGATE_CreateWrapKey           (BIT11)
# #define TPM_KEY_DELEGATE_CMK_CreateBlob          (BIT10)
# #define TPM_KEY_DELEGATE_CreateMigrationBlob     (BIT9)
# #define TPM_KEY_DELEGATE_ConvertMigrationBlob    (BIT8)
# #define TPM_KEY_DELEGATE_CreateKeyDelegation     (BIT7)
# #define TPM_KEY_DELEGATE_ChangeAuth              (BIT6)
# #define TPM_KEY_DELEGATE_GetPubKey               (BIT5)
# #define TPM_KEY_DELEGATE_UnBind                  (BIT4)
# #define TPM_KEY_DELEGATE_Quote                   (BIT3)
# #define TPM_KEY_DELEGATE_Unseal                  (BIT2)
# #define TPM_KEY_DELEGATE_Seal                    (BIT1)
# #define TPM_KEY_DELEGATE_LoadKey                 (BIT0)
TPM_KEY_DELEGATE_CMK_ConvertMigration       = BIT28
TPM_KEY_DELEGATE_TickStampBlob              = BIT27
TPM_KEY_DELEGATE_ChangeAuthAsymStart        = BIT26
TPM_KEY_DELEGATE_ChangeAuthAsymFinish       = BIT25
TPM_KEY_DELEGATE_CMK_CreateKey              = BIT24
TPM_KEY_DELEGATE_MigrateKey                 = BIT23
TPM_KEY_DELEGATE_LoadKey2                   = BIT22
TPM_KEY_DELEGATE_EstablishTransport         = BIT21
TPM_KEY_DELEGATE_ReleaseTransportSigned     = BIT20
TPM_KEY_DELEGATE_Quote2                     = BIT19
TPM_KEY_DELEGATE_Sealx                      = BIT18
TPM_KEY_DELEGATE_MakeIdentity               = BIT17
TPM_KEY_DELEGATE_ActivateIdentity           = BIT16
TPM_KEY_DELEGATE_GetAuditDigestSigned       = BIT15
TPM_KEY_DELEGATE_Sign                       = BIT14
TPM_KEY_DELEGATE_CertifyKey2                = BIT13
TPM_KEY_DELEGATE_CertifyKey                 = BIT12
TPM_KEY_DELEGATE_CreateWrapKey              = BIT11
TPM_KEY_DELEGATE_CMK_CreateBlob             = BIT10
TPM_KEY_DELEGATE_CreateMigrationBlob        = BIT9
TPM_KEY_DELEGATE_ConvertMigrationBlob       = BIT8
TPM_KEY_DELEGATE_CreateKeyDelegation        = BIT7
TPM_KEY_DELEGATE_ChangeAuth                 = BIT6
TPM_KEY_DELEGATE_GetPubKey                  = BIT5
TPM_KEY_DELEGATE_UnBind                     = BIT4
TPM_KEY_DELEGATE_Quote                      = BIT3
TPM_KEY_DELEGATE_Unseal                     = BIT2
TPM_KEY_DELEGATE_Seal                       = BIT1
TPM_KEY_DELEGATE_LoadKey                    = BIT0

# 
# //
# // Part 2, section 20.3: TPM_FAMILY_FLAGS
# //
# #define TPM_DELEGATE_ADMIN_LOCK  (BIT1)
# #define TPM_FAMFLAG_ENABLE       (BIT0)
TPM_DELEGATE_ADMIN_LOCK           = BIT1
TPM_FAMFLAG_ENABLE                = BIT0

# 
# ///
# /// Part 2, section 20.4: TPM_FAMILY_LABEL
# ///
# typedef struct tdTPM_FAMILY_LABEL {
#   UINT8    label;
# } TPM_FAMILY_LABEL;
class TPM_FAMILY_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

# 
# ///
# /// Part 2, section 20.5: TPM_FAMILY_TABLE_ENTRY
# ///
# typedef struct tdTPM_FAMILY_TABLE_ENTRY {
#   TPM_STRUCTURE_TAG          tag;
#   TPM_FAMILY_LABEL           label;
#   TPM_FAMILY_ID              familyID;
#   TPM_FAMILY_VERIFICATION    verificationCount;
#   TPM_FAMILY_FLAGS           flags;
# } TPM_FAMILY_TABLE_ENTRY;
class TPM_FAMILY_TABLE_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_FAMILY_LABEL),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
    ("flags",             TPM_FAMILY_FLAGS)
  ]

# 
# //
# // Part 2, section 20.6: TPM_FAMILY_TABLE
# //
# #define TPM_NUM_FAMILY_TABLE_ENTRY_MIN  8
TPM_NUM_FAMILY_TABLE_ENTRY_MIN = 8

# 
# typedef struct tdTPM_FAMILY_TABLE {
#   TPM_FAMILY_TABLE_ENTRY    famTableRow[TPM_NUM_FAMILY_TABLE_ENTRY_MIN];
# } TPM_FAMILY_TABLE;
class TPM_FAMILY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("famTableRow",     TPM_FAMILY_TABLE_ENTRY * TPM_NUM_FAMILY_TABLE_ENTRY_MIN)
  ]

# 
# ///
# /// Part 2, section 20.7: TPM_DELEGATE_LABEL
# ///
# typedef struct tdTPM_DELEGATE_LABEL {
#   UINT8    label;
# } TPM_DELEGATE_LABEL;
class TPM_DELEGATE_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

# 
# ///
# /// Part 2, section 20.8: TPM_DELEGATE_PUBLIC
# ///
# typedef struct tdTPM_DELEGATE_PUBLIC {
#   TPM_STRUCTURE_TAG          tag;
#   TPM_DELEGATE_LABEL         label;
#   TPM_PCR_INFO_SHORT         pcrInfo;
#   TPM_DELEGATIONS            permissions;
#   TPM_FAMILY_ID              familyID;
#   TPM_FAMILY_VERIFICATION    verificationCount;
# } TPM_DELEGATE_PUBLIC;
class TPM_DELEGATE_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_DELEGATE_LABEL),
    ("pcrInfo",           TPM_PCR_INFO_SHORT),
    ("permissions",       TPM_DELEGATIONS),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
  ]

# 
# ///
# /// Part 2, section 20.9: TPM_DELEGATE_TABLE_ROW
# ///
# typedef struct tdTPM_DELEGATE_TABLE_ROW {
#   TPM_STRUCTURE_TAG      tag;
#   TPM_DELEGATE_PUBLIC    pub;
#   TPM_SECRET             authValue;
# } TPM_DELEGATE_TABLE_ROW;
class TPM_DELEGATE_TABLE_ROW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("pub",       TPM_DELEGATE_PUBLIC),
    ("authValue", TPM_SECRET)
  ]

# 
# //
# // Part 2, section 20.10: TPM_DELEGATE_TABLE
# //
# #define TPM_NUM_DELEGATE_TABLE_ENTRY_MIN  2
TPM_NUM_DELEGATE_TABLE_ENTRY_MIN = 2

# 
# typedef struct tdTPM_DELEGATE_TABLE {
#   TPM_DELEGATE_TABLE_ROW    delRow[TPM_NUM_DELEGATE_TABLE_ENTRY_MIN];
# } TPM_DELEGATE_TABLE;
class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("delRow", TPM_DELEGATE_TABLE_ROW * TPM_NUM_DELEGATE_TABLE_ENTRY_MIN)
  ]

# 
# ///
# /// Part 2, section 20.11: TPM_DELEGATE_SENSITIVE
# ///
# typedef struct tdTPM_DELEGATE_SENSITIVE {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_SECRET           authValue;
# } TPM_DELEGATE_SENSITIVE;
class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authValue", TPM_SECRET)
  ]

# 
# ///
# /// Part 2, section 20.12: TPM_DELEGATE_OWNER_BLOB
# ///
# typedef struct tdTPM_DELEGATE_OWNER_BLOB {
#   TPM_STRUCTURE_TAG      tag;
#   TPM_DELEGATE_PUBLIC    pub;
#   TPM_DIGEST             integrityDigest;
#   UINT32                 additionalSize;
#   UINT8                  *additionalArea;
#   UINT32                 sensitiveSize;
#   UINT8                  *sensitiveArea;
# } TPM_DELEGATE_OWNER_BLOB;
class TPM_DELEGATE_OWNER_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 20.13: TTPM_DELEGATE_KEY_BLOB
# ///
# typedef struct tdTPM_DELEGATE_KEY_BLOB {
#   TPM_STRUCTURE_TAG      tag;
#   TPM_DELEGATE_PUBLIC    pub;
#   TPM_DIGEST             integrityDigest;
#   TPM_DIGEST             pubKeyDigest;
#   UINT32                 additionalSize;
#   UINT8                  *additionalArea;
#   UINT32                 sensitiveSize;
#   UINT8                  *sensitiveArea;
# } TPM_DELEGATE_KEY_BLOB;
class TPM_DELEGATE_KEY_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("pubKeyDigest",    TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

# 
# //
# // Part 2, section 20.14: TPM_FAMILY_OPERATION Values
# //
# #define TPM_FAMILY_CREATE      ((UINT32)0x00000001)
# #define TPM_FAMILY_ENABLE      ((UINT32)0x00000002)
# #define TPM_FAMILY_ADMIN       ((UINT32)0x00000003)
# #define TPM_FAMILY_INVALIDATE  ((UINT32)0x00000004)
TPM_FAMILY_CREATE                 = 0x00000001
TPM_FAMILY_ENABLE                 = 0x00000002
TPM_FAMILY_ADMIN                  = 0x00000003
TPM_FAMILY_INVALIDATE             = 0x00000004

# 
# //
# // Part 2, section 21.1: TPM_CAPABILITY_AREA for GetCapability
# //
# #define TPM_CAP_ORD           ((TPM_CAPABILITY_AREA) 0x00000001)
# #define TPM_CAP_ALG           ((TPM_CAPABILITY_AREA) 0x00000002)
# #define TPM_CAP_PID           ((TPM_CAPABILITY_AREA) 0x00000003)
# #define TPM_CAP_FLAG          ((TPM_CAPABILITY_AREA) 0x00000004)
# #define TPM_CAP_PROPERTY      ((TPM_CAPABILITY_AREA) 0x00000005)
# #define TPM_CAP_VERSION       ((TPM_CAPABILITY_AREA) 0x00000006)
# #define TPM_CAP_KEY_HANDLE    ((TPM_CAPABILITY_AREA) 0x00000007)
# #define TPM_CAP_CHECK_LOADED  ((TPM_CAPABILITY_AREA) 0x00000008)
# #define TPM_CAP_SYM_MODE      ((TPM_CAPABILITY_AREA) 0x00000009)
# #define TPM_CAP_KEY_STATUS    ((TPM_CAPABILITY_AREA) 0x0000000C)
# #define TPM_CAP_NV_LIST       ((TPM_CAPABILITY_AREA) 0x0000000D)
# #define TPM_CAP_MFR           ((TPM_CAPABILITY_AREA) 0x00000010)
# #define TPM_CAP_NV_INDEX      ((TPM_CAPABILITY_AREA) 0x00000011)
# #define TPM_CAP_TRANS_ALG     ((TPM_CAPABILITY_AREA) 0x00000012)
# #define TPM_CAP_HANDLE        ((TPM_CAPABILITY_AREA) 0x00000014)
# #define TPM_CAP_TRANS_ES      ((TPM_CAPABILITY_AREA) 0x00000015)
# #define TPM_CAP_AUTH_ENCRYPT  ((TPM_CAPABILITY_AREA) 0x00000017)
# #define TPM_CAP_SELECT_SIZE   ((TPM_CAPABILITY_AREA) 0x00000018)
# #define TPM_CAP_VERSION_VAL   ((TPM_CAPABILITY_AREA) 0x0000001A)
TPM_CAP_ORD                     = 0x00000001
TPM_CAP_ALG                     = 0x00000002
TPM_CAP_PID                     = 0x00000003
TPM_CAP_FLAG                    = 0x00000004
TPM_CAP_PROPERTY                = 0x00000005
TPM_CAP_VERSION                 = 0x00000006
TPM_CAP_KEY_HANDLE              = 0x00000007
TPM_CAP_CHECK_LOADED            = 0x00000008
TPM_CAP_SYM_MODE                = 0x00000009
TPM_CAP_KEY_STATUS              = 0x0000000C
TPM_CAP_NV_LIST                 = 0x0000000D
TPM_CAP_MFR                     = 0x00000010
TPM_CAP_NV_INDEX                = 0x00000011
TPM_CAP_TRANS_ALG               = 0x00000012
TPM_CAP_HANDLE                  = 0x00000014
TPM_CAP_TRANS_ES                = 0x00000015
TPM_CAP_AUTH_ENCRYPT            = 0x00000017
TPM_CAP_SELECT_SIZE             = 0x00000018
TPM_CAP_VERSION_VAL             = 0x0000001A

# 
# #define TPM_CAP_FLAG_PERMANENT  ((TPM_CAPABILITY_AREA) 0x00000108)
# #define TPM_CAP_FLAG_VOLATILE   ((TPM_CAPABILITY_AREA) 0x00000109)
TPM_CAP_FLAG_PERMANENT          = 0x00000108
TPM_CAP_FLAG_VOLATILE           = 0x00000109

# 
# //
# // Part 2, section 21.2: CAP_PROPERTY Subcap values for GetCapability
# //
# #define TPM_CAP_PROP_PCR               ((TPM_CAPABILITY_AREA) 0x00000101)
# #define TPM_CAP_PROP_DIR               ((TPM_CAPABILITY_AREA) 0x00000102)
# #define TPM_CAP_PROP_MANUFACTURER      ((TPM_CAPABILITY_AREA) 0x00000103)
# #define TPM_CAP_PROP_KEYS              ((TPM_CAPABILITY_AREA) 0x00000104)
# #define TPM_CAP_PROP_MIN_COUNTER       ((TPM_CAPABILITY_AREA) 0x00000107)
# #define TPM_CAP_PROP_AUTHSESS          ((TPM_CAPABILITY_AREA) 0x0000010A)
# #define TPM_CAP_PROP_TRANSESS          ((TPM_CAPABILITY_AREA) 0x0000010B)
# #define TPM_CAP_PROP_COUNTERS          ((TPM_CAPABILITY_AREA) 0x0000010C)
# #define TPM_CAP_PROP_MAX_AUTHSESS      ((TPM_CAPABILITY_AREA) 0x0000010D)
# #define TPM_CAP_PROP_MAX_TRANSESS      ((TPM_CAPABILITY_AREA) 0x0000010E)
# #define TPM_CAP_PROP_MAX_COUNTERS      ((TPM_CAPABILITY_AREA) 0x0000010F)
# #define TPM_CAP_PROP_MAX_KEYS          ((TPM_CAPABILITY_AREA) 0x00000110)
# #define TPM_CAP_PROP_OWNER             ((TPM_CAPABILITY_AREA) 0x00000111)
# #define TPM_CAP_PROP_CONTEXT           ((TPM_CAPABILITY_AREA) 0x00000112)
# #define TPM_CAP_PROP_MAX_CONTEXT       ((TPM_CAPABILITY_AREA) 0x00000113)
# #define TPM_CAP_PROP_FAMILYROWS        ((TPM_CAPABILITY_AREA) 0x00000114)
# #define TPM_CAP_PROP_TIS_TIMEOUT       ((TPM_CAPABILITY_AREA) 0x00000115)
# #define TPM_CAP_PROP_STARTUP_EFFECT    ((TPM_CAPABILITY_AREA) 0x00000116)
# #define TPM_CAP_PROP_DELEGATE_ROW      ((TPM_CAPABILITY_AREA) 0x00000117)
# #define TPM_CAP_PROP_DAA_MAX           ((TPM_CAPABILITY_AREA) 0x00000119)
# #define CAP_PROP_SESSION_DAA           ((TPM_CAPABILITY_AREA) 0x0000011A)
# #define TPM_CAP_PROP_CONTEXT_DIST      ((TPM_CAPABILITY_AREA) 0x0000011B)
# #define TPM_CAP_PROP_DAA_INTERRUPT     ((TPM_CAPABILITY_AREA) 0x0000011C)
# #define TPM_CAP_PROP_SESSIONS          ((TPM_CAPABILITY_AREA) 0x0000011D)
# #define TPM_CAP_PROP_MAX_SESSIONS      ((TPM_CAPABILITY_AREA) 0x0000011E)
# #define TPM_CAP_PROP_CMK_RESTRICTION   ((TPM_CAPABILITY_AREA) 0x0000011F)
# #define TPM_CAP_PROP_DURATION          ((TPM_CAPABILITY_AREA) 0x00000120)
# #define TPM_CAP_PROP_ACTIVE_COUNTER    ((TPM_CAPABILITY_AREA) 0x00000122)
# #define TPM_CAP_PROP_MAX_NV_AVAILABLE  ((TPM_CAPABILITY_AREA) 0x00000123)
# #define TPM_CAP_PROP_INPUT_BUFFER      ((TPM_CAPABILITY_AREA) 0x00000124)
TPM_CAP_PROP_PCR                = 0x00000101
TPM_CAP_PROP_DIR                = 0x00000102
TPM_CAP_PROP_MANUFACTURER       = 0x00000103
TPM_CAP_PROP_KEYS               = 0x00000104
TPM_CAP_PROP_MIN_COUNTER        = 0x00000107
TPM_CAP_PROP_AUTHSESS           = 0x0000010A
TPM_CAP_PROP_TRANSESS           = 0x0000010B
TPM_CAP_PROP_COUNTERS           = 0x0000010C
TPM_CAP_PROP_MAX_AUTHSESS       = 0x0000010D
TPM_CAP_PROP_MAX_TRANSESS       = 0x0000010E
TPM_CAP_PROP_MAX_COUNTERS       = 0x0000010F
TPM_CAP_PROP_MAX_KEYS           = 0x00000110
TPM_CAP_PROP_OWNER              = 0x00000111
TPM_CAP_PROP_CONTEXT            = 0x00000112
TPM_CAP_PROP_MAX_CONTEXT        = 0x00000113
TPM_CAP_PROP_FAMILYROWS         = 0x00000114
TPM_CAP_PROP_TIS_TIMEOUT        = 0x00000115
TPM_CAP_PROP_STARTUP_EFFECT     = 0x00000116
TPM_CAP_PROP_DELEGATE_ROW       = 0x00000117
TPM_CAP_PROP_DAA_MAX            = 0x00000119
CAP_PROP_SESSION_DAA            = 0x0000011A
TPM_CAP_PROP_CONTEXT_DIST       = 0x0000011B
TPM_CAP_PROP_DAA_INTERRUPT      = 0x0000011C
TPM_CAP_PROP_SESSIONS           = 0x0000011D
TPM_CAP_PROP_MAX_SESSIONS       = 0x0000011E
TPM_CAP_PROP_CMK_RESTRICTION    = 0x0000011F
TPM_CAP_PROP_DURATION           = 0x00000120
TPM_CAP_PROP_ACTIVE_COUNTER     = 0x00000122
TPM_CAP_PROP_MAX_NV_AVAILABLE   = 0x00000123
TPM_CAP_PROP_INPUT_BUFFER       = 0x00000124

# 
# //
# // Part 2, section 21.4: TPM_CAPABILITY_AREA for SetCapability
# //
# #define TPM_SET_PERM_FLAGS     ((TPM_CAPABILITY_AREA) 0x00000001)
# #define TPM_SET_PERM_DATA      ((TPM_CAPABILITY_AREA) 0x00000002)
# #define TPM_SET_STCLEAR_FLAGS  ((TPM_CAPABILITY_AREA) 0x00000003)
# #define TPM_SET_STCLEAR_DATA   ((TPM_CAPABILITY_AREA) 0x00000004)
# #define TPM_SET_STANY_FLAGS    ((TPM_CAPABILITY_AREA) 0x00000005)
# #define TPM_SET_STANY_DATA     ((TPM_CAPABILITY_AREA) 0x00000006)
TPM_SET_PERM_FLAGS              = 0x00000001
TPM_SET_PERM_DATA               = 0x00000002
TPM_SET_STCLEAR_FLAGS           = 0x00000003
TPM_SET_STCLEAR_DATA            = 0x00000004
TPM_SET_STANY_FLAGS             = 0x00000005
TPM_SET_STANY_DATA              = 0x00000006

# 
# ///
# /// Part 2, section 21.6: TPM_CAP_VERSION_INFO
# ///   [size_is(vendorSpecificSize)] BYTE* vendorSpecific;
# ///
# typedef struct tdTPM_CAP_VERSION_INFO {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_VERSION          version;
#   UINT16               specLevel;
#   UINT8                errataRev;
#   UINT8                tpmVendorID[4];
#   UINT16               vendorSpecificSize;
#   UINT8                *vendorSpecific;
# } TPM_CAP_VERSION_INFO;
class TPM_CAP_VERSION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("version",             TPM_VERSION),
    ("specLevel",           UINT16),
    ("errataRev",           UINT8),
    ("tpmVendorID",         UINT8 * 4),
    ("vendorSpecificSize",  UINT16),
    ("vendorSpecific",      POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 21.10: TPM_DA_ACTION_TYPE
# ///
# typedef struct tdTPM_DA_ACTION_TYPE {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               actions;
# } TPM_DA_ACTION_TYPE;
class TPM_DA_ACTION_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("actions", UINT32)
  ]

# 
# #define TPM_DA_ACTION_FAILURE_MODE  (((UINT32)1)<<3)
# #define TPM_DA_ACTION_DEACTIVATE    (((UINT32)1)<<2)
# #define TPM_DA_ACTION_DISABLE       (((UINT32)1)<<1)
# #define TPM_DA_ACTION_TIMEOUT       (((UINT32)1)<<0)
TPM_DA_ACTION_FAILURE_MODE     = 1 << 3
TPM_DA_ACTION_DEACTIVATE       = 1 << 2
TPM_DA_ACTION_DISABLE          = 1 << 1
TPM_DA_ACTION_TIMEOUT          = 1 << 0

# 
# ///
# /// Part 2, section 21.7: TPM_DA_INFO
# ///
# typedef struct tdTPM_DA_INFO {
#   TPM_STRUCTURE_TAG     tag;
#   TPM_DA_STATE          state;
#   UINT16                currentCount;
#   UINT16                thresholdCount;
#   TPM_DA_ACTION_TYPE    actionAtThreshold;
#   UINT32                actionDependValue;
#   UINT32                vendorDataSize;
#   UINT8                 *vendorData;
# } TPM_DA_INFO;
class TPM_DA_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("currentCount",      UINT16),
    ("thresholdCount",    UINT16),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("actionDependValue", UINT32),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 21.8: TPM_DA_INFO_LIMITED
# ///
# typedef struct tdTPM_DA_INFO_LIMITED {
#   TPM_STRUCTURE_TAG     tag;
#   TPM_DA_STATE          state;
#   TPM_DA_ACTION_TYPE    actionAtThreshold;
#   UINT32                vendorDataSize;
#   UINT8                 *vendorData;
# } TPM_DA_INFO_LIMITED;
class TPM_DA_INFO_LIMITED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

# 
# //
# // Part 2, section 21.9: CAP_PROPERTY Subcap values for GetCapability
# //
# #define TPM_DA_STATE_INACTIVE  ((UINT8)0x00)
# #define TPM_DA_STATE_ACTIVE    ((UINT8)0x01)
TPM_DA_STATE_INACTIVE          = UINT8(0x00).value
TPM_DA_STATE_ACTIVE            = UINT8(0x01).value

# 
# //
# // Part 2, section 22: DAA Structures
# //
# 
# //
# // Part 2, section 22.1: Size definitions
# //
# #define TPM_DAA_SIZE_r0             (43)
# #define TPM_DAA_SIZE_r1             (43)
# #define TPM_DAA_SIZE_r2             (128)
# #define TPM_DAA_SIZE_r3             (168)
# #define TPM_DAA_SIZE_r4             (219)
# #define TPM_DAA_SIZE_NT             (20)
# #define TPM_DAA_SIZE_v0             (128)
# #define TPM_DAA_SIZE_v1             (192)
# #define TPM_DAA_SIZE_NE             (256)
# #define TPM_DAA_SIZE_w              (256)
# #define TPM_DAA_SIZE_issuerModulus  (256)
TPM_DAA_SIZE_r0                = 43
TPM_DAA_SIZE_r1                = 43
TPM_DAA_SIZE_r2                = 128
TPM_DAA_SIZE_r3                = 168
TPM_DAA_SIZE_r4                = 219
TPM_DAA_SIZE_NT                = 20
TPM_DAA_SIZE_v0                = 128
TPM_DAA_SIZE_v1                = 192
TPM_DAA_SIZE_NE                = 256
TPM_DAA_SIZE_w                 = 256
TPM_DAA_SIZE_issuerModulus     = 256

# //
# // Part 2, section 22.2: Constant definitions
# //
# #define TPM_DAA_power0  (104)
# #define TPM_DAA_power1  (1024)
TPM_DAA_power0                 = 104
TPM_DAA_power1                 = 1024

# 
# ///
# /// Part 2, section 22.3: TPM_DAA_ISSUER
# ///
# typedef struct tdTPM_DAA_ISSUER {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           DAA_digest_R0;
#   TPM_DIGEST           DAA_digest_R1;
#   TPM_DIGEST           DAA_digest_S0;
#   TPM_DIGEST           DAA_digest_S1;
#   TPM_DIGEST           DAA_digest_n;
#   TPM_DIGEST           DAA_digest_gamma;
#   UINT8                DAA_generic_q[26];
# } TPM_DAA_ISSUER;
class TPM_DAA_ISSUER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digest_R0",     TPM_DIGEST),
    ("DAA_digest_R1",     TPM_DIGEST),
    ("DAA_digest_S0",     TPM_DIGEST),
    ("DAA_digest_S1",     TPM_DIGEST),
    ("DAA_digest_n",      TPM_DIGEST),
    ("DAA_digest_gamma",  TPM_DIGEST),
    ("DAA_generic_q",     UINT8 * 26)
  ]

# 
# ///
# /// Part 2, section 22.4: TPM_DAA_TPM
# ///
# typedef struct tdTPM_DAA_TPM {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_DIGEST           DAA_digestIssuer;
#   TPM_DIGEST           DAA_digest_v0;
#   TPM_DIGEST           DAA_digest_v1;
#   TPM_DIGEST           DAA_rekey;
#   UINT32               DAA_count;
# } TPM_DAA_TPM;
class TPM_DAA_TPM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestIssuer",  TPM_DIGEST),
    ("DAA_digest_v0",     TPM_DIGEST),
    ("DAA_digest_v1",     TPM_DIGEST),
    ("DAA_rekey",         TPM_DIGEST),
    ("DAA_count",         UINT32)
  ]

# 
# ///
# /// Part 2, section 22.5: TPM_DAA_CONTEXT
# ///
# typedef struct tdTPM_DAA_CONTEXT {
#   TPM_STRUCTURE_TAG       tag;
#   TPM_DIGEST              DAA_digestContext;
#   TPM_DIGEST              DAA_digest;
#   TPM_DAA_CONTEXT_SEED    DAA_contextSeed;
#   UINT8                   DAA_scratch[256];
#   UINT8                   DAA_stage;
# } TPM_DAA_CONTEXT;
class TPM_DAA_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestContext", TPM_DIGEST),
    ("DAA_digest",        TPM_DIGEST),
    ("DAA_contextSeed",   TPM_DAA_CONTEXT_SEED),
    ("DAA_scratch",       UINT8 * 256),
    ("DAA_stage",         UINT8)
  ]

# 
# ///
# /// Part 2, section 22.6: TPM_DAA_JOINDATA
# ///
# typedef struct tdTPM_DAA_JOINDATA {
#   UINT8         DAA_join_u0[128];
#   UINT8         DAA_join_u1[138];
#   TPM_DIGEST    DAA_digest_n0;
# } TPM_DAA_JOINDATA;
class TPM_DAA_JOINDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DAA_join_u0",   UINT8 * 128),
    ("DAA_join_u1",   UINT8 * 138),
    ("DAA_digest_n0", TPM_DIGEST)
  ]

# 
# ///
# /// Part 2, section 22.8: TPM_DAA_BLOB
# ///
# typedef struct tdTPM_DAA_BLOB {
#   TPM_STRUCTURE_TAG    tag;
#   TPM_RESOURCE_TYPE    resourceType;
#   UINT8                label[16];
#   TPM_DIGEST           blobIntegrity;
#   UINT32               additionalSize;
#   UINT8                *additionalData;
#   UINT32               sensitiveSize;
#   UINT8                *sensitiveData;
# } TPM_DAA_BLOB;
class TPM_DAA_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("label",           UINT8 * 16),
    ("blobIntegrity",   TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

# 
# ///
# /// Part 2, section 22.9: TPM_DAA_SENSITIVE
# ///
# typedef struct tdTPM_DAA_SENSITIVE {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               internalSize;
#   UINT8                *internalData;
# } TPM_DAA_SENSITIVE;
class TPM_DAA_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

# 
# //
# // Part 2, section 23: Redirection
# //
# 
# ///
# /// Part 2 section 23.1: TPM_REDIR_COMMAND
# /// This section defines exactly one value but does not
# /// give it a name. The definition of TPM_SetRedirection in Part3
# /// refers to exactly one name but does not give its value. We join
# /// them here.
# ///
# #define TPM_REDIR_GPIO  (0x00000001)
TPM_REDIR_GPIO              = 0x00000001

# 
# ///
# /// TPM Command Headers defined in Part 3
# ///
# typedef struct tdTPM_RQU_COMMAND_HDR {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               paramSize;
#   TPM_COMMAND_CODE     ordinal;
# } TPM_RQU_COMMAND_HDR;
class TPM_RQU_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("paramSize", UINT32),
    ("ordinal",   TPM_COMMAND_CODE)
  ]

# 
# ///
# /// TPM Response Headers defined in Part 3
# ///
# typedef struct tdTPM_RSP_COMMAND_HDR {
#   TPM_STRUCTURE_TAG    tag;
#   UINT32               paramSize;
#   TPM_RESULT           returnCode;
# } TPM_RSP_COMMAND_HDR;
class TPM_RSP_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("paramSize",   UINT32),
    ("returnCode",  TPM_RESULT)
  ]

# 
# #pragma pack ()
# 
# #endif
# 