# /** @file
#   EFI SMM Access2 Protocol as defined in the PI 1.2 specification.
# 
#   This protocol is used to control the visibility of the SMRAM on the platform.
#   It abstracts the location and characteristics of SMRAM.  The expectation is
#   that the north bridge or memory controller would publish this protocol.
# 
#   The principal functionality found in the memory controller includes the following:
#   - Exposing the SMRAM to all non-SMM agents, or the "open" state
#   - Shrouding the SMRAM to all but the SMM agents, or the "closed" state
#   - Preserving the system integrity, or "locking" the SMRAM, such that the settings cannot be
#     perturbed by either boot service or runtime agents
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# SmmAccess2.py
#
# EfiPy2.MdePkg.Protocol.SmmAccess2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _SMM_ACCESS2_H_
# #define _SMM_ACCESS2_H_
from EfiPy2 import *

# 
# #include <Protocol/MmAccess.h>
from EfiPy2.MdePkg.Protocol.MmAccess import gEfiMmAccessProtocolGuid,   \
                                            EFI_MM_ACCESS_PROTOCOL,     \
                                            EFI_MM_OPEN,                \
                                            EFI_MM_CLOSE,               \
                                            EFI_MM_LOCK,                \
                                            EFI_MM_CAPABILITIES

# 
# #define EFI_SMM_ACCESS2_PROTOCOL_GUID  EFI_MM_ACCESS_PROTOCOL_GUID
gEfiSmmAccess2ProtocolGuid = gEfiMmAccessProtocolGuid

# 
# typedef EFI_MM_ACCESS_PROTOCOL EFI_SMM_ACCESS2_PROTOCOL;
EFI_SMM_ACCESS2_PROTOCOL = EFI_MM_ACCESS_PROTOCOL

# 
# typedef EFI_MM_OPEN EFI_SMM_OPEN2;
EFI_SMM_OPEN2 = EFI_MM_OPEN

# 
# typedef EFI_MM_CLOSE EFI_SMM_CLOSE2;
EFI_SMM_CLOSE2 = EFI_MM_CLOSE

# 
# typedef EFI_MM_LOCK EFI_SMM_LOCK2;
EFI_SMM_LOCK2 = EFI_MM_LOCK

# 
# typedef EFI_MM_CAPABILITIES EFI_SMM_CAPABILITIES2;
EFI_SMM_CAPABILITIES2 = EFI_MM_CAPABILITIES

# extern EFI_GUID  gEfiSmmAccess2ProtocolGuid;
# 
# #endif
# 