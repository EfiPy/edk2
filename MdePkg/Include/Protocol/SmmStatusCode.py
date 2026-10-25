# /** @file
#   EFI SMM Status Code Protocol as defined in the PI 1.2 specification.
# 
#   This protocol provides the basic status code services while in SMM.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# SmmStatusCode.py
#
# EfiPy2.MdePkg.Protocol.SmmStatusCode
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_STATUS_CODE_H__
# #define _SMM_STATUS_CODE_H__
from EfiPy2 import *

# 
# #include <Protocol/MmStatusCode.h>
from EfiPy2.MdePkg.Protocol import MmStatusCode

# 
# #define EFI_SMM_STATUS_CODE_PROTOCOL_GUID  EFI_MM_STATUS_CODE_PROTOCOL_GUID
gEfiSmmStatusCodeProtocolGuid = MmStatusCode.gEfiMmStatusCodeProtocolGuid

# 
# typedef EFI_MM_STATUS_CODE_PROTOCOL EFI_SMM_STATUS_CODE_PROTOCOL;
EFI_SMM_STATUS_CODE_PROTOCOL = MmStatusCode.EFI_MM_STATUS_CODE_PROTOCOL

# 
# typedef EFI_MM_REPORT_STATUS_CODE EFI_SMM_REPORT_STATUS_CODE;
EFI_SMM_REPORT_STATUS_CODE = MmStatusCode.EFI_MM_REPORT_STATUS_CODE

# 
# extern EFI_GUID  gEfiSmmStatusCodeProtocolGuid;
# 
# #endif
# 