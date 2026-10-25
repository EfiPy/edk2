# /** @file
#   SMM General Purpose Input (GPI) Dispatch2 Protocol as defined in PI 1.1 Specification
#   Volume 4 System Management Mode Core Interface.
# 
#   This protocol provides the parent dispatch service for the General Purpose Input
#   (GPI) SMI source generator.
# 
#   The EFI_SMM_GPI_DISPATCH2_PROTOCOL provides the ability to install child handlers for the
#   given event types.  Several inputs can be enabled.  This purpose of this interface is to generate an
#   SMI in response to any of these inputs having a true value provided.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This protocol is from PI Version 1.1.
# 
# **/
# SmmGpiDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmGpiDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_GPI_DISPATCH2_H_
# #define _SMM_GPI_DISPATCH2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmGpiDispatch.h>
from EfiPy2.MdePkg.Protocol import MmGpiDispatch

# #include <Pi/PiSmmCis.h>
# 
# #define EFI_SMM_GPI_DISPATCH2_PROTOCOL_GUID  EFI_MM_GPI_DISPATCH_PROTOCOL_GUID
gEfiSmmGpiDispatch2ProtocolGuid = MmGpiDispatch.gEfiMmGpiDispatchProtocolGuid

# ///
# /// The dispatch function's context.
# ///
# typedef EFI_MM_GPI_REGISTER_CONTEXT EFI_SMM_GPI_REGISTER_CONTEXT;
EFI_SMM_GPI_REGISTER_CONTEXT = MmGpiDispatch.EFI_MM_GPI_REGISTER_CONTEXT

# 
# typedef EFI_MM_GPI_REGISTER EFI_SMM_GPI_REGISTER2;
EFI_SMM_GPI_REGISTER2 = MmGpiDispatch.EFI_MM_GPI_REGISTER

# 
# typedef EFI_MM_GPI_UNREGISTER EFI_SMM_GPI_UNREGISTER2;
EFI_SMM_GPI_UNREGISTER2 = MmGpiDispatch.EFI_MM_GPI_UNREGISTER

# 
# typedef EFI_MM_GPI_DISPATCH_PROTOCOL EFI_SMM_GPI_DISPATCH2_PROTOCOL;
EFI_SMM_GPI_DISPATCH2_PROTOCOL = MmGpiDispatch.EFI_MM_GPI_DISPATCH_PROTOCOL

# 
# extern EFI_GUID  gEfiSmmGpiDispatch2ProtocolGuid;
# 
# #endif
# 