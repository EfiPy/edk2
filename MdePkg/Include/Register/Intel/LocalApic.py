# /** @file
#   IA32 Local APIC Definitions.
# 
#   Copyright (c) 2010 - 2019, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# LocalApic.py
#
# EfiPy2.MdePkg.Register.Intel.LocalApic
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __INTEL_LOCAL_APIC_H__
# #define __INTEL_LOCAL_APIC_H__
from EfiPy2 import *

# 
# //
# // Definition for Local APIC registers and related values
# //
# #define XAPIC_ID_OFFSET                          0x20
# #define XAPIC_VERSION_OFFSET                     0x30
# #define XAPIC_EOI_OFFSET                         0x0b0
# #define XAPIC_ICR_DFR_OFFSET                     0x0e0
# #define XAPIC_SPURIOUS_VECTOR_OFFSET             0x0f0
# #define XAPIC_ICR_LOW_OFFSET                     0x300
# #define XAPIC_ICR_HIGH_OFFSET                    0x310
# #define XAPIC_LVT_TIMER_OFFSET                   0x320
# #define XAPIC_LVT_LINT0_OFFSET                   0x350
# #define XAPIC_LVT_LINT1_OFFSET                   0x360
# #define XAPIC_TIMER_INIT_COUNT_OFFSET            0x380
# #define XAPIC_TIMER_CURRENT_COUNT_OFFSET         0x390
# #define XAPIC_TIMER_DIVIDE_CONFIGURATION_OFFSET  0x3E0
XAPIC_ID_OFFSET                          = 0x20
XAPIC_VERSION_OFFSET                     = 0x30
XAPIC_EOI_OFFSET                         = 0x0b0
XAPIC_ICR_DFR_OFFSET                     = 0x0e0
XAPIC_SPURIOUS_VECTOR_OFFSET             = 0x0f0
XAPIC_ICR_LOW_OFFSET                     = 0x300
XAPIC_ICR_HIGH_OFFSET                    = 0x310
XAPIC_LVT_TIMER_OFFSET                   = 0x320
XAPIC_LVT_LINT0_OFFSET                   = 0x350
XAPIC_LVT_LINT1_OFFSET                   = 0x360
XAPIC_TIMER_INIT_COUNT_OFFSET            = 0x380
XAPIC_TIMER_CURRENT_COUNT_OFFSET         = 0x390
XAPIC_TIMER_DIVIDE_CONFIGURATION_OFFSET  = 0x3E0

# 
# #define X2APIC_MSR_BASE_ADDRESS  0x800
# #define X2APIC_MSR_ICR_ADDRESS   0x830
X2APIC_MSR_BASE_ADDRESS  = 0x800
X2APIC_MSR_ICR_ADDRESS   = 0x830

# 
# #define LOCAL_APIC_DELIVERY_MODE_FIXED            0
# #define LOCAL_APIC_DELIVERY_MODE_LOWEST_PRIORITY  1
# #define LOCAL_APIC_DELIVERY_MODE_SMI              2
# #define LOCAL_APIC_DELIVERY_MODE_NMI              4
# #define LOCAL_APIC_DELIVERY_MODE_INIT             5
# #define LOCAL_APIC_DELIVERY_MODE_STARTUP          6
# #define LOCAL_APIC_DELIVERY_MODE_EXTINT           7
LOCAL_APIC_DELIVERY_MODE_FIXED            = 0
LOCAL_APIC_DELIVERY_MODE_LOWEST_PRIORITY  = 1
LOCAL_APIC_DELIVERY_MODE_SMI              = 2
LOCAL_APIC_DELIVERY_MODE_NMI              = 4
LOCAL_APIC_DELIVERY_MODE_INIT             = 5
LOCAL_APIC_DELIVERY_MODE_STARTUP          = 6
LOCAL_APIC_DELIVERY_MODE_EXTINT           = 7

# 
# #define LOCAL_APIC_DESTINATION_SHORTHAND_NO_SHORTHAND        0
# #define LOCAL_APIC_DESTINATION_SHORTHAND_SELF                1
# #define LOCAL_APIC_DESTINATION_SHORTHAND_ALL_INCLUDING_SELF  2
# #define LOCAL_APIC_DESTINATION_SHORTHAND_ALL_EXCLUDING_SELF  3
LOCAL_APIC_DESTINATION_SHORTHAND_NO_SHORTHAND        = 0
LOCAL_APIC_DESTINATION_SHORTHAND_SELF                = 1
LOCAL_APIC_DESTINATION_SHORTHAND_ALL_INCLUDING_SELF  = 2
LOCAL_APIC_DESTINATION_SHORTHAND_ALL_EXCLUDING_SELF  = 3

# 
# //
# // Local APIC Version Register.
# //
# typedef union {
#   struct {
#     UINT32    Version                 : 8; ///< The version numbers of the local APIC.
#     UINT32    Reserved0               : 8; ///< Reserved.
#     UINT32    MaxLvtEntry             : 8; ///< Number of LVT entries minus 1.
#     UINT32    EoiBroadcastSuppression : 1; ///< 1 if EOI-broadcast suppression supported.
#     UINT32    Reserved1               : 7; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_VERSION;
class LOCAL_APIC_VERSION_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Version",                 UINT32, 8),
    ("Reserved0",               UINT32, 8),
    ("MaxLvtEntry",             UINT32, 8),
    ("EoiBroadcastSuppression", UINT32, 1),
    ("Reserved1",               UINT32, 7)
  ]

class LOCAL_APIC_VERSION (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_VERSION_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // Low half of Interrupt Command Register (ICR).
# //
# typedef union {
#   struct {
#     UINT32    Vector               : 8;  ///< The vector number of the interrupt being sent.
#     UINT32    DeliveryMode         : 3;  ///< Specifies the type of IPI to be sent.
#     UINT32    DestinationMode      : 1;  ///< 0: physical destination mode, 1: logical destination mode.
#     UINT32    DeliveryStatus       : 1;  ///< Indicates the IPI delivery status. This field is reserved in x2APIC mode.
#     UINT32    Reserved0            : 1;  ///< Reserved.
#     UINT32    Level                : 1;  ///< 0 for the INIT level de-assert delivery mode. Otherwise 1.
#     UINT32    TriggerMode          : 1;  ///< 0: edge, 1: level when using the INIT level de-assert delivery mode.
#     UINT32    Reserved1            : 2;  ///< Reserved.
#     UINT32    DestinationShorthand : 2;  ///< A shorthand notation to specify the destination of the interrupt.
#     UINT32    Reserved2            : 12; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_ICR_LOW;
class LOCAL_APIC_ICR_LOW_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",                  UINT32, 8),
    ("DeliveryMode",            UINT32, 3),
    ("DestinationMode",         UINT32, 1),
    ("DeliveryStatus",          UINT32, 1),
    ("Reserved0",               UINT32, 1),
    ("Level",                   UINT32, 1),
    ("TriggerMode",             UINT32, 1),
    ("Reserved1",               UINT32, 2),
    ("DestinationShorthand",    UINT32, 2),
    ("Reserved2",               UINT32, 12)
  ]

class LOCAL_APIC_ICR_LOW (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_ICR_LOW_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // High half of Interrupt Command Register (ICR)
# //
# typedef union {
#   struct {
#     UINT32    Reserved0   : 24; ///< Reserved.
#     UINT32    Destination : 8;  ///< Specifies the target processor or processors in xAPIC mode.
#   } Bits;
#   UINT32    Uint32;         ///< Destination field expanded to 32-bit in x2APIC mode.
# } LOCAL_APIC_ICR_HIGH;
class LOCAL_APIC_ICR_HIGH_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved0",       UINT32, 24),
    ("Destination",     UINT32, 8)
  ]

class LOCAL_APIC_ICR_HIGH (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_ICR_HIGH_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // Spurious-Interrupt Vector Register (SVR)
# //
# typedef union {
#   struct {
#     UINT32    SpuriousVector          : 8;  ///< Spurious Vector.
#     UINT32    SoftwareEnable          : 1;  ///< APIC Software Enable/Disable.
#     UINT32    FocusProcessorChecking  : 1;  ///< Focus Processor Checking.
#     UINT32    Reserved0               : 2;  ///< Reserved.
#     UINT32    EoiBroadcastSuppression : 1;  ///< EOI-Broadcast Suppression.
#     UINT32    Reserved1               : 19; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_SVR;
class LOCAL_APIC_SVR_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SpuriousVector",          UINT32, 8),
    ("SoftwareEnable",          UINT32, 1),
    ("FocusProcessorChecking",  UINT32, 1),
    ("Reserved0",               UINT32, 2),
    ("EoiBroadcastSuppression", UINT32, 1),
    ("Reserved1",               UINT32, 19)
  ]

class LOCAL_APIC_SVR (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_SVR_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // Divide Configuration Register (DCR)
# //
# typedef union {
#   struct {
#     UINT32    DivideValue1 : 2;  ///< Low 2 bits of the divide value.
#     UINT32    Reserved0    : 1;  ///< Always 0.
#     UINT32    DivideValue2 : 1;  ///< Highest 1 bit of the divide value.
#     UINT32    Reserved1    : 28; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_DCR;
class LOCAL_APIC_DCR_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DivideValue1",    UINT32, 2),
    ("Reserved0",       UINT32, 1),
    ("DivideValue2",    UINT32, 1),
    ("Reserved1",       UINT32, 28)
  ]

class LOCAL_APIC_DCR (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_DCR_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // LVT Timer Register
# //
# typedef union {
#   struct {
#     UINT32    Vector         : 8;  ///< The vector number of the interrupt being sent.
#     UINT32    Reserved0      : 4;  ///< Reserved.
#     UINT32    DeliveryStatus : 1;  ///< 0: Idle, 1: send pending.
#     UINT32    Reserved1      : 3;  ///< Reserved.
#     UINT32    Mask           : 1;  ///< 0: Not masked, 1: Masked.
#     UINT32    TimerMode      : 1;  ///< 0: One-shot, 1: Periodic.
#     UINT32    Reserved2      : 14; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_LVT_TIMER;
class LOCAL_APIC_LVT_TIMER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",          UINT32, 8),
    ("Reserved0",       UINT32, 4),
    ("DeliveryStatus",  UINT32, 1),
    ("Reserved1",       UINT32, 3),
    ("Mask",            UINT32, 1),
    ("TimerMode",       UINT32, 1),
    ("Reserved2",       UINT32, 14)
  ]

class LOCAL_APIC_LVT_TIMER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_LVT_TIMER_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // LVT LINT0/LINT1 Register
# //
# typedef union {
#   struct {
#     UINT32    Vector           : 8;  ///< The vector number of the interrupt being sent.
#     UINT32    DeliveryMode     : 3;  ///< Specifies the type of interrupt to be sent.
#     UINT32    Reserved0        : 1;  ///< Reserved.
#     UINT32    DeliveryStatus   : 1;  ///< 0: Idle, 1: send pending.
#     UINT32    InputPinPolarity : 1;  ///< Interrupt Input Pin Polarity.
#     UINT32    RemoteIrr        : 1;  ///< RO. Set when the local APIC accepts the interrupt and reset when an EOI is received.
#     UINT32    TriggerMode      : 1;  ///< 0:edge, 1:level.
#     UINT32    Mask             : 1;  ///< 0: Not masked, 1: Masked.
#     UINT32    Reserved1        : 15; ///< Reserved.
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_LVT_LINT;
class LOCAL_APIC_LVT_LINT_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",              UINT32, 8),
    ("DeliveryMode",        UINT32, 3),
    ("Reserved0",           UINT32, 1),
    ("DeliveryStatus",      UINT32, 1),
    ("InputPinPolarity",    UINT32, 1),
    ("RemoteIrr",           UINT32, 1),
    ("TriggerMode",         UINT32, 1),
    ("Mask",                UINT32, 1),
    ("Reserved1",           UINT32, 15)
  ]

class LOCAL_APIC_LVT_LINT (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_LVT_LINT_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // MSI Address Register
# //
# typedef union {
#   struct {
#     UINT32    Reserved0       : 2;  ///< Reserved
#     UINT32    DestinationMode : 1;  ///< Specifies the Destination Mode.
#     UINT32    RedirectionHint : 1;  ///< Specifies the Redirection Hint.
#     UINT32    Reserved1       : 8;  ///< Reserved.
#     UINT32    DestinationId   : 8;  ///< Specifies the Destination ID.
#     UINT32    BaseAddress     : 12; ///< Must be 0FEEH
#   } Bits;
#   UINT32    Uint32;
# } LOCAL_APIC_MSI_ADDRESS;
class LOCAL_APIC_MSI_ADDRESS_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved0",       UINT32, 2),
    ("DestinationMode", UINT32, 1),
    ("RedirectionHint", UINT32, 1),
    ("Reserved1",       UINT32, 8),
    ("DestinationId",   UINT32, 8),
    ("BaseAddress",     UINT32, 12)
  ]

class LOCAL_APIC_MSI_ADDRESS (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_MSI_ADDRESS_Bits),
    ("Uint32",  UINT32)
  ]

# 
# //
# // MSI Address Register
# //
# typedef union {
#   struct {
#     UINT32    Vector       : 8;  ///< Interrupt vector in range 010h..0FEH
#     UINT32    DeliveryMode : 3;  ///< Specifies the type of interrupt to be sent.
#     UINT32    Reserved0    : 3;  ///< Reserved.
#     UINT32    Level        : 1;  ///< 0:Deassert, 1:Assert.  Ignored for Edge triggered interrupts.
#     UINT32    TriggerMode  : 1;  ///< 0:Edge,     1:Level.
#     UINT32    Reserved1    : 16; ///< Reserved.
#     UINT32    Reserved2    : 32; ///< Reserved.
#   } Bits;
#   UINT64    Uint64;
# } LOCAL_APIC_MSI_DATA;
class LOCAL_APIC_MSI_DATA_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Vector",          UINT32, 8),
    ("DeliveryMode",    UINT32, 3),
    ("Reserved0",       UINT32, 3),
    ("Level",           UINT32, 1),
    ("TriggerMode",     UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class LOCAL_APIC_MSI_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    LOCAL_APIC_MSI_DATA_Bits),
    ("Uint64",  UINT64)
  ]

# 
# #endif
# 