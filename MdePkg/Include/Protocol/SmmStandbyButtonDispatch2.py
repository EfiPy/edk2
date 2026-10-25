# /** @file
#   SMM Standby Button Dispatch2 Protocol as defined in PI 1.1 Specification
#   Volume 4 System Management Mode Core Interface.
# 
#   This protocol provides the parent dispatch service for the standby button SMI source generator.
# 
#   Copyright (c) 2009 - 2010, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This protocol is from PI Version 1.1.
# 
# **/
# SmmStandbyButtonDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmStandbyButtonDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_STANDBY_BUTTON_DISPATCH2_H_
# #define _SMM_STANDBY_BUTTON_DISPATCH2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmStandbyButtonDispatch.h>
from EfiPy2.MdePkg.Protocol import MmStandbyButtonDispatch

# 
# #define EFI_SMM_STANDBY_BUTTON_DISPATCH2_PROTOCOL_GUID  EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL_GUID
gEfiSmmStandbyButtonDispatch2ProtocolGuid = MmStandbyButtonDispatch.gEfiMmStandbyButtonDispatchProtocolGuid

# 
# ///
# /// The dispatch function's context.
# ///
# typedef EFI_MM_STANDBY_BUTTON_REGISTER_CONTEXT EFI_SMM_STANDBY_BUTTON_REGISTER_CONTEXT;
EFI_SMM_STANDBY_BUTTON_REGISTER_CONTEXT = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_REGISTER_CONTEXT

# 
# typedef EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL EFI_SMM_STANDBY_BUTTON_DISPATCH2_PROTOCOL;
EFI_SMM_STANDBY_BUTTON_DISPATCH2_PROTOCOL = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_DISPATCH_PROTOCOL

# 
# typedef EFI_MM_STANDBY_BUTTON_REGISTER EFI_SMM_STANDBY_BUTTON_REGISTER2;
EFI_SMM_STANDBY_BUTTON_REGISTER2 = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_REGISTER
# 
# typedef EFI_MM_STANDBY_BUTTON_UNREGISTER EFI_SMM_STANDBY_BUTTON_UNREGISTER2;
EFI_SMM_STANDBY_BUTTON_UNREGISTER2 = MmStandbyButtonDispatch.EFI_MM_STANDBY_BUTTON_UNREGISTER

# 
# extern EFI_GUID  gEfiSmmStandbyButtonDispatch2ProtocolGuid;
# 
# #endif
# 