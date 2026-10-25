# /** @file
#   Simple Text Input protocol from the UEFI 2.0 specification.
# 
#   Abstraction of a very simple input device like a keyboard or serial
#   terminal.
# 
#   Copyright (c) 2006 - 2011, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
#
# SimpleTextIn.py
#
# EfiPy2.MdePkg.Protocol.SimpleTextIn
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
from EfiPy2  import *

# #ifndef __SIMPLE_TEXT_IN_PROTOCOL_H__
# #define __SIMPLE_TEXT_IN_PROTOCOL_H__
# 
# #define EFI_SIMPLE_TEXT_INPUT_PROTOCOL_GUID \
#   { \
#     0x387477c1, 0x69c7, 0x11d2, {0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b } \
#   }
# 
gEfiSimpleTextInProtocolGuid = EFI_GUID( 0x387477c1, 0x69c7, 0x11d2, (0x8e, 0x39, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b))

# typedef struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL EFI_SIMPLE_TEXT_INPUT_PROTOCOL;
# 
class EFI_SIMPLE_TEXT_INPUT_PROTOCOL (Structure):
  pass

# ///
# /// Protocol GUID name defined in EFI1.1.
# ///
# #define SIMPLE_INPUT_PROTOCOL  EFI_SIMPLE_TEXT_INPUT_PROTOCOL_GUID
# 
# ///
# /// Protocol name in EFI1.1 for backward-compatible.
# ///
# typedef struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL SIMPLE_INPUT_INTERFACE;
# 
# ///
# /// The keystroke information for the key that was pressed.
# ///
# typedef struct {
#   UINT16    ScanCode;
#   CHAR16    UnicodeChar;
# } EFI_INPUT_KEY;
# 
class EFI_INPUT_KEY (Structure):
  _fields_ = [
    ("ScanCode",    UINT16),
    ("UnicodeChar", CHAR16)
    ]

# //
# // Required unicode control chars
# //
# #define CHAR_BACKSPACE        0x0008
# #define CHAR_TAB              0x0009
# #define CHAR_LINEFEED         0x000A
# #define CHAR_CARRIAGE_RETURN  0x000D
# 
CHAR_NULL             = 0x0000
CHAR_BACKSPACE        = 0x0008
CHAR_TAB              = 0x0009
CHAR_LINEFEED         = 0x000A
CHAR_CARRIAGE_RETURN  = 0x000D

# //
# // EFI Scan codes
# //
# #define SCAN_NULL       0x0000
# #define SCAN_UP         0x0001
# #define SCAN_DOWN       0x0002
# #define SCAN_RIGHT      0x0003
# #define SCAN_LEFT       0x0004
# #define SCAN_HOME       0x0005
# #define SCAN_END        0x0006
# #define SCAN_INSERT     0x0007
# #define SCAN_DELETE     0x0008
# #define SCAN_PAGE_UP    0x0009
# #define SCAN_PAGE_DOWN  0x000A
# #define SCAN_F1         0x000B
# #define SCAN_F2         0x000C
# #define SCAN_F3         0x000D
# #define SCAN_F4         0x000E
# #define SCAN_F5         0x000F
# #define SCAN_F6         0x0010
# #define SCAN_F7         0x0011
# #define SCAN_F8         0x0012
# #define SCAN_F9         0x0013
# #define SCAN_F10        0x0014
# #define SCAN_ESC        0x0017
# 
SCAN_NULL       = 0x0000
SCAN_UP         = 0x0001
SCAN_DOWN       = 0x0002
SCAN_RIGHT      = 0x0003
SCAN_LEFT       = 0x0004
SCAN_HOME       = 0x0005
SCAN_END        = 0x0006
SCAN_INSERT     = 0x0007
SCAN_DELETE     = 0x0008
SCAN_PAGE_UP    = 0x0009
SCAN_PAGE_DOWN  = 0x000A
SCAN_F1         = 0x000B
SCAN_F2         = 0x000C
SCAN_F3         = 0x000D
SCAN_F4         = 0x000E
SCAN_F5         = 0x000F
SCAN_F6         = 0x0010
SCAN_F7         = 0x0011
SCAN_F8         = 0x0012
SCAN_F9         = 0x0013
SCAN_F10        = 0x0014
SCAN_ESC        = 0x0017

# /**
#   Reset the input device and optionally run diagnostics
# 
#   @param  This                 Protocol instance pointer.
#   @param  ExtendedVerification Driver may perform diagnostics on reset.
# 
#   @retval EFI_SUCCESS          The device was reset.
#   @retval EFI_DEVICE_ERROR     The device is not functioning properly and could not be reset.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_INPUT_RESET)(
#   IN EFI_SIMPLE_TEXT_INPUT_PROTOCOL       *This,
#   IN BOOLEAN                              ExtendedVerification
#   );
# 
EFI_INPUT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL),  # IN *This
  BOOLEAN                                   # IN ExtendedVerification
  )

# /**
#   Reads the next keystroke from the input device. The WaitForKey Event can
#   be used to test for existence of a keystroke via WaitForEvent () call.
# 
#   @param  This  Protocol instance pointer.
#   @param  Key   A pointer to a buffer that is filled in with the keystroke
#                 information for the key that was pressed.
# 
#   @retval EFI_SUCCESS      The keystroke information was returned.
#   @retval EFI_NOT_READY    There was no keystroke data available.
#   @retval EFI_DEVICE_ERROR The keystroke information was not returned due to
#                            hardware errors.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_INPUT_READ_KEY)(
#   IN EFI_SIMPLE_TEXT_INPUT_PROTOCOL       *This,
#   OUT EFI_INPUT_KEY                       *Key
#   );
# 
EFI_INPUT_READ_KEY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_SIMPLE_TEXT_INPUT_PROTOCOL),  # IN  *This
  POINTER(EFI_INPUT_KEY)                    # OUT *Key
  )

# ///
# /// The EFI_SIMPLE_TEXT_INPUT_PROTOCOL is used on the ConsoleIn device.
# /// It is the minimum required protocol for ConsoleIn.
# ///
# struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL {
#   EFI_INPUT_RESET       Reset;
#   EFI_INPUT_READ_KEY    ReadKeyStroke;
#   ///
#   /// Event to use with WaitForEvent() to wait for a key to be available
#   ///
#   EFI_EVENT             WaitForKey;
# };
EFI_SIMPLE_TEXT_INPUT_PROTOCOL._fields_ = [
  ("Reset",         EFI_INPUT_RESET),
  ("ReadKeyStroke", EFI_INPUT_READ_KEY),
  ("WaitForKey",    EFI_EVENT)
  ]

# 
# extern EFI_GUID  gEfiSimpleTextInProtocolGuid;
# 
# #endif
# 