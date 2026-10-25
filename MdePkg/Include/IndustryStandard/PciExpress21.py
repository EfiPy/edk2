# /** @file
#   Support for the latest PCI standard.
# 
#   Copyright (c) 2006 - 2021, Intel Corporation. All rights reserved.<BR>
#   (C) Copyright 2016 Hewlett Packard Enterprise Development LP<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# PciExpress21.py
#
# EfiPy2.MdePkg.IndustryStandard.PciExpress21
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _PCIEXPRESS21_H_
# #define _PCIEXPRESS21_H_
# 
# #include <IndustryStandard/Pci30.h>
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard.Pci30 import EFI_PCI_CAPABILITY_HDR

# 
# /**
#   Macro that converts PCI Bus, PCI Device, PCI Function and PCI Register to an
#   ECAM (Enhanced Configuration Access Mechanism) address. The unused upper bits
#   of Bus, Device, Function and Register are stripped prior to the generation of
#   the address.
# 
#   @param  Bus       PCI Bus number. Range 0..255.
#   @param  Device    PCI Device number. Range 0..31.
#   @param  Function  PCI Function number. Range 0..7.
#   @param  Register  PCI Register number. Range 0..4095.
# 
#   @return The encode ECAM address.
# 
# **/
# #define PCI_ECAM_ADDRESS(Bus, Device, Function, Offset) \
#   (((Offset) & 0xfff) | (((Function) & 0x07) << 12) | (((Device) & 0x1f) << 15) | (((Bus) & 0xff) << 20))
def PCI_ECAM_ADDRESS(Bus, Device, Function, Offset):

  return (((Offset) & 0xfff) | (((Function) & 0x07) << 12) | (((Device) & 0x1f) << 15) | (((Bus) & 0xff) << 20))

# 
# #pragma pack(1)
# ///
# /// PCI Express Capability Structure
# ///
# typedef union {
#   struct {
#     UINT16    Version                : 4;
#     UINT16    DevicePortType         : 4;
#     UINT16    SlotImplemented        : 1;
#     UINT16    InterruptMessageNumber : 5;
#     UINT16    Undefined              : 1;
#     UINT16    Reserved               : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_CAPABILITY;
class PCI_REG_PCIE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",                UINT16, 4),
    ("DevicePortType",         UINT16, 4),
    ("SlotImplemented",        UINT16, 1),
    ("InterruptMessageNumber", UINT16, 5),
    ("Undefined",              UINT16, 1),
    ("Reserved",               UINT16, 1)
  ]

class PCI_REG_PCIE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_CAPABILITY_Bits),
    ("Uint16",          UINT16)
    ]

# 
# #define PCIE_DEVICE_PORT_TYPE_PCIE_ENDPOINT                     0
# #define PCIE_DEVICE_PORT_TYPE_LEGACY_PCIE_ENDPOINT              1
# #define PCIE_DEVICE_PORT_TYPE_ROOT_PORT                         4
# #define PCIE_DEVICE_PORT_TYPE_UPSTREAM_PORT                     5
# #define PCIE_DEVICE_PORT_TYPE_DOWNSTREAM_PORT                   6
# #define PCIE_DEVICE_PORT_TYPE_PCIE_TO_PCI_BRIDGE                7
# #define PCIE_DEVICE_PORT_TYPE_PCI_TO_PCIE_BRIDGE                8
# #define PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_INTEGRATED_ENDPOINT  9
# #define PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_EVENT_COLLECTOR      10
# 
PCIE_DEVICE_PORT_TYPE_PCIE_ENDPOINT                     = 0
PCIE_DEVICE_PORT_TYPE_LEGACY_PCIE_ENDPOINT              = 1
PCIE_DEVICE_PORT_TYPE_ROOT_PORT                         = 4
PCIE_DEVICE_PORT_TYPE_UPSTREAM_PORT                     = 5
PCIE_DEVICE_PORT_TYPE_DOWNSTREAM_PORT                   = 6
PCIE_DEVICE_PORT_TYPE_PCIE_TO_PCI_BRIDGE                = 7
PCIE_DEVICE_PORT_TYPE_PCI_TO_PCIE_BRIDGE                = 8
PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_INTEGRATED_ENDPOINT  = 9
PCIE_DEVICE_PORT_TYPE_ROOT_COMPLEX_EVENT_COLLECTOR      = 10

# typedef union {
#   struct {
#     UINT32    MaxPayloadSize               : 3;
#     UINT32    PhantomFunctions             : 2;
#     UINT32    ExtendedTagField             : 1;
#     UINT32    EndpointL0sAcceptableLatency : 3;
#     UINT32    EndpointL1AcceptableLatency  : 3;
#     UINT32    Undefined                    : 3;
#     UINT32    RoleBasedErrorReporting      : 1;
#     UINT32    Reserved                     : 2;
#     UINT32    CapturedSlotPowerLimitValue  : 8;
#     UINT32    CapturedSlotPowerLimitScale  : 2;
#     UINT32    FunctionLevelReset           : 1;
#     UINT32    Reserved2                    : 3;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_DEVICE_CAPABILITY;
class PCI_REG_PCIE_DEVICE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxPayloadSize",                  UINT32, 3),
    ("PhantomFunctions",                UINT32, 2),
    ("ExtendedTagField",                UINT32, 1),
    ("EndpointL0sAcceptableLatency",    UINT32, 3),
    ("EndpointL1AcceptableLatency",     UINT32, 3),
    ("Undefined",                       UINT32, 3),
    ("RoleBasedErrorReporting",         UINT32, 1),
    ("Reserved",                        UINT32, 2),
    ("CapturedSlotPowerLimitValue",     UINT32, 8),
    ("CapturedSlotPowerLimitScale",     UINT32, 2),
    ("FunctionLevelReset",              UINT32, 1),
    ("Reserved2",                       UINT32, 3)
  ]

class PCI_REG_PCIE_DEVICE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT16    CorrectableError                             : 1;
#     UINT16    NonFatalError                                : 1;
#     UINT16    FatalError                                   : 1;
#     UINT16    UnsupportedRequest                           : 1;
#     UINT16    RelaxedOrdering                              : 1;
#     UINT16    MaxPayloadSize                               : 3;
#     UINT16    ExtendedTagField                             : 1;
#     UINT16    PhantomFunctions                             : 1;
#     UINT16    AuxPower                                     : 1;
#     UINT16    NoSnoop                                      : 1;
#     UINT16    MaxReadRequestSize                           : 3;
#     UINT16    BridgeConfigurationRetryOrFunctionLevelReset : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_DEVICE_CONTROL;
class PCI_REG_PCIE_DEVICE_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CorrectableError",                                UINT16, 1),
    ("NonFatalError",                                   UINT16, 1),
    ("FatalError",                                      UINT16, 1),
    ("UnsupportedRequest",                              UINT16, 1),
    ("RelaxedOrdering",                                 UINT16, 1),
    ("MaxPayloadSize",                                  UINT16, 3),
    ("ExtendedTagField",                                UINT16, 1),
    ("PhantomFunctions",                                UINT16, 1),
    ("AuxPower",                                        UINT16, 1),
    ("NoSnoop",                                         UINT16, 1),
    ("MaxReadRequestSize",                              UINT16, 3),
    ("BridgeConfigurationRetryOrFunctionLevelReset",    UINT16, 1)
  ]

class PCI_REG_PCIE_DEVICE_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

# 
# #define PCIE_MAX_PAYLOAD_SIZE_128B   0
# #define PCIE_MAX_PAYLOAD_SIZE_256B   1
# #define PCIE_MAX_PAYLOAD_SIZE_512B   2
# #define PCIE_MAX_PAYLOAD_SIZE_1024B  3
# #define PCIE_MAX_PAYLOAD_SIZE_2048B  4
# #define PCIE_MAX_PAYLOAD_SIZE_4096B  5
# #define PCIE_MAX_PAYLOAD_SIZE_RVSD1  6
# #define PCIE_MAX_PAYLOAD_SIZE_RVSD2  7
# 
PCIE_MAX_PAYLOAD_SIZE_128B   = 0
PCIE_MAX_PAYLOAD_SIZE_256B   = 1
PCIE_MAX_PAYLOAD_SIZE_512B   = 2
PCIE_MAX_PAYLOAD_SIZE_1024B  = 3
PCIE_MAX_PAYLOAD_SIZE_2048B  = 4
PCIE_MAX_PAYLOAD_SIZE_4096B  = 5
PCIE_MAX_PAYLOAD_SIZE_RVSD1  = 6
PCIE_MAX_PAYLOAD_SIZE_RVSD2  = 7

# #define PCIE_MAX_READ_REQ_SIZE_128B   0
# #define PCIE_MAX_READ_REQ_SIZE_256B   1
# #define PCIE_MAX_READ_REQ_SIZE_512B   2
# #define PCIE_MAX_READ_REQ_SIZE_1024B  3
# #define PCIE_MAX_READ_REQ_SIZE_2048B  4
# #define PCIE_MAX_READ_REQ_SIZE_4096B  5
# #define PCIE_MAX_READ_REQ_SIZE_RVSD1  6
# #define PCIE_MAX_READ_REQ_SIZE_RVSD2  7
# 
PCIE_MAX_READ_REQ_SIZE_128B   = 0
PCIE_MAX_READ_REQ_SIZE_256B   = 1
PCIE_MAX_READ_REQ_SIZE_512B   = 2
PCIE_MAX_READ_REQ_SIZE_1024B  = 3
PCIE_MAX_READ_REQ_SIZE_2048B  = 4
PCIE_MAX_READ_REQ_SIZE_4096B  = 5
PCIE_MAX_READ_REQ_SIZE_RVSD1  = 6
PCIE_MAX_READ_REQ_SIZE_RVSD2  = 7

# typedef union {
#   struct {
#     UINT16    CorrectableError    : 1;
#     UINT16    NonFatalError       : 1;
#     UINT16    FatalError          : 1;
#     UINT16    UnsupportedRequest  : 1;
#     UINT16    AuxPower            : 1;
#     UINT16    TransactionsPending : 1;
#     UINT16    Reserved            : 10;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_DEVICE_STATUS;
class PCI_REG_PCIE_DEVICE_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CorrectableError",        UINT16, 1),
    ("NonFatalError",           UINT16, 1),
    ("FatalError",              UINT16, 1),
    ("UnsupportedRequest",      UINT16, 1),
    ("AuxPower",                UINT16, 1),
    ("TransactionsPending",     UINT16, 1),
    ("Reserved",                UINT16, 10)
  ]

class PCI_REG_PCIE_DEVICE_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT32    MaxLinkSpeed              : 4;
#     UINT32    MaxLinkWidth              : 6;
#     UINT32    Aspm                      : 2;
#     UINT32    L0sExitLatency            : 3;
#     UINT32    L1ExitLatency             : 3;
#     UINT32    ClockPowerManagement      : 1;
#     UINT32    SurpriseDownError         : 1;
#     UINT32    DataLinkLayerLinkActive   : 1;
#     UINT32    LinkBandwidthNotification : 1;
#     UINT32    AspmOptionalityCompliance : 1;
#     UINT32    Reserved                  : 1;
#     UINT32    PortNumber                : 8;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_LINK_CAPABILITY;
class PCI_REG_PCIE_LINK_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxLinkSpeed",                UINT32, 4),
    ("MaxLinkWidth",                UINT32, 6),
    ("Aspm",                        UINT32, 2),
    ("L0sExitLatency",              UINT32, 3),
    ("L1ExitLatency",               UINT32, 3),
    ("ClockPowerManagement",        UINT32, 1),
    ("SurpriseDownError",           UINT32, 1),
    ("DataLinkLayerLinkActive",     UINT32, 1),
    ("LinkBandwidthNotification",   UINT32, 1),
    ("AspmOptionalityCompliance",   UINT32, 1),
    ("Reserved",                    UINT32, 1),
    ("PortNumber",                  UINT32, 8)
  ]

class PCI_REG_PCIE_LINK_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

# 
# #define PCIE_LINK_ASPM_L0S  BIT0
# #define PCIE_LINK_ASPM_L1   BIT1
# 
PCIE_LINK_ASPM_L0S  = BIT0
PCIE_LINK_ASPM_L1   = BIT1

# typedef union {
#   struct {
#     UINT16    AspmControl                      : 2;
#     UINT16    Reserved                         : 1;
#     UINT16    ReadCompletionBoundary           : 1;
#     UINT16    LinkDisable                      : 1;
#     UINT16    RetrainLink                      : 1;
#     UINT16    CommonClockConfiguration         : 1;
#     UINT16    ExtendedSynch                    : 1;
#     UINT16    ClockPowerManagement             : 1;
#     UINT16    HardwareAutonomousWidthDisable   : 1;
#     UINT16    LinkBandwidthManagementInterrupt : 1;
#     UINT16    LinkAutonomousBandwidthInterrupt : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_LINK_CONTROL;
class PCI_REG_PCIE_LINK_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AspmControl",                         UINT16, 2),
    ("Reserved",                            UINT16, 1),
    ("ReadCompletionBoundary",              UINT16, 1),
    ("LinkDisable",                         UINT16, 1),
    ("RetrainLink",                         UINT16, 1),
    ("CommonClockConfiguration",            UINT16, 1),
    ("ExtendedSynch",                       UINT16, 1),
    ("ClockPowerManagement",                UINT16, 1),
    ("HardwareAutonomousWidthDisable",      UINT16, 1),
    ("LinkBandwidthManagementInterrupt",    UINT16, 1),
    ("LinkAutonomousBandwidthInterrupt",    UINT16, 1)
  ]

class PCI_REG_PCIE_LINK_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT16    CurrentLinkSpeed        : 4;
#     UINT16    NegotiatedLinkWidth     : 6;
#     UINT16    Undefined               : 1;
#     UINT16    LinkTraining            : 1;
#     UINT16    SlotClockConfiguration  : 1;
#     UINT16    DataLinkLayerLinkActive : 1;
#     UINT16    LinkBandwidthManagement : 1;
#     UINT16    LinkAutonomousBandwidth : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_LINK_STATUS;
class PCI_REG_PCIE_LINK_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentLinkSpeed",        UINT16, 4),
    ("NegotiatedLinkWidth",     UINT16, 6),
    ("Undefined",               UINT16, 1),
    ("LinkTraining",            UINT16, 1),
    ("SlotClockConfiguration ", UINT16, 1),
    ("DataLinkLayerLinkActive", UINT16, 1),
    ("LinkBandwidthManagement", UINT16, 1),
    ("LinkAutonomousBandwidth", UINT16, 1)
  ]

class PCI_REG_PCIE_LINK_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT32    AttentionButton            : 1;
#     UINT32    PowerController            : 1;
#     UINT32    MrlSensor                  : 1;
#     UINT32    AttentionIndicator         : 1;
#     UINT32    PowerIndicator             : 1;
#     UINT32    HotPlugSurprise            : 1;
#     UINT32    HotPlugCapable             : 1;
#     UINT32    SlotPowerLimitValue        : 8;
#     UINT32    SlotPowerLimitScale        : 2;
#     UINT32    ElectromechanicalInterlock : 1;
#     UINT32    NoCommandCompleted         : 1;
#     UINT32    PhysicalSlotNumber         : 13;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_SLOT_CAPABILITY;
class PCI_REG_PCIE_SLOT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButton",             UINT32, 1),
    ("PowerController",             UINT32, 1),
    ("MrlSensor",                   UINT32, 1),
    ("AttentionIndicator",          UINT32, 1),
    ("PowerIndicator",              UINT32, 1),
    ("HotPlugSurprise",             UINT32, 1),
    ("HotPlugCapable",              UINT32, 1),
    ("SlotPowerLimitValue",         UINT32, 8),
    ("SlotPowerLimitScale",         UINT32, 2),
    ("ElectromechanicalInterlock",  UINT32, 1),
    ("NoCommandCompleted",          UINT32, 1),
    ("PhysicalSlotNumber",          UINT32, 13)
  ]

class PCI_REG_PCIE_SLOT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT16    AttentionButtonPressed     : 1;
#     UINT16    PowerFaultDetected         : 1;
#     UINT16    MrlSensorChanged           : 1;
#     UINT16    PresenceDetectChanged      : 1;
#     UINT16    CommandCompletedInterrupt  : 1;
#     UINT16    HotPlugInterrupt           : 1;
#     UINT16    AttentionIndicator         : 2;
#     UINT16    PowerIndicator             : 2;
#     UINT16    PowerController            : 1;
#     UINT16    ElectromechanicalInterlock : 1;
#     UINT16    DataLinkLayerStateChanged  : 1;
#     UINT16    Reserved                   : 3;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_SLOT_CONTROL;
class PCI_REG_PCIE_SLOT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButtonPressed",      UINT16, 1),
    ("PowerFaultDetected",          UINT16, 1),
    ("MrlSensorChanged",            UINT16, 1),
    ("PresenceDetectChanged",       UINT16, 1),
    ("CommandCompletedInterrupt",   UINT16, 1),
    ("HotPlugInterrupt",            UINT16, 1),
    ("AttentionIndicator",          UINT16, 2),
    ("PowerIndicator",              UINT16, 2),
    ("PowerController",             UINT16, 1),
    ("ElectromechanicalInterlock",  UINT16, 1),
    ("DataLinkLayerStateChanged",   UINT16, 1),
    ("Reserved",                    UINT16, 3)
  ]

class PCI_REG_PCIE_SLOT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT16    AttentionButtonPressed     : 1;
#     UINT16    PowerFaultDetected         : 1;
#     UINT16    MrlSensorChanged           : 1;
#     UINT16    PresenceDetectChanged      : 1;
#     UINT16    CommandCompleted           : 1;
#     UINT16    MrlSensor                  : 1;
#     UINT16    PresenceDetect             : 1;
#     UINT16    ElectromechanicalInterlock : 1;
#     UINT16    DataLinkLayerStateChanged  : 1;
#     UINT16    Reserved                   : 7;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_SLOT_STATUS;
class PCI_REG_PCIE_SLOT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AttentionButtonPressed",      UINT16, 1),
    ("PowerFaultDetected",          UINT16, 1),
    ("MrlSensorChanged",            UINT16, 1),
    ("PresenceDetectChanged",       UINT16, 1),
    ("CommandCompleted",            UINT16, 1),
    ("MrlSensor",                   UINT16, 1),
    ("PresenceDetect",              UINT16, 1),
    ("ElectromechanicalInterlock",  UINT16, 1),
    ("DataLinkLayerStateChanged",   UINT16, 1),
    ("Reserved",                    UINT16, 7)
  ]

class PCI_REG_PCIE_SLOT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_SLOT_STATUS_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT16    SystemErrorOnCorrectableError : 1;
#     UINT16    SystemErrorOnNonFatalError    : 1;
#     UINT16    SystemErrorOnFatalError       : 1;
#     UINT16    PmeInterrupt                  : 1;
#     UINT16    CrsSoftwareVisibility         : 1;
#     UINT16    Reserved                      : 11;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_ROOT_CONTROL;
class PCI_REG_PCIE_ROOT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemErrorOnCorrectableError",   UINT16, 1),
    ("SystemErrorOnNonFatalError",      UINT16, 1),
    ("SystemErrorOnFatalError",         UINT16, 1),
    ("PmeInterrupt",                    UINT16, 1),
    ("CrsSoftwareVisibility",           UINT16, 1),
    ("Reserved",                        UINT16, 11)
  ]

class PCI_REG_PCIE_ROOT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_CONTROL_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT16    CrsSoftwareVisibility : 1;
#     UINT16    Reserved              : 15;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_ROOT_CAPABILITY;
class PCI_REG_PCIE_ROOT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CrsSoftwareVisibility",           UINT16, 1),
    ("Reserved",                        UINT16, 15)
  ]

class PCI_REG_PCIE_ROOT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_CAPABILITY_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT32    PmeRequesterId : 16;
#     UINT32    PmeStatus      : 1;
#     UINT32    PmePending     : 1;
#     UINT32    Reserved       : 14;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_ROOT_STATUS;
class PCI_REG_PCIE_ROOT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PmeRequesterId",  UINT32, 16),
    ("PmeStatus",       UINT32, 1),
    ("PmePending",      UINT32, 1),
    ("Reserved",        UINT32, 14)
  ]

class PCI_REG_PCIE_ROOT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_ROOT_STATUS_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    CompletionTimeoutRanges                       : 4;
#     UINT32    CompletionTimeoutDisable                      : 1;
#     UINT32    AriForwarding                                 : 1;
#     UINT32    AtomicOpRouting                               : 1;
#     UINT32    AtomicOp32Completer                           : 1;
#     UINT32    AtomicOp64Completer                           : 1;
#     UINT32    Cas128Completer                               : 1;
#     UINT32    NoRoEnabledPrPrPassing                        : 1;
#     UINT32    LtrMechanism                                  : 1;
#     UINT32    TphCompleter                                  : 2;
#     UINT32    LnSystemCLS                                   : 2;
#     UINT32    TenBitTagCompleterSupported                   : 1;
#     UINT32    TenBitTagRequesterSupported                   : 1;
#     UINT32    Obff                                          : 2;
#     UINT32    ExtendedFmtField                              : 1;
#     UINT32    EndEndTlpPrefix                               : 1;
#     UINT32    MaxEndEndTlpPrefixes                          : 2;
#     UINT32    EmergencyPowerReductionSupported              : 2;
#     UINT32    EmergencyPowerReductionInitializationRequired : 1;
#     UINT32    Reserved3                                     : 4;
#     UINT32    FrsSupported                                  : 1;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_DEVICE_CAPABILITY2;
class PCI_REG_PCIE_DEVICE_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionTimeoutRanges",                         UINT32, 4),
    ("CompletionTimeoutDisable",                        UINT32, 1),
    ("AriForwarding",                                   UINT32, 1),
    ("AtomicOpRouting",                                 UINT32, 1),
    ("AtomicOp32Completer",                             UINT32, 1),
    ("AtomicOp64Completer",                             UINT32, 1),
    ("Cas128Completer",                                 UINT32, 1),
    ("NoRoEnabledPrPrPassing",                          UINT32, 1),
    ("LtrMechanism",                                    UINT32, 1),
    ("TphCompleter",                                    UINT32, 2),
    ("LnSystemCLS",                                     UINT32, 2),
    ("TenBitTagCompleterSupported",                     UINT32, 1),
    ("TenBitTagRequesterSupported",                     UINT32, 1),
    ("Obff",                                            UINT32, 2),
    ("ExtendedFmtField",                                UINT32, 1),
    ("EndEndTlpPrefix",                                 UINT32, 1),
    ("MaxEndEndTlpPrefixes",                            UINT32, 2),
    ("EmergencyPowerReductionSupported",                UINT32, 2),
    ("EmergencyPowerReductionInitializationRequired",   UINT32, 1),
    ("Reserved3",                                       UINT32, 4),
    ("FrsSupported",                                    UINT32, 1)
  ]

class PCI_REG_PCIE_DEVICE_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CAPABILITY2_Bits),
    ("Uint32",          UINT32)
    ]

# 
# #define PCIE_COMPLETION_TIMEOUT_NOT_SUPPORTED            0
# #define PCIE_COMPLETION_TIMEOUT_RANGE_A_SUPPORTED        1
# #define PCIE_COMPLETION_TIMEOUT_RANGE_B_SUPPORTED        2
# #define PCIE_COMPLETION_TIMEOUT_RANGE_A_B_SUPPORTED      3
# #define PCIE_COMPLETION_TIMEOUT_RANGE_B_C_SUPPORTED      6
# #define PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_SUPPORTED    7
# #define PCIE_COMPLETION_TIMEOUT_RANGE_B_C_D_SUPPORTED    14
# #define PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_D_SUPPORTED  15
# 
PCIE_COMPLETION_TIMEOUT_NOT_SUPPORTED            = 0
PCIE_COMPLETION_TIMEOUT_RANGE_A_SUPPORTED        = 1
PCIE_COMPLETION_TIMEOUT_RANGE_B_SUPPORTED        = 2
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_SUPPORTED      = 3
PCIE_COMPLETION_TIMEOUT_RANGE_B_C_SUPPORTED      = 6
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_SUPPORTED    = 7
PCIE_COMPLETION_TIMEOUT_RANGE_B_C_D_SUPPORTED    = 14
PCIE_COMPLETION_TIMEOUT_RANGE_A_B_C_D_SUPPORTED  = 15

# #define PCIE_DEVICE_CAPABILITY_OBFF_MESSAGE  BIT0
# #define PCIE_DEVICE_CAPABILITY_OBFF_WAKE     BIT1
# 
PCIE_DEVICE_CAPABILITY_OBFF_MESSAGE  = BIT0
PCIE_DEVICE_CAPABILITY_OBFF_WAKE     = BIT1

# typedef union {
#   struct {
#     UINT16    CompletionTimeoutValue         : 4;
#     UINT16    CompletionTimeoutDisable       : 1;
#     UINT16    AriForwarding                  : 1;
#     UINT16    AtomicOpRequester              : 1;
#     UINT16    AtomicOpEgressBlocking         : 1;
#     UINT16    IdoRequest                     : 1;
#     UINT16    IdoCompletion                  : 1;
#     UINT16    LtrMechanism                   : 1;
#     UINT16    EmergencyPowerReductionRequest : 1;
#     UINT16    TenBitTagRequesterEnable       : 1;
#     UINT16    Obff                           : 2;
#     UINT16    EndEndTlpPrefixBlocking        : 1;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_DEVICE_CONTROL2;
class PCI_REG_PCIE_DEVICE_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionTimeoutValue",          UINT16, 4),
    ("CompletionTimeoutDisable",        UINT16, 1),
    ("AriForwarding",                   UINT16, 1),
    ("AtomicOpRequester",               UINT16, 1),
    ("AtomicOpEgressBlocking",          UINT16, 1),
    ("IdoRequest",                      UINT16, 1),
    ("IdoCompletion",                   UINT16, 1),
    ("LtrMechanism",                    UINT16, 1),
    ("EmergencyPowerReductionRequest",  UINT16, 1),
    ("TenBitTagRequesterEnable",        UINT16, 1),
    ("Obff",                            UINT16, 2),
    ("EndEndTlpPrefixBlocking",         UINT16, 1)
  ]

class PCI_REG_PCIE_DEVICE_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_DEVICE_CONTROL2_Bits),
    ("Uint16",          UINT16)
    ]

# 
# #define PCIE_COMPLETION_TIMEOUT_50US_50MS    0
# #define PCIE_COMPLETION_TIMEOUT_50US_100US   1
# #define PCIE_COMPLETION_TIMEOUT_1MS_10MS     2
# #define PCIE_COMPLETION_TIMEOUT_16MS_55MS    5
# #define PCIE_COMPLETION_TIMEOUT_65MS_210MS   6
# #define PCIE_COMPLETION_TIMEOUT_260MS_900MS  9
# #define PCIE_COMPLETION_TIMEOUT_1S_3_5S      10
# #define PCIE_COMPLETION_TIMEOUT_4S_13S       13
# #define PCIE_COMPLETION_TIMEOUT_17S_64S      14
# 
PCIE_COMPLETION_TIMEOUT_50US_50MS    = 0
PCIE_COMPLETION_TIMEOUT_50US_100US   = 1
PCIE_COMPLETION_TIMEOUT_1MS_10MS     = 2
PCIE_COMPLETION_TIMEOUT_16MS_55MS    = 5
PCIE_COMPLETION_TIMEOUT_65MS_210MS   = 6
PCIE_COMPLETION_TIMEOUT_260MS_900MS  = 9
PCIE_COMPLETION_TIMEOUT_1S_3_5S      = 10
PCIE_COMPLETION_TIMEOUT_4S_13S       = 13
PCIE_COMPLETION_TIMEOUT_17S_64S      = 14

# #define PCIE_DEVICE_CONTROL_OBFF_DISABLED   0
# #define PCIE_DEVICE_CONTROL_OBFF_MESSAGE_A  1
# #define PCIE_DEVICE_CONTROL_OBFF_MESSAGE_B  2
# #define PCIE_DEVICE_CONTROL_OBFF_WAKE       3
# 
PCIE_DEVICE_CONTROL_OBFF_DISABLED   = 0
PCIE_DEVICE_CONTROL_OBFF_MESSAGE_A  = 1
PCIE_DEVICE_CONTROL_OBFF_MESSAGE_B  = 2
PCIE_DEVICE_CONTROL_OBFF_WAKE       = 3

# typedef union {
#   struct {
#     UINT32    Reserved         : 1;
#     UINT32    LinkSpeedsVector : 7;
#     UINT32    Crosslink        : 1;
#     UINT32    Reserved2        : 23;
#   } Bits;
#   UINT32    Uint32;
# } PCI_REG_PCIE_LINK_CAPABILITY2;
class PCI_REG_PCIE_LINK_CAPABILITY2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT32, 1),
    ("LinkSpeedsVector",    UINT32, 7),
    ("Crosslink",           UINT32, 1),
    ("Reserved2",           UINT32, 23)
  ]

class PCI_REG_PCIE_LINK_CAPABILITY2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CAPABILITY2_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT16    TargetLinkSpeed                : 4;
#     UINT16    EnterCompliance                : 1;
#     UINT16    HardwareAutonomousSpeedDisable : 1;
#     UINT16    SelectableDeemphasis           : 1;
#     UINT16    TransmitMargin                 : 3;
#     UINT16    EnterModifiedCompliance        : 1;
#     UINT16    ComplianceSos                  : 1;
#     UINT16    CompliancePresetDeemphasis     : 4;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_LINK_CONTROL2;
class PCI_REG_PCIE_LINK_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TargetLinkSpeed",                 UINT16, 4),
    ("EnterCompliance",                 UINT16, 1),
    ("HardwareAutonomousSpeedDisable",  UINT16, 1),
    ("SelectableDeemphasis",            UINT16, 1),
    ("TransmitMargin",                  UINT16, 3),
    ("EnterModifiedCompliance",         UINT16, 1),
    ("ComplianceSos",                   UINT16, 1),
    ("CompliancePresetDeemphasis",      UINT16, 4)
  ]

class PCI_REG_PCIE_LINK_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_CONTROL2_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef union {
#   struct {
#     UINT16    CurrentDeemphasisLevel       : 1;
#     UINT16    EqualizationComplete         : 1;
#     UINT16    EqualizationPhase1Successful : 1;
#     UINT16    EqualizationPhase2Successful : 1;
#     UINT16    EqualizationPhase3Successful : 1;
#     UINT16    LinkEqualizationRequest      : 1;
#     UINT16    Reserved                     : 10;
#   } Bits;
#   UINT16    Uint16;
# } PCI_REG_PCIE_LINK_STATUS2;
class PCI_REG_PCIE_LINK_STATUS2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentDeemphasisLevel",          UINT16, 1),
    ("EqualizationComplete",            UINT16, 1),
    ("EqualizationPhase1Successful",    UINT16, 1),
    ("EqualizationPhase2Successful",    UINT16, 1),
    ("EqualizationPhase3Successful",    UINT16, 1),
    ("LinkEqualizationRequest",         UINT16, 1),
    ("Reserved  ",                      UINT16, 10)
  ]

class PCI_REG_PCIE_LINK_STATUS2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_REG_PCIE_LINK_STATUS2_Bits),
    ("Uint16",          UINT16)
    ]

# 
# typedef struct {
#   EFI_PCI_CAPABILITY_HDR             Hdr;
#   PCI_REG_PCIE_CAPABILITY            Capability;
#   PCI_REG_PCIE_DEVICE_CAPABILITY     DeviceCapability;
#   PCI_REG_PCIE_DEVICE_CONTROL        DeviceControl;
#   PCI_REG_PCIE_DEVICE_STATUS         DeviceStatus;
#   PCI_REG_PCIE_LINK_CAPABILITY       LinkCapability;
#   PCI_REG_PCIE_LINK_CONTROL          LinkControl;
#   PCI_REG_PCIE_LINK_STATUS           LinkStatus;
#   PCI_REG_PCIE_SLOT_CAPABILITY       SlotCapability;
#   PCI_REG_PCIE_SLOT_CONTROL          SlotControl;
#   PCI_REG_PCIE_SLOT_STATUS           SlotStatus;
#   PCI_REG_PCIE_ROOT_CONTROL          RootControl;
#   PCI_REG_PCIE_ROOT_CAPABILITY       RootCapability;
#   PCI_REG_PCIE_ROOT_STATUS           RootStatus;
#   PCI_REG_PCIE_DEVICE_CAPABILITY2    DeviceCapability2;
#   PCI_REG_PCIE_DEVICE_CONTROL2       DeviceControl2;
#   UINT16                             DeviceStatus2;
#   PCI_REG_PCIE_LINK_CAPABILITY2      LinkCapability2;
#   PCI_REG_PCIE_LINK_CONTROL2         LinkControl2;
#   PCI_REG_PCIE_LINK_STATUS2          LinkStatus2;
#   UINT32                             SlotCapability2;
#   UINT16                             SlotControl2;
#   UINT16                             SlotStatus2;
# } PCI_CAPABILITY_PCIEXP;
class PCI_CAPABILITY_PCIEXP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hdr",                 EFI_PCI_CAPABILITY_HDR             ),
    ("Capability",          PCI_REG_PCIE_CAPABILITY            ),
    ("DeviceCapability",    PCI_REG_PCIE_DEVICE_CAPABILITY     ),
    ("DeviceControl",       PCI_REG_PCIE_DEVICE_CONTROL        ),
    ("DeviceStatus",        PCI_REG_PCIE_DEVICE_STATUS         ),
    ("LinkCapability",      PCI_REG_PCIE_LINK_CAPABILITY       ),
    ("LinkControl",         PCI_REG_PCIE_LINK_CONTROL          ),
    ("LinkStatus",          PCI_REG_PCIE_LINK_STATUS           ),
    ("SlotCapability",      PCI_REG_PCIE_SLOT_CAPABILITY       ),
    ("SlotControl",         PCI_REG_PCIE_SLOT_CONTROL          ),
    ("SlotStatus",          PCI_REG_PCIE_SLOT_STATUS           ),
    ("RootControl",         PCI_REG_PCIE_ROOT_CONTROL          ),
    ("RootCapability",      PCI_REG_PCIE_ROOT_CAPABILITY       ),
    ("RootStatus",          PCI_REG_PCIE_ROOT_STATUS           ),
    ("DeviceCapability2",   PCI_REG_PCIE_DEVICE_CAPABILITY2    ),
    ("DeviceControl2",      PCI_REG_PCIE_DEVICE_CONTROL2       ),
    ("DeviceStatus2",       UINT16                             ),
    ("LinkCapability2",     PCI_REG_PCIE_LINK_CAPABILITY2      ),
    ("LinkControl2",        PCI_REG_PCIE_LINK_CONTROL2         ),
    ("LinkStatus2",         PCI_REG_PCIE_LINK_STATUS2          ),
    ("SlotCapability2",     UINT32                             ),
    ("SlotControl2",        UINT16                             ),
    ("SlotStatus2",         UINT16                             )
  ]

# 
# #define EFI_PCIE_CAPABILITY_BASE_OFFSET                           0x100
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL_ARI_HIERARCHY        0x10
# #define EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_OFFSET          0x24
# #define EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_ARI_FORWARDING  0x20
# #define EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_OFFSET               0x28
# #define EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_ARI_FORWARDING       0x20
EFI_PCIE_CAPABILITY_BASE_OFFSET                             = 0x100
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL_ARI_HIERARCHY          = 0x10 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_OFFSET            = 0x24 
EFI_PCIE_CAPABILITY_DEVICE_CAPABILITIES_2_ARI_FORWARDING    = 0x20 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_OFFSET                 = 0x28 
EFI_PCIE_CAPABILITY_DEVICE_CONTROL_2_ARI_FORWARDING         = 0x20 

# 
# //
# // for SR-IOV
# //
# #define EFI_PCIE_CAPABILITY_ID_ARI    0x0E
# #define EFI_PCIE_CAPABILITY_ID_ATS    0x0F
# #define EFI_PCIE_CAPABILITY_ID_SRIOV  0x10
# #define EFI_PCIE_CAPABILITY_ID_MRIOV  0x11
EFI_PCIE_CAPABILITY_ID_ARI        = 0x0E
EFI_PCIE_CAPABILITY_ID_ATS        = 0x0F
EFI_PCIE_CAPABILITY_ID_SRIOV      = 0x10
EFI_PCIE_CAPABILITY_ID_MRIOV      = 0x11

# 
# typedef struct {
#   UINT32    CapabilityHeader;
#   UINT32    Capability;
#   UINT16    Control;
#   UINT16    Status;
#   UINT16    InitialVFs;
#   UINT16    TotalVFs;
#   UINT16    NumVFs;
#   UINT8     FunctionDependencyLink;
#   UINT8     Reserved0;
#   UINT16    FirstVFOffset;
#   UINT16    VFStride;
#   UINT16    Reserved1;
#   UINT16    VFDeviceID;
#   UINT32    SupportedPageSize;
#   UINT32    SystemPageSize;
#   UINT32    VFBar[6];
#   UINT32    VFMigrationStateArrayOffset;
# } SR_IOV_CAPABILITY_REGISTER;
class SR_IOV_CAPABILITY_REGISTER (Structure):
  _fields_ = [
    ("CapabilityHeader",            UINT32),
    ("Capability",                  UINT32),
    ("Control",                     UINT16),
    ("Status",                      UINT16),
    ("InitialVFs",                  UINT16),
    ("TotalVFs",                    UINT16),
    ("NumVFs",                      UINT16),
    ("FunctionDependencyLink",      UINT8),
    ("Reserved0",                   UINT8),
    ("FirstVFOffset",               UINT16),
    ("VFStride",                    UINT16),
    ("Reserved1",                   UINT16),
    ("VFDeviceID",                  UINT16),
    ("SupportedPageSize",           UINT32),
    ("SystemPageSize",              UINT32),
    ("VFBar",                       UINT32 * 6),
    ("VFMigrationStateArrayOffset", UINT32)
    ]

# 
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_CAPABILITIES              0x04
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL                   0x08
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_STATUS                    0x0A
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_INITIALVFS                0x0C
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_TOTALVFS                  0x0E
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_NUMVFS                    0x10
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_FUNCTION_DEPENDENCY_LINK  0x12
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_FIRSTVF                   0x14
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_VFSTRIDE                  0x16
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_VFDEVICEID                0x1A
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_SUPPORTED_PAGE_SIZE       0x1C
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_SYSTEM_PAGE_SIZE          0x20
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR0                      0x24
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR1                      0x28
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR2                      0x2C
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR3                      0x30
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR4                      0x34
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_BAR5                      0x38
# #define EFI_PCIE_CAPABILITY_ID_SRIOV_VF_MIGRATION_STATE        0x3C
EFI_PCIE_CAPABILITY_ID_SRIOV_CAPABILITIES               = 0x04
EFI_PCIE_CAPABILITY_ID_SRIOV_CONTROL                    = 0x08
EFI_PCIE_CAPABILITY_ID_SRIOV_STATUS                     = 0x0A
EFI_PCIE_CAPABILITY_ID_SRIOV_INITIALVFS                 = 0x0C
EFI_PCIE_CAPABILITY_ID_SRIOV_TOTALVFS                   = 0x0E
EFI_PCIE_CAPABILITY_ID_SRIOV_NUMVFS                     = 0x10
EFI_PCIE_CAPABILITY_ID_SRIOV_FUNCTION_DEPENDENCY_LINK   = 0x12
EFI_PCIE_CAPABILITY_ID_SRIOV_FIRSTVF                    = 0x14
EFI_PCIE_CAPABILITY_ID_SRIOV_VFSTRIDE                   = 0x16
EFI_PCIE_CAPABILITY_ID_SRIOV_VFDEVICEID                 = 0x1A
EFI_PCIE_CAPABILITY_ID_SRIOV_SUPPORTED_PAGE_SIZE        = 0x1C
EFI_PCIE_CAPABILITY_ID_SRIOV_SYSTEM_PAGE_SIZE           = 0x20
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR0                       = 0x24
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR1                       = 0x28
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR2                       = 0x2C
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR3                       = 0x30
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR4                       = 0x34
EFI_PCIE_CAPABILITY_ID_SRIOV_BAR5                       = 0x38
EFI_PCIE_CAPABILITY_ID_SRIOV_VF_MIGRATION_STATE         = 0x3C

# 
# typedef struct {
#   UINT32    CapabilityId         : 16;
#   UINT32    CapabilityVersion    : 4;
#   UINT32    NextCapabilityOffset : 12;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER (Structure):
  _fields_ = [
    ("CapabilityId",            UINT32, 16),
    ("CapabilityVersion",       UINT32,  4),
    ("NextCapabilityOffset",    UINT32, 12)
    ]

# 
# #define PCI_EXP_EXT_HDR  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER
PCI_EXP_EXT_HDR = PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_ID    0x0001
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER1  0x1
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER2  0x2
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_ID   = 0x0001
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER1 = 0x1   
PCI_EXPRESS_EXTENDED_CAPABILITY_ADVANCED_ERROR_REPORTING_VER2 = 0x2   

# 
# typedef union {
#   struct {
#     UINT32    Undefined                  : 1;
#     UINT32    Reserved                   : 3;
#     UINT32    DataLinkProtocolError      : 1;
#     UINT32    SurpriseDownError          : 1;
#     UINT32    Reserved2                  : 6;
#     UINT32    PoisonedTlp                : 1;
#     UINT32    FlowControlProtocolError   : 1;
#     UINT32    CompletionTimeout          : 1;
#     UINT32    CompleterAbort             : 1;
#     UINT32    UnexpectedCompletion       : 1;
#     UINT32    ReceiverOverflow           : 1;
#     UINT32    MalformedTlp               : 1;
#     UINT32    EcrcError                  : 1;
#     UINT32    UnsupportedRequestError    : 1;
#     UINT32    AcsVoilation               : 1;
#     UINT32    UncorrectableInternalError : 1;
#     UINT32    McBlockedTlp               : 1;
#     UINT32    AtomicOpEgressBlocked      : 1;
#     UINT32    TlpPrefixBlockedError      : 1;
#     UINT32    Reserved3                  : 6;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_REG_UNCORRECTABLE_ERROR;
class PCI_EXPRESS_REG_UNCORRECTABLE_ERROR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Undefined",                   UINT32, 1),
    ("Reserved",                    UINT32, 3),
    ("DataLinkProtocolError",       UINT32, 1),
    ("SurpriseDownError",           UINT32, 1),
    ("Reserved2",                   UINT32, 6),
    ("PoisonedTlp",                 UINT32, 1),
    ("FlowControlProtocolError",    UINT32, 1),
    ("CompletionTimeout",           UINT32, 1),
    ("CompleterAbort",              UINT32, 1),
    ("UnexpectedCompletion",        UINT32, 1),
    ("ReceiverOverflow",            UINT32, 1),
    ("MalformedTlp",                UINT32, 1),
    ("EcrcError",                   UINT32, 1),
    ("UnsupportedRequestError",     UINT32, 1),
    ("AcsVoilation",                UINT32, 1),
    ("UncorrectableInternalError",  UINT32, 1),
    ("McBlockedTlp",                UINT32, 1),
    ("AtomicOpEgressBlocked",       UINT32, 1),
    ("TlpPrefixBlockedError",       UINT32, 1),
    ("Reserved3",                   UINT32, 6)
  ]

class PCI_EXPRESS_REG_UNCORRECTABLE_ERROR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_REG_UNCORRECTABLE_ERROR_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   PCI_EXPRESS_REG_UNCORRECTABLE_ERROR         UncorrectableErrorStatus;
#   PCI_EXPRESS_REG_UNCORRECTABLE_ERROR         UncorrectableErrorMask;
#   PCI_EXPRESS_REG_UNCORRECTABLE_ERROR         UncorrectableErrorSeverity;
#   UINT32                                      CorrectableErrorStatus;
#   UINT32                                      CorrectableErrorMask;
#   UINT32                                      AdvancedErrorCapabilitiesAndControl;
#   UINT32                                      HeaderLog[4];
#   UINT32                                      RootErrorCommand;
#   UINT32                                      RootErrorStatus;
#   UINT16                                      ErrorSourceIdentification;
#   UINT16                                      CorrectableErrorSourceIdentification;
#   UINT32                                      TlpPrefixLog[4];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_ADVANCED_ERROR_REPORTING;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_ADVANCED_ERROR_REPORTING (Structure):
  _fields_ = [
    ("Header",                                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("UncorrectableErrorStatus",              PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("UncorrectableErrorMask",                PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("UncorrectableErrorSeverity",            PCI_EXPRESS_REG_UNCORRECTABLE_ERROR),
    ("CorrectableErrorStatus",                UINT32),
    ("CorrectableErrorMask",                  UINT32),
    ("AdvancedErrorCapabilitiesAndControl",   UINT32),
    ("HeaderLog",                             UINT32 * 4),
    ("RootErrorCommand",                      UINT32),
    ("RootErrorStatus",                       UINT32),
    ("ErrorSourceIdentification",             UINT16),
    ("CorrectableErrorSourceIdentification",  UINT16),
    ("TlpPrefixLog",                          UINT32 * 4)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_ID    0x0002
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_MFVC  0x0009
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_ID    = 0x0002
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_MFVC  = 0x0009
PCI_EXPRESS_EXTENDED_CAPABILITY_VIRTUAL_CHANNEL_VER1  = 0x1   

# 
# typedef struct {
#   UINT32    VcResourceCapability : 24;
#   UINT32    PortArbTableOffset   : 8;
#   UINT32    VcResourceControl;
#   UINT16    Reserved1;
#   UINT16    VcResourceStatus;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC (Structure):
  _fields_ = [
    ("VcResourceCapability",  UINT32, 24),
    ("PortArbTableOffset",    UINT32,  8),
    ("VcResourceControl",     UINT32),
    ("Reserved1",             UINT16),
    ("VcResourceStatus",      UINT16)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                Header;
#   UINT32                                                  ExtendedVcCount   : 3;
#   UINT32                                                  PortVcCapability1 : 29;
#   UINT32                                                  PortVcCapability2 : 24;
#   UINT32                                                  VcArbTableOffset  : 8;
#   UINT16                                                  PortVcControl;
#   UINT16                                                  PortVcStatus;
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC    Capability[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ExtendedVcCount",   UINT32,  3),
    ("PortVcCapability1", UINT32, 29),
    ("PortVcCapability2", UINT32, 24),
    ("VcArbTableOffset",  UINT32,  8),
    ("PortVcControl",     UINT16),
    ("PortVcStatus",      UINT16),
    ("Capability",        PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_VC * 1)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_ID    0x0003
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_ID    = 0x0003
PCI_EXPRESS_EXTENDED_CAPABILITY_SERIAL_NUMBER_VER1  = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT64                                      SerialNumber;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_SERIAL_NUMBER;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_SERIAL_NUMBER (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("SerialNumber",  UINT64)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_ID    0x0005
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_ID   = 0x0005
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      ElementSelfDescription;
#   UINT32                                      Reserved;
#   UINT32                                      LinkEntry[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_LINK_DECLARATION;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_LINK_DECLARATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("ElementSelfDescription",  UINT32),
    ("Reserved",                UINT32),
    ("LinkEntry",               UINT32 * 1)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_GET_LINK_COUNT(LINK_DECLARATION)  (UINT8)(((LINK_DECLARATION->ElementSelfDescription)&0x0000ff00)>>8)
def PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_DECLARATION_GET_LINK_COUNT (LINK_DECLARATION):

  return cast(((LINK_DECLARATION.ElementSelfDescription) & 0x0000ff00)>>8, UINT8)

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_ID    0x0006
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_ID   = 0x0006
PCI_EXPRESS_EXTENDED_CAPABILITY_LINK_CONTROL_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      RootComplexLinkCapabilities;
#   UINT16                                      RootComplexLinkControl;
#   UINT16                                      RootComplexLinkStatus;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_INTERNAL_LINK_CONTROL;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_INTERNAL_LINK_CONTROL (Structure):
  _fields_ = [
    ("Header",                      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("RootComplexLinkCapabilities", UINT32),
    ("RootComplexLinkControl",      UINT16),
    ("RootComplexLinkStatus",       UINT16)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_ID    0x0004
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_ID   = 0x0004
PCI_EXPRESS_EXTENDED_CAPABILITY_POWER_BUDGETING_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      DataSelect            : 8;
#   UINT32                                      Reserved              : 24;
#   UINT32                                      Data;
#   UINT32                                      PowerBudgetCapability : 1;
#   UINT32                                      Reserved2             : 7;
#   UINT32                                      Reserved3             : 24;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_POWER_BUDGETING;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_POWER_BUDGETING (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DataSelect",            UINT32,  8),
    ("Reserved",              UINT32, 24),
    ("Data",                  UINT32),
    ("PowerBudgetCapability", UINT32,  1),
    ("Reserved2",             UINT32,  7),
    ("Reserved3",             UINT32, 24)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_ID    0x000D
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_ID   = 0x000D
PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT16                                      AcsCapability;
#   UINT16                                      AcsControl;
#   UINT8                                       EgressControlVectorArray[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_ACS_EXTENDED;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_ACS_EXTENDED (Structure):
  _fields_ = [
    ("Header",                    PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AcsCapability",             UINT16),
    ("AcsControl",                UINT16),
    ("EgressControlVectorArray",  UINT8 * 1)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_CONTROL(ACS_EXTENDED)      (UINT8)(((ACS_EXTENDED->AcsCapability)&0x00000020))
def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_CONTROL (ACS_EXTENDED):

  return cast(((ACS_EXTENDED.AcsCapability)&0x00000020), UINT8)

# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_VECTOR_SIZE(ACS_EXTENDED)  (UINT8)(((ACS_EXTENDED->AcsCapability)&0x0000FF00))
def PCI_EXPRESS_EXTENDED_CAPABILITY_ACS_EXTENDED_GET_EGRES_VECTOR_SIZE(ACS_EXTENDED):

  return cast(((ACS_EXTENDED.AcsCapability)&0x0000FF00), UINT8)

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_ID    0x0007
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_ID   = 0x0007
PCI_EXPRESS_EXTENDED_CAPABILITY_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      AssociationBitmap;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_EVENT_COLLECTOR_ENDPOINT_ASSOCIATION (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AssociationBitmap", UINT32)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_ID    0x0008
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_ID    = 0x0008
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTI_FUNCTION_VIRTUAL_CHANNEL_VER1  = 0x1   

# 
# typedef PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTI_FUNCTION_VIRTUAL_CHANNEL_CAPABILITY;
PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTI_FUNCTION_VIRTUAL_CHANNEL_CAPABILITY = PCI_EXPRESS_EXTENDED_CAPABILITIES_VIRTUAL_CHANNEL_CAPABILITY

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_ID    0x000B
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_ID   = 0x000B
PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      VendorSpecificHeader;
#   UINT8                                       VendorSpecific[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_VENDOR_SPECIFIC;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_VENDOR_SPECIFIC (Structure):
  _fields_ = [
    ("Header",                PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorSpecificHeader",  UINT32),
    ("VendorSpecific",        UINT8 * 1)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_GET_SIZE(VENDOR)  (UINT16)(((VENDOR->VendorSpecificHeader)&0xFFF00000)>>20)
def PCI_EXPRESS_EXTENDED_CAPABILITY_VENDOR_SPECIFIC_GET_SIZE(VENDOR):

  return cast(((VENDOR.VendorSpecificHeader)&0xFFF00000)>>20, UINT16)

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_ID    0x000A
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_ID   = 0x000A
PCI_EXPRESS_EXTENDED_CAPABILITY_RCRB_HEADER_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT16                                      VendorId;
#   UINT16                                      DeviceId;
#   UINT32                                      RcrbCapabilities;
#   UINT32                                      RcrbControl;
#   UINT32                                      Reserved;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_RCRB_HEADER;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_RCRB_HEADER (Structure):
  _fields_ = [
    ("Header",            PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("VendorId",          UINT16),
    ("DeviceId",          UINT16),
    ("RcrbCapabilities",  UINT32),
    ("RcrbControl",       UINT32),
    ("Reserved",          UINT32)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_ID    0x0012
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_ID   = 0x0012
PCI_EXPRESS_EXTENDED_CAPABILITY_MULTICAST_VER1 = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT16                                      MultiCastCapability;
#   UINT16                                      MulticastControl;
#   UINT64                                      McBaseAddress;
#   UINT64                                      McReceiveAddress;
#   UINT64                                      McBlockAll;
#   UINT64                                      McBlockUntranslated;
#   UINT64                                      McOverlayBar;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTICAST;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_MULTICAST (Structure):
  _fields_ = [
    ("Header",              PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("MultiCastCapability", UINT16),
    ("MulticastControl",    UINT16),
    ("McBaseAddress",       UINT64),
    ("McReceiveAddress",    UINT64),
    ("McBlockAll",          UINT64),
    ("McBlockUntranslated", UINT64),
    ("McOverlayBar",        UINT64)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_ID    0x0015
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_ID    = 0x0015
PCI_EXPRESS_EXTENDED_CAPABILITY_RESIZABLE_BAR_VER1  = 0x1   

# 
# typedef union {
#   struct {
#     UINT32    Reserved          : 4;
#     UINT32    BarSizeCapability : 28;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT32, 4),
    ("BarSizeCapability",   UINT32, 28)
  ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef union {
#   struct {
#     UINT32    BarIndex           : 3;
#     UINT32    Reserved           : 2;
#     UINT32    ResizableBarNumber : 3;
#     UINT32    BarSize            : 6;
#     UINT32    Reserved2          : 2;
#     UINT32    BarSizeCapability  : 16;
#   } Bits;
#   UINT32    Uint32;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BarIndex",            UINT32, 3),
    ("Reserved",            UINT32, 2),
    ("ResizableBarNumber",  UINT32, 3),
    ("BarSize",             UINT32, 6),
    ("Reserved2",           UINT32, 2),
    ("BarSizeCapability",   UINT32, 16)
  ]

class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL_Bits),
    ("Uint32",          UINT32)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY    ResizableBarCapability;
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL       ResizableBarControl;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY (Structure):
  _fields_ = [
    ("ResizableBarCapability",  PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CAPABILITY),
    ("ResizableBarControl",     PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_CONTROL)
    ]

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER                 Header;
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY    Capability[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR (Structure):
  _fields_ = [
    ("Header",      PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("Capability",  PCI_EXPRESS_EXTENDED_CAPABILITIES_RESIZABLE_BAR_ENTRY * 1)
    ]

# 
# #define GET_NUMBER_RESIZABLE_BARS(x)  (x->Capability[0].ResizableBarControl.Bits.ResizableBarNumber)
def GET_NUMBER_RESIZABLE_BARS(x):

  return x.Capability[0].ResizableBarControl.Bits.ResizableBarNumber

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_ID    0x000E
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_ID    = 0x000E
PCI_EXPRESS_EXTENDED_CAPABILITY_ARI_CAPABILITY_VER1  = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT16                                      AriCapability;
#   UINT16                                      AriControl;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_ARI_CAPABILITY;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_ARI_CAPABILITY (Structure):
  _fields_ = [
    ("Header",        PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("AriCapability", UINT16),
    ("AriControl",    UINT16)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_ID    0x0016
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_ID    = 0x0016
PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_VER1  = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      DpaCapability;
#   UINT32                                      DpaLatencyIndicator;
#   UINT16                                      DpaStatus;
#   UINT16                                      DpaControl;
#   UINT8                                       DpaPowerAllocationArray[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_DYNAMIC_POWER_ALLOCATION;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_DYNAMIC_POWER_ALLOCATION (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("DpaCapability",           UINT32),
    ("DpaLatencyIndicator",     UINT32),
    ("DpaStatus",               UINT16),
    ("DpaControl",              UINT16),
    ("DpaPowerAllocationArray", UINT8 * 1)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_GET_SUBSTATE_MAX(POWER)  (UINT16)(((POWER->DpaCapability)&0x0000000F))
def PCI_EXPRESS_EXTENDED_CAPABILITY_DYNAMIC_POWER_ALLOCATION_GET_SUBSTATE_MAX(POWER):

  return cast(((POWER.DpaCapability)&0x0000000F), UINT16)

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_ID    0x0018
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_ID    = 0x0018
PCI_EXPRESS_EXTENDED_CAPABILITY_LATENCE_TOLERANCE_REPORTING_VER1  = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT16                                      MaxSnoopLatency;
#   UINT16                                      MaxNoSnoopLatency;
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_LATENCE_TOLERANCE_REPORTING;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_LATENCE_TOLERANCE_REPORTING (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("MaxSnoopLatency",         UINT16),
    ("MaxNoSnoopLatency",       UINT16)
    ]

# 
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_ID    0x0017
# #define PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_VER1  0x1
PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_ID    = 0x0017
PCI_EXPRESS_EXTENDED_CAPABILITY_TPH_VER1  = 0x1   

# 
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER    Header;
#   UINT32                                      TphRequesterCapability;
#   UINT32                                      TphRequesterControl;
#   UINT16                                      TphStTable[1];
# } PCI_EXPRESS_EXTENDED_CAPABILITIES_TPH;
class PCI_EXPRESS_EXTENDED_CAPABILITIES_TPH (Structure):
  _fields_ = [
    ("Header",                  PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER),
    ("TphRequesterCapability",  UINT32),
    ("TphRequesterControl",     UINT32),
    ("TphStTable",              UINT16 * 1)
    ]

# 
# #define GET_TPH_TABLE_SIZE(x)  ((x->TphRequesterCapability & 0x7FF0000)>>16) * sizeof(UINT16)
def GET_TPH_TABLE_SIZE(x):

  return ((x.TphRequesterCapability & 0x7FF0000)>>16) * sizeof(UINT16)

# 
# #pragma pack()
# 
# #endif
# 