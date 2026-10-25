# /** @file
#   This file defines the Legacy SPI SMM Controler Protocol.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#     This Protocol was introduced in UEFI PI Specification 1.6.
# 
# **/
# LegacySpiSmmController.py
#
# EfiPy2.MdePkg.Protocol.LegacySpiSmmController
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __LEGACY_SPI_SMM_CONTROLLER_PROTOCOL_H__
# #define __LEGACY_SPI_SMM_CONTROLLER_PROTOCOL_H__
from EfiPy2 import *

# 
# #include <Protocol/LegacySpiController.h>
from EfiPy2.MdePkg.Protocol.LegacySpiController import EFI_LEGACY_SPI_CONTROLLER_PROTOCOL

# 
# ///
# /// Global ID for the Legacy SPI SMM Controller Protocol
# ///
# #define EFI_LEGACY_SPI_SMM_CONTROLLER_PROTOCOL_GUID  \
#   { 0x62331b78, 0xd8d0, 0x4c8c,                 \
#     { 0x8c, 0xcb, 0xd2, 0x7d, 0xfe, 0x32, 0xdb, 0x9b }}
gEfiLegacySpiSmmControllerProtocolGuid = \
  EFI_GUID (0x62331b78, 0xd8d0, 0x4c8c, (0x8c, 0xcb, 0xd2, 0x7d, 0xfe, 0x32, 0xdb, 0x9b ))

# 
# typedef
#   struct _EFI_LEGACY_SPI_CONTROLLER_PROTOCOL
# EFI_LEGACY_SPI_SMM_CONTROLLER_PROTOCOL;
EFI_LEGACY_SPI_SMM_CONTROLLER_PROTOCOL = EFI_LEGACY_SPI_CONTROLLER_PROTOCOL
# 
# extern EFI_GUID  gEfiLegacySpiSmmControllerProtocolGuid;
# 
# #endif // __LEGACY_SPI_SMM_CONTROLLER_PROTOCOL_H__
# 