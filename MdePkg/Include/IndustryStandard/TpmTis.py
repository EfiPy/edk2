# /** @file
#   TPM Interface Specification definition.
#   It covers both TPM1.2 and TPM2.0.
# 
# Copyright (c) 2016 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# TpmTis.py
#
# EfiPy2.MdePkg.IndustryStandard.TpmTis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _TPM_TIS_H_
# #define _TPM_TIS_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# //
# // Set structure alignment to 1-byte
# //
# #pragma pack (1)
# 
# //
# // Register set map as specified in TIS specification Chapter 10
# //
# typedef struct {
#   ///
#   /// Used to gain ownership for this particular port.
#   ///
#   UINT8     Access;                                     // 0
#   UINT8     Reserved1[7];                               // 1
#   ///
#   /// Controls interrupts.
#   ///
#   UINT32    IntEnable;                                  // 8
#   ///
#   /// SIRQ vector to be used by the TPM.
#   ///
#   UINT8     IntVector;                                  // 0ch
#   UINT8     Reserved2[3];                               // 0dh
#   ///
#   /// What caused interrupt.
#   ///
#   UINT32    IntSts;                                     // 10h
#   ///
#   /// Shows which interrupts are supported by that particular TPM.
#   ///
#   UINT32    IntfCapability;                             // 14h
#   ///
#   /// Status Register. Provides status of the TPM.
#   ///
#   UINT8     Status;                                     // 18h
#   ///
#   /// Number of consecutive writes that can be done to the TPM.
#   ///
#   UINT16    BurstCount;                                 // 19h
#   UINT8     Reserved3[9];
#   ///
#   /// Read or write FIFO, depending on transaction.
#   ///
#   UINT32    DataFifo;                                   // 24h
#   UINT8     Reserved4[0xed8];                           // 28h
#   ///
#   /// Vendor ID
#   ///
#   UINT16    Vid;                                        // 0f00h
#   ///
#   /// Device ID
#   ///
#   UINT16    Did;                                        // 0f02h
#   ///
#   /// Revision ID
#   ///
#   UINT8     Rid;                                        // 0f04h
#   UINT8     Reserved[0x7b];                             // 0f05h
#   ///
#   /// Alias to I/O legacy space.
#   ///
#   UINT32    LegacyAddress1;                             // 0f80h
#   ///
#   /// Additional 8 bits for I/O legacy space extension.
#   ///
#   UINT32    LegacyAddress1Ex;                           // 0f84h
#   ///
#   /// Alias to second I/O legacy space.
#   ///
#   UINT32    LegacyAddress2;                             // 0f88h
#   ///
#   /// Additional 8 bits for second I/O legacy space extension.
#   ///
#   UINT32    LegacyAddress2Ex;                           // 0f8ch
#   ///
#   /// Vendor-defined configuration registers.
#   ///
#   UINT8     VendorDefined[0x70];                        // 0f90h
# } TIS_PC_REGISTERS;
class TIS_PC_REGISTERS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Access",            UINT8),
    ("Reserved1",         UINT8 * 7),
    ("IntEnable",         UINT32),
    ("IntVector",         UINT8),
    ("Reserved2",         UINT8 * 3),
    ("IntSts",            UINT32),
    ("IntfCapability",    UINT32),
    ("Status",            UINT8),
    ("BurstCount",        UINT16),
    ("Reserved3",         UINT8 * 9),
    ("DataFifo",          UINT32),
    ("Reserved4",         UINT8 * 0xed8),
    ("Vid",               UINT16),
    ("Did",               UINT16),
    ("Rid",               UINT8),
    ("Reserved",          UINT8 * 0x7b),
    ("LegacyAddress1",    UINT32),
    ("LegacyAddress1Ex",  UINT32),
    ("LegacyAddress2",    UINT32),
    ("LegacyAddress2Ex",  UINT32),
    ("VendorDefined",     UINT8 * 0x70)
  ]

# 
# //
# // Restore original structure alignment
# //
# #pragma pack ()
# 
# //
# // Define pointer types used to access TIS registers on PC
# //
# typedef TIS_PC_REGISTERS *TIS_PC_REGISTERS_PTR;
# 
# //
# // Define bits of ACCESS and STATUS registers
# //
# 
# ///
# /// This bit is a 1 to indicate that the other bits in this register are valid.
# ///
# #define TIS_PC_VALID  BIT7
# ///
# /// Indicate that this locality is active.
# ///
# #define TIS_PC_ACC_ACTIVE  BIT5
TIS_PC_ACC_ACTIVE           = BIT5
# ///
# /// Set to 1 to indicate that this locality had the TPM taken away while
# /// this locality had the TIS_PC_ACC_ACTIVE bit set.
# ///
# #define TIS_PC_ACC_SEIZED  BIT4
TIS_PC_ACC_SEIZED           = BIT4
# ///
# /// Set to 1 to indicate that TPM MUST reset the
# /// TIS_PC_ACC_ACTIVE bit and remove ownership for localities less than the
# /// locality that is writing this bit.
# ///
# #define TIS_PC_ACC_SEIZE  BIT3
TIS_PC_ACC_SEIZE            = BIT3
# ///
# /// When this bit is 1, another locality is requesting usage of the TPM.
# ///
# #define TIS_PC_ACC_PENDIND  BIT2
TIS_PC_ACC_PENDIND          = BIT2
# ///
# /// Set to 1 to indicate that this locality is requesting to use TPM.
# ///
# #define TIS_PC_ACC_RQUUSE  BIT1
TIS_PC_ACC_RQUUSE           = BIT1
# ///
# /// A value of 1 indicates that a T/OS has not been established on the platform
# ///
# #define TIS_PC_ACC_ESTABLISH  BIT0
TIS_PC_ACC_ESTABLISH        = BIT0

# 
# ///
# /// Write a 1 to this bit to notify TPM to cancel currently executing command
# ///
# #define TIS_PC_STS_CANCEL  BIT24
# ///
# /// This field indicates that STS_DATA and STS_EXPECT are valid
# ///
# #define TIS_PC_STS_VALID  BIT7
TIS_PC_STS_VALID            = BIT7
# ///
# /// When this bit is 1, TPM is in the Ready state,
# /// indicating it is ready to receive a new command.
# ///
# #define TIS_PC_STS_READY  BIT6
TIS_PC_STS_READY            = BIT6
# ///
# /// Write a 1 to this bit to cause the TPM to execute that command.
# ///
# #define TIS_PC_STS_GO  BIT5
TIS_PC_STS_GO               = BIT5
# ///
# /// This bit indicates that the TPM has data available as a response.
# ///
# #define TIS_PC_STS_DATA  BIT4
TIS_PC_STS_DATA             = BIT4
# ///
# /// The TPM sets this bit to a value of 1 when it expects another byte of data for a command.
# ///
# #define TIS_PC_STS_EXPECT  BIT3
TIS_PC_STS_EXPECT           = BIT3
# ///
# /// Indicates that the TPM has completed all self-test actions following a TPM_ContinueSelfTest command.
# ///
# #define TIS_PC_STS_SELFTEST_DONE  BIT2
TIS_PC_STS_SELFTEST_DONE    = BIT2
# ///
# /// Writes a 1 to this bit to force the TPM to re-send the response.
# ///
# #define TIS_PC_STS_RETRY  BIT1
TIS_PC_STS_RETRY            = BIT1

# 
# //
# // Default TimeOut value
# //
# #define TIS_TIMEOUT_A  (750  * 1000)               // 750ms
# #define TIS_TIMEOUT_B  (2000 * 1000)               // 2s
# #define TIS_TIMEOUT_C  (750  * 1000)               // 750ms
# #define TIS_TIMEOUT_D  (750  * 1000)               // 750ms
TIS_TIMEOUT_A               = (750  * 1000)
TIS_TIMEOUT_B               = (2000 * 1000)
TIS_TIMEOUT_C               = (750  * 1000)
TIS_TIMEOUT_D               = (750  * 1000)

# 
# #endif
# 