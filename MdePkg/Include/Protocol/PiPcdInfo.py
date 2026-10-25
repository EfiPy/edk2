# /** @file
#   Platform Configuration Database (PCD) Info Protocol defined in PI 1.2.1 Vol3.
# 
#   The protocol that provides additional information about items that reside in the PCD database.
# 
#   Copyright (c) 2013, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   PI Version 1.2.1 Vol 3.
# **/
# PiPcdInfo.py
#
# EfiPy2.MdePkg.Protocol.PiPcdInfo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __PI_PCD_INFO_H__
# #define __PI_PCD_INFO_H__
from EfiPy2 import *

from EfiPy2.MdePkg.Pi.PiMultiPhase import EFI_PCD_INFO

# 
# extern EFI_GUID  gEfiGetPcdInfoProtocolGuid;
# 
# #define EFI_GET_PCD_INFO_PROTOCOL_GUID \
#   { 0xfd0f4478,  0xefd, 0x461d, { 0xba, 0x2d, 0xe5, 0x8c, 0x45, 0xfd, 0x5f, 0x5e } }
gEfiGetPcdInfoProtocolGuid  = \
  EFI_GUID (0xfd0f4478,  0xefd, 0x461d, ( 0xba, 0x2d, 0xe5, 0x8c, 0x45, 0xfd, 0x5f, 0x5e ))

# 
# ///
# /// The forward declaration for EFI_GET_PCD_INFO_PROTOCOL.
# ///
# typedef struct _EFI_GET_PCD_INFO_PROTOCOL EFI_GET_PCD_INFO_PROTOCOL;
class EFI_GET_PCD_INFO_PROTOCOL (Structure):
  pass

# 
# /**
#   Retrieve additional information associated with a PCD token.
# 
#   This includes information such as the type of value the TokenNumber is associated with as well as possible
#   human readable name that is associated with the token.
# 
#   @param[in]    Guid        The 128-bit unique value that designates the namespace from which to extract the value.
#   @param[in]    TokenNumber The PCD token number.
#   @param[out]   PcdInfo     The returned information associated with the requested TokenNumber.
# 
#   @retval  EFI_SUCCESS      The PCD information was returned successfully
#   @retval  EFI_NOT_FOUND    The PCD service could not find the requested token number.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_GET_PCD_INFO_PROTOCOL_GET_INFO)(
#   IN CONST  EFI_GUID        *Guid,
#   IN        UINTN           TokenNumber,
#   OUT       EFI_PCD_INFO    *PcdInfo
#   );
EFI_GET_PCD_INFO_PROTOCOL_GET_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_GUID),                  # IN CONST  *Guid,
  UINTN,                              # IN        TokenNumber,
  POINTER(EFI_PCD_INFO)  # OUT       *PcdInfo
  )

# 
# /**
#   Retrieve the currently set SKU Id.
# 
#   @return   The currently set SKU Id. If the platform has not set at a SKU Id, then the
#             default SKU Id value of 0 is returned. If the platform has set a SKU Id, then the currently set SKU
#             Id is returned.
# **/
# typedef
# UINTN
# (EFIAPI *EFI_GET_PCD_INFO_PROTOCOL_GET_SKU)(
#   VOID
#   );
EFI_GET_PCD_INFO_PROTOCOL_GET_SKU = CFUNCTYPE (
  UINTN
  )

# 
# ///
# /// Callers to this protocol must be at a TPL_APPLICATION task priority level.
# /// This is the PCD service to use when querying for some additional data that can be contained in the
# /// PCD database.
# ///
# struct _EFI_GET_PCD_INFO_PROTOCOL {
#   ///
#   /// Retrieve additional information associated with a PCD.
#   ///
#   EFI_GET_PCD_INFO_PROTOCOL_GET_INFO    GetInfo;
#   ///
#   /// Retrieve the currently set SKU Id.
#   ///
#   EFI_GET_PCD_INFO_PROTOCOL_GET_SKU     GetSku;
# };
EFI_GET_PCD_INFO_PROTOCOL._fields_ = [
    ("GetInfo", EFI_GET_PCD_INFO_PROTOCOL_GET_INFO),
    ("GetSku",  EFI_GET_PCD_INFO_PROTOCOL_GET_SKU)
  ]

# 
# #endif
# 