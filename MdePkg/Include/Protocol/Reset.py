# /** @file
#   Reset Architectural Protocol as defined in PI Specification VOLUME 2 DXE
# 
#   Used to provide ResetSystem runtime services
# 
#   The ResetSystem () UEFI 2.0 service is added to the EFI system table and the
#   EFI_RESET_ARCH_PROTOCOL_GUID protocol is registered with a NULL pointer.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# Reset.py
#
# EfiPy2.MdePkg.Protocol.Reset
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __ARCH_PROTOCOL_RESET_H__
# #define __ARCH_PROTOCOL_RESET_H__
from EfiPy2 import *

# 
# ///
# /// Global ID for the Reset Architectural Protocol
# ///
# #define EFI_RESET_ARCH_PROTOCOL_GUID  \
#   { 0x27CFAC88, 0x46CC, 0x11d4, {0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D } }
gEfiResetArchProtocolGuid   = \
  EFI_GUID (0x27CFAC88, 0x46CC, 0x11d4, (0x9A, 0x38, 0x00, 0x90, 0x27, 0x3F, 0xC1, 0x4D ))

# 
# extern EFI_GUID  gEfiResetArchProtocolGuid;
# 
# #endif
# 