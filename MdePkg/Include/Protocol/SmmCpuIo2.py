# /** @file
#   SMM CPU I/O 2 protocol as defined in the PI 1.2 specification.
# 
#   This protocol provides CPU I/O and memory access within SMM.
# 
#   Copyright (c) 2009 - 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# SmmCpuIo2.py
#
# EfiPy2.MdePkg.Protocol.SmmCpuIo2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_CPU_IO2_H_
# #define _SMM_CPU_IO2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmCpuIo.h>
from EfiPy2.MdePkg.Protocol import MmCpuIo
# 
# #define EFI_SMM_CPU_IO2_PROTOCOL_GUID  EFI_MM_CPU_IO_PROTOCOL_GUID
gEfiSmmCpuIo2ProtocolGuid = MmCpuIo.gEfiMmCpuIoProtocolGuid
# 
# typedef EFI_MM_CPU_IO_PROTOCOL EFI_SMM_CPU_IO2_PROTOCOL;
EFI_SMM_CPU_IO2_PROTOCOL  = MmCpuIo.EFI_MM_CPU_IO_PROTOCOL

# 
# ///
# /// Width of the SMM CPU I/O operations
# ///
# #define SMM_IO_UINT8   MM_IO_UINT8
# #define SMM_IO_UINT16  MM_IO_UINT16
# #define SMM_IO_UINT32  MM_IO_UINT32
# #define SMM_IO_UINT64  MM_IO_UINT64
SMM_IO_UINT8   = MmCpuIo.MM_IO_UINT8
SMM_IO_UINT16  = MmCpuIo.MM_IO_UINT16
SMM_IO_UINT32  = MmCpuIo.MM_IO_UINT32
SMM_IO_UINT64  = MmCpuIo.MM_IO_UINT64

# 
# typedef EFI_MM_IO_WIDTH EFI_SMM_IO_WIDTH;
EFI_SMM_IO_WIDTH    = MmCpuIo.EFI_MM_IO_WIDTH
# typedef EFI_MM_CPU_IO   EFI_SMM_CPU_IO2;
EFI_SMM_CPU_IO2     = MmCpuIo.EFI_MM_CPU_IO

# 
# typedef EFI_MM_IO_ACCESS EFI_SMM_IO_ACCESS2;
EFI_SMM_IO_ACCESS2  = MmCpuIo.EFI_MM_IO_ACCESS
# 
# extern EFI_GUID  gEfiSmmCpuIo2ProtocolGuid;
# 
# #endif
# 