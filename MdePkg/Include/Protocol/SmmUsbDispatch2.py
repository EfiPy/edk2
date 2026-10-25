# /** @file
#   SMM USB Dispatch2 Protocol as defined in PI 1.1 Specification
#   Volume 4 System Management Mode Core Interface.
# 
#   Provides the parent dispatch service for the USB SMI source generator.
# 
#   Copyright (c) 2009 - 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This protocol is from PI Version 1.1.
# 
# **/
# SmmUsbDispatch2.py
#
# EfiPy2.MdePkg.Protocol.SmmUsbDispatch2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_USB_DISPATCH2_H_
# #define _SMM_USB_DISPATCH2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmUsbDispatch.h>
from EfiPy2.MdePkg.Protocol import MmUsbDispatch

# 
# #define EFI_SMM_USB_DISPATCH2_PROTOCOL_GUID  EFI_MM_USB_DISPATCH_PROTOCOL_GUID
gEfiSmmUsbDispatch2ProtocolGuid = MmUsbDispatch.gEfiMmUsbDispatchProtocolGuid

# 
# ///
# /// USB SMI event types
# ///
# typedef EFI_USB_MMI_TYPE EFI_USB_SMI_TYPE;
EFI_USB_SMI_TYPE = MmUsbDispatch.EFI_USB_MMI_TYPE

# 
# ///
# /// The dispatch function's context.
# ///
# typedef EFI_MM_USB_REGISTER_CONTEXT EFI_SMM_USB_REGISTER_CONTEXT;
EFI_SMM_USB_REGISTER_CONTEXT = MmUsbDispatch.EFI_MM_USB_REGISTER_CONTEXT

# 
# typedef EFI_MM_USB_DISPATCH_PROTOCOL EFI_SMM_USB_DISPATCH2_PROTOCOL;
EFI_SMM_USB_DISPATCH2_PROTOCOL = MmUsbDispatch.EFI_MM_USB_DISPATCH_PROTOCOL

# 
# typedef EFI_MM_USB_REGISTER EFI_SMM_USB_REGISTER2;
EFI_SMM_USB_REGISTER2 = MmUsbDispatch.EFI_MM_USB_REGISTER

# 
# typedef EFI_MM_USB_UNREGISTER EFI_SMM_USB_UNREGISTER2;
EFI_SMM_USB_UNREGISTER2 = MmUsbDispatch.EFI_MM_USB_UNREGISTER

# 
# extern EFI_GUID  gEfiSmmUsbDispatch2ProtocolGuid;
# 
# #endif
# 