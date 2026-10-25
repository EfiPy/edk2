# /** @file
#   SMM Sx Dispatch Protocol as defined in PI 1.2 Specification
#   Volume 4 System Management Mode Core Interface.
# 
#   Provides the parent dispatch service for a given Sx-state source generator.
# 
#   Copyright (c) 2009 - 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# SmmSxDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmSxDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_SX_DISPATCH2_H_
# #define _SMM_SX_DISPATCH2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmSxDispatch.h>
from EfiPy2.MdePkg.Protocol import MmSxDispatch
from EfiPy2.MdePkg.Protocol import MmSwDispatch

# 
# #define EFI_SMM_SX_DISPATCH2_PROTOCOL_GUID  EFI_MM_SX_DISPATCH_PROTOCOL_GUID
gEfiSmmSxDispatch2ProtocolGuid = MmSwDispatch.gEfiMmSwDispatchProtocolGuid

# 
# ///
# /// The dispatch function's context
# ///
# typedef EFI_MM_SX_REGISTER_CONTEXT EFI_SMM_SX_REGISTER_CONTEXT;
EFI_SMM_SX_REGISTER_CONTEXT = MmSxDispatch.EFI_MM_SX_REGISTER_CONTEXT

# 
# typedef EFI_MM_SX_DISPATCH_PROTOCOL EFI_SMM_SX_DISPATCH2_PROTOCOL;
EFI_SMM_SX_DISPATCH2_PROTOCOL = MmSxDispatch.EFI_MM_SX_DISPATCH_PROTOCOL

# 
# typedef EFI_MM_SX_REGISTER EFI_SMM_SX_REGISTER2;
EFI_SMM_SX_REGISTER2 = MmSxDispatch.EFI_MM_SX_REGISTER

# 
# typedef EFI_MM_SX_UNREGISTER EFI_SMM_SX_UNREGISTER2;
EFI_SMM_SX_UNREGISTER2 = MmSxDispatch.EFI_MM_SX_UNREGISTER

# 
# extern EFI_GUID  gEfiSmmSxDispatch2ProtocolGuid;
# 
# #endif
# 