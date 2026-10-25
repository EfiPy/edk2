# /** @file
#   This file defines the SPI SMM Configuration Protocol.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#     This Protocol was introduced in UEFI PI Specification 1.6.
# 
# **/
# SpiSmmConfiguration.py
#
# EfiPy2.MdePkg.Protocol.SpiSmmConfiguration
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __SPI_SMM_CONFIGURATION_PROTOCOL_H__
# #define __SPI_SMM_CONFIGURATION_PROTOCOL_H__
from EfiPy2 import *

# 
# #include <Protocol/SpiConfiguration.h>
from EfiPy2.MdePkg.Protocol.SpiConfiguration import EFI_SPI_CONFIGURATION_PROTOCOL

# 
# ///
# /// Global ID for the SPI SMM Configuration Protocol
# ///
# #define EFI_SPI_SMM_CONFIGURATION_PROTOCOL_GUID  \
#   { 0x995c6eca, 0x171b, 0x45fd,                  \
#     { 0xa3, 0xaa, 0xfd, 0x4c, 0x9c, 0x9d, 0xef, 0x59 }}
gEfiSpiSmmConfigurationProtocolGuid = \
  EFI_GUID (0x995c6eca, 0x171b, 0x45fd, (0xa3, 0xaa, 0xfd, 0x4c, 0x9c, 0x9d, 0xef, 0x59 ))

# 
# typedef
#   struct _EFI_SPI_CONFIGURATION_PROTOCOL
# EFI_SPI_SMM_CONFIGURATION_PROTOCOL;
EFI_SPI_SMM_CONFIGURATION_PROTOCOL = EFI_SPI_CONFIGURATION_PROTOCOL

# 
# extern EFI_GUID  gEfiSpiSmmConfigurationProtocolGuid;
# 
# #endif // __SPI_SMM_CONFIGURATION_H__
# 