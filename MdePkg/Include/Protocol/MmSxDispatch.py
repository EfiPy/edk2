# /** @file
#   MM Sx Dispatch Protocol as defined in PI 1.5 Specification
#   Volume 4 Management Mode Core Interface.
# 
#   Provides the parent dispatch service for a given Sx-state source generator.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# MmSxDispatch.py
#
# EfiPy2.MdePkg.Protocol.MmSxDispatch
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _MM_SX_DISPATCH_H_
# #define _MM_SX_DISPATCH_H_
from EfiPy2 import *

# 
# #include <Pi/PiMmCis.h>
from EfiPy2.MdePkg.Pi.PiMmCis       import EFI_MM_HANDLER_ENTRY_POINT

# 
# #define EFI_MM_SX_DISPATCH_PROTOCOL_GUID \
#   { \
#     0x456d2859, 0xa84b, 0x4e47, {0xa2, 0xee, 0x32, 0x76, 0xd8, 0x86, 0x99, 0x7d } \
#   }
gEfiMmSxDispatchProtocolGuid = \
  EFI_GUID (0x456d2859, 0xa84b, 0x4e47, (0xa2, 0xee, 0x32, 0x76, 0xd8, 0x86, 0x99, 0x7d ))

# 
# ///
# /// Sleep states S0-S5
# ///
# typedef enum {
#   SxS0,
#   SxS1,
#   SxS2,
#   SxS3,
#   SxS4,
#   SxS5,
#   EfiMaximumSleepType
# } EFI_SLEEP_TYPE;
SxS0                = 1
SxS1                = 2
SxS2                = 3
SxS3                = 4
SxS4                = 5
SxS5                = 6
EfiMaximumSleepType = 7
EFI_SLEEP_TYPE      = ENUM

# 
# ///
# /// Sleep state phase: entry or exit
# ///
# typedef enum {
#   SxEntry,
#   SxExit,
#   EfiMaximumPhase
# } EFI_SLEEP_PHASE;
SxEntry         = 1
SxExit          = 2
EfiMaximumPhase = 3
EFI_SLEEP_PHASE = ENUM

# 
# ///
# /// The dispatch function's context
# ///
# typedef struct {
#   EFI_SLEEP_TYPE     Type;
#   EFI_SLEEP_PHASE    Phase;
# } EFI_MM_SX_REGISTER_CONTEXT;
class EFI_MM_SX_REGISTER_CONTEXT (Structure):
  _fields_ = [
    ("Type",    EFI_SLEEP_TYPE),
    ("Phase",   EFI_SLEEP_PHASE)
  ]

# 
# typedef struct _EFI_MM_SX_DISPATCH_PROTOCOL EFI_MM_SX_DISPATCH_PROTOCOL;
class EFI_MM_SX_DISPATCH_PROTOCOL (Structure):
  pass

# 
# /**
#   Provides the parent dispatch service for a given Sx source generator.
# 
#   This service registers a function (DispatchFunction) which will be called when the sleep state
#   event specified by RegisterContext is detected. On return, DispatchHandle contains a
#   unique handle which may be used later to unregister the function using UnRegister().
#   The DispatchFunction will be called with Context set to the same value as was passed into
#   this function in RegisterContext and with CommBuffer and CommBufferSize set to
#   NULL and 0 respectively.
# 
#   @param[in] This                Pointer to the EFI_MM_SX_DISPATCH_PROTOCOL instance.
#   @param[in] DispatchFunction    Function to register for handler when the specified sleep state event occurs.
#   @param[in] RegisterContext     Pointer to the dispatch function's context.
#                                  The caller fills this context in before calling
#                                  the register function to indicate to the register
#                                  function which Sx state type and phase the caller
#                                  wishes to be called back on. For this intertace,
#                                  the Sx driver will call the registered handlers for
#                                  all Sx type and phases, so the Sx state handler(s)
#                                  must check the Type and Phase field of the Dispatch
#                                  context and act accordingly.
#   @param[out]  DispatchHandle    Handle of dispatch function, for when interfacing
#                                  with the parent Sx state MM driver.
# 
#   @retval EFI_SUCCESS            The dispatch function has been successfully
#                                  registered and the MMI source has been enabled.
#   @retval EFI_UNSUPPORTED        The Sx driver or hardware does not support that
#                                  Sx Type/Phase.
#   @retval EFI_DEVICE_ERROR       The Sx driver was unable to enable the MMI source.
#   @retval EFI_INVALID_PARAMETER  RegisterContext is invalid. Type & Phase are not
#                                  within valid range.
#   @retval EFI_OUT_OF_RESOURCES   There is not enough memory (system or MM) to manage this
#                                  child.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_MM_SX_REGISTER)(
#   IN  CONST EFI_MM_SX_DISPATCH_PROTOCOL  *This,
#   IN        EFI_MM_HANDLER_ENTRY_POINT   DispatchFunction,
#   IN  CONST EFI_MM_SX_REGISTER_CONTEXT   *RegisterContext,
#   OUT       EFI_HANDLE                   *DispatchHandle
#   );
EFI_MM_SX_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SX_DISPATCH_PROTOCOL),     #   IN CONST *This
  EFI_MM_HANDLER_ENTRY_POINT,               #   IN        DispatchFunction,
  POINTER(EFI_MM_SX_REGISTER_CONTEXT),      #   IN  CONST *RegisterContext,
  POINTER(EFI_HANDLE)                       #   OUT       *DispatchHandle
  )

# 
# /**
#   Unregisters an Sx-state service.
# 
#   This service removes the handler associated with DispatchHandle so that it will no longer be
#   called in response to sleep event.
# 
#   @param[in] This                Pointer to the EFI_MM_SX_DISPATCH_PROTOCOL instance.
#   @param[in] DispatchHandle      Handle of the service to remove.
# 
#   @retval EFI_SUCCESS            The service has been successfully removed.
#   @retval EFI_INVALID_PARAMETER  The DispatchHandle was not valid.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_MM_SX_UNREGISTER)(
#   IN CONST EFI_MM_SX_DISPATCH_PROTOCOL  *This,
#   IN       EFI_HANDLE                   DispatchHandle
#   );
EFI_MM_SX_UNREGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_SX_DISPATCH_PROTOCOL), #   IN CONST *This
  EFI_HANDLE                            #   IN       DispatchHandle
  )

# 
# ///
# /// Interface structure for the MM Sx Dispatch Protocol
# ///
# /// The EFI_MM_SX_DISPATCH_PROTOCOL provides the ability to install child handlers to
# /// respond to sleep state related events.
# ///
# struct _EFI_MM_SX_DISPATCH_PROTOCOL {
#   EFI_MM_SX_REGISTER      Register;
#   EFI_MM_SX_UNREGISTER    UnRegister;
# };
EFI_MM_SX_DISPATCH_PROTOCOL._fields_ = [
    ("Register",    EFI_MM_SX_REGISTER),
    ("UnRegister",  EFI_MM_SX_UNREGISTER)
  ]

# 
# extern EFI_GUID  gEfiMmSxDispatchProtocolGuid;
# 
# #endif
# 