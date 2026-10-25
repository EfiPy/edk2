# /** @file
#   SMM PCI Root Bridge IO protocol as defined in the PI 1.2 specification.
# 
#   This protocol provides PCI I/O and memory access within SMM.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# SmmPciRootBridgeIo.py
#
# EfiPy2.MdePkg.Protocol.SmmPciRootBridgeIo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_PCI_ROOT_BRIDGE_IO_H_
# #define _SMM_PCI_ROOT_BRIDGE_IO_H_
from EfiPy2 import *

# 
# #include <Protocol/MmPciRootBridgeIo.h>
from EfiPy2.MdePkg.Protocol import MmPciRootBridgeIo

# 
# #define EFI_SMM_PCI_ROOT_BRIDGE_IO_PROTOCOL_GUID  EFI_MM_PCI_ROOT_BRIDGE_IO_PROTOCOL_GUID
gEfiSmmPciRootBridgeIoProtocolGuid = MmPciRootBridgeIo.gEfiMmPciRootBridgeIoProtocolGuid

# 
# ///
# /// This protocol provides the same functionality as the PCI Root Bridge I/O Protocol defined in the
# /// UEFI 2.1 Specifcation, section 13.2, except that the functions for Map() and Unmap() may return
# /// EFI_UNSUPPORTED.
# ///
# typedef EFI_MM_PCI_ROOT_BRIDGE_IO_PROTOCOL EFI_SMM_PCI_ROOT_BRIDGE_IO_PROTOCOL;
EFI_SMM_PCI_ROOT_BRIDGE_IO_PROTOCOL = MmPciRootBridgeIo.EFI_MM_PCI_ROOT_BRIDGE_IO_PROTOCOL

# 
# extern EFI_GUID  gEfiSmmPciRootBridgeIoProtocolGuid;
# 
# #endif
# 