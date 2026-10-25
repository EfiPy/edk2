# /** @file
#   This file defines the EFI EAP Configuration protocol.
# 
#   Copyright (c) 2015 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol is introduced in UEFI Specification 2.5
# 
# **/
# EapConfiguration.py
#
# EfiPy2.MdePkg.Protocol.EapConfiguration
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __EFI_EAP_CONFIGURATION_PROTOCOL_H__
# #define __EFI_EAP_CONFIGURATION_PROTOCOL_H__
from EfiPy2 import *

# 
# ///
# /// EFI EAP Configuration protocol provides a way to set and get EAP configuration.
# ///
# #define EFI_EAP_CONFIGURATION_PROTOCOL_GUID \
#   { \
#     0xe5b58dbb, 0x7688, 0x44b4, {0x97, 0xbf, 0x5f, 0x1d, 0x4b, 0x7c, 0xc8, 0xdb } \
#   }
gEfiEapConfigurationProtocolGuid  = \
  EFI_GUID (0xe5b58dbb, 0x7688, 0x44b4, (0x97, 0xbf, 0x5f, 0x1d, 0x4b, 0x7c, 0xc8, 0xdb ))

# 
# typedef struct _EFI_EAP_CONFIGURATION_PROTOCOL EFI_EAP_CONFIGURATION_PROTOCOL;
class EFI_EAP_CONFIGURATION_PROTOCOL (Structure):
  pass

# 
# ///
# /// Make sure it not conflict with any real EapTypeXXX
# ///
# #define EFI_EAP_TYPE_ATTRIBUTE  0
EFI_EAP_TYPE_ATTRIBUTE = 0

# 
# typedef enum {
#   ///
#   /// EFI_EAP_TYPE_ATTRIBUTE
#   ///
#   EfiEapConfigEapAuthMethod,
#   EfiEapConfigEapSupportedAuthMethod,
#   ///
#   /// EapTypeIdentity
#   ///
#   EfiEapConfigIdentityString,
#   ///
#   /// EapTypeEAPTLS/EapTypePEAP
#   ///
#   EfiEapConfigEapTlsCACert,
#   EfiEapConfigEapTlsClientCert,
#   EfiEapConfigEapTlsClientPrivateKeyFile,
#   EfiEapConfigEapTlsClientPrivateKeyFilePassword, // ASCII format, Volatile
#   EfiEapConfigEapTlsCipherSuite,
#   EfiEapConfigEapTlsSupportedCipherSuite,
#   ///
#   /// EapTypeMSChapV2
#   ///
#   EfiEapConfigEapMSChapV2Password, // UNICODE format, Volatile
#   ///
#   /// EapTypePEAP
#   ///
#   EfiEapConfigEap2ndAuthMethod,
#   ///
#   /// More...
#   ///
# } EFI_EAP_CONFIG_DATA_TYPE;
EfiEapConfigEapAuthMethod                       =  0
EfiEapConfigEapSupportedAuthMethod              =  1
EfiEapConfigIdentityString                      =  2
EfiEapConfigEapTlsCACert                        =  3
EfiEapConfigEapTlsClientCert                    =  4
EfiEapConfigEapTlsClientPrivateKeyFile          =  5
EfiEapConfigEapTlsClientPrivateKeyFilePassword  =  6
EfiEapConfigEapTlsCipherSuite                   =  7
EfiEapConfigEapTlsSupportedCipherSuite          =  8
EfiEapConfigEapMSChapV2Password                 =  9
EfiEapConfigEap2ndAuthMethod                    = 10
EFI_EAP_CONFIG_DATA_TYPE                        = ENUM

# 
# ///
# /// EFI_EAP_TYPE
# ///
# typedef UINT8 EFI_EAP_TYPE;
# #define EFI_EAP_TYPE_ATTRIBUTE      0
# #define EFI_EAP_TYPE_IDENTITY       1
# #define EFI_EAP_TYPE_NOTIFICATION   2
# #define EFI_EAP_TYPE_NAK            3
# #define EFI_EAP_TYPE_MD5CHALLENGE   4
# #define EFI_EAP_TYPE_OTP            5
# #define EFI_EAP_TYPE_GTC            6
# #define EFI_EAP_TYPE_EAPTLS         13
# #define EFI_EAP_TYPE_EAPSIM         18
# #define EFI_EAP_TYPE_TTLS           21
# #define EFI_EAP_TYPE_PEAP           25
# #define EFI_EAP_TYPE_MSCHAPV2       26
# #define EFI_EAP_TYPE_EAP_EXTENSION  33
EFI_EAP_TYPE                = UINT8
EFI_EAP_TYPE_ATTRIBUTE      = 0
EFI_EAP_TYPE_IDENTITY       = 1
EFI_EAP_TYPE_NOTIFICATION   = 2
EFI_EAP_TYPE_NAK            = 3
EFI_EAP_TYPE_MD5CHALLENGE   = 4
EFI_EAP_TYPE_OTP            = 5
EFI_EAP_TYPE_GTC            = 6
EFI_EAP_TYPE_EAPTLS         = 13
EFI_EAP_TYPE_EAPSIM         = 18
EFI_EAP_TYPE_TTLS           = 21
EFI_EAP_TYPE_PEAP           = 25
EFI_EAP_TYPE_MSCHAPV2       = 26
EFI_EAP_TYPE_EAP_EXTENSION  = 33

# 
# /**
#   Set EAP configuration data.
# 
#   The SetData() function sets EAP configuration to non-volatile storage or volatile
#   storage.
# 
#   @param[in]  This                Pointer to the EFI_EAP_CONFIGURATION_PROTOCOL instance.
#   @param[in]  EapType             EAP type.
#   @param[in]  DataType            Configuration data type.
#   @param[in]  Data                Pointer to configuration data.
#   @param[in]  DataSize            Total size of configuration data.
# 
#   @retval EFI_SUCCESS             The EAP configuration data is set successfully.
#   @retval EFI_INVALID_PARAMETER   One or more of the following conditions is TRUE:
#                                   Data is NULL.
#                                   DataSize is 0.
#   @retval EFI_UNSUPPORTED         The EapType or DataType is unsupported.
#   @retval EFI_OUT_OF_RESOURCES    Required system resources could not be allocated.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EAP_CONFIGURATION_SET_DATA)(
#   IN EFI_EAP_CONFIGURATION_PROTOCOL       *This,
#   IN EFI_EAP_TYPE                         EapType,
#   IN EFI_EAP_CONFIG_DATA_TYPE             DataType,
#   IN VOID                                 *Data,
#   IN UINTN                                DataSize
#   );
EFI_EAP_CONFIGURATION_SET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_CONFIGURATION_PROTOCOL),  # IN *This,
  EFI_EAP_TYPE,                             # IN EapType,
  EFI_EAP_CONFIG_DATA_TYPE,                 # IN DataType,
  PVOID,                                    # IN *Data,
  UINTN                                     # IN DataSize
  )

# 
# /**
#   Get EAP configuration data.
# 
#   The GetData() function gets EAP configuration.
# 
#   @param[in]       This           Pointer to the EFI_EAP_CONFIGURATION_PROTOCOL instance.
#   @param[in]       EapType        EAP type.
#   @param[in]       DataType       Configuration data type.
#   @param[in, out]  Data           Pointer to configuration data.
#   @param[in, out]  DataSize       Total size of configuration data. On input, it means
#                                   the size of Data buffer. On output, it means the size
#                                   of copied Data buffer if EFI_SUCCESS, and means the
#                                   size of desired Data buffer if EFI_BUFFER_TOO_SMALL.
# 
#   @retval EFI_SUCCESS             The EAP configuration data is got successfully.
#   @retval EFI_INVALID_PARAMETER   One or more of the following conditions is TRUE:
#                                   Data is NULL.
#                                   DataSize is NULL.
#   @retval EFI_UNSUPPORTED         The EapType or DataType is unsupported.
#   @retval EFI_NOT_FOUND           The EAP configuration data is not found.
#   @retval EFI_BUFFER_TOO_SMALL    The buffer is too small to hold the buffer.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EAP_CONFIGURATION_GET_DATA)(
#   IN EFI_EAP_CONFIGURATION_PROTOCOL       *This,
#   IN EFI_EAP_TYPE                         EapType,
#   IN EFI_EAP_CONFIG_DATA_TYPE             DataType,
#   IN OUT VOID                             *Data,
#   IN OUT UINTN                            *DataSize
#   );
EFI_EAP_CONFIGURATION_GET_DATA = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EAP_CONFIGURATION_PROTOCOL),  # IN      *This,
  EFI_EAP_TYPE,                             # IN      EapType,
  EFI_EAP_CONFIG_DATA_TYPE,                 # IN      DataType,
  PVOID,                                    # IN OUT  *Data,
  POINTER(UINTN)                            # IN OUT  DataSize
  )

# 
# ///
# /// The EFI_EAP_CONFIGURATION_PROTOCOL
# /// is designed to provide a way to set and get EAP configuration, such as Certificate,
# /// private key file.
# ///
# struct _EFI_EAP_CONFIGURATION_PROTOCOL {
#   EFI_EAP_CONFIGURATION_SET_DATA    SetData;
#   EFI_EAP_CONFIGURATION_GET_DATA    GetData;
# };
EFI_EAP_CONFIGURATION_PROTOCOL._fields_ = [
    ("SetData", EFI_EAP_CONFIGURATION_SET_DATA),
    ("GetData", EFI_EAP_CONFIGURATION_GET_DATA)
  ]

# 
# extern EFI_GUID  gEfiEapConfigurationProtocolGuid;
# 
# #endif
# 