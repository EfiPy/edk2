# /** @file
#   TPM2.0 Specification data structures
#   (Trusted Platform Module Library Specification, Family "2.0", Level 00, Revision 00.96,
#   @http://www.trustedcomputinggroup.org/resources/tpm_library_specification)
# 
#   Check http://trustedcomputinggroup.org for latest specification updates.
# 
# Copyright (c) 2013 - 2015, Intel Corporation. All rights reserved. <BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Tpm20.py
#
# EfiPy2.MdePkg.IndustryStandard.Tpm20
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2024 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _TPM20_H_
# #define _TPM20_H_
# 
# #include <IndustryStandard/Tpm12.h>
from EfiPy2.MdePkg.IndustryStandard    import *
from EfiPy2.MdePkg.IndustryStandard   import Tpm12

# 
# #pragma pack (1)
# 
# // Annex A Algorithm Constants
# 
# // Table 205 - Defines for SHA1 Hash Values
# #define SHA1_DIGEST_SIZE  20
# #define SHA1_BLOCK_SIZE   64
SHA1_DIGEST_SIZE = 20
SHA1_BLOCK_SIZE  = 64

# 
# // Table 206 - Defines for SHA256 Hash Values
# #define SHA256_DIGEST_SIZE  32
# #define SHA256_BLOCK_SIZE   64
SHA256_DIGEST_SIZE = 32
SHA256_BLOCK_SIZE  = 64

# 
# // Table 207 - Defines for SHA384 Hash Values
# #define SHA384_DIGEST_SIZE  48
# #define SHA384_BLOCK_SIZE   128
SHA384_DIGEST_SIZE = 48
SHA384_BLOCK_SIZE  = 128

# 
# // Table 208 - Defines for SHA512 Hash Values
# #define SHA512_DIGEST_SIZE  64
# #define SHA512_BLOCK_SIZE   128
SHA512_DIGEST_SIZE = 64
SHA512_BLOCK_SIZE  = 128

# 
# // Table 209 - Defines for SM3_256 Hash Values
# #define SM3_256_DIGEST_SIZE  32
# #define SM3_256_BLOCK_SIZE   64
SM3_256_DIGEST_SIZE = 32
SM3_256_BLOCK_SIZE  = 64

# 
# // Table 210 - Defines for Architectural Limits Values
# #define MAX_SESSION_NUMBER  3
MAX_SESSION_NUMBER = 3

# 
# // Annex B Implementation Definitions
# 
# // Table 211 - Defines for Logic Values
# #define YES    1
# #define NO     0
# #define SET    1
# #define CLEAR  0
YES   = 1
NO    = 0
SET   = 1
CLEAR = 0

# 
# // Table 215 - Defines for RSA Algorithm Constants
# #define MAX_RSA_KEY_BITS   2048
# #define MAX_RSA_KEY_BYTES  ((MAX_RSA_KEY_BITS + 7) / 8)
MAX_RSA_KEY_BITS  = 2048
MAX_RSA_KEY_BYTES = ((MAX_RSA_KEY_BITS + 7) // 8)

# 
# // Table 216 - Defines for ECC Algorithm Constants
# #define MAX_ECC_KEY_BITS   256
# #define MAX_ECC_KEY_BYTES  ((MAX_ECC_KEY_BITS + 7) / 8)
MAX_ECC_KEY_BITS  = 256
MAX_ECC_KEY_BYTES = ((MAX_ECC_KEY_BITS + 7) // 8)

# 
# // Table 217 - Defines for AES Algorithm Constants
# #define MAX_AES_KEY_BITS          128
# #define MAX_AES_BLOCK_SIZE_BYTES  16
# #define MAX_AES_KEY_BYTES         ((MAX_AES_KEY_BITS + 7) / 8)
MAX_AES_KEY_BITS         = 128
MAX_AES_BLOCK_SIZE_BYTES = 16
MAX_AES_KEY_BYTES        = ((MAX_AES_KEY_BITS + 7) // 8)

# 
# // Table 218 - Defines for SM4 Algorithm Constants
# #define MAX_SM4_KEY_BITS          128
# #define MAX_SM4_BLOCK_SIZE_BYTES  16
# #define MAX_SM4_KEY_BYTES         ((MAX_SM4_KEY_BITS + 7) / 8)
MAX_SM4_KEY_BITS         = 128
MAX_SM4_BLOCK_SIZE_BYTES = 16
MAX_SM4_KEY_BYTES        = ((MAX_SM4_KEY_BITS + 7) // 8)

# 
# // Table 219 - Defines for Symmetric Algorithm Constants
# #define MAX_SYM_KEY_BITS    MAX_AES_KEY_BITS
# #define MAX_SYM_KEY_BYTES   MAX_AES_KEY_BYTES
# #define MAX_SYM_BLOCK_SIZE  MAX_AES_BLOCK_SIZE_BYTES
MAX_SYM_KEY_BITS   = MAX_AES_KEY_BITS
MAX_SYM_KEY_BYTES  = MAX_AES_KEY_BYTES
MAX_SYM_BLOCK_SIZE = MAX_AES_BLOCK_SIZE_BYTES

# 
# // Table 220 - Defines for Implementation Values
# typedef UINT16 BSIZE;
# #define BUFFER_ALIGNMENT     4
# #define IMPLEMENTATION_PCR   24
# #define PLATFORM_PCR         24
# #define DRTM_PCR             17
# #define NUM_LOCALITIES       5
# #define MAX_HANDLE_NUM       3
# #define MAX_ACTIVE_SESSIONS  64
BSIZE               = UINT16
BUFFER_ALIGNMENT    = 4
IMPLEMENTATION_PCR  = 24
PLATFORM_PCR        = 24
DRTM_PCR            = 17
NUM_LOCALITIES      = 5
MAX_HANDLE_NUM      = 3
MAX_ACTIVE_SESSIONS = 64
# typedef UINT16 CONTEXT_SLOT;
# typedef UINT64 CONTEXT_COUNTER;
CONTEXT_SLOT        = UINT16
CONTEXT_COUNTER     = UINT64
# #define MAX_LOADED_SESSIONS            3
# #define MAX_SESSION_NUM                3
# #define MAX_LOADED_OBJECTS             3
# #define MIN_EVICT_OBJECTS              2
# #define PCR_SELECT_MIN                 ((PLATFORM_PCR + 7) / 8)
# #define PCR_SELECT_MAX                 ((IMPLEMENTATION_PCR + 7) / 8)
# #define NUM_POLICY_PCR_GROUP           1
# #define NUM_AUTHVALUE_PCR_GROUP        1
# #define MAX_CONTEXT_SIZE               4000
# #define MAX_DIGEST_BUFFER              1024
# #define MAX_NV_INDEX_SIZE              1024
# #define MAX_CAP_BUFFER                 1024
# #define NV_MEMORY_SIZE                 16384
# #define NUM_STATIC_PCR                 16
# #define MAX_ALG_LIST_SIZE              64
# #define TIMER_PRESCALE                 100000
# #define PRIMARY_SEED_SIZE              32
# #define CONTEXT_ENCRYPT_ALG            TPM_ALG_AES
# #define CONTEXT_ENCRYPT_KEY_BITS       MAX_SYM_KEY_BITS
# #define CONTEXT_ENCRYPT_KEY_BYTES      ((CONTEXT_ENCRYPT_KEY_BITS + 7) / 8)
# #define CONTEXT_INTEGRITY_HASH_ALG     TPM_ALG_SHA256
# #define CONTEXT_INTEGRITY_HASH_SIZE    SHA256_DIGEST_SIZE
# #define PROOF_SIZE                     CONTEXT_INTEGRITY_HASH_SIZE
# #define NV_CLOCK_UPDATE_INTERVAL       12
# #define NUM_POLICY_PCR                 1
# #define MAX_COMMAND_SIZE               4096
# #define MAX_RESPONSE_SIZE              4096
# #define ORDERLY_BITS                   8
# #define MAX_ORDERLY_COUNT              ((1 << ORDERLY_BITS) - 1)
# #define ALG_ID_FIRST                   TPM_ALG_FIRST
# #define ALG_ID_LAST                    TPM_ALG_LAST
# #define MAX_SYM_DATA                   128
# #define MAX_RNG_ENTROPY_SIZE           64
# #define RAM_INDEX_SPACE                512
# #define RSA_DEFAULT_PUBLIC_EXPONENT    0x00010001
# #define CRT_FORMAT_RSA                 YES
# #define PRIVATE_VENDOR_SPECIFIC_BYTES  ((MAX_RSA_KEY_BYTES / 2) * ( 3 + CRT_FORMAT_RSA * 2))
MAX_LOADED_SESSIONS           = 3
MAX_SESSION_NUM               = 3
MAX_LOADED_OBJECTS            = 3
MIN_EVICT_OBJECTS             = 2
PCR_SELECT_MIN                = ((PLATFORM_PCR + 7) // 8)
PCR_SELECT_MAX                = ((IMPLEMENTATION_PCR + 7) // 8)
NUM_POLICY_PCR_GROUP          = 1
NUM_AUTHVALUE_PCR_GROUP       = 1
MAX_CONTEXT_SIZE              = 4000
MAX_DIGEST_BUFFER             = 1024
MAX_NV_INDEX_SIZE             = 1024
MAX_CAP_BUFFER                = 1024
NV_MEMORY_SIZE                = 16384
NUM_STATIC_PCR                = 16
MAX_ALG_LIST_SIZE             = 64
TIMER_PRESCALE                = 100000
PRIMARY_SEED_SIZE             = 32
TPM_ALG_AES                   = 0x0006
CONTEXT_ENCRYPT_ALG           = TPM_ALG_AES
CONTEXT_ENCRYPT_KEY_BITS      = MAX_SYM_KEY_BITS
CONTEXT_ENCRYPT_KEY_BYTES     = ((CONTEXT_ENCRYPT_KEY_BITS + 7) // 8)
TPM_ALG_SHA256                = 0x000B
CONTEXT_INTEGRITY_HASH_ALG    = TPM_ALG_SHA256
CONTEXT_INTEGRITY_HASH_SIZE   = SHA256_DIGEST_SIZE
PROOF_SIZE                    = CONTEXT_INTEGRITY_HASH_SIZE
NV_CLOCK_UPDATE_INTERVAL      = 12
NUM_POLICY_PCR                = 1
MAX_COMMAND_SIZE              = 4096
MAX_RESPONSE_SIZE             = 4096
ORDERLY_BITS                  = 8
MAX_ORDERLY_COUNT             = ((1 << ORDERLY_BITS) - 1)
TPM_ALG_FIRST                 = 0x0001
ALG_ID_FIRST                  = TPM_ALG_FIRST
TPM_ALG_LAST                  = 0x0044
ALG_ID_LAST                   = TPM_ALG_LAST
MAX_SYM_DATA                  = 128
MAX_RNG_ENTROPY_SIZE          = 64
RAM_INDEX_SPACE               = 512
RSA_DEFAULT_PUBLIC_EXPONENT   = 0x00010001
CRT_FORMAT_RSA                = YES
PRIVATE_VENDOR_SPECIFIC_BYTES = ((MAX_RSA_KEY_BYTES // 2) * ( 3 + CRT_FORMAT_RSA * 2))

# 
# // Capability related MAX_ value
# #define MAX_CAP_DATA        (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))
# #define MAX_CAP_ALGS        (MAX_CAP_DATA / sizeof(TPMS_ALG_PROPERTY))
# #define MAX_CAP_HANDLES     (MAX_CAP_DATA / sizeof(TPM_HANDLE))
# #define MAX_CAP_CC          (MAX_CAP_DATA / sizeof(TPM_CC))
# #define MAX_TPM_PROPERTIES  (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PROPERTY))
# #define MAX_PCR_PROPERTIES  (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PCR_SELECT))
# #define MAX_ECC_CURVES      (MAX_CAP_DATA / sizeof(TPM_ECC_CURVE))
# MAX_CAP_DATA        = (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))
# MAX_CAP_ALGS        = (MAX_CAP_DATA // sizeof(TPMS_ALG_PROPERTY))
# MAX_CAP_HANDLES     = (MAX_CAP_DATA // sizeof(Tpm12.TPM_HANDLE))
# MAX_CAP_CC          = (MAX_CAP_DATA // sizeof(TPM_CC))
# MAX_TPM_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PROPERTY))
# MAX_PCR_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PCR_SELECT))
# MAX_ECC_CURVES      = (MAX_CAP_DATA // sizeof(TPM_ECC_CURVE))

# 
# //
# // Always set 5 here, because we want to support all hash algo in BIOS.
# //
# #define HASH_COUNT  5
HASH_COUNT  = 5

# 
# // 5 Base Types
# 
# // Table 3 - Definition of Base Types
# typedef UINT8 BYTE;
BYTE = UINT8

# 
# // Table 4 - Definition of Types for Documentation Clarity
# //
# // NOTE: Comment because it has same name as TPM1.2 (value is same, so not runtime issue)
# //
# // typedef UINT32 TPM_ALGORITHM_ID;
# // typedef UINT32 TPM_MODIFIER_INDICATOR;
# typedef UINT32 TPM_AUTHORIZATION_SIZE;
# typedef UINT32 TPM_PARAMETER_SIZE;
# typedef UINT16 TPM_KEY_SIZE;
# typedef UINT16 TPM_KEY_BITS;
TPM_AUTHORIZATION_SIZE  = UINT32
TPM_PARAMETER_SIZE      = UINT32
TPM_KEY_SIZE            = UINT16
TPM_KEY_BITS            = UINT16

# 
# // 6 Constants
# 
# // Table 6 - TPM_GENERATED Constants
# typedef UINT32 TPM_GENERATED;
TPM_GENERATED       = UINT32
# #define TPM_GENERATED_VALUE  (TPM_GENERATED)(0xff544347)
TPM_GENERATED_VALUE = 0xff544347

# 
# // Table 7 - TPM_ALG_ID Constants
# typedef UINT16 TPM_ALG_ID;
TPM_ALG_ID          = UINT16

# //
# // NOTE: Comment some algo which has same name as TPM1.2 (value is same, so not runtime issue)
# //
# #define TPM_ALG_ERROR  (TPM_ALG_ID)(0x0000)
# #define TPM_ALG_FIRST  (TPM_ALG_ID)(0x0001)
TPM_ALG_ERROR       = 0x0000
# TPM_ALG_FIRST       = 0x0001
# // #define TPM_ALG_RSA            (TPM_ALG_ID)(0x0001)
# // #define TPM_ALG_SHA            (TPM_ALG_ID)(0x0004)
# #define TPM_ALG_SHA1  (TPM_ALG_ID)(0x0004)
TPM_ALG_SHA1        = 0x0004
# // #define TPM_ALG_HMAC           (TPM_ALG_ID)(0x0005)
# #define TPM_ALG_AES  (TPM_ALG_ID)(0x0006)
# TPM_ALG_AES         = 0x0006
# // #define TPM_ALG_MGF1           (TPM_ALG_ID)(0x0007)
# #define TPM_ALG_KEYEDHASH  (TPM_ALG_ID)(0x0008)
TPM_ALG_KEYEDHASH   = 0x0008
# // #define TPM_ALG_XOR            (TPM_ALG_ID)(0x000A)
# #define TPM_ALG_SHA256          (TPM_ALG_ID)(0x000B)
# #define TPM_ALG_SHA384          (TPM_ALG_ID)(0x000C)
# #define TPM_ALG_SHA512          (TPM_ALG_ID)(0x000D)
# #define TPM_ALG_NULL            (TPM_ALG_ID)(0x0010)
# #define TPM_ALG_SM3_256         (TPM_ALG_ID)(0x0012)
# #define TPM_ALG_SM4             (TPM_ALG_ID)(0x0013)
# #define TPM_ALG_RSASSA          (TPM_ALG_ID)(0x0014)
# #define TPM_ALG_RSAES           (TPM_ALG_ID)(0x0015)
# #define TPM_ALG_RSAPSS          (TPM_ALG_ID)(0x0016)
# #define TPM_ALG_OAEP            (TPM_ALG_ID)(0x0017)
# #define TPM_ALG_ECDSA           (TPM_ALG_ID)(0x0018)
# #define TPM_ALG_ECDH            (TPM_ALG_ID)(0x0019)
# #define TPM_ALG_ECDAA           (TPM_ALG_ID)(0x001A)
# #define TPM_ALG_SM2             (TPM_ALG_ID)(0x001B)
# #define TPM_ALG_ECSCHNORR       (TPM_ALG_ID)(0x001C)
# #define TPM_ALG_ECMQV           (TPM_ALG_ID)(0x001D)
# #define TPM_ALG_KDF1_SP800_56a  (TPM_ALG_ID)(0x0020)
# #define TPM_ALG_KDF2            (TPM_ALG_ID)(0x0021)
# #define TPM_ALG_KDF1_SP800_108  (TPM_ALG_ID)(0x0022)
# #define TPM_ALG_ECC             (TPM_ALG_ID)(0x0023)
# #define TPM_ALG_SYMCIPHER       (TPM_ALG_ID)(0x0025)
# #define TPM_ALG_CTR             (TPM_ALG_ID)(0x0040)
# #define TPM_ALG_OFB             (TPM_ALG_ID)(0x0041)
# #define TPM_ALG_CBC             (TPM_ALG_ID)(0x0042)
# #define TPM_ALG_CFB             (TPM_ALG_ID)(0x0043)
# #define TPM_ALG_ECB             (TPM_ALG_ID)(0x0044)
# #define TPM_ALG_LAST            (TPM_ALG_ID)(0x0044)
# TPM_ALG_SHA256          = 0x000B
TPM_ALG_SHA384          = 0x000C
TPM_ALG_SHA512          = 0x000D
TPM_ALG_NULL            = 0x0010
TPM_ALG_SM3_256         = 0x0012
TPM_ALG_SM4             = 0x0013
TPM_ALG_RSASSA          = 0x0014
TPM_ALG_RSAES           = 0x0015
TPM_ALG_RSAPSS          = 0x0016
TPM_ALG_OAEP            = 0x0017
TPM_ALG_ECDSA           = 0x0018
TPM_ALG_ECDH            = 0x0019
TPM_ALG_ECDAA           = 0x001A
TPM_ALG_SM2             = 0x001B
TPM_ALG_ECSCHNORR       = 0x001C
TPM_ALG_ECMQV           = 0x001D
TPM_ALG_KDF1_SP800_56a  = 0x0020
TPM_ALG_KDF2            = 0x0021
TPM_ALG_KDF1_SP800_108  = 0x0022
TPM_ALG_ECC             = 0x0023
TPM_ALG_SYMCIPHER       = 0x0025
TPM_ALG_CTR             = 0x0040
TPM_ALG_OFB             = 0x0041
TPM_ALG_CBC             = 0x0042
TPM_ALG_CFB             = 0x0043
TPM_ALG_ECB             = 0x0044
# TPM_ALG_LAST            = 0x0044

# 
# // Table 8 - TPM_ECC_CURVE Constants
# typedef UINT16 TPM_ECC_CURVE;
# #define TPM_ECC_NONE       (TPM_ECC_CURVE)(0x0000)
# #define TPM_ECC_NIST_P192  (TPM_ECC_CURVE)(0x0001)
# #define TPM_ECC_NIST_P224  (TPM_ECC_CURVE)(0x0002)
# #define TPM_ECC_NIST_P256  (TPM_ECC_CURVE)(0x0003)
# #define TPM_ECC_NIST_P384  (TPM_ECC_CURVE)(0x0004)
# #define TPM_ECC_NIST_P521  (TPM_ECC_CURVE)(0x0005)
# #define TPM_ECC_BN_P256    (TPM_ECC_CURVE)(0x0010)
# #define TPM_ECC_BN_P638    (TPM_ECC_CURVE)(0x0011)
# #define TPM_ECC_SM2_P256   (TPM_ECC_CURVE)(0x0020)
TPM_ECC_CURVE = UINT16
TPM_ECC_NONE       = 0x0000
TPM_ECC_NIST_P192  = 0x0001
TPM_ECC_NIST_P224  = 0x0002
TPM_ECC_NIST_P256  = 0x0003
TPM_ECC_NIST_P384  = 0x0004
TPM_ECC_NIST_P521  = 0x0005
TPM_ECC_BN_P256    = 0x0010
TPM_ECC_BN_P638    = 0x0011
TPM_ECC_SM2_P256   = 0x0020

# 
# // Table 11 - TPM_CC Constants (Numeric Order)
# typedef UINT32 TPM_CC;
TPM_CC                            = UINT32

# #define TPM_CC_FIRST                       (TPM_CC)(0x0000011F)
# #define TPM_CC_PP_FIRST                    (TPM_CC)(0x0000011F)
# #define TPM_CC_NV_UndefineSpaceSpecial     (TPM_CC)(0x0000011F)
# #define TPM_CC_EvictControl                (TPM_CC)(0x00000120)
# #define TPM_CC_HierarchyControl            (TPM_CC)(0x00000121)
# #define TPM_CC_NV_UndefineSpace            (TPM_CC)(0x00000122)
# #define TPM_CC_ChangeEPS                   (TPM_CC)(0x00000124)
# #define TPM_CC_ChangePPS                   (TPM_CC)(0x00000125)
# #define TPM_CC_Clear                       (TPM_CC)(0x00000126)
# #define TPM_CC_ClearControl                (TPM_CC)(0x00000127)
# #define TPM_CC_ClockSet                    (TPM_CC)(0x00000128)
# #define TPM_CC_HierarchyChangeAuth         (TPM_CC)(0x00000129)
# #define TPM_CC_NV_DefineSpace              (TPM_CC)(0x0000012A)
# #define TPM_CC_PCR_Allocate                (TPM_CC)(0x0000012B)
# #define TPM_CC_PCR_SetAuthPolicy           (TPM_CC)(0x0000012C)
# #define TPM_CC_PP_Commands                 (TPM_CC)(0x0000012D)
# #define TPM_CC_SetPrimaryPolicy            (TPM_CC)(0x0000012E)
# #define TPM_CC_FieldUpgradeStart           (TPM_CC)(0x0000012F)
# #define TPM_CC_ClockRateAdjust             (TPM_CC)(0x00000130)
# #define TPM_CC_CreatePrimary               (TPM_CC)(0x00000131)
# #define TPM_CC_NV_GlobalWriteLock          (TPM_CC)(0x00000132)
# #define TPM_CC_PP_LAST                     (TPM_CC)(0x00000132)
# #define TPM_CC_GetCommandAuditDigest       (TPM_CC)(0x00000133)
# #define TPM_CC_NV_Increment                (TPM_CC)(0x00000134)
# #define TPM_CC_NV_SetBits                  (TPM_CC)(0x00000135)
# #define TPM_CC_NV_Extend                   (TPM_CC)(0x00000136)
# #define TPM_CC_NV_Write                    (TPM_CC)(0x00000137)
# #define TPM_CC_NV_WriteLock                (TPM_CC)(0x00000138)
# #define TPM_CC_DictionaryAttackLockReset   (TPM_CC)(0x00000139)
# #define TPM_CC_DictionaryAttackParameters  (TPM_CC)(0x0000013A)
# #define TPM_CC_NV_ChangeAuth               (TPM_CC)(0x0000013B)
# #define TPM_CC_PCR_Event                   (TPM_CC)(0x0000013C)
# #define TPM_CC_PCR_Reset                   (TPM_CC)(0x0000013D)
# #define TPM_CC_SequenceComplete            (TPM_CC)(0x0000013E)
# #define TPM_CC_SetAlgorithmSet             (TPM_CC)(0x0000013F)
# #define TPM_CC_SetCommandCodeAuditStatus   (TPM_CC)(0x00000140)
# #define TPM_CC_FieldUpgradeData            (TPM_CC)(0x00000141)
# #define TPM_CC_IncrementalSelfTest         (TPM_CC)(0x00000142)
# #define TPM_CC_SelfTest                    (TPM_CC)(0x00000143)
# #define TPM_CC_Startup                     (TPM_CC)(0x00000144)
# #define TPM_CC_Shutdown                    (TPM_CC)(0x00000145)
# #define TPM_CC_StirRandom                  (TPM_CC)(0x00000146)
# #define TPM_CC_ActivateCredential          (TPM_CC)(0x00000147)
# #define TPM_CC_Certify                     (TPM_CC)(0x00000148)
# #define TPM_CC_PolicyNV                    (TPM_CC)(0x00000149)
# #define TPM_CC_CertifyCreation             (TPM_CC)(0x0000014A)
# #define TPM_CC_Duplicate                   (TPM_CC)(0x0000014B)
# #define TPM_CC_GetTime                     (TPM_CC)(0x0000014C)
# #define TPM_CC_GetSessionAuditDigest       (TPM_CC)(0x0000014D)
# #define TPM_CC_NV_Read                     (TPM_CC)(0x0000014E)
# #define TPM_CC_NV_ReadLock                 (TPM_CC)(0x0000014F)
# #define TPM_CC_ObjectChangeAuth            (TPM_CC)(0x00000150)
# #define TPM_CC_PolicySecret                (TPM_CC)(0x00000151)
# #define TPM_CC_Rewrap                      (TPM_CC)(0x00000152)
# #define TPM_CC_Create                      (TPM_CC)(0x00000153)
# #define TPM_CC_ECDH_ZGen                   (TPM_CC)(0x00000154)
# #define TPM_CC_HMAC                        (TPM_CC)(0x00000155)
# #define TPM_CC_Import                      (TPM_CC)(0x00000156)
# #define TPM_CC_Load                        (TPM_CC)(0x00000157)
# #define TPM_CC_Quote                       (TPM_CC)(0x00000158)
# #define TPM_CC_RSA_Decrypt                 (TPM_CC)(0x00000159)
# #define TPM_CC_HMAC_Start                  (TPM_CC)(0x0000015B)
# #define TPM_CC_SequenceUpdate              (TPM_CC)(0x0000015C)
# #define TPM_CC_Sign                        (TPM_CC)(0x0000015D)
# #define TPM_CC_Unseal                      (TPM_CC)(0x0000015E)
# #define TPM_CC_PolicySigned                (TPM_CC)(0x00000160)
# #define TPM_CC_ContextLoad                 (TPM_CC)(0x00000161)
# #define TPM_CC_ContextSave                 (TPM_CC)(0x00000162)
# #define TPM_CC_ECDH_KeyGen                 (TPM_CC)(0x00000163)
# #define TPM_CC_EncryptDecrypt              (TPM_CC)(0x00000164)
# #define TPM_CC_FlushContext                (TPM_CC)(0x00000165)
# #define TPM_CC_LoadExternal                (TPM_CC)(0x00000167)
# #define TPM_CC_MakeCredential              (TPM_CC)(0x00000168)
# #define TPM_CC_NV_ReadPublic               (TPM_CC)(0x00000169)
# #define TPM_CC_PolicyAuthorize             (TPM_CC)(0x0000016A)
# #define TPM_CC_PolicyAuthValue             (TPM_CC)(0x0000016B)
# #define TPM_CC_PolicyCommandCode           (TPM_CC)(0x0000016C)
# #define TPM_CC_PolicyCounterTimer          (TPM_CC)(0x0000016D)
# #define TPM_CC_PolicyCpHash                (TPM_CC)(0x0000016E)
# #define TPM_CC_PolicyLocality              (TPM_CC)(0x0000016F)
# #define TPM_CC_PolicyNameHash              (TPM_CC)(0x00000170)
# #define TPM_CC_PolicyOR                    (TPM_CC)(0x00000171)
# #define TPM_CC_PolicyTicket                (TPM_CC)(0x00000172)
# #define TPM_CC_ReadPublic                  (TPM_CC)(0x00000173)
# #define TPM_CC_RSA_Encrypt                 (TPM_CC)(0x00000174)
# #define TPM_CC_StartAuthSession            (TPM_CC)(0x00000176)
# #define TPM_CC_VerifySignature             (TPM_CC)(0x00000177)
# #define TPM_CC_ECC_Parameters              (TPM_CC)(0x00000178)
# #define TPM_CC_FirmwareRead                (TPM_CC)(0x00000179)
# #define TPM_CC_GetCapability               (TPM_CC)(0x0000017A)
# #define TPM_CC_GetRandom                   (TPM_CC)(0x0000017B)
# #define TPM_CC_GetTestResult               (TPM_CC)(0x0000017C)
# #define TPM_CC_Hash                        (TPM_CC)(0x0000017D)
# #define TPM_CC_PCR_Read                    (TPM_CC)(0x0000017E)
# #define TPM_CC_PolicyPCR                   (TPM_CC)(0x0000017F)
# #define TPM_CC_PolicyRestart               (TPM_CC)(0x00000180)
# #define TPM_CC_ReadClock                   (TPM_CC)(0x00000181)
# #define TPM_CC_PCR_Extend                  (TPM_CC)(0x00000182)
# #define TPM_CC_PCR_SetAuthValue            (TPM_CC)(0x00000183)
# #define TPM_CC_NV_Certify                  (TPM_CC)(0x00000184)
# #define TPM_CC_EventSequenceComplete       (TPM_CC)(0x00000185)
# #define TPM_CC_HashSequenceStart           (TPM_CC)(0x00000186)
# #define TPM_CC_PolicyPhysicalPresence      (TPM_CC)(0x00000187)
# #define TPM_CC_PolicyDuplicationSelect     (TPM_CC)(0x00000188)
# #define TPM_CC_PolicyGetDigest             (TPM_CC)(0x00000189)
# #define TPM_CC_TestParms                   (TPM_CC)(0x0000018A)
# #define TPM_CC_Commit                      (TPM_CC)(0x0000018B)
# #define TPM_CC_PolicyPassword              (TPM_CC)(0x0000018C)
# #define TPM_CC_ZGen_2Phase                 (TPM_CC)(0x0000018D)
# #define TPM_CC_EC_Ephemeral                (TPM_CC)(0x0000018E)
# #define TPM_CC_LAST                        (TPM_CC)(0x0000018E)
TPM_CC_FIRST                      = 0x0000011F
TPM_CC_PP_FIRST                   = 0x0000011F
TPM_CC_NV_UndefineSpaceSpecial    = 0x0000011F
TPM_CC_EvictControl               = 0x00000120
TPM_CC_HierarchyControl           = 0x00000121
TPM_CC_NV_UndefineSpace           = 0x00000122
TPM_CC_ChangeEPS                  = 0x00000124
TPM_CC_ChangePPS                  = 0x00000125
TPM_CC_Clear                      = 0x00000126
TPM_CC_ClearControl               = 0x00000127
TPM_CC_ClockSet                   = 0x00000128
TPM_CC_HierarchyChangeAuth        = 0x00000129
TPM_CC_NV_DefineSpace             = 0x0000012A
TPM_CC_PCR_Allocate               = 0x0000012B
TPM_CC_PCR_SetAuthPolicy          = 0x0000012C
TPM_CC_PP_Commands                = 0x0000012D
TPM_CC_SetPrimaryPolicy           = 0x0000012E
TPM_CC_FieldUpgradeStart          = 0x0000012F
TPM_CC_ClockRateAdjust            = 0x00000130
TPM_CC_CreatePrimary              = 0x00000131
TPM_CC_NV_GlobalWriteLock         = 0x00000132
TPM_CC_PP_LAST                    = 0x00000132
TPM_CC_GetCommandAuditDigest      = 0x00000133
TPM_CC_NV_Increment               = 0x00000134
TPM_CC_NV_SetBits                 = 0x00000135
TPM_CC_NV_Extend                  = 0x00000136
TPM_CC_NV_Write                   = 0x00000137
TPM_CC_NV_WriteLock               = 0x00000138
TPM_CC_DictionaryAttackLockReset  = 0x00000139
TPM_CC_DictionaryAttackParameters = 0x0000013A
TPM_CC_NV_ChangeAuth              = 0x0000013B
TPM_CC_PCR_Event                  = 0x0000013C
TPM_CC_PCR_Reset                  = 0x0000013D
TPM_CC_SequenceComplete           = 0x0000013E
TPM_CC_SetAlgorithmSet            = 0x0000013F
TPM_CC_SetCommandCodeAuditStatus  = 0x00000140
TPM_CC_FieldUpgradeData           = 0x00000141
TPM_CC_IncrementalSelfTest        = 0x00000142
TPM_CC_SelfTest                   = 0x00000143
TPM_CC_Startup                    = 0x00000144
TPM_CC_Shutdown                   = 0x00000145
TPM_CC_StirRandom                 = 0x00000146
TPM_CC_ActivateCredential         = 0x00000147
TPM_CC_Certify                    = 0x00000148
TPM_CC_PolicyNV                   = 0x00000149
TPM_CC_CertifyCreation            = 0x0000014A
TPM_CC_Duplicate                  = 0x0000014B
TPM_CC_GetTime                    = 0x0000014C
TPM_CC_GetSessionAuditDigest      = 0x0000014D
TPM_CC_NV_Read                    = 0x0000014E
TPM_CC_NV_ReadLock                = 0x0000014F
TPM_CC_ObjectChangeAuth           = 0x00000150
TPM_CC_PolicySecret               = 0x00000151
TPM_CC_Rewrap                     = 0x00000152
TPM_CC_Create                     = 0x00000153
TPM_CC_ECDH_ZGen                  = 0x00000154
TPM_CC_HMAC                       = 0x00000155
TPM_CC_Import                     = 0x00000156
TPM_CC_Load                       = 0x00000157
TPM_CC_Quote                      = 0x00000158
TPM_CC_RSA_Decrypt                = 0x00000159
TPM_CC_HMAC_Start                 = 0x0000015B
TPM_CC_SequenceUpdate             = 0x0000015C
TPM_CC_Sign                       = 0x0000015D
TPM_CC_Unseal                     = 0x0000015E
TPM_CC_PolicySigned               = 0x00000160
TPM_CC_ContextLoad                = 0x00000161
TPM_CC_ContextSave                = 0x00000162
TPM_CC_ECDH_KeyGen                = 0x00000163
TPM_CC_EncryptDecrypt             = 0x00000164
TPM_CC_FlushContext               = 0x00000165
TPM_CC_LoadExternal               = 0x00000167
TPM_CC_MakeCredential             = 0x00000168
TPM_CC_NV_ReadPublic              = 0x00000169
TPM_CC_PolicyAuthorize            = 0x0000016A
TPM_CC_PolicyAuthValue            = 0x0000016B
TPM_CC_PolicyCommandCode          = 0x0000016C
TPM_CC_PolicyCounterTimer         = 0x0000016D
TPM_CC_PolicyCpHash               = 0x0000016E
TPM_CC_PolicyLocality             = 0x0000016F
TPM_CC_PolicyNameHash             = 0x00000170
TPM_CC_PolicyOR                   = 0x00000171
TPM_CC_PolicyTicket               = 0x00000172
TPM_CC_ReadPublic                 = 0x00000173
TPM_CC_RSA_Encrypt                = 0x00000174
TPM_CC_StartAuthSession           = 0x00000176
TPM_CC_VerifySignature            = 0x00000177
TPM_CC_ECC_Parameters             = 0x00000178
TPM_CC_FirmwareRead               = 0x00000179
TPM_CC_GetCapability              = 0x0000017A
TPM_CC_GetRandom                  = 0x0000017B
TPM_CC_GetTestResult              = 0x0000017C
TPM_CC_Hash                       = 0x0000017D
TPM_CC_PCR_Read                   = 0x0000017E
TPM_CC_PolicyPCR                  = 0x0000017F
TPM_CC_PolicyRestart              = 0x00000180
TPM_CC_ReadClock                  = 0x00000181
TPM_CC_PCR_Extend                 = 0x00000182
TPM_CC_PCR_SetAuthValue           = 0x00000183
TPM_CC_NV_Certify                 = 0x00000184
TPM_CC_EventSequenceComplete      = 0x00000185
TPM_CC_HashSequenceStart          = 0x00000186
TPM_CC_PolicyPhysicalPresence     = 0x00000187
TPM_CC_PolicyDuplicationSelect    = 0x00000188
TPM_CC_PolicyGetDigest            = 0x00000189
TPM_CC_TestParms                  = 0x0000018A
TPM_CC_Commit                     = 0x0000018B
TPM_CC_PolicyPassword             = 0x0000018C
TPM_CC_ZGen_2Phase                = 0x0000018D
TPM_CC_EC_Ephemeral               = 0x0000018E
TPM_CC_LAST                       = 0x0000018E

# 
# // Table 15 - TPM_RC Constants (Actions)
# typedef UINT32 TPM_RC;
# #define TPM_RC_SUCCESS            (TPM_RC)(0x000)
# #define TPM_RC_BAD_TAG            (TPM_RC)(0x030)
# #define RC_VER1                   (TPM_RC)(0x100)
# #define TPM_RC_INITIALIZE         (TPM_RC)(RC_VER1 + 0x000)
# #define TPM_RC_FAILURE            (TPM_RC)(RC_VER1 + 0x001)
# #define TPM_RC_SEQUENCE           (TPM_RC)(RC_VER1 + 0x003)
# #define TPM_RC_PRIVATE            (TPM_RC)(RC_VER1 + 0x00B)
# #define TPM_RC_HMAC               (TPM_RC)(RC_VER1 + 0x019)
# #define TPM_RC_DISABLED           (TPM_RC)(RC_VER1 + 0x020)
# #define TPM_RC_EXCLUSIVE          (TPM_RC)(RC_VER1 + 0x021)
# #define TPM_RC_AUTH_TYPE          (TPM_RC)(RC_VER1 + 0x024)
# #define TPM_RC_AUTH_MISSING       (TPM_RC)(RC_VER1 + 0x025)
# #define TPM_RC_POLICY             (TPM_RC)(RC_VER1 + 0x026)
# #define TPM_RC_PCR                (TPM_RC)(RC_VER1 + 0x027)
# #define TPM_RC_PCR_CHANGED        (TPM_RC)(RC_VER1 + 0x028)
# #define TPM_RC_UPGRADE            (TPM_RC)(RC_VER1 + 0x02D)
# #define TPM_RC_TOO_MANY_CONTEXTS  (TPM_RC)(RC_VER1 + 0x02E)
# #define TPM_RC_AUTH_UNAVAILABLE   (TPM_RC)(RC_VER1 + 0x02F)
# #define TPM_RC_REBOOT             (TPM_RC)(RC_VER1 + 0x030)
# #define TPM_RC_UNBALANCED         (TPM_RC)(RC_VER1 + 0x031)
# #define TPM_RC_COMMAND_SIZE       (TPM_RC)(RC_VER1 + 0x042)
# #define TPM_RC_COMMAND_CODE       (TPM_RC)(RC_VER1 + 0x043)
# #define TPM_RC_AUTHSIZE           (TPM_RC)(RC_VER1 + 0x044)
# #define TPM_RC_AUTH_CONTEXT       (TPM_RC)(RC_VER1 + 0x045)
# #define TPM_RC_NV_RANGE           (TPM_RC)(RC_VER1 + 0x046)
# #define TPM_RC_NV_SIZE            (TPM_RC)(RC_VER1 + 0x047)
# #define TPM_RC_NV_LOCKED          (TPM_RC)(RC_VER1 + 0x048)
# #define TPM_RC_NV_AUTHORIZATION   (TPM_RC)(RC_VER1 + 0x049)
# #define TPM_RC_NV_UNINITIALIZED   (TPM_RC)(RC_VER1 + 0x04A)
# #define TPM_RC_NV_SPACE           (TPM_RC)(RC_VER1 + 0x04B)
# #define TPM_RC_NV_DEFINED         (TPM_RC)(RC_VER1 + 0x04C)
# #define TPM_RC_BAD_CONTEXT        (TPM_RC)(RC_VER1 + 0x050)
# #define TPM_RC_CPHASH             (TPM_RC)(RC_VER1 + 0x051)
# #define TPM_RC_PARENT             (TPM_RC)(RC_VER1 + 0x052)
# #define TPM_RC_NEEDS_TEST         (TPM_RC)(RC_VER1 + 0x053)
# #define TPM_RC_NO_RESULT          (TPM_RC)(RC_VER1 + 0x054)
# #define TPM_RC_SENSITIVE          (TPM_RC)(RC_VER1 + 0x055)
# #define RC_MAX_FM0                (TPM_RC)(RC_VER1 + 0x07F)
# #define RC_FMT1                   (TPM_RC)(0x080)
# #define TPM_RC_ASYMMETRIC         (TPM_RC)(RC_FMT1 + 0x001)
# #define TPM_RC_ATTRIBUTES         (TPM_RC)(RC_FMT1 + 0x002)
# #define TPM_RC_HASH               (TPM_RC)(RC_FMT1 + 0x003)
# #define TPM_RC_VALUE              (TPM_RC)(RC_FMT1 + 0x004)
# #define TPM_RC_HIERARCHY          (TPM_RC)(RC_FMT1 + 0x005)
# #define TPM_RC_KEY_SIZE           (TPM_RC)(RC_FMT1 + 0x007)
# #define TPM_RC_MGF                (TPM_RC)(RC_FMT1 + 0x008)
# #define TPM_RC_MODE               (TPM_RC)(RC_FMT1 + 0x009)
# #define TPM_RC_TYPE               (TPM_RC)(RC_FMT1 + 0x00A)
# #define TPM_RC_HANDLE             (TPM_RC)(RC_FMT1 + 0x00B)
# #define TPM_RC_KDF                (TPM_RC)(RC_FMT1 + 0x00C)
# #define TPM_RC_RANGE              (TPM_RC)(RC_FMT1 + 0x00D)
# #define TPM_RC_AUTH_FAIL          (TPM_RC)(RC_FMT1 + 0x00E)
# #define TPM_RC_NONCE              (TPM_RC)(RC_FMT1 + 0x00F)
# #define TPM_RC_PP                 (TPM_RC)(RC_FMT1 + 0x010)
# #define TPM_RC_SCHEME             (TPM_RC)(RC_FMT1 + 0x012)
# #define TPM_RC_SIZE               (TPM_RC)(RC_FMT1 + 0x015)
# #define TPM_RC_SYMMETRIC          (TPM_RC)(RC_FMT1 + 0x016)
# #define TPM_RC_TAG                (TPM_RC)(RC_FMT1 + 0x017)
# #define TPM_RC_SELECTOR           (TPM_RC)(RC_FMT1 + 0x018)
# #define TPM_RC_INSUFFICIENT       (TPM_RC)(RC_FMT1 + 0x01A)
# #define TPM_RC_SIGNATURE          (TPM_RC)(RC_FMT1 + 0x01B)
# #define TPM_RC_KEY                (TPM_RC)(RC_FMT1 + 0x01C)
# #define TPM_RC_POLICY_FAIL        (TPM_RC)(RC_FMT1 + 0x01D)
# #define TPM_RC_INTEGRITY          (TPM_RC)(RC_FMT1 + 0x01F)
# #define TPM_RC_TICKET             (TPM_RC)(RC_FMT1 + 0x020)
# #define TPM_RC_RESERVED_BITS      (TPM_RC)(RC_FMT1 + 0x021)
# #define TPM_RC_BAD_AUTH           (TPM_RC)(RC_FMT1 + 0x022)
# #define TPM_RC_EXPIRED            (TPM_RC)(RC_FMT1 + 0x023)
# #define TPM_RC_POLICY_CC          (TPM_RC)(RC_FMT1 + 0x024 )
# #define TPM_RC_BINDING            (TPM_RC)(RC_FMT1 + 0x025)
# #define TPM_RC_CURVE              (TPM_RC)(RC_FMT1 + 0x026)
# #define TPM_RC_ECC_POINT          (TPM_RC)(RC_FMT1 + 0x027)
# #define RC_WARN                   (TPM_RC)(0x900)
# #define TPM_RC_CONTEXT_GAP        (TPM_RC)(RC_WARN + 0x001)
# #define TPM_RC_OBJECT_MEMORY      (TPM_RC)(RC_WARN + 0x002)
# #define TPM_RC_SESSION_MEMORY     (TPM_RC)(RC_WARN + 0x003)
# #define TPM_RC_MEMORY             (TPM_RC)(RC_WARN + 0x004)
# #define TPM_RC_SESSION_HANDLES    (TPM_RC)(RC_WARN + 0x005)
# #define TPM_RC_OBJECT_HANDLES     (TPM_RC)(RC_WARN + 0x006)
# #define TPM_RC_LOCALITY           (TPM_RC)(RC_WARN + 0x007)
# #define TPM_RC_YIELDED            (TPM_RC)(RC_WARN + 0x008)
# #define TPM_RC_CANCELED           (TPM_RC)(RC_WARN + 0x009)
# #define TPM_RC_TESTING            (TPM_RC)(RC_WARN + 0x00A)
# #define TPM_RC_REFERENCE_H0       (TPM_RC)(RC_WARN + 0x010)
# #define TPM_RC_REFERENCE_H1       (TPM_RC)(RC_WARN + 0x011)
# #define TPM_RC_REFERENCE_H2       (TPM_RC)(RC_WARN + 0x012)
# #define TPM_RC_REFERENCE_H3       (TPM_RC)(RC_WARN + 0x013)
# #define TPM_RC_REFERENCE_H4       (TPM_RC)(RC_WARN + 0x014)
# #define TPM_RC_REFERENCE_H5       (TPM_RC)(RC_WARN + 0x015)
# #define TPM_RC_REFERENCE_H6       (TPM_RC)(RC_WARN + 0x016)
# #define TPM_RC_REFERENCE_S0       (TPM_RC)(RC_WARN + 0x018)
# #define TPM_RC_REFERENCE_S1       (TPM_RC)(RC_WARN + 0x019)
# #define TPM_RC_REFERENCE_S2       (TPM_RC)(RC_WARN + 0x01A)
# #define TPM_RC_REFERENCE_S3       (TPM_RC)(RC_WARN + 0x01B)
# #define TPM_RC_REFERENCE_S4       (TPM_RC)(RC_WARN + 0x01C)
# #define TPM_RC_REFERENCE_S5       (TPM_RC)(RC_WARN + 0x01D)
# #define TPM_RC_REFERENCE_S6       (TPM_RC)(RC_WARN + 0x01E)
# #define TPM_RC_NV_RATE            (TPM_RC)(RC_WARN + 0x020)
# #define TPM_RC_LOCKOUT            (TPM_RC)(RC_WARN + 0x021)
# #define TPM_RC_RETRY              (TPM_RC)(RC_WARN + 0x022)
# #define TPM_RC_NV_UNAVAILABLE     (TPM_RC)(RC_WARN + 0x023)
# #define TPM_RC_NOT_USED           (TPM_RC)(RC_WARN + 0x7F)
# #define TPM_RC_H                  (TPM_RC)(0x000)
# #define TPM_RC_P                  (TPM_RC)(0x040)
# #define TPM_RC_S                  (TPM_RC)(0x800)
# #define TPM_RC_1                  (TPM_RC)(0x100)
# #define TPM_RC_2                  (TPM_RC)(0x200)
# #define TPM_RC_3                  (TPM_RC)(0x300)
# #define TPM_RC_4                  (TPM_RC)(0x400)
# #define TPM_RC_5                  (TPM_RC)(0x500)
# #define TPM_RC_6                  (TPM_RC)(0x600)
# #define TPM_RC_7                  (TPM_RC)(0x700)
# #define TPM_RC_8                  (TPM_RC)(0x800)
# #define TPM_RC_9                  (TPM_RC)(0x900)
# #define TPM_RC_A                  (TPM_RC)(0xA00)
# #define TPM_RC_B                  (TPM_RC)(0xB00)
# #define TPM_RC_C                  (TPM_RC)(0xC00)
# #define TPM_RC_D                  (TPM_RC)(0xD00)
# #define TPM_RC_E                  (TPM_RC)(0xE00)
# #define TPM_RC_F                  (TPM_RC)(0xF00)
# #define TPM_RC_N_MASK             (TPM_RC)(0xF00)
TPM_RC                   = UINT32
TPM_RC_SUCCESS           = 0x000
TPM_RC_BAD_TAG           = 0x030
RC_VER1                  = 0x100
TPM_RC_INITIALIZE        = RC_VER1 + 0x000
TPM_RC_FAILURE           = RC_VER1 + 0x001
TPM_RC_SEQUENCE          = RC_VER1 + 0x003
TPM_RC_PRIVATE           = RC_VER1 + 0x00B
TPM_RC_HMAC              = RC_VER1 + 0x019
TPM_RC_DISABLED          = RC_VER1 + 0x020
TPM_RC_EXCLUSIVE         = RC_VER1 + 0x021
TPM_RC_AUTH_TYPE         = RC_VER1 + 0x024
TPM_RC_AUTH_MISSING      = RC_VER1 + 0x025
TPM_RC_POLICY            = RC_VER1 + 0x026
TPM_RC_PCR               = RC_VER1 + 0x027
TPM_RC_PCR_CHANGED       = RC_VER1 + 0x028
TPM_RC_UPGRADE           = RC_VER1 + 0x02D
TPM_RC_TOO_MANY_CONTEXTS = RC_VER1 + 0x02E
TPM_RC_AUTH_UNAVAILABLE  = RC_VER1 + 0x02F
TPM_RC_REBOOT            = RC_VER1 + 0x030
TPM_RC_UNBALANCED        = RC_VER1 + 0x031
TPM_RC_COMMAND_SIZE      = RC_VER1 + 0x042
TPM_RC_COMMAND_CODE      = RC_VER1 + 0x043
TPM_RC_AUTHSIZE          = RC_VER1 + 0x044
TPM_RC_AUTH_CONTEXT      = RC_VER1 + 0x045
TPM_RC_NV_RANGE          = RC_VER1 + 0x046
TPM_RC_NV_SIZE           = RC_VER1 + 0x047
TPM_RC_NV_LOCKED         = RC_VER1 + 0x048
TPM_RC_NV_AUTHORIZATION  = RC_VER1 + 0x049
TPM_RC_NV_UNINITIALIZED  = RC_VER1 + 0x04A
TPM_RC_NV_SPACE          = RC_VER1 + 0x04B
TPM_RC_NV_DEFINED        = RC_VER1 + 0x04C
TPM_RC_BAD_CONTEXT       = RC_VER1 + 0x050
TPM_RC_CPHASH            = RC_VER1 + 0x051
TPM_RC_PARENT            = RC_VER1 + 0x052
TPM_RC_NEEDS_TEST        = RC_VER1 + 0x053
TPM_RC_NO_RESULT         = RC_VER1 + 0x054
TPM_RC_SENSITIVE         = RC_VER1 + 0x055
RC_MAX_FM0               = RC_VER1 + 0x07F
RC_FMT1                  = 0x080
TPM_RC_ASYMMETRIC        = RC_FMT1 + 0x001
TPM_RC_ATTRIBUTES        = RC_FMT1 + 0x002
TPM_RC_HASH              = RC_FMT1 + 0x003
TPM_RC_VALUE             = RC_FMT1 + 0x004
TPM_RC_HIERARCHY         = RC_FMT1 + 0x005
TPM_RC_KEY_SIZE          = RC_FMT1 + 0x007
TPM_RC_MGF               = RC_FMT1 + 0x008
TPM_RC_MODE              = RC_FMT1 + 0x009
TPM_RC_TYPE              = RC_FMT1 + 0x00A
TPM_RC_HANDLE            = RC_FMT1 + 0x00B
TPM_RC_KDF               = RC_FMT1 + 0x00C
TPM_RC_RANGE             = RC_FMT1 + 0x00D
TPM_RC_AUTH_FAIL         = RC_FMT1 + 0x00E
TPM_RC_NONCE             = RC_FMT1 + 0x00F
TPM_RC_PP                = RC_FMT1 + 0x010
TPM_RC_SCHEME            = RC_FMT1 + 0x012
TPM_RC_SIZE              = RC_FMT1 + 0x015
TPM_RC_SYMMETRIC         = RC_FMT1 + 0x016
TPM_RC_TAG               = RC_FMT1 + 0x017
TPM_RC_SELECTOR          = RC_FMT1 + 0x018
TPM_RC_INSUFFICIENT      = RC_FMT1 + 0x01A
TPM_RC_SIGNATURE         = RC_FMT1 + 0x01B
TPM_RC_KEY               = RC_FMT1 + 0x01C
TPM_RC_POLICY_FAIL       = RC_FMT1 + 0x01D
TPM_RC_INTEGRITY         = RC_FMT1 + 0x01F
TPM_RC_TICKET            = RC_FMT1 + 0x020
TPM_RC_RESERVED_BITS     = RC_FMT1 + 0x021
TPM_RC_BAD_AUTH          = RC_FMT1 + 0x022
TPM_RC_EXPIRED           = RC_FMT1 + 0x023
TPM_RC_POLICY_CC         = RC_FMT1 + 0x024e
TPM_RC_BINDING           = RC_FMT1 + 0x025
TPM_RC_CURVE             = RC_FMT1 + 0x026
TPM_RC_ECC_POINT         = RC_FMT1 + 0x027
RC_WARN                  = 0x900
TPM_RC_CONTEXT_GAP       = RC_WARN + 0x001
TPM_RC_OBJECT_MEMORY     = RC_WARN + 0x002
TPM_RC_SESSION_MEMORY    = RC_WARN + 0x003
TPM_RC_MEMORY            = RC_WARN + 0x004
TPM_RC_SESSION_HANDLES   = RC_WARN + 0x005
TPM_RC_OBJECT_HANDLES    = RC_WARN + 0x006
TPM_RC_LOCALITY          = RC_WARN + 0x007
TPM_RC_YIELDED           = RC_WARN + 0x008
TPM_RC_CANCELED          = RC_WARN + 0x009
TPM_RC_TESTING           = RC_WARN + 0x00A
TPM_RC_REFERENCE_H0      = RC_WARN + 0x010
TPM_RC_REFERENCE_H1      = RC_WARN + 0x011
TPM_RC_REFERENCE_H2      = RC_WARN + 0x012
TPM_RC_REFERENCE_H3      = RC_WARN + 0x013
TPM_RC_REFERENCE_H4      = RC_WARN + 0x014
TPM_RC_REFERENCE_H5      = RC_WARN + 0x015
TPM_RC_REFERENCE_H6      = RC_WARN + 0x016
TPM_RC_REFERENCE_S0      = RC_WARN + 0x018
TPM_RC_REFERENCE_S1      = RC_WARN + 0x019
TPM_RC_REFERENCE_S2      = RC_WARN + 0x01A
TPM_RC_REFERENCE_S3      = RC_WARN + 0x01B
TPM_RC_REFERENCE_S4      = RC_WARN + 0x01C
TPM_RC_REFERENCE_S5      = RC_WARN + 0x01D
TPM_RC_REFERENCE_S6      = RC_WARN + 0x01E
TPM_RC_NV_RATE           = RC_WARN + 0x020
TPM_RC_LOCKOUT           = RC_WARN + 0x021
TPM_RC_RETRY             = RC_WARN + 0x022
TPM_RC_NV_UNAVAILABLE    = RC_WARN + 0x023
TPM_RC_NOT_USED          = RC_WARN + 0x7F
TPM_RC_H                 = 0x000
TPM_RC_P                 = 0x040
TPM_RC_S                 = 0x800
TPM_RC_1                 = 0x100
TPM_RC_2                 = 0x200
TPM_RC_3                 = 0x300
TPM_RC_4                 = 0x400
TPM_RC_5                 = 0x500
TPM_RC_6                 = 0x600
TPM_RC_7                 = 0x700
TPM_RC_8                 = 0x800
TPM_RC_9                 = 0x900
TPM_RC_A                 = 0xA00
TPM_RC_B                 = 0xB00
TPM_RC_C                 = 0xC00
TPM_RC_D                 = 0xD00
TPM_RC_E                 = 0xE00
TPM_RC_F                 = 0xF00
TPM_RC_N_MASK            = 0xF00

# 
# // Table 16 - TPM_CLOCK_ADJUST Constants
# typedef INT8 TPM_CLOCK_ADJUST;
# #define TPM_CLOCK_COARSE_SLOWER  (TPM_CLOCK_ADJUST)(-3)
# #define TPM_CLOCK_MEDIUM_SLOWER  (TPM_CLOCK_ADJUST)(-2)
# #define TPM_CLOCK_FINE_SLOWER    (TPM_CLOCK_ADJUST)(-1)
# #define TPM_CLOCK_NO_CHANGE      (TPM_CLOCK_ADJUST)(0)
# #define TPM_CLOCK_FINE_FASTER    (TPM_CLOCK_ADJUST)(1)
# #define TPM_CLOCK_MEDIUM_FASTER  (TPM_CLOCK_ADJUST)(2)
# #define TPM_CLOCK_COARSE_FASTER  (TPM_CLOCK_ADJUST)(3)
TPM_CLOCK_ADJUST        = INT8
TPM_CLOCK_COARSE_SLOWER = -3
TPM_CLOCK_MEDIUM_SLOWER = -2
TPM_CLOCK_FINE_SLOWER   = -1
TPM_CLOCK_NO_CHANGE     = 0
TPM_CLOCK_FINE_FASTER   = 1
TPM_CLOCK_MEDIUM_FASTER = 2
TPM_CLOCK_COARSE_FASTER = 3

# 
# // Table 17 - TPM_EO Constants
# typedef UINT16 TPM_EO;
# #define TPM_EO_EQ           (TPM_EO)(0x0000)
# #define TPM_EO_NEQ          (TPM_EO)(0x0001)
# #define TPM_EO_SIGNED_GT    (TPM_EO)(0x0002)
# #define TPM_EO_UNSIGNED_GT  (TPM_EO)(0x0003)
# #define TPM_EO_SIGNED_LT    (TPM_EO)(0x0004)
# #define TPM_EO_UNSIGNED_LT  (TPM_EO)(0x0005)
# #define TPM_EO_SIGNED_GE    (TPM_EO)(0x0006)
# #define TPM_EO_UNSIGNED_GE  (TPM_EO)(0x0007)
# #define TPM_EO_SIGNED_LE    (TPM_EO)(0x0008)
# #define TPM_EO_UNSIGNED_LE  (TPM_EO)(0x0009)
# #define TPM_EO_BITSET       (TPM_EO)(0x000A)
# #define TPM_EO_BITCLEAR     (TPM_EO)(0x000B)
TPM_EO             = UINT16
TPM_EO_EQ          = 0x0000
TPM_EO_NEQ         = 0x0001
TPM_EO_SIGNED_GT   = 0x0002
TPM_EO_UNSIGNED_GT = 0x0003
TPM_EO_SIGNED_LT   = 0x0004
TPM_EO_UNSIGNED_LT = 0x0005
TPM_EO_SIGNED_GE   = 0x0006
TPM_EO_UNSIGNED_GE = 0x0007
TPM_EO_SIGNED_LE   = 0x0008
TPM_EO_UNSIGNED_LE = 0x0009
TPM_EO_BITSET      = 0x000A
TPM_EO_BITCLEAR    = 0x000B

# 
# // Table 18 - TPM_ST Constants
# typedef UINT16 TPM_ST;
# #define TPM_ST_RSP_COMMAND           (TPM_ST)(0x00C4)
# #define TPM_ST_NULL                  (TPM_ST)(0X8000)
# #define TPM_ST_NO_SESSIONS           (TPM_ST)(0x8001)
# #define TPM_ST_SESSIONS              (TPM_ST)(0x8002)
# #define TPM_ST_ATTEST_NV             (TPM_ST)(0x8014)
# #define TPM_ST_ATTEST_COMMAND_AUDIT  (TPM_ST)(0x8015)
# #define TPM_ST_ATTEST_SESSION_AUDIT  (TPM_ST)(0x8016)
# #define TPM_ST_ATTEST_CERTIFY        (TPM_ST)(0x8017)
# #define TPM_ST_ATTEST_QUOTE          (TPM_ST)(0x8018)
# #define TPM_ST_ATTEST_TIME           (TPM_ST)(0x8019)
# #define TPM_ST_ATTEST_CREATION       (TPM_ST)(0x801A)
# #define TPM_ST_CREATION              (TPM_ST)(0x8021)
# #define TPM_ST_VERIFIED              (TPM_ST)(0x8022)
# #define TPM_ST_AUTH_SECRET           (TPM_ST)(0x8023)
# #define TPM_ST_HASHCHECK             (TPM_ST)(0x8024)
# #define TPM_ST_AUTH_SIGNED           (TPM_ST)(0x8025)
# #define TPM_ST_FU_MANIFEST           (TPM_ST)(0x8029)
TPM_ST                      = UINT16
TPM_ST_RSP_COMMAND          = 0x00C4
TPM_ST_NULL                 = 0X8000
TPM_ST_NO_SESSIONS          = 0x8001
TPM_ST_SESSIONS             = 0x8002
TPM_ST_ATTEST_NV            = 0x8014
TPM_ST_ATTEST_COMMAND_AUDIT = 0x8015
TPM_ST_ATTEST_SESSION_AUDIT = 0x8016
TPM_ST_ATTEST_CERTIFY       = 0x8017
TPM_ST_ATTEST_QUOTE         = 0x8018
TPM_ST_ATTEST_TIME          = 0x8019
TPM_ST_ATTEST_CREATION      = 0x801A
TPM_ST_CREATION             = 0x8021
TPM_ST_VERIFIED             = 0x8022
TPM_ST_AUTH_SECRET          = 0x8023
TPM_ST_HASHCHECK            = 0x8024
TPM_ST_AUTH_SIGNED          = 0x8025
TPM_ST_FU_MANIFEST          = 0x8029

# 
# // Table 19 - TPM_SU Constants
# typedef UINT16 TPM_SU;
# #define TPM_SU_CLEAR  (TPM_SU)(0x0000)
# #define TPM_SU_STATE  (TPM_SU)(0x0001)
TPM_SU       = UINT16
TPM_SU_CLEAR = 0x0000
TPM_SU_STATE = 0x0001

# 
# // Table 20 - TPM_SE Constants
# typedef UINT8 TPM_SE;
# #define TPM_SE_HMAC    (TPM_SE)(0x00)
# #define TPM_SE_POLICY  (TPM_SE)(0x01)
# #define TPM_SE_TRIAL   (TPM_SE)(0x03)
TPM_SE        = UINT8
TPM_SE_HMAC   = 0x00
TPM_SE_POLICY = 0x01
TPM_SE_TRIAL  = 0x03

# 
# // Table 21 - TPM_CAP Constants
# typedef UINT32 TPM_CAP;
TPM_CAP                 = UINT32

# #define TPM_CAP_FIRST            (TPM_CAP)(0x00000000)
# #define TPM_CAP_ALGS             (TPM_CAP)(0x00000000)
# #define TPM_CAP_HANDLES          (TPM_CAP)(0x00000001)
# #define TPM_CAP_COMMANDS         (TPM_CAP)(0x00000002)
# #define TPM_CAP_PP_COMMANDS      (TPM_CAP)(0x00000003)
# #define TPM_CAP_AUDIT_COMMANDS   (TPM_CAP)(0x00000004)
# #define TPM_CAP_PCRS             (TPM_CAP)(0x00000005)
# #define TPM_CAP_TPM_PROPERTIES   (TPM_CAP)(0x00000006)
# #define TPM_CAP_PCR_PROPERTIES   (TPM_CAP)(0x00000007)
# #define TPM_CAP_ECC_CURVES       (TPM_CAP)(0x00000008)
# #define TPM_CAP_LAST             (TPM_CAP)(0x00000008)
# #define TPM_CAP_VENDOR_PROPERTY  (TPM_CAP)(0x00000100)
TPM_CAP_FIRST           = 0x00000000
TPM_CAP_ALGS            = 0x00000000
TPM_CAP_HANDLES         = 0x00000001
TPM_CAP_COMMANDS        = 0x00000002
TPM_CAP_PP_COMMANDS     = 0x00000003
TPM_CAP_AUDIT_COMMANDS  = 0x00000004
TPM_CAP_PCRS            = 0x00000005
TPM_CAP_TPM_PROPERTIES  = 0x00000006
TPM_CAP_PCR_PROPERTIES  = 0x00000007
TPM_CAP_ECC_CURVES      = 0x00000008
TPM_CAP_LAST            = 0x00000008
TPM_CAP_VENDOR_PROPERTY = 0x00000100

# 
# // Table 22 - TPM_PT Constants
# typedef UINT32 TPM_PT;
# #define TPM_PT_NONE                 (TPM_PT)(0x00000000)
# #define PT_GROUP                    (TPM_PT)(0x00000100)
# #define PT_FIXED                    (TPM_PT)(PT_GROUP * 1)
# #define TPM_PT_FAMILY_INDICATOR     (TPM_PT)(PT_FIXED + 0)
# #define TPM_PT_LEVEL                (TPM_PT)(PT_FIXED + 1)
# #define TPM_PT_REVISION             (TPM_PT)(PT_FIXED + 2)
# #define TPM_PT_DAY_OF_YEAR          (TPM_PT)(PT_FIXED + 3)
# #define TPM_PT_YEAR                 (TPM_PT)(PT_FIXED + 4)
# #define TPM_PT_MANUFACTURER         (TPM_PT)(PT_FIXED + 5)
# #define TPM_PT_VENDOR_STRING_1      (TPM_PT)(PT_FIXED + 6)
# #define TPM_PT_VENDOR_STRING_2      (TPM_PT)(PT_FIXED + 7)
# #define TPM_PT_VENDOR_STRING_3      (TPM_PT)(PT_FIXED + 8)
# #define TPM_PT_VENDOR_STRING_4      (TPM_PT)(PT_FIXED + 9)
# #define TPM_PT_VENDOR_TPM_TYPE      (TPM_PT)(PT_FIXED + 10)
# #define TPM_PT_FIRMWARE_VERSION_1   (TPM_PT)(PT_FIXED + 11)
# #define TPM_PT_FIRMWARE_VERSION_2   (TPM_PT)(PT_FIXED + 12)
# #define TPM_PT_INPUT_BUFFER         (TPM_PT)(PT_FIXED + 13)
# #define TPM_PT_HR_TRANSIENT_MIN     (TPM_PT)(PT_FIXED + 14)
# #define TPM_PT_HR_PERSISTENT_MIN    (TPM_PT)(PT_FIXED + 15)
# #define TPM_PT_HR_LOADED_MIN        (TPM_PT)(PT_FIXED + 16)
# #define TPM_PT_ACTIVE_SESSIONS_MAX  (TPM_PT)(PT_FIXED + 17)
# #define TPM_PT_PCR_COUNT            (TPM_PT)(PT_FIXED + 18)
# #define TPM_PT_PCR_SELECT_MIN       (TPM_PT)(PT_FIXED + 19)
# #define TPM_PT_CONTEXT_GAP_MAX      (TPM_PT)(PT_FIXED + 20)
# #define TPM_PT_NV_COUNTERS_MAX      (TPM_PT)(PT_FIXED + 22)
# #define TPM_PT_NV_INDEX_MAX         (TPM_PT)(PT_FIXED + 23)
# #define TPM_PT_MEMORY               (TPM_PT)(PT_FIXED + 24)
# #define TPM_PT_CLOCK_UPDATE         (TPM_PT)(PT_FIXED + 25)
# #define TPM_PT_CONTEXT_HASH         (TPM_PT)(PT_FIXED + 26)
# #define TPM_PT_CONTEXT_SYM          (TPM_PT)(PT_FIXED + 27)
# #define TPM_PT_CONTEXT_SYM_SIZE     (TPM_PT)(PT_FIXED + 28)
# #define TPM_PT_ORDERLY_COUNT        (TPM_PT)(PT_FIXED + 29)
# #define TPM_PT_MAX_COMMAND_SIZE     (TPM_PT)(PT_FIXED + 30)
# #define TPM_PT_MAX_RESPONSE_SIZE    (TPM_PT)(PT_FIXED + 31)
# #define TPM_PT_MAX_DIGEST           (TPM_PT)(PT_FIXED + 32)
# #define TPM_PT_MAX_OBJECT_CONTEXT   (TPM_PT)(PT_FIXED + 33)
# #define TPM_PT_MAX_SESSION_CONTEXT  (TPM_PT)(PT_FIXED + 34)
# #define TPM_PT_PS_FAMILY_INDICATOR  (TPM_PT)(PT_FIXED + 35)
# #define TPM_PT_PS_LEVEL             (TPM_PT)(PT_FIXED + 36)
# #define TPM_PT_PS_REVISION          (TPM_PT)(PT_FIXED + 37)
# #define TPM_PT_PS_DAY_OF_YEAR       (TPM_PT)(PT_FIXED + 38)
# #define TPM_PT_PS_YEAR              (TPM_PT)(PT_FIXED + 39)
# #define TPM_PT_SPLIT_MAX            (TPM_PT)(PT_FIXED + 40)
# #define TPM_PT_TOTAL_COMMANDS       (TPM_PT)(PT_FIXED + 41)
# #define TPM_PT_LIBRARY_COMMANDS     (TPM_PT)(PT_FIXED + 42)
# #define TPM_PT_VENDOR_COMMANDS      (TPM_PT)(PT_FIXED + 43)
# #define PT_VAR                      (TPM_PT)(PT_GROUP * 2)
# #define TPM_PT_PERMANENT            (TPM_PT)(PT_VAR + 0)
# #define TPM_PT_STARTUP_CLEAR        (TPM_PT)(PT_VAR + 1)
# #define TPM_PT_HR_NV_INDEX          (TPM_PT)(PT_VAR + 2)
# #define TPM_PT_HR_LOADED            (TPM_PT)(PT_VAR + 3)
# #define TPM_PT_HR_LOADED_AVAIL      (TPM_PT)(PT_VAR + 4)
# #define TPM_PT_HR_ACTIVE            (TPM_PT)(PT_VAR + 5)
# #define TPM_PT_HR_ACTIVE_AVAIL      (TPM_PT)(PT_VAR + 6)
# #define TPM_PT_HR_TRANSIENT_AVAIL   (TPM_PT)(PT_VAR + 7)
# #define TPM_PT_HR_PERSISTENT        (TPM_PT)(PT_VAR + 8)
# #define TPM_PT_HR_PERSISTENT_AVAIL  (TPM_PT)(PT_VAR + 9)
# #define TPM_PT_NV_COUNTERS          (TPM_PT)(PT_VAR + 10)
# #define TPM_PT_NV_COUNTERS_AVAIL    (TPM_PT)(PT_VAR + 11)
# #define TPM_PT_ALGORITHM_SET        (TPM_PT)(PT_VAR + 12)
# #define TPM_PT_LOADED_CURVES        (TPM_PT)(PT_VAR + 13)
# #define TPM_PT_LOCKOUT_COUNTER      (TPM_PT)(PT_VAR + 14)
# #define TPM_PT_MAX_AUTH_FAIL        (TPM_PT)(PT_VAR + 15)
# #define TPM_PT_LOCKOUT_INTERVAL     (TPM_PT)(PT_VAR + 16)
# #define TPM_PT_LOCKOUT_RECOVERY     (TPM_PT)(PT_VAR + 17)
# #define TPM_PT_NV_WRITE_RECOVERY    (TPM_PT)(PT_VAR + 18)
# #define TPM_PT_AUDIT_COUNTER_0      (TPM_PT)(PT_VAR + 19)
# #define TPM_PT_AUDIT_COUNTER_1      (TPM_PT)(PT_VAR + 20)
TPM_PT                     = UINT32
TPM_PT_NONE                = 0x00000000
PT_GROUP                   = 0x00000100
PT_FIXED                   = PT_GROUP * 1
TPM_PT_FAMILY_INDICATOR    = PT_FIXED + 0
TPM_PT_LEVEL               = PT_FIXED + 1
TPM_PT_REVISION            = PT_FIXED + 2
TPM_PT_DAY_OF_YEAR         = PT_FIXED + 3
TPM_PT_YEAR                = PT_FIXED + 4
TPM_PT_MANUFACTURER        = PT_FIXED + 5
TPM_PT_VENDOR_STRING_1     = PT_FIXED + 6
TPM_PT_VENDOR_STRING_2     = PT_FIXED + 7
TPM_PT_VENDOR_STRING_3     = PT_FIXED + 8
TPM_PT_VENDOR_STRING_4     = PT_FIXED + 9
TPM_PT_VENDOR_TPM_TYPE     = PT_FIXED + 10
TPM_PT_FIRMWARE_VERSION_1  = PT_FIXED + 11
TPM_PT_FIRMWARE_VERSION_2  = PT_FIXED + 12
TPM_PT_INPUT_BUFFER        = PT_FIXED + 13
TPM_PT_HR_TRANSIENT_MIN    = PT_FIXED + 14
TPM_PT_HR_PERSISTENT_MIN   = PT_FIXED + 15
TPM_PT_HR_LOADED_MIN       = PT_FIXED + 16
TPM_PT_ACTIVE_SESSIONS_MAX = PT_FIXED + 17
TPM_PT_PCR_COUNT           = PT_FIXED + 18
TPM_PT_PCR_SELECT_MIN      = PT_FIXED + 19
TPM_PT_CONTEXT_GAP_MAX     = PT_FIXED + 20
TPM_PT_NV_COUNTERS_MAX     = PT_FIXED + 22
TPM_PT_NV_INDEX_MAX        = PT_FIXED + 23
TPM_PT_MEMORY              = PT_FIXED + 24
TPM_PT_CLOCK_UPDATE        = PT_FIXED + 25
TPM_PT_CONTEXT_HASH        = PT_FIXED + 26
TPM_PT_CONTEXT_SYM         = PT_FIXED + 27
TPM_PT_CONTEXT_SYM_SIZE    = PT_FIXED + 28
TPM_PT_ORDERLY_COUNT       = PT_FIXED + 29
TPM_PT_MAX_COMMAND_SIZE    = PT_FIXED + 30
TPM_PT_MAX_RESPONSE_SIZE   = PT_FIXED + 31
TPM_PT_MAX_DIGEST          = PT_FIXED + 32
TPM_PT_MAX_OBJECT_CONTEXT  = PT_FIXED + 33
TPM_PT_MAX_SESSION_CONTEXT = PT_FIXED + 34
TPM_PT_PS_FAMILY_INDICATOR = PT_FIXED + 35
TPM_PT_PS_LEVEL            = PT_FIXED + 36
TPM_PT_PS_REVISION         = PT_FIXED + 37
TPM_PT_PS_DAY_OF_YEAR      = PT_FIXED + 38
TPM_PT_PS_YEAR             = PT_FIXED + 39
TPM_PT_SPLIT_MAX           = PT_FIXED + 40
TPM_PT_TOTAL_COMMANDS      = PT_FIXED + 41
TPM_PT_LIBRARY_COMMANDS    = PT_FIXED + 42
TPM_PT_VENDOR_COMMANDS     = PT_FIXED + 43
PT_VAR                     = PT_GROUP * 2
TPM_PT_PERMANENT           = PT_VAR + 0
TPM_PT_STARTUP_CLEAR       = PT_VAR + 1
TPM_PT_HR_NV_INDEX         = PT_VAR + 2
TPM_PT_HR_LOADED           = PT_VAR + 3
TPM_PT_HR_LOADED_AVAIL     = PT_VAR + 4
TPM_PT_HR_ACTIVE           = PT_VAR + 5
TPM_PT_HR_ACTIVE_AVAIL     = PT_VAR + 6
TPM_PT_HR_TRANSIENT_AVAIL  = PT_VAR + 7
TPM_PT_HR_PERSISTENT       = PT_VAR + 8
TPM_PT_HR_PERSISTENT_AVAIL = PT_VAR + 9
TPM_PT_NV_COUNTERS         = PT_VAR + 10
TPM_PT_NV_COUNTERS_AVAIL   = PT_VAR + 11
TPM_PT_ALGORITHM_SET       = PT_VAR + 12
TPM_PT_LOADED_CURVES       = PT_VAR + 13
TPM_PT_LOCKOUT_COUNTER     = PT_VAR + 14
TPM_PT_MAX_AUTH_FAIL       = PT_VAR + 15
TPM_PT_LOCKOUT_INTERVAL    = PT_VAR + 16
TPM_PT_LOCKOUT_RECOVERY    = PT_VAR + 17
TPM_PT_NV_WRITE_RECOVERY   = PT_VAR + 18
TPM_PT_AUDIT_COUNTER_0     = PT_VAR + 19
TPM_PT_AUDIT_COUNTER_1     = PT_VAR + 20

# 
# // Table 23 - TPM_PT_PCR Constants
# typedef UINT32 TPM_PT_PCR;
# #define TPM_PT_PCR_FIRST         (TPM_PT_PCR)(0x00000000)
# #define TPM_PT_PCR_SAVE          (TPM_PT_PCR)(0x00000000)
# #define TPM_PT_PCR_EXTEND_L0     (TPM_PT_PCR)(0x00000001)
# #define TPM_PT_PCR_RESET_L0      (TPM_PT_PCR)(0x00000002)
# #define TPM_PT_PCR_EXTEND_L1     (TPM_PT_PCR)(0x00000003)
# #define TPM_PT_PCR_RESET_L1      (TPM_PT_PCR)(0x00000004)
# #define TPM_PT_PCR_EXTEND_L2     (TPM_PT_PCR)(0x00000005)
# #define TPM_PT_PCR_RESET_L2      (TPM_PT_PCR)(0x00000006)
# #define TPM_PT_PCR_EXTEND_L3     (TPM_PT_PCR)(0x00000007)
# #define TPM_PT_PCR_RESET_L3      (TPM_PT_PCR)(0x00000008)
# #define TPM_PT_PCR_EXTEND_L4     (TPM_PT_PCR)(0x00000009)
# #define TPM_PT_PCR_RESET_L4      (TPM_PT_PCR)(0x0000000A)
# #define TPM_PT_PCR_NO_INCREMENT  (TPM_PT_PCR)(0x00000011)
# #define TPM_PT_PCR_DRTM_RESET    (TPM_PT_PCR)(0x00000012)
# #define TPM_PT_PCR_POLICY        (TPM_PT_PCR)(0x00000013)
# #define TPM_PT_PCR_AUTH          (TPM_PT_PCR)(0x00000014)
# #define TPM_PT_PCR_LAST          (TPM_PT_PCR)(0x00000014)
TPM_PT_PCR              = UINT32
TPM_PT_PCR_FIRST        = 0x00000000
TPM_PT_PCR_SAVE         = 0x00000000
TPM_PT_PCR_EXTEND_L0    = 0x00000001
TPM_PT_PCR_RESET_L0     = 0x00000002
TPM_PT_PCR_EXTEND_L1    = 0x00000003
TPM_PT_PCR_RESET_L1     = 0x00000004
TPM_PT_PCR_EXTEND_L2    = 0x00000005
TPM_PT_PCR_RESET_L2     = 0x00000006
TPM_PT_PCR_EXTEND_L3    = 0x00000007
TPM_PT_PCR_RESET_L3     = 0x00000008
TPM_PT_PCR_EXTEND_L4    = 0x00000009
TPM_PT_PCR_RESET_L4     = 0x0000000A
TPM_PT_PCR_NO_INCREMENT = 0x00000011
TPM_PT_PCR_DRTM_RESET   = 0x00000012
TPM_PT_PCR_POLICY       = 0x00000013
TPM_PT_PCR_AUTH         = 0x00000014
TPM_PT_PCR_LAST         = 0x00000014

# 
# // Table 24 - TPM_PS Constants
# typedef UINT32 TPM_PS;
# #define TPM_PS_MAIN            (TPM_PS)(0x00000000)
# #define TPM_PS_PC              (TPM_PS)(0x00000001)
# #define TPM_PS_PDA             (TPM_PS)(0x00000002)
# #define TPM_PS_CELL_PHONE      (TPM_PS)(0x00000003)
# #define TPM_PS_SERVER          (TPM_PS)(0x00000004)
# #define TPM_PS_PERIPHERAL      (TPM_PS)(0x00000005)
# #define TPM_PS_TSS             (TPM_PS)(0x00000006)
# #define TPM_PS_STORAGE         (TPM_PS)(0x00000007)
# #define TPM_PS_AUTHENTICATION  (TPM_PS)(0x00000008)
# #define TPM_PS_EMBEDDED        (TPM_PS)(0x00000009)
# #define TPM_PS_HARDCOPY        (TPM_PS)(0x0000000A)
# #define TPM_PS_INFRASTRUCTURE  (TPM_PS)(0x0000000B)
# #define TPM_PS_VIRTUALIZATION  (TPM_PS)(0x0000000C)
# #define TPM_PS_TNC             (TPM_PS)(0x0000000D)
# #define TPM_PS_MULTI_TENANT    (TPM_PS)(0x0000000E)
# #define TPM_PS_TC              (TPM_PS)(0x0000000F)
TPM_PS                = UINT32
TPM_PS_MAIN           = 0x00000000
TPM_PS_PC             = 0x00000001
TPM_PS_PDA            = 0x00000002
TPM_PS_CELL_PHONE     = 0x00000003
TPM_PS_SERVER         = 0x00000004
TPM_PS_PERIPHERAL     = 0x00000005
TPM_PS_TSS            = 0x00000006
TPM_PS_STORAGE        = 0x00000007
TPM_PS_AUTHENTICATION = 0x00000008
TPM_PS_EMBEDDED       = 0x00000009
TPM_PS_HARDCOPY       = 0x0000000A
TPM_PS_INFRASTRUCTURE = 0x0000000B
TPM_PS_VIRTUALIZATION = 0x0000000C
TPM_PS_TNC            = 0x0000000D
TPM_PS_MULTI_TENANT   = 0x0000000E
TPM_PS_TC             = 0x0000000F

# 
# // 7 Handles
# 
# // Table 25 - Handles Types
# //
# // NOTE: Comment because it has same name as TPM1.2 (value is same, so not runtime issue)
# //
# // typedef UINT32    TPM_HANDLE;
# 
# // Table 26 - TPM_HT Constants
# typedef UINT8 TPM_HT;
# #define TPM_HT_PCR             (TPM_HT)(0x00)
# #define TPM_HT_NV_INDEX        (TPM_HT)(0x01)
# #define TPM_HT_HMAC_SESSION    (TPM_HT)(0x02)
# #define TPM_HT_LOADED_SESSION  (TPM_HT)(0x02)
# #define TPM_HT_POLICY_SESSION  (TPM_HT)(0x03)
# #define TPM_HT_ACTIVE_SESSION  (TPM_HT)(0x03)
# #define TPM_HT_PERMANENT       (TPM_HT)(0x40)
# #define TPM_HT_TRANSIENT       (TPM_HT)(0x80)
# #define TPM_HT_PERSISTENT      (TPM_HT)(0x81)
TPM_HT                = UINT8
TPM_HT_PCR            = 0x00
TPM_HT_NV_INDEX       = 0x01
TPM_HT_HMAC_SESSION   = 0x02
TPM_HT_LOADED_SESSION = 0x02
TPM_HT_POLICY_SESSION = 0x03
TPM_HT_ACTIVE_SESSION = 0x03
TPM_HT_PERMANENT      = 0x40
TPM_HT_TRANSIENT      = 0x80
TPM_HT_PERSISTENT     = 0x81

# 
# // Table 27 - TPM_RH Constants
# typedef UINT32 TPM_RH;
# #define TPM_RH_FIRST        (TPM_RH)(0x40000000)
# #define TPM_RH_SRK          (TPM_RH)(0x40000000)
# #define TPM_RH_OWNER        (TPM_RH)(0x40000001)
# #define TPM_RH_REVOKE       (TPM_RH)(0x40000002)
# #define TPM_RH_TRANSPORT    (TPM_RH)(0x40000003)
# #define TPM_RH_OPERATOR     (TPM_RH)(0x40000004)
# #define TPM_RH_ADMIN        (TPM_RH)(0x40000005)
# #define TPM_RH_EK           (TPM_RH)(0x40000006)
# #define TPM_RH_NULL         (TPM_RH)(0x40000007)
# #define TPM_RH_UNASSIGNED   (TPM_RH)(0x40000008)
# #define TPM_RS_PW           (TPM_RH)(0x40000009)
# #define TPM_RH_LOCKOUT      (TPM_RH)(0x4000000A)
# #define TPM_RH_ENDORSEMENT  (TPM_RH)(0x4000000B)
# #define TPM_RH_PLATFORM     (TPM_RH)(0x4000000C)
# #define TPM_RH_PLATFORM_NV  (TPM_RH)(0x4000000D)
# #define TPM_RH_AUTH_00      (TPM_RH)(0x40000010)
# #define TPM_RH_AUTH_FF      (TPM_RH)(0x4000010F)
# #define TPM_RH_LAST         (TPM_RH)(0x4000010F)
TPM_RH             = UINT32
TPM_RH_FIRST       = 0x40000000
TPM_RH_SRK         = 0x40000000
TPM_RH_OWNER       = 0x40000001
TPM_RH_REVOKE      = 0x40000002
TPM_RH_TRANSPORT   = 0x40000003
TPM_RH_OPERATOR    = 0x40000004
TPM_RH_ADMIN       = 0x40000005
TPM_RH_EK          = 0x40000006
TPM_RH_NULL        = 0x40000007
TPM_RH_UNASSIGNED  = 0x40000008
TPM_RS_PW          = 0x40000009
TPM_RH_LOCKOUT     = 0x4000000A
TPM_RH_ENDORSEMENT = 0x4000000B
TPM_RH_PLATFORM    = 0x4000000C
TPM_RH_LAST        = 0x4000000C

# 
# // Table 28 - TPM_HC Constants
# typedef TPM_HANDLE TPM_HC;
# #define HR_HANDLE_MASK        (TPM_HC)(0x00FFFFFF)
# #define HR_RANGE_MASK         (TPM_HC)(0xFF000000)
# #define HR_SHIFT              (TPM_HC)(24)
# #define HR_PCR                (TPM_HC)((TPM_HC)TPM_HT_PCR << HR_SHIFT)
# #define HR_HMAC_SESSION       (TPM_HC)((TPM_HC)TPM_HT_HMAC_SESSION << HR_SHIFT)
# #define HR_POLICY_SESSION     (TPM_HC)((TPM_HC)TPM_HT_POLICY_SESSION << HR_SHIFT)
# #define HR_TRANSIENT          (TPM_HC)((TPM_HC)TPM_HT_TRANSIENT << HR_SHIFT)
# #define HR_PERSISTENT         (TPM_HC)((TPM_HC)TPM_HT_PERSISTENT << HR_SHIFT)
# #define HR_NV_INDEX           (TPM_HC)((TPM_HC)TPM_HT_NV_INDEX << HR_SHIFT)
# #define HR_PERMANENT          (TPM_HC)((TPM_HC)TPM_HT_PERMANENT << HR_SHIFT)
# #define PCR_FIRST             (TPM_HC)(HR_PCR + 0)
# #define PCR_LAST              (TPM_HC)(PCR_FIRST + IMPLEMENTATION_PCR - 1)
# #define HMAC_SESSION_FIRST    (TPM_HC)(HR_HMAC_SESSION + 0)
# #define HMAC_SESSION_LAST     (TPM_HC)(HMAC_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1)
# #define LOADED_SESSION_FIRST  (TPM_HC)(HMAC_SESSION_FIRST)
# #define LOADED_SESSION_LAST   (TPM_HC)(HMAC_SESSION_LAST)
# #define POLICY_SESSION_FIRST  (TPM_HC)(HR_POLICY_SESSION + 0)
# #define POLICY_SESSION_LAST   (TPM_HC)(POLICY_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1)
# #define TRANSIENT_FIRST       (TPM_HC)(HR_TRANSIENT + 0)
# #define ACTIVE_SESSION_FIRST  (TPM_HC)(POLICY_SESSION_FIRST)
# #define ACTIVE_SESSION_LAST   (TPM_HC)(POLICY_SESSION_LAST)
# #define TRANSIENT_LAST        (TPM_HC)(TRANSIENT_FIRST+MAX_LOADED_OBJECTS - 1)
# #define PERSISTENT_FIRST      (TPM_HC)(HR_PERSISTENT + 0)
# #define PERSISTENT_LAST       (TPM_HC)(PERSISTENT_FIRST + 0x00FFFFFF)
# #define PLATFORM_PERSISTENT   (TPM_HC)(PERSISTENT_FIRST + 0x00800000)
# #define NV_INDEX_FIRST        (TPM_HC)(HR_NV_INDEX + 0)
# #define NV_INDEX_LAST         (TPM_HC)(NV_INDEX_FIRST + 0x00FFFFFF)
# #define PERMANENT_FIRST       (TPM_HC)(TPM_RH_FIRST)
# #define PERMANENT_LAST        (TPM_HC)(TPM_RH_LAST)
TPM_HC               = Tpm12.TPM_HANDLE
HR_HANDLE_MASK       = 0x00FFFFFF
HR_RANGE_MASK        = 0xFF000000
HR_SHIFT             = 24
HR_PCR               = TPM_HT_PCR << HR_SHIFT
HR_HMAC_SESSION      = TPM_HT_HMAC_SESSION << HR_SHIFT
HR_POLICY_SESSION    = TPM_HT_POLICY_SESSION << HR_SHIFT
HR_TRANSIENT         = TPM_HT_TRANSIENT << HR_SHIFT
HR_PERSISTENT        = TPM_HT_PERSISTENT << HR_SHIFT
HR_NV_INDEX          = TPM_HT_NV_INDEX << HR_SHIFT
HR_PERMANENT         = TPM_HT_PERMANENT << HR_SHIFT
PCR_FIRST            = HR_PCR + 0
PCR_LAST             = PCR_FIRST + IMPLEMENTATION_PCR - 1
HMAC_SESSION_FIRST   = HR_HMAC_SESSION + 0
HMAC_SESSION_LAST    = HMAC_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1
LOADED_SESSION_FIRST = HMAC_SESSION_FIRST
LOADED_SESSION_LAST  = HMAC_SESSION_LAST
POLICY_SESSION_FIRST = HR_POLICY_SESSION + 0
POLICY_SESSION_LAST  = POLICY_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1
TRANSIENT_FIRST      = HR_TRANSIENT + 0
ACTIVE_SESSION_FIRST = POLICY_SESSION_FIRST
ACTIVE_SESSION_LAST  = POLICY_SESSION_LAST
TRANSIENT_LAST       = TRANSIENT_FIRST+MAX_LOADED_OBJECTS - 1
PERSISTENT_FIRST     = HR_PERSISTENT + 0
PERSISTENT_LAST      = PERSISTENT_FIRST + 0x00FFFFFF
PLATFORM_PERSISTENT  = PERSISTENT_FIRST + 0x00800000
NV_INDEX_FIRST       = HR_NV_INDEX + 0
NV_INDEX_LAST        = NV_INDEX_FIRST + 0x00FFFFFF
PERMANENT_FIRST      = TPM_RH_FIRST
PERMANENT_LAST       = TPM_RH_LAST

# 
# // 8 Attribute Structures
# 
# // Table 29 - TPMA_ALGORITHM Bits
# typedef struct {
#   UINT32    asymmetric    : 1;
#   UINT32    symmetric     : 1;
#   UINT32    hash          : 1;
#   UINT32    object        : 1;
#   UINT32    reserved4_7   : 4;
#   UINT32    signing       : 1;
#   UINT32    encrypting    : 1;
#   UINT32    method        : 1;
#   UINT32    reserved11_31 : 21;
# } TPMA_ALGORITHM;
class TPMA_ALGORITHM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymmetric",    UINT32, 1),
    ("symmetric",     UINT32, 1),
    ("hash",          UINT32, 1),
    ("object",        UINT32, 1),
    ("reserved4_7",   UINT32, 4),
    ("signing",       UINT32, 1),
    ("encrypting",    UINT32, 1),
    ("method",        UINT32, 1),
    ("reserved11_31", UINT32, 21)
  ]

# 
# // Table 30 - TPMA_OBJECT Bits
# typedef struct {
#   UINT32    reserved1            : 1;
#   UINT32    fixedTPM             : 1;
#   UINT32    stClear              : 1;
#   UINT32    reserved4            : 1;
#   UINT32    fixedParent          : 1;
#   UINT32    sensitiveDataOrigin  : 1;
#   UINT32    userWithAuth         : 1;
#   UINT32    adminWithPolicy      : 1;
#   UINT32    reserved8_9          : 2;
#   UINT32    noDA                 : 1;
#   UINT32    encryptedDuplication : 1;
#   UINT32    reserved12_15        : 4;
#   UINT32    restricted           : 1;
#   UINT32    decrypt              : 1;
#   UINT32    sign                 : 1;
#   UINT32    reserved19_31        : 13;
# } TPMA_OBJECT;
class TPMA_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("reserved1",             UINT32, 1),
    ("fixedTPM",              UINT32, 1),
    ("stClear",               UINT32, 1),
    ("reserved4",             UINT32, 1),
    ("fixedParent",           UINT32, 1),
    ("sensitiveDataOrigin",   UINT32, 1),
    ("userWithAuth",          UINT32, 1),
    ("adminWithPolicy",       UINT32, 1),
    ("reserved8_9",           UINT32, 2),
    ("noDA",                  UINT32, 1),
    ("encryptedDuplication",  UINT32, 1),
    ("reserved12_15",         UINT32, 4),
    ("restricted",            UINT32, 1),
    ("decrypt",               UINT32, 1),
    ("sign",                  UINT32, 1),
    ("reserved19_31",         UINT32, 13)
  ]

# 
# // Table 31 - TPMA_SESSION Bits
# typedef struct {
#   UINT8    continueSession : 1;
#   UINT8    auditExclusive  : 1;
#   UINT8    auditReset      : 1;
#   UINT8    reserved3_4     : 2;
#   UINT8    decrypt         : 1;
#   UINT8    encrypt         : 1;
#   UINT8    audit           : 1;
# } TPMA_SESSION;
class TPMA_SESSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("continueSession", UINT8, 1),
    ("auditExclusive",  UINT8, 1),
    ("auditReset",      UINT8, 1),
    ("reserved3_4",     UINT8, 2),
    ("decrypt",         UINT8, 1),
    ("encrypt",         UINT8, 1),
    ("audit",           UINT8, 1)
  ]

# 
# // Table 32 - TPMA_LOCALITY Bits
# //
# // NOTE: Use low case here to resolve conflict
# //
# typedef struct {
#   UINT8    locZero  : 1;
#   UINT8    locOne   : 1;
#   UINT8    locTwo   : 1;
#   UINT8    locThree : 1;
#   UINT8    locFour  : 1;
#   UINT8    Extended : 3;
# } TPMA_LOCALITY;
class TPMA_LOCALITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("locZero",   UINT8, 1),
    ("locOne",    UINT8, 1),
    ("locTwo",    UINT8, 1),
    ("locThree",  UINT8, 1),
    ("locFour",   UINT8, 1),
    ("Extended",  UINT8, 3)
  ]

# 
# // Table 33 - TPMA_PERMANENT Bits
# typedef struct {
#   UINT32    ownerAuthSet       : 1;
#   UINT32    endorsementAuthSet : 1;
#   UINT32    lockoutAuthSet     : 1;
#   UINT32    reserved3_7        : 5;
#   UINT32    disableClear       : 1;
#   UINT32    inLockout          : 1;
#   UINT32    tpmGeneratedEPS    : 1;
#   UINT32    reserved11_31      : 21;
# } TPMA_PERMANENT;
class TPMA_PERMANENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ownerAuthSet",        UINT32, 1),
    ("endorsementAuthSet",  UINT32, 1),
    ("lockoutAuthSet",      UINT32, 1),
    ("reserved3_7",         UINT32, 5),
    ("disableClear",        UINT32, 1),
    ("inLockout",           UINT32, 1),
    ("tpmGeneratedEPS",     UINT32, 1),
    ("reserved11_31",       UINT32, 21)
  ]

# 
# // Table 34 - TPMA_STARTUP_CLEAR Bits
# typedef struct {
#   UINT32    phEnable     : 1;
#   UINT32    shEnable     : 1;
#   UINT32    ehEnable     : 1;
#   UINT32    reserved3_30 : 28;
#   UINT32    orderly      : 1;
# } TPMA_STARTUP_CLEAR;
class TPMA_STARTUP_CLEAR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("phEnable",      UINT32, 1),
    ("shEnable",      UINT32, 1),
    ("ehEnable",      UINT32, 1),
    ("reserved3_30",  UINT32, 28),
    ("orderly",       UINT32, 1)
  ]

# 
# // Table 35 - TPMA_MEMORY Bits
# typedef struct {
#   UINT32    sharedRAM         : 1;
#   UINT32    sharedNV          : 1;
#   UINT32    objectCopiedToRam : 1;
#   UINT32    reserved3_31      : 29;
# } TPMA_MEMORY;
class TPMA_MEMORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sharedRAM",         UINT32, 1),
    ("sharedNV",          UINT32, 1),
    ("objectCopiedToRam", UINT32, 1),
    ("reserved3_31",      UINT32, 29)
  ]

# 
# // Table 36 - TPMA_CC Bits
# typedef struct {
#   UINT32    commandIndex  : 16;
#   UINT32    reserved16_21 : 6;
#   UINT32    nv            : 1;
#   UINT32    extensive     : 1;
#   UINT32    flushed       : 1;
#   UINT32    cHandles      : 3;
#   UINT32    rHandle       : 1;
#   UINT32    V             : 1;
#   UINT32    Res           : 2;
# } TPMA_CC;
class TPMA_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("commandIndex",      UINT32, 16),
    ("reserved16_21",     UINT32, 6),
    ("nv",                UINT32, 1),
    ("extensive",         UINT32, 1),
    ("flushed",           UINT32, 1),
    ("cHandles",          UINT32, 3),
    ("rHandle",           UINT32, 1),
    ("V",                 UINT32, 1),
    ("Res",               UINT32, 2)
  ]

# 
# // 9 Interface Types
# 
# // Table 37 - TPMI_YES_NO Type
# typedef BYTE TPMI_YES_NO;
TPMI_YES_NO = BYTE

# 
# // Table 38 - TPMI_DH_OBJECT Type
# typedef TPM_HANDLE TPMI_DH_OBJECT;
TPMI_DH_OBJECT = Tpm12.TPM_HANDLE
# 
# // Table 39 - TPMI_DH_PERSISTENT Type
# typedef TPM_HANDLE TPMI_DH_PERSISTENT;
TPMI_DH_PERSISTENT = Tpm12.TPM_HANDLE
# 
# // Table 40 - TPMI_DH_ENTITY Type
# typedef TPM_HANDLE TPMI_DH_ENTITY;
TPMI_DH_ENTITY = Tpm12.TPM_HANDLE
# 
# // Table 41 - TPMI_DH_PCR Type
# typedef TPM_HANDLE TPMI_DH_PCR;
TPMI_DH_PCR = Tpm12.TPM_HANDLE
# 
# // Table 42 - TPMI_SH_AUTH_SESSION Type
# typedef TPM_HANDLE TPMI_SH_AUTH_SESSION;
TPMI_SH_AUTH_SESSION = Tpm12.TPM_HANDLE
# 
# // Table 43 - TPMI_SH_HMAC Type
# typedef TPM_HANDLE TPMI_SH_HMAC;
TPMI_SH_HMAC = Tpm12.TPM_HANDLE
# 
# // Table 44 - TPMI_SH_POLICY Type
# typedef TPM_HANDLE TPMI_SH_POLICY;
TPMI_SH_POLICY = Tpm12.TPM_HANDLE
# 
# // Table 45 - TPMI_DH_CONTEXT Type
# typedef TPM_HANDLE TPMI_DH_CONTEXT;
TPMI_DH_CONTEXT = Tpm12.TPM_HANDLE
# 
# // Table 46 - TPMI_RH_HIERARCHY Type
# typedef TPM_HANDLE TPMI_RH_HIERARCHY;
TPMI_RH_HIERARCHY = Tpm12.TPM_HANDLE
# 
# // Table 47 - TPMI_RH_HIERARCHY_AUTH Type
# typedef TPM_HANDLE TPMI_RH_HIERARCHY_AUTH;
TPMI_RH_HIERARCHY_AUTH = Tpm12.TPM_HANDLE
# 
# // Table 48 - TPMI_RH_PLATFORM Type
# typedef TPM_HANDLE TPMI_RH_PLATFORM;
TPMI_RH_PLATFORM = Tpm12.TPM_HANDLE
# 
# // Table 49 - TPMI_RH_OWNER Type
# typedef TPM_HANDLE TPMI_RH_OWNER;
TPMI_RH_OWNER = Tpm12.TPM_HANDLE
# 
# // Table 50 - TPMI_RH_ENDORSEMENT Type
# typedef TPM_HANDLE TPMI_RH_ENDORSEMENT;
TPMI_RH_ENDORSEMENT = Tpm12.TPM_HANDLE
# 
# // Table 51 - TPMI_RH_PROVISION Type
# typedef TPM_HANDLE TPMI_RH_PROVISION;
TPMI_RH_PROVISION = Tpm12.TPM_HANDLE
# 
# // Table 52 - TPMI_RH_CLEAR Type
# typedef TPM_HANDLE TPMI_RH_CLEAR;
TPMI_RH_CLEAR = Tpm12.TPM_HANDLE
# 
# // Table 53 - TPMI_RH_NV_AUTH Type
# typedef TPM_HANDLE TPMI_RH_NV_AUTH;
TPMI_RH_NV_AUTH = Tpm12.TPM_HANDLE
# 
# // Table 54 - TPMI_RH_LOCKOUT Type
# typedef TPM_HANDLE TPMI_RH_LOCKOUT;
TPMI_RH_LOCKOUT = Tpm12.TPM_HANDLE
# 
# // Table 55 - TPMI_RH_NV_INDEX Type
# typedef TPM_HANDLE TPMI_RH_NV_INDEX;
TPMI_RH_NV_INDEX = Tpm12.TPM_HANDLE
# 
# // Table 56 - TPMI_ALG_HASH Type
# typedef TPM_ALG_ID TPMI_ALG_HASH;
TPMI_ALG_HASH = TPM_ALG_ID
# 
# // Table 57 - TPMI_ALG_ASYM Type
# typedef TPM_ALG_ID TPMI_ALG_ASYM;
TPMI_ALG_ASYM = TPM_ALG_ID
# 
# // Table 58 - TPMI_ALG_SYM Type
# typedef TPM_ALG_ID TPMI_ALG_SYM;
TPMI_ALG_SYM = TPM_ALG_ID
# 
# // Table 59 - TPMI_ALG_SYM_OBJECT Type
# typedef TPM_ALG_ID TPMI_ALG_SYM_OBJECT;
TPMI_ALG_SYM_OBJECT = TPM_ALG_ID
# 
# // Table 60 - TPMI_ALG_SYM_MODE Type
# typedef TPM_ALG_ID TPMI_ALG_SYM_MODE;
TPMI_ALG_SYM_MODE = TPM_ALG_ID
# 
# // Table 61 - TPMI_ALG_KDF Type
# typedef TPM_ALG_ID TPMI_ALG_KDF;
TPMI_ALG_KDF = TPM_ALG_ID
# 
# // Table 62 - TPMI_ALG_SIG_SCHEME Type
# typedef TPM_ALG_ID TPMI_ALG_SIG_SCHEME;
TPMI_ALG_SIG_SCHEME = TPM_ALG_ID
# 
# // Table 63 - TPMI_ECC_KEY_EXCHANGE Type
# typedef TPM_ALG_ID TPMI_ECC_KEY_EXCHANGE;
TPMI_ECC_KEY_EXCHANGE = TPM_ALG_ID
# 
# // Table 64 - TPMI_ST_COMMAND_TAG Type
# typedef TPM_ST TPMI_ST_COMMAND_TAG;
TPMI_ST_COMMAND_TAG = TPM_ST

# 
# // 10 Structure Definitions
# 
# // Table 65 - TPMS_ALGORITHM_DESCRIPTION Structure
# typedef struct {
#   TPM_ALG_ID        alg;
#   TPMA_ALGORITHM    attributes;
# } TPMS_ALGORITHM_DESCRIPTION;
class TPMS_ALGORITHM_DESCRIPTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",         TPM_ALG_ID),
    ("attributes",  TPMA_ALGORITHM)
  ]

# 
# // Table 66 - TPMU_HA Union
# typedef union {
#   BYTE    sha1[SHA1_DIGEST_SIZE];
#   BYTE    sha256[SHA256_DIGEST_SIZE];
#   BYTE    sm3_256[SM3_256_DIGEST_SIZE];
#   BYTE    sha384[SHA384_DIGEST_SIZE];
#   BYTE    sha512[SHA512_DIGEST_SIZE];
# } TPMU_HA;
class TPMU_HA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("sha1",    BYTE * SHA1_DIGEST_SIZE),
    ("sha256",  BYTE * SHA256_DIGEST_SIZE),
    ("sm3_256", BYTE * SM3_256_DIGEST_SIZE),
    ("sha384",  BYTE * SHA384_DIGEST_SIZE),
    ("sha512",  BYTE * SHA512_DIGEST_SIZE)
  ]

# 
# // Table 67 - TPMT_HA Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
#   TPMU_HA          digest;
# } TPMT_HA;
class TPMT_HA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  TPMU_HA)
  ]

class TPMT_HA_SHA1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA1_DIGEST_SIZE)
  ]

class TPMT_HA_SHA256 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA256_DIGEST_SIZE)
  ]

class TPMT_HA_SM3_256 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SM3_256_DIGEST_SIZE)
  ]

class TPMT_HA_SHA384 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA384_DIGEST_SIZE)
  ]

class TPMT_HA_SHA512 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  BYTE * SHA512_DIGEST_SIZE)
  ]

# 
# // Table 68 - TPM2B_DIGEST Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (TPMU_HA)];
# } TPM2B_DIGEST;
class TPM2B_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMU_HA))
  ]

# 
# // Table 69 - TPM2B_DATA Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (TPMT_HA)];
# } TPM2B_DATA;
class TPM2B_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMT_HA))
  ]

# 
# // Table 70 - TPM2B_NONCE Types
# typedef TPM2B_DIGEST TPM2B_NONCE;
# 
# // Table 71 - TPM2B_AUTH Types
# typedef TPM2B_DIGEST TPM2B_AUTH;
# 
# // Table 72 - TPM2B_OPERAND Types
# typedef TPM2B_DIGEST TPM2B_OPERAND;
TPM2B_NONCE = TPM2B_DIGEST
TPM2B_AUTH = TPM2B_DIGEST
TPM2B_OPERAND = TPM2B_DIGEST

# 
# // Table 73 - TPM2B_EVENT Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[1024];
# } TPM2B_EVENT;
class TPM2B_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * 1024)
  ]

# 
# // Table 74 - TPM2B_MAX_BUFFER Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_DIGEST_BUFFER];
# } TPM2B_MAX_BUFFER;
class TPM2B_MAX_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_DIGEST_BUFFER)
  ]

# 
# // Table 75 - TPM2B_MAX_NV_BUFFER Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_NV_INDEX_SIZE];
# } TPM2B_MAX_NV_BUFFER;
class TPM2B_MAX_NV_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_NV_INDEX_SIZE)
  ]

# 
# // Table 76 - TPM2B_TIMEOUT Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (UINT64)];
# } TPM2B_TIMEOUT;
class TPM2B_TIMEOUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (UINT64))
  ]

# 
# // Table 77 -- TPM2B_IV Structure <I/O>
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_SYM_BLOCK_SIZE];
# } TPM2B_IV;
class TPM2B_IV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_BLOCK_SIZE)
  ]

# 
# // Table 78 - TPMU_NAME Union
# typedef union {
#   TPMT_HA       digest;
#   TPM_HANDLE    handle;
# } TPMU_NAME;
class TPMU_NAME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("digest",  TPMT_HA),
    ("handle",  Tpm12.TPM_HANDLE)
  ]

# 
# // Table 79 - TPM2B_NAME Structure
# typedef struct {
#   UINT16    size;
#   BYTE      name[sizeof (TPMU_NAME)];
# } TPM2B_NAME;
class TPM2B_NAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("name",  BYTE * sizeof(TPMU_NAME))
  ]

# 
# // Table 80 - TPMS_PCR_SELECT Structure
# typedef struct {
#   UINT8    sizeofSelect;
#   BYTE     pcrSelect[PCR_SELECT_MAX];
# } TPMS_PCR_SELECT;
class TPMS_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeofSelect",  UINT16),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

# 
# // Table 81 - TPMS_PCR_SELECTION Structure
# typedef struct {
#   TPMI_ALG_HASH    hash;
#   UINT8            sizeofSelect;
#   BYTE             pcrSelect[PCR_SELECT_MAX];
# } TPMS_PCR_SELECTION;
class TPMS_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",          TPMI_ALG_HASH),
    ("sizeofSelect",  UINT8),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

# 
# // Table 84 - TPMT_TK_CREATION Structure
# typedef struct {
#   TPM_ST               tag;
#   TPMI_RH_HIERARCHY    hierarchy;
#   TPM2B_DIGEST         digest;
# } TPMT_TK_CREATION;
class TPMT_TK_CREATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_ST),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

# 
# // Table 85 - TPMT_TK_VERIFIED Structure
# typedef struct {
#   TPM_ST               tag;
#   TPMI_RH_HIERARCHY    hierarchy;
#   TPM2B_DIGEST         digest;
# } TPMT_TK_VERIFIED;
class TPMT_TK_VERIFIED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_ST),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

# 
# // Table 86 - TPMT_TK_AUTH Structure
# typedef struct {
#   TPM_ST               tag;
#   TPMI_RH_HIERARCHY    hierarchy;
#   TPM2B_DIGEST         digest;
# } TPMT_TK_AUTH;
TPMT_TK_AUTH = TPMT_TK_VERIFIED

# 
# // Table 87 - TPMT_TK_HASHCHECK Structure
# typedef struct {
#   TPM_ST               tag;
#   TPMI_RH_HIERARCHY    hierarchy;
#   TPM2B_DIGEST         digest;
# } TPMT_TK_HASHCHECK;
TPMT_TK_HASHCHECK = TPMT_TK_VERIFIED

# 
# // Table 88 - TPMS_ALG_PROPERTY Structure
# typedef struct {
#   TPM_ALG_ID        alg;
#   TPMA_ALGORITHM    algProperties;
# } TPMS_ALG_PROPERTY;
class TPMS_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",           TPM_ALG_ID),
    ("algProperties", TPMA_ALGORITHM)
  ]

#
# // Table 89 - TPMS_TAGGED_PROPERTY Structure
# typedef struct {
#   TPM_PT    property;
#   UINT32    value;
# } TPMS_TAGGED_PROPERTY;
class TPMS_TAGGED_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("property",  TPM_PT),
    ("value",     UINT32)
  ]

# 
# // Table 90 - TPMS_TAGGED_PCR_SELECT Structure
# typedef struct {
#   TPM_PT    tag;
#   UINT8     sizeofSelect;
#   BYTE      pcrSelect[PCR_SELECT_MAX];
# } TPMS_TAGGED_PCR_SELECT;
class TPMS_TAGGED_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_PT),
    ("sizeofSelect",  UINT8),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

MAX_CAP_DATA        = (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))
MAX_CAP_ALGS        = (MAX_CAP_DATA // sizeof(TPMS_ALG_PROPERTY))
MAX_CAP_HANDLES     = (MAX_CAP_DATA // sizeof(Tpm12.TPM_HANDLE))
MAX_CAP_CC          = (MAX_CAP_DATA // sizeof(TPM_CC))
MAX_TPM_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PROPERTY))
MAX_PCR_PROPERTIES  = (MAX_CAP_DATA // sizeof(TPMS_TAGGED_PCR_SELECT))
MAX_ECC_CURVES      = (MAX_CAP_DATA // sizeof(TPM_ECC_CURVE))

# 
# // Table 91 - TPML_CC Structure
# typedef struct {
#   UINT32    count;
#   TPM_CC    commandCodes[MAX_CAP_CC];
# } TPML_CC;
class TPML_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("commandCodes",  TPM_CC * MAX_CAP_CC)
  ]

# 
# // Table 92 - TPML_CCA Structure
# typedef struct {
#   UINT32     count;
#   TPMA_CC    commandAttributes[MAX_CAP_CC];
# } TPML_CCA;
class TPML_CCA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",             UINT32),
    ("commandAttributes", TPMA_CC * MAX_CAP_CC)
  ]

# 
# // Table 93 - TPML_ALG Structure
# typedef struct {
#   UINT32        count;
#   TPM_ALG_ID    algorithms[MAX_ALG_LIST_SIZE];
# } TPML_ALG;
class TPML_ALG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("algorithms",  TPM_ALG_ID * MAX_ALG_LIST_SIZE)
  ]

# 
# // Table 94 - TPML_HANDLE Structure
# typedef struct {
#   UINT32        count;
#   TPM_HANDLE    handle[MAX_CAP_HANDLES];
# } TPML_HANDLE;
class TPML_HANDLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("handle",  Tpm12.TPM_HANDLE * MAX_CAP_HANDLES)
  ]

# 
# // Table 95 - TPML_DIGEST Structure
# typedef struct {
#   UINT32          count;
#   TPM2B_DIGEST    digests[8];
# } TPML_DIGEST;
class TPML_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPM2B_DIGEST * 8)
  ]

# 
# // Table 96 -- TPML_DIGEST_VALUES Structure <I/O>
# typedef struct {
#   UINT32     count;
#   TPMT_HA    digests[HASH_COUNT];
# } TPML_DIGEST_VALUES;
class TPML_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPMT_HA * HASH_COUNT)
  ]

# 
# // Table 97 - TPM2B_DIGEST_VALUES Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (TPML_DIGEST_VALUES)];
# } TPM2B_DIGEST_VALUES;
class TPM2B_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",   UINT16),
    ("buffer", BYTE * sizeof (TPML_DIGEST_VALUES))
  ]

# 
# // Table 98 - TPML_PCR_SELECTION Structure
# typedef struct {
#   UINT32                count;
#   TPMS_PCR_SELECTION    pcrSelections[HASH_COUNT];
# } TPML_PCR_SELECTION;
class TPML_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("pcrSelections", TPMS_PCR_SELECTION * HASH_COUNT)
  ]

# 
# // Table 99 - TPML_ALG_PROPERTY Structure
# typedef struct {
#   UINT32               count;
#   TPMS_ALG_PROPERTY    algProperties[MAX_CAP_ALGS];
# } TPML_ALG_PROPERTY;
class TPML_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("algProperties", TPMS_ALG_PROPERTY * MAX_CAP_ALGS)
  ]

# 
# // Table 100 - TPML_TAGGED_TPM_PROPERTY Structure
# typedef struct {
#   UINT32                  count;
#   TPMS_TAGGED_PROPERTY    tpmProperty[MAX_TPM_PROPERTIES];
# } TPML_TAGGED_TPM_PROPERTY;
class TPML_TAGGED_TPM_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("tpmProperty", TPMS_TAGGED_PROPERTY * MAX_TPM_PROPERTIES)
  ]

# 
# // Table 101 - TPML_TAGGED_PCR_PROPERTY Structure
# typedef struct {
#   UINT32                    count;
#   TPMS_TAGGED_PCR_SELECT    pcrProperty[MAX_PCR_PROPERTIES];
# } TPML_TAGGED_PCR_PROPERTY;
class TPML_TAGGED_PCR_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("pcrProperty", TPMS_TAGGED_PCR_SELECT * MAX_PCR_PROPERTIES)
  ]

# 
# // Table 102 - TPML_ECC_CURVE Structure
# typedef struct {
#   UINT32           count;
#   TPM_ECC_CURVE    eccCurves[MAX_ECC_CURVES];
# } TPML_ECC_CURVE;
class TPML_ECC_CURVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("eccCurves",   TPM_ECC_CURVE * MAX_ECC_CURVES)
  ]

# 
# // Table 103 - TPMU_CAPABILITIES Union
# typedef union {
#   TPML_ALG_PROPERTY           algorithms;
#   TPML_HANDLE                 handles;
#   TPML_CCA                    command;
#   TPML_CC                     ppCommands;
#   TPML_CC                     auditCommands;
#   TPML_PCR_SELECTION          assignedPCR;
#   TPML_TAGGED_TPM_PROPERTY    tpmProperties;
#   TPML_TAGGED_PCR_PROPERTY    pcrProperties;
#   TPML_ECC_CURVE              eccCurves;
# } TPMU_CAPABILITIES;
class TPMU_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("algorithms",    TPML_ALG_PROPERTY),
    ("handles",       TPML_HANDLE),
    ("command",       TPML_CCA),
    ("ppCommands",    TPML_CC),
    ("auditCommands", TPML_CC),
    ("assignedPCR",   TPML_PCR_SELECTION),
    ("tpmProperties", TPML_TAGGED_TPM_PROPERTY),
    ("pcrProperties", TPML_TAGGED_PCR_PROPERTY),
    ("eccCurves",     TPML_ECC_CURVE)
  ]

# 
# // Table 104 - TPMS_CAPABILITY_DATA Structure
# typedef struct {
#   TPM_CAP              capability;
#   TPMU_CAPABILITIES    data;
# } TPMS_CAPABILITY_DATA;
class TPMS_CAPABILITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("capability",  TPM_CAP),
    ("data",        TPMU_CAPABILITIES)
  ]

# 
# // Table 105 - TPMS_CLOCK_INFO Structure
# typedef struct {
#   UINT64         clock;
#   UINT32         resetCount;
#   UINT32         restartCount;
#   TPMI_YES_NO    safe;
# } TPMS_CLOCK_INFO;
class TPMS_CLOCK_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("clock",         UINT64),
    ("resetCount",    UINT32),
    ("restartCount",  UINT32),
    ("safe",          TPMI_YES_NO)
  ]

# 
# // Table 106 - TPMS_TIME_INFO Structure
# typedef struct {
#   UINT64             time;
#   TPMS_CLOCK_INFO    clockInfo;
# } TPMS_TIME_INFO;
class TPMS_TIME_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",      UINT64),
    ("clockInfo", TPMS_CLOCK_INFO)
  ]

# 
# // Table 107 - TPMS_TIME_ATTEST_INFO Structure
# typedef struct {
#   TPMS_TIME_INFO    time;
#   UINT64            firmwareVersion;
# } TPMS_TIME_ATTEST_INFO;
class TPMS_TIME_ATTEST_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",            TPMS_TIME_INFO),
    ("firmwareVersion", UINT64)
  ]

# 
# // Table 108 - TPMS_CERTIFY_INFO Structure
# typedef struct {
#   TPM2B_NAME    name;
#   TPM2B_NAME    qualifiedName;
# } TPMS_CERTIFY_INFO;
class TPMS_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("name",          TPM2B_NAME),
    ("qualifiedName", TPM2B_NAME)
  ]

# 
# // Table 109 - TPMS_QUOTE_INFO Structure
# typedef struct {
#   TPML_PCR_SELECTION    pcrSelect;
#   TPM2B_DIGEST          pcrDigest;
# } TPMS_QUOTE_INFO;
class TPMS_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect", TPML_PCR_SELECTION),
    ("pcrDigest", TPM2B_DIGEST)
  ]

# 
# // Table 110 - TPMS_COMMAND_AUDIT_INFO Structure
# typedef struct {
#   UINT64          auditCounter;
#   TPM_ALG_ID      digestAlg;
#   TPM2B_DIGEST    auditDigest;
#   TPM2B_DIGEST    commandDigest;
# } TPMS_COMMAND_AUDIT_INFO;
class TPMS_COMMAND_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("auditCounter",  UINT64),
    ("digestAlg",     TPM_ALG_ID),
    ("auditDigest",   TPM2B_DIGEST),
    ("commandDigest", TPM2B_DIGEST)
  ]

# 
# // Table 111 - TPMS_SESSION_AUDIT_INFO Structure
# typedef struct {
#   TPMI_YES_NO     exclusiveSession;
#   TPM2B_DIGEST    sessionDigest;
# } TPMS_SESSION_AUDIT_INFO;
class TPMS_SESSION_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("exclusiveSession",  TPMI_YES_NO),
    ("sessionDigest",     TPM2B_DIGEST)
  ]

# 
# // Table 112 - TPMS_CREATION_INFO Structure
# typedef struct {
#   TPM2B_NAME      objectName;
#   TPM2B_DIGEST    creationHash;
# } TPMS_CREATION_INFO;
class TPMS_CREATION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("objectName",    TPM2B_NAME),
    ("creationHash",  TPM2B_DIGEST)
  ]

# 
# // Table 113 - TPMS_NV_CERTIFY_INFO Structure
# typedef struct {
#   TPM2B_NAME             indexName;
#   UINT16                 offset;
#   TPM2B_MAX_NV_BUFFER    nvContents;
# } TPMS_NV_CERTIFY_INFO;
class TPMS_NV_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("indexName",   TPM2B_NAME),
    ("offset",      UINT16),
    ("nvContents",  TPM2B_MAX_NV_BUFFER),
  ]
# 
# // Table 114 - TPMI_ST_ATTEST Type
# typedef TPM_ST TPMI_ST_ATTEST;
TPMI_ST_ATTEST = TPM_ST
# 
# // Table 115 - TPMU_ATTEST Union
# typedef union {
#   TPMS_CERTIFY_INFO          certify;
#   TPMS_CREATION_INFO         creation;
#   TPMS_QUOTE_INFO            quote;
#   TPMS_COMMAND_AUDIT_INFO    commandAudit;
#   TPMS_SESSION_AUDIT_INFO    sessionAudit;
#   TPMS_TIME_ATTEST_INFO      time;
#   TPMS_NV_CERTIFY_INFO       nv;
# } TPMU_ATTEST;
class TPMU_ATTEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("certify",       TPMS_CERTIFY_INFO),
    ("creation",      TPMS_CREATION_INFO),
    ("quote",         TPMS_QUOTE_INFO),
    ("commandAudit",  TPMS_COMMAND_AUDIT_INFO),
    ("sessionAudit",  TPMS_SESSION_AUDIT_INFO),
    ("time",          TPMS_TIME_ATTEST_INFO),
    ("nv",            TPMS_NV_CERTIFY_INFO)
  ]

# 
# // Table 116 - TPMS_ATTEST Structure
# typedef struct {
#   TPM_GENERATED      magic;
#   TPMI_ST_ATTEST     type;
#   TPM2B_NAME         qualifiedSigner;
#   TPM2B_DATA         extraData;
#   TPMS_CLOCK_INFO    clockInfo;
#   UINT64             firmwareVersion;
#   TPMU_ATTEST        attested;
# } TPMS_ATTEST;
class TPMS_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("magic",           TPM_GENERATED),
    ("type",            TPMI_ST_ATTEST),
    ("qualifiedSigner", TPM2B_NAME),
    ("extraData",       TPM2B_DATA),
    ("clockInfo",       TPMS_CLOCK_INFO),
    ("firmwareVersion", UINT64),
    ("attested",        TPMU_ATTEST)
  ]

# 
# // Table 117 - TPM2B_ATTEST Structure
# typedef struct {
#   UINT16    size;
#   BYTE      attestationData[sizeof (TPMS_ATTEST)];
# } TPM2B_ATTEST;
class TPM2B_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",            UINT16),
    ("attestationData", BYTE * sizeof (TPMS_ATTEST))
  ]

# 
# // Table 118 - TPMS_AUTH_COMMAND Structure
# typedef struct {
#   TPMI_SH_AUTH_SESSION    sessionHandle;
#   TPM2B_NONCE             nonce;
#   TPMA_SESSION            sessionAttributes;
#   TPM2B_AUTH              hmac;
# } TPMS_AUTH_COMMAND;
class TPMS_AUTH_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionHandle",     TPMI_SH_AUTH_SESSION),
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

# 
# // Table 119 - TPMS_AUTH_RESPONSE Structure
# typedef struct {
#   TPM2B_NONCE     nonce;
#   TPMA_SESSION    sessionAttributes;
#   TPM2B_AUTH      hmac;
# } TPMS_AUTH_RESPONSE;
class TPMS_AUTH_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

# 
# // 11 Algorithm Parameters and Structures
# 
# // Table 120 - TPMI_AES_KEY_BITS Type
# typedef TPM_KEY_BITS TPMI_AES_KEY_BITS;
# 
# // Table 121 - TPMI_SM4_KEY_BITS Type
# typedef TPM_KEY_BITS TPMI_SM4_KEY_BITS;
TPMI_AES_KEY_BITS = TPM_KEY_BITS
TPMI_SM4_KEY_BITS = TPM_KEY_BITS

# 
# // Table 122 - TPMU_SYM_KEY_BITS Union
# typedef union {
#   TPMI_AES_KEY_BITS    aes;
#   TPMI_SM4_KEY_BITS    SM4;
#   TPM_KEY_BITS         sym;
#   TPMI_ALG_HASH     xor;
# } TPMU_SYM_KEY_BITS;
class TPMU_SYM_KEY_BITS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_AES_KEY_BITS),
    ("SM4", TPMI_SM4_KEY_BITS),
    ("sym", TPM_KEY_BITS),
    ("xor", TPMI_ALG_HASH)
  ]

# 
# // Table 123 - TPMU_SYM_MODE Union
# typedef union {
#   TPMI_ALG_SYM_MODE    aes;
#   TPMI_ALG_SYM_MODE    SM4;
#   TPMI_ALG_SYM_MODE    sym;
# } TPMU_SYM_MODE;
class TPMU_SYM_MODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_ALG_SYM_MODE),
    ("SM4", TPMI_ALG_SYM_MODE),
    ("sym", TPMI_ALG_SYM_MODE)
  ]

# 
# // Table 125 - TPMT_SYM_DEF Structure
# typedef struct {
#   TPMI_ALG_SYM         algorithm;
#   TPMU_SYM_KEY_BITS    keyBits;
#   TPMU_SYM_MODE        mode;
# } TPMT_SYM_DEF;
class TPMT_SYM_DEF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

# 
# // Table 126 - TPMT_SYM_DEF_OBJECT Structure
# typedef struct {
#   TPMI_ALG_SYM_OBJECT    algorithm;
#   TPMU_SYM_KEY_BITS      keyBits;
#   TPMU_SYM_MODE          mode;
# } TPMT_SYM_DEF_OBJECT;
class TPMT_SYM_DEF_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM_OBJECT),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

# 
# // Table 127 - TPM2B_SYM_KEY Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_SYM_KEY_BYTES];
# } TPM2B_SYM_KEY;
class TPM2B_SYM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_KEY_BYTES)
  ]

# 
# // Table 128 - TPMS_SYMCIPHER_PARMS Structure
# typedef struct {
#   TPMT_SYM_DEF_OBJECT    sym;
# } TPMS_SYMCIPHER_PARMS;
class TPMS_SYMCIPHER_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sym",    TPMT_SYM_DEF_OBJECT)
  ]

# 
# // Table 129 - TPM2B_SENSITIVE_DATA Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_SYM_DATA];
# } TPM2B_SENSITIVE_DATA;
class TPM2B_SENSITIVE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_DATA)
  ]

# 
# // Table 130 - TPMS_SENSITIVE_CREATE Structure
# typedef struct {
#   TPM2B_AUTH              userAuth;
#   TPM2B_SENSITIVE_DATA    data;
# } TPMS_SENSITIVE_CREATE;
class TPMS_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("userAuth",    TPM2B_AUTH),
    ("data",        TPM2B_SENSITIVE_DATA)
  ]

# 
# // Table 131 - TPM2B_SENSITIVE_CREATE Structure
# typedef struct {
#   UINT16                   size;
#   TPMS_SENSITIVE_CREATE    sensitive;
# } TPM2B_SENSITIVE_CREATE;
class TPM2B_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("sensitive", TPMS_SENSITIVE_CREATE)
  ]

# 
# // Table 132 - TPMS_SCHEME_SIGHASH Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_SIGHASH;
class TPMS_SCHEME_SIGHASH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

# 
# // Table 133 - TPMI_ALG_KEYEDHASH_SCHEME Type
# typedef TPM_ALG_ID TPMI_ALG_KEYEDHASH_SCHEME;
# 
# // Table 134 - HMAC_SIG_SCHEME Types
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_HMAC;
TPMI_ALG_KEYEDHASH_SCHEME = TPM_ALG_ID
TPMS_SCHEME_HMAC = TPMS_SCHEME_SIGHASH

# 
# // Table 135 - TPMS_SCHEME_XOR Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
#   TPMI_ALG_KDF     kdf;
# } TPMS_SCHEME_XOR;
class TPMS_SCHEME_XOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("kdf",     TPMI_ALG_KDF)
  ]

# 
# // Table 136 - TPMU_SCHEME_KEYEDHASH Union
# typedef union {
#   TPMS_SCHEME_HMAC    hmac;
#   TPMS_SCHEME_XOR  xor;
# } TPMU_SCHEME_KEYEDHASH;
class TPMU_SCHEME_KEYEDHASH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("hmac",  TPMS_SCHEME_HMAC),
    ("xor",   TPMS_SCHEME_XOR)
  ]

# 
# // Table 137 - TPMT_KEYEDHASH_SCHEME Structure
# typedef struct {
#   TPMI_ALG_KEYEDHASH_SCHEME    scheme;
#   TPMU_SCHEME_KEYEDHASH        details;
# } TPMT_KEYEDHASH_SCHEME;
class TPMT_KEYEDHASH_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KEYEDHASH_SCHEME),
    ("details", TPMU_SCHEME_KEYEDHASH)
  ]

# 
# // Table 138 - RSA_SIG_SCHEMES Types
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_RSASSA;
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_RSAPSS;
# 
# // Table 139 - ECC_SIG_SCHEMES Types
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_ECDSA;
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_SM2;
# typedef TPMS_SCHEME_SIGHASH TPMS_SCHEME_ECSCHNORR;
TPMS_SCHEME_RSASSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_RSAPSS = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECDSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_SM2 = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECSCHNORR = TPMS_SCHEME_SIGHASH

# 
# // Table 140 - TPMS_SCHEME_ECDAA Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
#   UINT16           count;
# } TPMS_SCHEME_ECDAA;
class TPMS_SCHEME_ECDAA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("count",   UINT16)
  ]

# 
# // Table 141 - TPMU_SIG_SCHEME Union
# typedef union {
#   TPMS_SCHEME_RSASSA       rsassa;
#   TPMS_SCHEME_RSAPSS       rsapss;
#   TPMS_SCHEME_ECDSA        ecdsa;
#   TPMS_SCHEME_ECDAA        ecdaa;
#   TPMS_SCHEME_ECSCHNORR    ecSchnorr;
#   TPMS_SCHEME_HMAC         hmac;
#   TPMS_SCHEME_SIGHASH      any;
# } TPMU_SIG_SCHEME;
class TPMU_SIG_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("hmac",      TPMS_SCHEME_HMAC),
    ("any",       TPMS_SCHEME_SIGHASH),
  ]

# 
# // Table 142 - TPMT_SIG_SCHEME Structure
# typedef struct {
#   TPMI_ALG_SIG_SCHEME    scheme;
#   TPMU_SIG_SCHEME        details;
# } TPMT_SIG_SCHEME;
class TPMT_SIG_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_SIG_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

# 
# // Table 143 - TPMS_SCHEME_OAEP Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_OAEP;
class TPMS_SCHEME_OAEP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

# 
# // Table 144 - TPMS_SCHEME_ECDH Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_ECDH;
TPMS_SCHEME_ECDH = TPMS_SCHEME_OAEP

# 
# // Table 145 - TPMS_SCHEME_MGF1 Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_MGF1;
TPMS_SCHEME_MGF1 = TPMS_SCHEME_OAEP

# 
# // Table 146 - TPMS_SCHEME_KDF1_SP800_56a Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_KDF1_SP800_56a;
TPMS_SCHEME_KDF1_SP800_56a = TPMS_SCHEME_OAEP

# 
# // Table 147 - TPMS_SCHEME_KDF2 Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_KDF2;
TPMS_SCHEME_KDF2 = TPMS_SCHEME_OAEP

# 
# // Table 148 - TPMS_SCHEME_KDF1_SP800_108 Structure
# typedef struct {
#   TPMI_ALG_HASH    hashAlg;
# } TPMS_SCHEME_KDF1_SP800_108;
TPMS_SCHEME_KDF1_SP800_108 = TPMS_SCHEME_OAEP

# 
# // Table 149 - TPMU_KDF_SCHEME Union
# typedef union {
#   TPMS_SCHEME_MGF1              mgf1;
#   TPMS_SCHEME_KDF1_SP800_56a    kdf1_SP800_56a;
#   TPMS_SCHEME_KDF2              kdf2;
#   TPMS_SCHEME_KDF1_SP800_108    kdf1_sp800_108;
# } TPMU_KDF_SCHEME;
class TPMU_KDF_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("mgf1",            TPMS_SCHEME_MGF1),
    ("kdf1_SP800_56a",  TPMS_SCHEME_KDF1_SP800_56a),
    ("kdf2",            TPMS_SCHEME_KDF2),
    ("kdf1_sp800_108",  TPMS_SCHEME_KDF1_SP800_108),
  ]

# 
# // Table 150 - TPMT_KDF_SCHEME Structure
# typedef struct {
#   TPMI_ALG_KDF       scheme;
#   TPMU_KDF_SCHEME    details;
# } TPMT_KDF_SCHEME;
class TPMT_KDF_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KDF),
    ("details", TPMU_KDF_SCHEME)
  ]

# 
# // Table 151 - TPMI_ALG_ASYM_SCHEME Type
# typedef TPM_ALG_ID TPMI_ALG_ASYM_SCHEME;
TPMI_ALG_ASYM_SCHEME = TPM_ALG_ID

# 
# // Table 152 - TPMU_ASYM_SCHEME Union
# typedef union {
#   TPMS_SCHEME_RSASSA       rsassa;
#   TPMS_SCHEME_RSAPSS       rsapss;
#   TPMS_SCHEME_OAEP         oaep;
#   TPMS_SCHEME_ECDSA        ecdsa;
#   TPMS_SCHEME_ECDAA        ecdaa;
#   TPMS_SCHEME_ECSCHNORR    ecSchnorr;
#   TPMS_SCHEME_SIGHASH      anySig;
# } TPMU_ASYM_SCHEME;
class TPMU_ASYM_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("oaep",      TPMS_SCHEME_OAEP),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("anySig",    TPMS_SCHEME_SIGHASH)
  ]

# 
# // Table 153 - TPMT_ASYM_SCHEME Structure
# typedef struct {
#   TPMI_ALG_ASYM_SCHEME    scheme;
#   TPMU_ASYM_SCHEME        details;
# } TPMT_ASYM_SCHEME;
class TPMT_ASYM_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ASYM_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

# 
# // Table 154 - TPMI_ALG_RSA_SCHEME Type
# typedef TPM_ALG_ID TPMI_ALG_RSA_SCHEME;
TPMI_ALG_RSA_SCHEME = TPM_ALG_ID

# 
# // Table 155 - TPMT_RSA_SCHEME Structure
# typedef struct {
#   TPMI_ALG_RSA_SCHEME    scheme;
#   TPMU_ASYM_SCHEME       details;
# } TPMT_RSA_SCHEME;
class TPMT_RSA_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

# 
# // Table 156 - TPMI_ALG_RSA_DECRYPT Type
# typedef TPM_ALG_ID TPMI_ALG_RSA_DECRYPT;
TPMI_ALG_RSA_DECRYPT = TPM_ALG_ID

# 
# // Table 157 - TPMT_RSA_DECRYPT Structure
# typedef struct {
#   TPMI_ALG_RSA_DECRYPT    scheme;
#   TPMU_ASYM_SCHEME        details;
# } TPMT_RSA_DECRYPT;
class TPMT_RSA_DECRYPT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_DECRYPT),
    ("details", TPMU_ASYM_SCHEME)
  ]

# 
# // Table 158 - TPM2B_PUBLIC_KEY_RSA Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_RSA_KEY_BYTES];
# } TPM2B_PUBLIC_KEY_RSA;
class TPM2B_PUBLIC_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_RSA_KEY_BYTES)
  ]

# 
# // Table 159 - TPMI_RSA_KEY_BITS Type
# typedef TPM_KEY_BITS TPMI_RSA_KEY_BITS;
TPMI_RSA_KEY_BITS = TPM_KEY_BITS

# 
# // Table 160 - TPM2B_PRIVATE_KEY_RSA Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_RSA_KEY_BYTES/2];
# } TPM2B_PRIVATE_KEY_RSA;
class TPM2B_PRIVATE_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * (MAX_RSA_KEY_BYTES // 2))
  ]

# 
# // Table 161 - TPM2B_ECC_PARAMETER Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_ECC_KEY_BYTES];
# } TPM2B_ECC_PARAMETER;
class TPM2B_ECC_PARAMETER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_ECC_KEY_BYTES)
  ]

# 
# // Table 162 - TPMS_ECC_POINT Structure
# typedef struct {
#   TPM2B_ECC_PARAMETER    x;
#   TPM2B_ECC_PARAMETER    y;
# } TPMS_ECC_POINT;
class TPMS_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("x", TPM2B_ECC_PARAMETER),
    ("y", TPM2B_ECC_PARAMETER)
  ]

# 
# // Table 163 -- TPM2B_ECC_POINT Structure <I/O>
# typedef struct {
#   UINT16            size;
#   TPMS_ECC_POINT    point;
# } TPM2B_ECC_POINT;
class TPM2B_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("point", TPMS_ECC_POINT)
  ]

# 
# // Table 164 - TPMI_ALG_ECC_SCHEME Type
# typedef TPM_ALG_ID TPMI_ALG_ECC_SCHEME;
# 
# // Table 165 - TPMI_ECC_CURVE Type
# typedef TPM_ECC_CURVE TPMI_ECC_CURVE;
TPMI_ALG_ECC_SCHEME = TPM_ALG_ID
TPMI_ECC_CURVE = TPM_ECC_CURVE

# 
# // Table 166 - TPMT_ECC_SCHEME Structure
# typedef struct {
#   TPMI_ALG_ECC_SCHEME    scheme;
#   TPMU_SIG_SCHEME        details;
# } TPMT_ECC_SCHEME;
class TPMT_ECC_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ECC_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

# 
# // Table 167 - TPMS_ALGORITHM_DETAIL_ECC Structure
# typedef struct {
#   TPM_ECC_CURVE          curveID;
#   UINT16                 keySize;
#   TPMT_KDF_SCHEME        kdf;
#   TPMT_ECC_SCHEME        sign;
#   TPM2B_ECC_PARAMETER    p;
#   TPM2B_ECC_PARAMETER    a;
#   TPM2B_ECC_PARAMETER    b;
#   TPM2B_ECC_PARAMETER    gX;
#   TPM2B_ECC_PARAMETER    gY;
#   TPM2B_ECC_PARAMETER    n;
#   TPM2B_ECC_PARAMETER    h;
# } TPMS_ALGORITHM_DETAIL_ECC;
class TPMS_ALGORITHM_DETAIL_ECC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("curveID", TPM_ECC_CURVE),
    ("keySize", UINT16),
    ("kdf",     TPMT_KDF_SCHEME),
    ("sign",    TPMT_ECC_SCHEME),
    ("p",       TPM2B_ECC_PARAMETER),
    ("a",       TPM2B_ECC_PARAMETER),
    ("b",       TPM2B_ECC_PARAMETER),
    ("gX",      TPM2B_ECC_PARAMETER),
    ("gY",      TPM2B_ECC_PARAMETER),
    ("n",       TPM2B_ECC_PARAMETER),
    ("h",       TPM2B_ECC_PARAMETER)
  ]

# 
# // Table 168 - TPMS_SIGNATURE_RSASSA Structure
# typedef struct {
#   TPMI_ALG_HASH           hash;
#   TPM2B_PUBLIC_KEY_RSA    sig;
# } TPMS_SIGNATURE_RSASSA;
class TPMS_SIGNATURE_RSASSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",    TPMI_ALG_HASH),
    ("sig",     TPM2B_PUBLIC_KEY_RSA)
  ]

# 
# // Table 169 - TPMS_SIGNATURE_RSAPSS Structure
# typedef struct {
#   TPMI_ALG_HASH           hash;
#   TPM2B_PUBLIC_KEY_RSA    sig;
# } TPMS_SIGNATURE_RSAPSS;
class TPMS_SIGNATURE_RSAPSS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",    TPMI_ALG_HASH),
    ("sig",     TPM2B_PUBLIC_KEY_RSA)
  ]

# 
# // Table 170 - TPMS_SIGNATURE_ECDSA Structure
# typedef struct {
#   TPMI_ALG_HASH          hash;
#   TPM2B_ECC_PARAMETER    signatureR;
#   TPM2B_ECC_PARAMETER    signatureS;
# } TPMS_SIGNATURE_ECDSA;
class TPMS_SIGNATURE_ECDSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",        TPMI_ALG_HASH),
    ("signatureR",  TPM2B_ECC_PARAMETER),
    ("signatureS",  TPM2B_ECC_PARAMETER)
  ]

# 
# // Table 171 - TPMU_SIGNATURE Union
# typedef union {
#   TPMS_SIGNATURE_RSASSA    rsassa;
#   TPMS_SIGNATURE_RSAPSS    rsapss;
#   TPMS_SIGNATURE_ECDSA     ecdsa;
#   TPMS_SIGNATURE_ECDSA     sm2;
#   TPMS_SIGNATURE_ECDSA     ecdaa;
#   TPMS_SIGNATURE_ECDSA     ecschnorr;
#   TPMT_HA                  hmac;
#   TPMS_SCHEME_SIGHASH      any;
# } TPMU_SIGNATURE;
class TPMU_SIGNATURE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SIGNATURE_RSASSA),
    ("rsapss",    TPMS_SIGNATURE_RSAPSS),
    ("ecdsa",     TPMS_SIGNATURE_ECDSA),
    ("sm2",       TPMS_SIGNATURE_ECDSA),
    ("ecdaa",     TPMS_SIGNATURE_ECDSA),
    ("ecschnorr", TPMS_SIGNATURE_ECDSA),
    ("hmac",      TPMT_HA),
    ("any",       TPMS_SCHEME_SIGHASH)
  ]

# 
# // Table 172 - TPMT_SIGNATURE Structure
# typedef struct {
#   TPMI_ALG_SIG_SCHEME    sigAlg;
#   TPMU_SIGNATURE         signature;
# } TPMT_SIGNATURE;
class TPMT_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sigAlg",    TPMI_ALG_SIG_SCHEME),
    ("signature", TPMU_SIGNATURE)
  ]

# 
# // Table 173 - TPMU_ENCRYPTED_SECRET Union
# typedef union {
#   BYTE    ecc[sizeof (TPMS_ECC_POINT)];
#   BYTE    rsa[MAX_RSA_KEY_BYTES];
#   BYTE    symmetric[sizeof (TPM2B_DIGEST)];
#   BYTE    keyedHash[sizeof (TPM2B_DIGEST)];
# } TPMU_ENCRYPTED_SECRET;
class TPMU_ENCRYPTED_SECRET (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("ecc",       BYTE * sizeof (TPMS_ECC_POINT)),
    ("rsa",       BYTE * MAX_RSA_KEY_BYTES),
    ("symmetric", BYTE * sizeof (TPM2B_DIGEST)),
    ("keyedHash", BYTE * sizeof (TPM2B_DIGEST))
  ]

# 
# // Table 174 - TPM2B_ENCRYPTED_SECRET Structure
# typedef struct {
#   UINT16    size;
#   BYTE      secret[sizeof (TPMU_ENCRYPTED_SECRET)];
# } TPM2B_ENCRYPTED_SECRET;
class TPM2B_ENCRYPTED_SECRET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("secret",  BYTE * sizeof (TPMU_ENCRYPTED_SECRET))
  ]

# 
# // 12 Key/Object Complex
# 
# // Table 175 - TPMI_ALG_PUBLIC Type
# typedef TPM_ALG_ID TPMI_ALG_PUBLIC;
TPMI_ALG_PUBLIC = TPM_ALG_ID

# 
# // Table 176 - TPMU_PUBLIC_ID Union
# typedef union {
#   TPM2B_DIGEST            keyedHash;
#   TPM2B_DIGEST            sym;
#   TPM2B_PUBLIC_KEY_RSA    rsa;
#   TPMS_ECC_POINT          ecc;
# } TPMU_PUBLIC_ID;
class TPMU_PUBLIC_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHash", TPM2B_DIGEST),
    ("sym",       TPM2B_DIGEST),
    ("rsa",       TPM2B_PUBLIC_KEY_RSA),
    ("ecc",       TPMS_ECC_POINT)
  ]

# 
# // Table 177 - TPMS_KEYEDHASH_PARMS Structure
# typedef struct {
#   TPMT_KEYEDHASH_SCHEME    scheme;
# } TPMS_KEYEDHASH_PARMS;
class TPMS_KEYEDHASH_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMT_KEYEDHASH_SCHEME)
  ]

# 
# // Table 178 - TPMS_ASYM_PARMS Structure
# typedef struct {
#   TPMT_SYM_DEF_OBJECT    symmetric;
#   TPMT_ASYM_SCHEME       scheme;
# } TPMS_ASYM_PARMS;
class TPMS_ASYM_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ASYM_SCHEME)
  ]

# 
# // Table 179 - TPMS_RSA_PARMS Structure
# typedef struct {
#   TPMT_SYM_DEF_OBJECT    symmetric;
#   TPMT_RSA_SCHEME        scheme;
#   TPMI_RSA_KEY_BITS      keyBits;
#   UINT32                 exponent;
# } TPMS_RSA_PARMS;
class TPMS_RSA_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_RSA_SCHEME),
    ("keyBits",   TPMI_RSA_KEY_BITS),
    ("exponent",  UINT32)
  ]

# 
# // Table 180 - TPMS_ECC_PARMS Structure
# typedef struct {
#   TPMT_SYM_DEF_OBJECT    symmetric;
#   TPMT_ECC_SCHEME        scheme;
#   TPMI_ECC_CURVE         curveID;
#   TPMT_KDF_SCHEME        kdf;
# } TPMS_ECC_PARMS;
class TPMS_ECC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ECC_SCHEME),
    ("curveID",   TPMI_ECC_CURVE),
    ("kdf",       TPMT_KDF_SCHEME)
  ]

# 
# // Table 181 - TPMU_PUBLIC_PARMS Union
# typedef union {
#   TPMS_KEYEDHASH_PARMS    keyedHashDetail;
#   TPMT_SYM_DEF_OBJECT     symDetail;
#   TPMS_RSA_PARMS          rsaDetail;
#   TPMS_ECC_PARMS          eccDetail;
#   TPMS_ASYM_PARMS         asymDetail;
# } TPMU_PUBLIC_PARMS;
class TPMU_PUBLIC_PARMS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHashDetail", TPMS_KEYEDHASH_PARMS),
    ("symDetail",       TPMT_SYM_DEF_OBJECT),
    ("rsaDetail",       TPMS_RSA_PARMS),
    ("eccDetail",       TPMS_ECC_PARMS),
    ("asymDetail",      TPMS_ASYM_PARMS)
  ]

# 
# // Table 182 - TPMT_PUBLIC_PARMS Structure
# typedef struct {
#   TPMI_ALG_PUBLIC      type;
#   TPMU_PUBLIC_PARMS    parameters;
# } TPMT_PUBLIC_PARMS;
class TPMT_PUBLIC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",        TPMI_ALG_PUBLIC),
    ("parameters",  TPMU_PUBLIC_PARMS)
  ]

# 
# // Table 183 - TPMT_PUBLIC Structure
# typedef struct {
#   TPMI_ALG_PUBLIC      type;
#   TPMI_ALG_HASH        nameAlg;
#   TPMA_OBJECT          objectAttributes;
#   TPM2B_DIGEST         authPolicy;
#   TPMU_PUBLIC_PARMS    parameters;
#   TPMU_PUBLIC_ID       unique;
# } TPMT_PUBLIC;
class TPMT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",              TPMI_ALG_PUBLIC),
    ("nameAlg",           TPMI_ALG_HASH),
    ("objectAttributes",  TPMA_OBJECT),
    ("authPolicy",        TPM2B_DIGEST),
    ("parameters",        TPMU_PUBLIC_PARMS),
    ("unique",            TPMU_PUBLIC_ID)
  ]

# 
# // Table 184 - TPM2B_PUBLIC Structure
# typedef struct {
#   UINT16         size;
#   TPMT_PUBLIC    publicArea;
# } TPM2B_PUBLIC;
class TPM2B_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("publicArea",  TPMT_PUBLIC)
  ]

# 
# // Table 185 - TPM2B_PRIVATE_VENDOR_SPECIFIC Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[PRIVATE_VENDOR_SPECIFIC_BYTES];
# } TPM2B_PRIVATE_VENDOR_SPECIFIC;
class TPM2B_PRIVATE_VENDOR_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * PRIVATE_VENDOR_SPECIFIC_BYTES)
  ]

# 
# // Table 186 - TPMU_SENSITIVE_COMPOSITE Union
# typedef union {
#   TPM2B_PRIVATE_KEY_RSA            rsa;
#   TPM2B_ECC_PARAMETER              ecc;
#   TPM2B_SENSITIVE_DATA             bits;
#   TPM2B_SYM_KEY                    sym;
#   TPM2B_PRIVATE_VENDOR_SPECIFIC    any;
# } TPMU_SENSITIVE_COMPOSITE;
class TPMU_SENSITIVE_COMPOSITE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsa",   TPM2B_PRIVATE_KEY_RSA),
    ("ecc",   TPM2B_ECC_PARAMETER),
    ("bits",  TPM2B_SENSITIVE_DATA),
    ("sym",   TPM2B_SYM_KEY),
    ("any",   TPM2B_PRIVATE_VENDOR_SPECIFIC)
  ]

# 
# // Table 187 - TPMT_SENSITIVE Structure
# typedef struct {
#   TPMI_ALG_PUBLIC             sensitiveType;
#   TPM2B_AUTH                  authValue;
#   TPM2B_DIGEST                seedValue;
#   TPMU_SENSITIVE_COMPOSITE    sensitive;
# } TPMT_SENSITIVE;
class TPMT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sensitiveType", TPMI_ALG_PUBLIC),
    ("authValue",     TPM2B_AUTH),
    ("seedValue",     TPM2B_DIGEST),
    ("sensitive",     TPMU_SENSITIVE_COMPOSITE)
  ]

# 
# // Table 188 - TPM2B_SENSITIVE Structure
# typedef struct {
#   UINT16            size;
#   TPMT_SENSITIVE    sensitiveArea;
# } TPM2B_SENSITIVE;
class TPM2B_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",          UINT16),
    ("sensitiveArea", TPMT_SENSITIVE)
  ]

# 
# // Table 189 - _PRIVATE Structure
# typedef struct {
#   TPM2B_DIGEST      integrityOuter;
#   TPM2B_DIGEST      integrityInner;
#   TPMT_SENSITIVE    sensitive;
# } _PRIVATE;
class _PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityOuter",  TPM2B_DIGEST),
    ("integrityInner",  TPM2B_DIGEST),
    ("sensitive",       TPMT_SENSITIVE)
  ]

# 
# // Table 190 - TPM2B_PRIVATE Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (_PRIVATE)];
# } TPM2B_PRIVATE;
class TPM2B_PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (_PRIVATE))
  ]

# 
# // Table 191 - _ID_OBJECT Structure
# typedef struct {
#   TPM2B_DIGEST    integrityHMAC;
#   TPM2B_DIGEST    encIdentity;
# } _ID_OBJECT;
class _ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityHMAC", TPM2B_DIGEST),
    ("encIdentity",   TPM2B_DIGEST)
  ]

# 
# // Table 192 - TPM2B_ID_OBJECT Structure
# typedef struct {
#   UINT16    size;
#   BYTE      credential[sizeof (_ID_OBJECT)];
# } TPM2B_ID_OBJECT;
class TPM2B_ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("credential",  BYTE * sizeof (_ID_OBJECT))
  ]

# 
# // 13 NV Storage Structures
# 
# // Table 193 - TPM_NV_INDEX Bits
# //
# // NOTE: Comment here to resolve conflict
# //
# // typedef struct {
# //  UINT32 index : 22;
# //  UINT32 space : 2;
# //  UINT32 RH_NV : 8;
# // } TPM_NV_INDEX;
# 
# // Table 195 - TPMA_NV Bits
# typedef struct {
#   UINT32    TPMA_NV_PPWRITE        : 1;
#   UINT32    TPMA_NV_OWNERWRITE     : 1;
#   UINT32    TPMA_NV_AUTHWRITE      : 1;
#   UINT32    TPMA_NV_POLICYWRITE    : 1;
#   UINT32    TPMA_NV_COUNTER        : 1;
#   UINT32    TPMA_NV_BITS           : 1;
#   UINT32    TPMA_NV_EXTEND         : 1;
#   UINT32    reserved7_9            : 3;
#   UINT32    TPMA_NV_POLICY_DELETE  : 1;
#   UINT32    TPMA_NV_WRITELOCKED    : 1;
#   UINT32    TPMA_NV_WRITEALL       : 1;
#   UINT32    TPMA_NV_WRITEDEFINE    : 1;
#   UINT32    TPMA_NV_WRITE_STCLEAR  : 1;
#   UINT32    TPMA_NV_GLOBALLOCK     : 1;
#   UINT32    TPMA_NV_PPREAD         : 1;
#   UINT32    TPMA_NV_OWNERREAD      : 1;
#   UINT32    TPMA_NV_AUTHREAD       : 1;
#   UINT32    TPMA_NV_POLICYREAD     : 1;
#   UINT32    reserved20_24          : 5;
#   UINT32    TPMA_NV_NO_DA          : 1;
#   UINT32    TPMA_NV_ORDERLY        : 1;
#   UINT32    TPMA_NV_CLEAR_STCLEAR  : 1;
#   UINT32    TPMA_NV_READLOCKED     : 1;
#   UINT32    TPMA_NV_WRITTEN        : 1;
#   UINT32    TPMA_NV_PLATFORMCREATE : 1;
#   UINT32    TPMA_NV_READ_STCLEAR   : 1;
# } TPMA_NV;
class TPMA_NV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TPMA_NV_PPWRITE",         UINT32, 1),
    ("TPMA_NV_OWNERWRITE ",     UINT32, 1),
    ("TPMA_NV_AUTHWRITE",       UINT32, 1),
    ("TPMA_NV_POLICYWRITE",     UINT32, 1),
    ("TPMA_NV_COUNTER",         UINT32, 1),
    ("TPMA_NV_BITS",            UINT32, 1),
    ("TPMA_NV_EXTEND",          UINT32, 1),
    ("reserved7_9",             UINT32, 3),
    ("TPMA_NV_POLICY_DELETE ",  UINT32, 1),
    ("TPMA_NV_WRITELOCKED",     UINT32, 1),
    ("TPMA_NV_WRITEALL",        UINT32, 1),
    ("TPMA_NV_WRITEDEFINE",     UINT32, 1),
    ("TPMA_NV_WRITE_STCLEAR ",  UINT32, 1),
    ("TPMA_NV_GLOBALLOCK",      UINT32, 1),
    ("TPMA_NV_PPREAD",          UINT32, 1),
    ("TPMA_NV_OWNERREAD",       UINT32, 1),
    ("TPMA_NV_AUTHREAD",        UINT32, 1),
    ("TPMA_NV_POLICYREAD",      UINT32, 1),
    ("reserved20_24",           UINT32, 5),
    ("TPMA_NV_NO_DA",           UINT32, 1),
    ("TPMA_NV_ORDERLY",         UINT32, 1),
    ("TPMA_NV_CLEAR_STCLEAR",   UINT32, 1),
    ("TPMA_NV_READLOCKED",      UINT32, 1),
    ("TPMA_NV_WRITTEN",         UINT32, 1),
    ("TPMA_NV_PLATFORMCREATE",  UINT32, 1),
    ("TPMA_NV_READ_STCLEAR",    UINT32, 1)
  ]

# 
# // Table 196 - TPMS_NV_PUBLIC Structure
# typedef struct {
#   TPMI_RH_NV_INDEX    nvIndex;
#   TPMI_ALG_HASH       nameAlg;
#   TPMA_NV             attributes;
#   TPM2B_DIGEST        authPolicy;
#   UINT16              dataSize;
# } TPMS_NV_PUBLIC;
class TPMS_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nvIndex",     TPMI_RH_NV_INDEX),
    ("nameAlg",     TPMI_ALG_HASH),
    ("attributes",  TPMA_NV),
    ("authPolicy",  TPM2B_DIGEST),
    ("dataSize",    UINT16)
  ]

# 
# // Table 197 - TPM2B_NV_PUBLIC Structure
# typedef struct {
#   UINT16            size;
#   TPMS_NV_PUBLIC    nvPublic;
# } TPM2B_NV_PUBLIC;
class TPM2B_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("nvPublic",  TPMS_NV_PUBLIC)
  ]

# 
# // 14 Context Data
# 
# // Table 198 - TPM2B_CONTEXT_SENSITIVE Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[MAX_CONTEXT_SIZE];
# } TPM2B_CONTEXT_SENSITIVE;
class TPM2B_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_CONTEXT_SIZE)
  ]

# 
# // Table 199 - TPMS_CONTEXT_DATA Structure
# typedef struct {
#   TPM2B_DIGEST               integrity;
#   TPM2B_CONTEXT_SENSITIVE    encrypted;
# } TPMS_CONTEXT_DATA;
class TPMS_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrity", TPM2B_DIGEST),
    ("encrypted", TPM2B_CONTEXT_SENSITIVE)
  ]

# 
# // Table 200 - TPM2B_CONTEXT_DATA Structure
# typedef struct {
#   UINT16    size;
#   BYTE      buffer[sizeof (TPMS_CONTEXT_DATA)];
# } TPM2B_CONTEXT_DATA;
class TPM2B_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof(TPMS_CONTEXT_DATA))
  ]

# 
# // Table 201 - TPMS_CONTEXT Structure
# typedef struct {
#   UINT64                sequence;
#   TPMI_DH_CONTEXT       savedHandle;
#   TPMI_RH_HIERARCHY     hierarchy;
#   TPM2B_CONTEXT_DATA    contextBlob;
# } TPMS_CONTEXT;
class TPMS_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sequence",    UINT64),
    ("savedHandle", TPMI_DH_CONTEXT),
    ("hierarchy",   TPMI_RH_HIERARCHY),
    ("contextBlob", TPM2B_CONTEXT_DATA)
  ]

# 
# // 15 Creation Data
# 
# // Table 203 - TPMS_CREATION_DATA Structure
# typedef struct {
#   TPML_PCR_SELECTION    pcrSelect;
#   TPM2B_DIGEST          pcrDigest;
#   TPMA_LOCALITY         locality;
#   TPM_ALG_ID            parentNameAlg;
#   TPM2B_NAME            parentName;
#   TPM2B_NAME            parentQualifiedName;
#   TPM2B_DATA            outsideInfo;
# } TPMS_CREATION_DATA;
class TPMS_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect",           TPML_PCR_SELECTION),
    ("pcrDigest",           TPM2B_DIGEST),
    ("locality",            TPMA_LOCALITY),
    ("parentNameAlg",       TPM_ALG_ID),
    ("parentName",          TPM2B_NAME),
    ("parentQualifiedName", TPM2B_NAME),
    ("outsideInfo",         TPM2B_DATA)
  ]

# 
# // Table 204 - TPM2B_CREATION_DATA Structure
# typedef struct {
#   UINT16                size;
#   TPMS_CREATION_DATA    creationData;
# } TPM2B_CREATION_DATA;
class TPM2B_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",            UINT16),
    ("creationData",    TPMS_CREATION_DATA)
  ]

# 
# //
# // Command Header
# //
# typedef struct {
#   TPM_ST    tag;
#   UINT32    paramSize;
#   TPM_CC    commandCode;
# } TPM2_COMMAND_HEADER;
class TPM2_COMMAND_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_ST),
    ("paramSize",   UINT32),
    ("commandCode", TPM_CC)
  ]

# 
# typedef struct {
#   TPM_ST    tag;
#   UINT32    paramSize;
#   TPM_RC    responseCode;
# } TPM2_RESPONSE_HEADER;
class TPM2_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_ST),
    ("paramSize",     UINT32),
    ("responseCode",  TPM_RC)
  ]

# 
# #pragma pack ()
# 
# //
# // TCG Algorithm Registry
# //
# #define HASH_ALG_SHA1     0x00000001
# #define HASH_ALG_SHA256   0x00000002
# #define HASH_ALG_SHA384   0x00000004
# #define HASH_ALG_SHA512   0x00000008
# #define HASH_ALG_SM3_256  0x00000010
HASH_ALG_SHA1     = 0x00000001
HASH_ALG_SHA256   = 0x00000002
HASH_ALG_SHA384   = 0x00000004
HASH_ALG_SHA512   = 0x00000008
HASH_ALG_SM3_256  = 0x00000010

# 
# #endif
# 