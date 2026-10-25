# /** @file
#   The file provides the protocol to provide interface to accept memory.
# 
#   Copyright (c) 2021 - 2022, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# MemoryAccept.py
#
# EfiPy2.MdePkg.Protocol.MemoryAccept
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef MEMORY_ACCEPT_H_
# #define MEMORY_ACCEPT_H_
from EfiPy2 import *

# 
# #define EDKII_MEMORY_ACCEPT_PROTOCOL_GUID \
#   { 0x38c74800, 0x5590, 0x4db4, { 0xa0, 0xf3, 0x67, 0x5d, 0x9b, 0x8e, 0x80, 0x26 } };
gEdkiiMemoryAcceptProtocolGuid  = \
  EFI_GUID (0x38c74800, 0x5590, 0x4db4, ( 0xa0, 0xf3, 0x67, 0x5d, 0x9b, 0x8e, 0x80, 0x26 ))

# 
# typedef struct _EDKII_MEMORY_ACCEPT_PROTOCOL EDKII_MEMORY_ACCEPT_PROTOCOL;
class EDKII_MEMORY_ACCEPT_PROTOCOL (Structure):
  pass

# 
# /**
#   @param This                   A pointer to a EDKII_MEMORY_ACCEPT_PROTOCOL.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EDKII_ACCEPT_MEMORY)(
#   IN  EDKII_MEMORY_ACCEPT_PROTOCOL  *This,
#   IN  EFI_PHYSICAL_ADDRESS          StartAddress,
#   IN  UINTN                         Size
#   );
EDKII_ACCEPT_MEMORY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EDKII_MEMORY_ACCEPT_PROTOCOL),    #   IN  *This
  EFI_PHYSICAL_ADDRESS,                     #   IN  StartAddress,
  UINTN                                     #   IN  Size
  )

# 
# ///
# /// The EDKII_MEMORY_ACCEPT_PROTOCOL provides the ability for memory services
# /// to accept memory.
# ///
# struct _EDKII_MEMORY_ACCEPT_PROTOCOL {
#   EDKII_ACCEPT_MEMORY    AcceptMemory;
# };
EDKII_MEMORY_ACCEPT_PROTOCOL._fields_ = [
    ("AcceptMemory",  EDKII_ACCEPT_MEMORY)
  ]

# 
# extern EFI_GUID  gEdkiiMemoryAcceptProtocolGuid;
# 
# #endif
# 