# /** @file
#   EFI MM Communication Protocol 2 as defined in the PI 1.7 errata A specification.
# 
#   This protocol provides a means of communicating between drivers outside of MM and MMI
#   handlers inside of MM.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   Copyright (c) 2019, Arm Limited. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# MmCommunication2.py
#
# EfiPy2.MdePkg.Protocol.MmCommunication2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _MM_COMMUNICATION2_H_
# #define _MM_COMMUNICATION2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmCommunication.h>
from EfiPy2.MdePkg.Protocol import MmCommunication

# 
# #define EFI_MM_COMMUNICATION2_PROTOCOL_GUID \
#   { \
#     0x378daedc, 0xf06b, 0x4446, { 0x83, 0x14, 0x40, 0xab, 0x93, 0x3c, 0x87, 0xa3 } \
#   }
gEfiMmCommunication2ProtocolGuid = \
  EFI_GUID (0x378daedc, 0xf06b, 0x4446, ( 0x83, 0x14, 0x40, 0xab, 0x93, 0x3c, 0x87, 0xa3 ))

# 
# typedef struct _EFI_MM_COMMUNICATION2_PROTOCOL EFI_MM_COMMUNICATION2_PROTOCOL;
class EFI_MM_COMMUNICATION2_PROTOCOL (Structure):
  pass

# 
# /**
#   Communicates with a registered handler.
# 
#   This function provides a service to send and receive messages from a registered UEFI service.
# 
#   @param[in] This                     The EFI_MM_COMMUNICATION_PROTOCOL instance.
#   @param[in, out] CommBufferPhysical  Physical address of the MM communication buffer
#   @param[in, out] CommBufferVirtual   Virtual address of the MM communication buffer
#   @param[in, out] CommSize            The size of the data buffer being passed in. On exit, the
#                                       size of data being returned. Zero if the handler does not
#                                       wish to reply with any data. This parameter is optional
#                                       and may be NULL.
# 
#   @retval EFI_SUCCESS            The message was successfully posted.
#   @retval EFI_INVALID_PARAMETER  CommBufferPhysical was NULL or CommBufferVirtual was NULL.
#   @retval EFI_BAD_BUFFER_SIZE    The buffer is too large for the MM implementation.
#                                  If this error is returned, the MessageLength field
#                                  in the CommBuffer header or the integer pointed by
#                                  CommSize, are updated to reflect the maximum payload
#                                  size the implementation can accommodate.
#   @retval EFI_ACCESS_DENIED      The CommunicateBuffer parameter or CommSize parameter,
#                                  if not omitted, are in address range that cannot be
#                                  accessed by the MM environment.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_MM_COMMUNICATE2)(
#   IN CONST EFI_MM_COMMUNICATION2_PROTOCOL   *This,
#   IN OUT VOID                               *CommBufferPhysical,
#   IN OUT VOID                               *CommBufferVirtual,
#   IN OUT UINTN                              *CommSize OPTIONAL
#   );
EFI_MM_COMMUNICATE2 = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_COMMUNICATION2_PROTOCOL),  #   IN CONST  *This,
  PVOID,                                    #   IN OUT    *CommBufferPhysical,
  PVOID,                                    #   IN OUT    *CommBufferVirtual,
  POINTER(UINTN),                           #   IN OUT    *CommSize OPTIONAL
  )

# 
# ///
# /// EFI MM Communication Protocol provides runtime services for communicating
# /// between DXE drivers and a registered MMI handler.
# ///
# struct _EFI_MM_COMMUNICATION2_PROTOCOL {
#   EFI_MM_COMMUNICATE2    Communicate;
# };
EFI_MM_COMMUNICATION2_PROTOCOL._fields_ = [
    ("Communicate", EFI_MM_COMMUNICATE2)
  ]

# 
# extern EFI_GUID  gEfiMmCommunication2ProtocolGuid;
# 
# #endif
# 