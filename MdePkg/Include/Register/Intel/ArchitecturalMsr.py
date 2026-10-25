# /** @file
#   Intel Architectural MSR Definitions.
# 
#   Provides defines for Machine Specific Registers(MSR) indexes. Data structures
#   are provided for MSRs that contain one or more bit fields.  If the MSR value
#   returned is a single 32-bit or 64-bit value, then a data structure is not
#   provided for that MSR.
# 
#   Copyright (c) 2016 - 2023, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Specification Reference:
#   Intel(R) 64 and IA-32 Architectures Software Developer's Manual, Volume 4,
#   May 2018, Volume 4: Model-Specific-Registers (MSR)
# 
# **/
# ArchitecturalMsr.py
#
# EfiPy2.MdePkg.Register.Intel.ArchitecturalMsr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __INTEL_ARCHITECTURAL_MSR_H__
# #define __INTEL_ARCHITECTURAL_MSR_H__
from EfiPy2 import *

# 
# # pragma warning (disable:4819)
# 
# /**
#   See Section 2.22, "MSRs in Pentium Processors.". Pentium Processor (05_01H).
# 
#   @param  ECX  MSR_IA32_P5_MC_ADDR (0x00000000)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_P5_MC_ADDR);
#   AsmWriteMsr64 (MSR_IA32_P5_MC_ADDR, Msr);
#   @endcode
#   @note MSR_IA32_P5_MC_ADDR is defined as IA32_P5_MC_ADDR in SDM.
# **/
# #define MSR_IA32_P5_MC_ADDR  0x00000000
MSR_IA32_P5_MC_ADDR             = 0x00000000

# 
# /**
#   See Section 2.22, "MSRs in Pentium Processors.". DF_DM = 05_01H.
# 
#   @param  ECX  MSR_IA32_P5_MC_TYPE (0x00000001)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_P5_MC_TYPE);
#   AsmWriteMsr64 (MSR_IA32_P5_MC_TYPE, Msr);
#   @endcode
#   @note MSR_IA32_P5_MC_TYPE is defined as IA32_P5_MC_TYPE in SDM.
# **/
# #define MSR_IA32_P5_MC_TYPE  0x00000001
MSR_IA32_P5_MC_TYPE             = 0x00000001

# 
# /**
#   See Section 8.10.5, "Monitor/Mwait Address Range Determination.". Introduced
#   at Display Family / Display Model 0F_03H.
# 
#   @param  ECX  MSR_IA32_MONITOR_FILTER_SIZE (0x00000006)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MONITOR_FILTER_SIZE);
#   AsmWriteMsr64 (MSR_IA32_MONITOR_FILTER_SIZE, Msr);
#   @endcode
#   @note MSR_IA32_MONITOR_FILTER_SIZE is defined as IA32_MONITOR_FILTER_SIZE in SDM.
# **/
# #define MSR_IA32_MONITOR_FILTER_SIZE  0x00000006
MSR_IA32_MONITOR_FILTER_SIZE    = 0x00000006

# 
# /**
#   See Section 17.17, "Time-Stamp Counter.". Introduced at Display Family /
#   Display Model 05_01H.
# 
#   @param  ECX  MSR_IA32_TIME_STAMP_COUNTER (0x00000010)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_TIME_STAMP_COUNTER);
#   AsmWriteMsr64 (MSR_IA32_TIME_STAMP_COUNTER, Msr);
#   @endcode
#   @note MSR_IA32_TIME_STAMP_COUNTER is defined as IA32_TIME_STAMP_COUNTER in SDM.
# **/
# #define MSR_IA32_TIME_STAMP_COUNTER  0x00000010
MSR_IA32_TIME_STAMP_COUNTER     = 0x00000010

# 
# /**
#   Platform ID (RO)  The operating system can use this MSR to determine "slot"
#   information for the processor and the proper microcode update to load.
#   Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_PLATFORM_ID (0x00000017)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PLATFORM_ID_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PLATFORM_ID_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PLATFORM_ID_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PLATFORM_ID);
#   @endcode
#   @note MSR_IA32_PLATFORM_ID is defined as IA32_PLATFORM_ID in SDM.
# **/
# #define MSR_IA32_PLATFORM_ID  0x00000017
MSR_IA32_PLATFORM_ID            = 0x00000017

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PLATFORM_ID
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved1 : 32;
#     UINT32    Reserved2 : 18;
#     ///
#     /// [Bits 52:50] Platform Id (RO)  Contains information concerning the
#     /// intended platform for the processor.
#     ///   52 51 50
#     ///   -- -- --
#     ///    0  0  0  Processor Flag 0.
#     ///    0  0  1  Processor Flag 1
#     ///    0  1  0  Processor Flag 2
#     ///    0  1  1  Processor Flag 3
#     ///    1  0  0  Processor Flag 4
#     ///    1  0  1  Processor Flag 5
#     ///    1  1  0  Processor Flag 6
#     ///    1  1  1  Processor Flag 7
#     ///
#     UINT32    PlatformId : 3;
#     UINT32    Reserved3  : 11;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PLATFORM_ID_REGISTER;
class MSR_IA32_PLATFORM_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 32),
    ("Reserved2",   UINT32, 18),
    ("PlatformId",  UINT32, 3),
    ("Reserved3",   UINT32, 11)
  ]

class MSR_IA32_PLATFORM_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PLATFORM_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   06_01H.
# 
#   @param  ECX  MSR_IA32_APIC_BASE (0x0000001B)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_APIC_BASE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_APIC_BASE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_APIC_BASE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_APIC_BASE);
#   AsmWriteMsr64 (MSR_IA32_APIC_BASE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_APIC_BASE is defined as IA32_APIC_BASE in SDM.
# **/
# #define MSR_IA32_APIC_BASE  0x0000001B
MSR_IA32_APIC_BASE              = 0x0000001B

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_APIC_BASE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved1  : 8;
#     ///
#     /// [Bit 8] BSP flag (R/W).
#     ///
#     UINT32    BSP        : 1;
#     UINT32    Reserved2  : 1;
#     ///
#     /// [Bit 10] Enable x2APIC mode. Introduced at Display Family / Display
#     /// Model 06_1AH.
#     ///
#     UINT32    EXTD       : 1;
#     ///
#     /// [Bit 11] APIC Global Enable (R/W).
#     ///
#     UINT32    EN         : 1;
#     ///
#     /// [Bits 31:12] APIC Base (R/W).
#     ///
#     UINT32    ApicBase   : 20;
#     ///
#     /// [Bits 63:32] APIC Base (R/W).
#     ///
#     UINT32    ApicBaseHi : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_APIC_BASE_REGISTER;
class MSR_IA32_APIC_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 8),
    ("BSP",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("EXTD",        UINT32, 1),
    ("EN",          UINT32, 1),
    ("ApicBase",    UINT32, 20),
    ("ApicBaseHi",  UINT32, 32)
  ]

class MSR_IA32_APIC_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_APIC_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Control Features in Intel 64 Processor (R/W). If any one enumeration
#   condition for defined bit field holds.
# 
#   @param  ECX  MSR_IA32_FEATURE_CONTROL (0x0000003A)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_FEATURE_CONTROL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_FEATURE_CONTROL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_FEATURE_CONTROL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_FEATURE_CONTROL);
#   AsmWriteMsr64 (MSR_IA32_FEATURE_CONTROL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_FEATURE_CONTROL is defined as IA32_FEATURE_CONTROL in SDM.
# **/
# #define MSR_IA32_FEATURE_CONTROL  0x0000003A
MSR_IA32_FEATURE_CONTROL        = 0x0000003A

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_FEATURE_CONTROL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Lock bit (R/WO): (1 = locked). When set, locks this MSR from
#     /// being written, writes to this bit will result in GP(0). Note: Once the
#     /// Lock bit is set, the contents of this register cannot be modified.
#     /// Therefore the lock bit must be set after configuring support for Intel
#     /// Virtualization Technology and prior to transferring control to an
#     /// option ROM or the OS. Hence, once the Lock bit is set, the entire
#     /// IA32_FEATURE_CONTROL contents are preserved across RESET when PWRGOOD
#     /// is not deasserted. If any one enumeration condition for defined bit
#     /// field position greater than bit 0 holds.
#     ///
#     UINT32    Lock : 1;
#     ///
#     /// [Bit 1] Enable VMX inside SMX operation (R/WL): This bit enables a
#     /// system executive to use VMX in conjunction with SMX to support
#     /// Intel(R) Trusted Execution Technology. BIOS must set this bit only
#     /// when the CPUID function 1 returns VMX feature flag and SMX feature
#     /// flag set (ECX bits 5 and 6 respectively). If CPUID.01H:ECX[5] = 1 &&
#     /// CPUID.01H:ECX[6] = 1.
#     ///
#     UINT32    EnableVmxInsideSmx         : 1;
#     ///
#     /// [Bit 2] Enable VMX outside SMX operation (R/WL): This bit enables VMX
#     /// for system executive that do not require SMX. BIOS must set this bit
#     /// only when the CPUID function 1 returns VMX feature flag set (ECX bit
#     /// 5). If CPUID.01H:ECX[5] = 1.
#     ///
#     UINT32    EnableVmxOutsideSmx        : 1;
#     UINT32    Reserved1                  : 5;
#     ///
#     /// [Bits 14:8] SENTER Local Function Enables (R/WL): When set, each bit
#     /// in the field represents an enable control for a corresponding SENTER
#     /// function. This bit is supported only if CPUID.1:ECX.[bit 6] is set. If
#     /// CPUID.01H:ECX[6] = 1.
#     ///
#     UINT32    SenterLocalFunctionEnables : 7;
#     ///
#     /// [Bit 15] SENTER Global Enable (R/WL): This bit must be set to enable
#     /// SENTER leaf functions. This bit is supported only if CPUID.1:ECX.[bit
#     /// 6] is set. If CPUID.01H:ECX[6] = 1.
#     ///
#     UINT32    SenterGlobalEnable         : 1;
#     UINT32    Reserved2                  : 1;
#     ///
#     /// [Bit 17] SGX Launch Control Enable (R/WL): This bit must be set to
#     /// enable runtime reconfiguration of SGX Launch Control via
#     /// IA32_SGXLEPUBKEYHASHn MSR. If CPUID.(EAX=07H, ECX=0H): ECX[30] = 1.
#     ///
#     UINT32    SgxLaunchControlEnable     : 1;
#     ///
#     /// [Bit 18] SGX Global Enable (R/WL): This bit must be set to enable SGX
#     /// leaf functions. If CPUID.(EAX=07H, ECX=0H): EBX[2] = 1.
#     ///
#     UINT32    SgxEnable                  : 1;
#     UINT32    Reserved3                  : 1;
#     ///
#     /// [Bit 20] LMCE On (R/WL): When set, system software can program the
#     /// MSRs associated with LMCE to configure delivery of some machine check
#     /// exceptions to a single logical processor. If IA32_MCG_CAP[27] = 1.
#     ///
#     UINT32    LmceOn                     : 1;
#     UINT32    Reserved4                  : 11;
#     UINT32    Reserved5                  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_FEATURE_CONTROL_REGISTER;
class MSR_IA32_FEATURE_CONTROL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                        UINT32, 1),
    ("EnableVmxInsideSmx",          UINT32, 1),
    ("EnableVmxOutsideSmx",         UINT32, 1),
    ("Reserved1",                   UINT32, 5),
    ("SenterLocalFunctionEnables",  UINT32, 7),
    ("SenterGlobalEnable",          UINT32, 1),
    ("Reserved2",                   UINT32, 1),
    ("SgxLaunchControlEnable",      UINT32, 1),
    ("SgxEnable",                   UINT32, 1),
    ("Reserved3",                   UINT32, 1),
    ("LmceOn",                      UINT32, 1),
    ("Reserved4",                   UINT32, 11),
    ("Reserved5",                   UINT32, 32)
  ]

class MSR_IA32_FEATURE_CONTROL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_FEATURE_CONTROL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Per Logical Processor TSC Adjust (R/Write to clear). If CPUID.(EAX=07H,
#   ECX=0H): EBX[1] = 1. THREAD_ADJUST:  Local offset value of the IA32_TSC for
#   a logical processor. Reset value is Zero. A write to IA32_TSC will modify
#   the local offset in IA32_TSC_ADJUST and the content of IA32_TSC, but does
#   not affect the internal invariant TSC hardware.
# 
#   @param  ECX  MSR_IA32_TSC_ADJUST (0x0000003B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_TSC_ADJUST);
#   AsmWriteMsr64 (MSR_IA32_TSC_ADJUST, Msr);
#   @endcode
#   @note MSR_IA32_TSC_ADJUST is defined as IA32_TSC_ADJUST in SDM.
# **/
# #define MSR_IA32_TSC_ADJUST  0x0000003B
MSR_IA32_TSC_ADJUST             = 0x0000003B

# 
# /**
#   BIOS Update Trigger (W) Executing a WRMSR instruction to this MSR causes a
#   microcode update to be loaded into the processor. See Section 9.11.6,
#   "Microcode Update Loader." A processor may prevent writing to this MSR when
#   loading guest states on VM entries or saving guest states on VM exits.
#   Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_BIOS_UPDT_TRIG (0x00000079)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = 0;
#   AsmWriteMsr64 (MSR_IA32_BIOS_UPDT_TRIG, Msr);
#   @endcode
#   @note MSR_IA32_BIOS_UPDT_TRIG is defined as IA32_BIOS_UPDT_TRIG in SDM.
# **/
# #define MSR_IA32_BIOS_UPDT_TRIG  0x00000079
MSR_IA32_BIOS_UPDT_TRIG         = 0x00000079

# 
# /**
#   BIOS Update Signature (RO) Returns the microcode update signature following
#   the execution of CPUID.01H. A processor may prevent writing to this MSR when
#   loading guest states on VM entries or saving guest states on VM exits.
#   Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_BIOS_SIGN_ID (0x0000008B)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_BIOS_SIGN_ID_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_BIOS_SIGN_ID_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_BIOS_SIGN_ID_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_BIOS_SIGN_ID);
#   @endcode
#   @note MSR_IA32_BIOS_SIGN_ID is defined as IA32_BIOS_SIGN_ID in SDM.
# **/
# #define MSR_IA32_BIOS_SIGN_ID  0x0000008B
MSR_IA32_BIOS_SIGN_ID           = 0x0000008B

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_BIOS_SIGN_ID
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved : 32;
#     ///
#     /// [Bits 63:32] Microcode update signature. This field contains the
#     /// signature of the currently loaded microcode update when read following
#     /// the execution of the CPUID instruction, function 1. It is required
#     /// that this register field be pre-loaded with zero prior to executing
#     /// the CPUID, function 1. If the field remains equal to zero, then there
#     /// is no microcode update loaded. Another nonzero value will be the
#     /// signature.
#     ///
#     UINT32    MicrocodeUpdateSignature : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_BIOS_SIGN_ID_REGISTER;
class MSR_IA32_BIOS_SIGN_ID_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",                    UINT32, 32),
    ("MicrocodeUpdateSignature",    UINT32, 32)
  ]

class MSR_IA32_BIOS_SIGN_ID_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_BIOS_SIGN_ID_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   IA32_SGXLEPUBKEYHASH[(64*n+63):(64*n)] (R/W) Bits (64*n+63):(64*n) of the
#   SHA256 digest of the SIGSTRUCT.MODULUS for SGX Launch Enclave. On reset, the
#   default value is the digest of Intel's signing key. Read permitted If
#   CPUID.(EAX=12H,ECX=0H):EAX[0]=1, Write permitted if CPUID.(EAX=12H,ECX=0H):
#   EAX[0]=1 && IA32_FEATURE_CONTROL[17] = 1 && IA32_FEATURE_CONTROL[0] = 1.
# 
#   @param  ECX  MSR_IA32_SGXLEPUBKEYHASHn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_SGXLEPUBKEYHASHn);
#   AsmWriteMsr64 (MSR_IA32_SGXLEPUBKEYHASHn, Msr);
#   @endcode
#   @note MSR_IA32_SGXLEPUBKEYHASH0 is defined as IA32_SGXLEPUBKEYHASH0 in SDM.
#         MSR_IA32_SGXLEPUBKEYHASH1 is defined as IA32_SGXLEPUBKEYHASH1 in SDM.
#         MSR_IA32_SGXLEPUBKEYHASH2 is defined as IA32_SGXLEPUBKEYHASH2 in SDM.
#         MSR_IA32_SGXLEPUBKEYHASH3 is defined as IA32_SGXLEPUBKEYHASH3 in SDM.
#   @{
# **/
# #define MSR_IA32_SGXLEPUBKEYHASH0  0x0000008C
# #define MSR_IA32_SGXLEPUBKEYHASH1  0x0000008D
# #define MSR_IA32_SGXLEPUBKEYHASH2  0x0000008E
# #define MSR_IA32_SGXLEPUBKEYHASH3  0x0000008F
MSR_IA32_SGXLEPUBKEYHASH0       = 0x0000008C
MSR_IA32_SGXLEPUBKEYHASH1       = 0x0000008D
MSR_IA32_SGXLEPUBKEYHASH2       = 0x0000008E
MSR_IA32_SGXLEPUBKEYHASH3       = 0x0000008F

# /// @}
# 
# /**
#   SMM Monitor Configuration (R/W). If CPUID.01H: ECX[5]=1 or CPUID.01H: ECX[6] =
#   1.
# 
#   @param  ECX  MSR_IA32_SMM_MONITOR_CTL (0x0000009B)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_SMM_MONITOR_CTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_SMM_MONITOR_CTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_SMM_MONITOR_CTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_SMM_MONITOR_CTL);
#   AsmWriteMsr64 (MSR_IA32_SMM_MONITOR_CTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_SMM_MONITOR_CTL is defined as IA32_SMM_MONITOR_CTL in SDM.
# **/
# #define MSR_IA32_SMM_MONITOR_CTL  0x0000009B
MSR_IA32_SMM_MONITOR_CTL        = 0x0000009B

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_SMM_MONITOR_CTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Valid (R/W).  The STM may be invoked using VMCALL only if this
#     /// bit is 1. Because VMCALL is used to activate the dual-monitor treatment
#     /// (see Section 34.15.6), the dual-monitor treatment cannot be activated
#     /// if the bit is 0. This bit is cleared when the logical processor is
#     /// reset.
#     ///
#     UINT32    Valid     : 1;
#     UINT32    Reserved1 : 1;
#     ///
#     /// [Bit 2] Controls SMI unblocking by VMXOFF (see Section 34.14.4). If
#     /// IA32_VMX_MISC[28].
#     ///
#     UINT32    BlockSmi  : 1;
#     UINT32    Reserved2 : 9;
#     ///
#     /// [Bits 31:12] MSEG Base (R/W).
#     ///
#     UINT32    MsegBase  : 20;
#     UINT32    Reserved3 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_SMM_MONITOR_CTL_REGISTER;
class MSR_IA32_SMM_MONITOR_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Valid",       UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("BlockSmi",    UINT32, 1),
    ("Reserved2",   UINT32, 9),
    ("MsegBase",    UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_SMM_MONITOR_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMM_MONITOR_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MSEG header that is located at the physical address specified by the MsegBase
#   field of #MSR_IA32_SMM_MONITOR_CTL_REGISTER.
# **/
# typedef struct {
#   ///
#   /// Different processors may use different MSEG revision identifiers. These
#   /// identifiers enable software to avoid using an MSEG header formatted for
#   /// one processor on a processor that uses a different format. Software can
#   /// discover the MSEG revision identifier that a processor uses by reading
#   /// the VMX capability MSR IA32_VMX_MISC.
#   //
#   UINT32    MsegHeaderRevision;
#   ///
#   /// Bits 31:1 of this field are reserved and must be zero. Bit 0 of the field
#   /// is the IA-32e mode SMM feature bit. It indicates whether the logical
#   /// processor will be in IA-32e mode after the STM is activated.
#   ///
#   UINT32    MonitorFeatures;
#   UINT32    GdtrLimit;
#   UINT32    GdtrBaseOffset;
#   UINT32    CsSelector;
#   UINT32    EipOffset;
#   UINT32    EspOffset;
#   UINT32    Cr3Offset;
#   ///
#   /// Pad header so total size is 2KB
#   ///
#   UINT8     Reserved[SIZE_2KB - 8 * sizeof (UINT32)];
# } MSEG_HEADER;
class MSEG_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("MsegHeaderRevision",  UINT32),
    ("MonitorFeatures",     UINT32),
    ("GdtrLimit",           UINT32),
    ("GdtrBaseOffset",      UINT32),
    ("CsSelector",          UINT32),
    ("EipOffset",           UINT32),
    ("EspOffset",           UINT32),
    ("Cr3Offset",           UINT32),
    ("Reserved",            UINT8 * (SIZE_2KB - 8 * sizeof (UINT32)))
  ]

# 
# ///
# /// @{ Define values for the MonitorFeatures field of #MSEG_HEADER
# ///
# #define STM_FEATURES_IA32E  0x1
STM_FEATURES_IA32E  = 0x1

# ///
# /// @}
# ///
# 
# /**
#   Base address of the logical processor's SMRAM image (RO, SMM only). If
#   IA32_VMX_MISC[15].
# 
#   @param  ECX  MSR_IA32_SMBASE (0x0000009E)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_SMBASE);
#   @endcode
#   @note MSR_IA32_SMBASE is defined as IA32_SMBASE in SDM.
# **/
# #define MSR_IA32_SMBASE  0x0000009E
MSR_IA32_SMBASE                 = 0x0000009E

# 
# /**
#   General Performance Counters (R/W).
#   MSR_IA32_PMCn is supported if CPUID.0AH: EAX[15:8] > n.
# 
#   @param  ECX  MSR_IA32_PMCn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_PMC0);
#   AsmWriteMsr64 (MSR_IA32_PMC0, Msr);
#   @endcode
#   @note MSR_IA32_PMC0 is defined as IA32_PMC0 in SDM.
#         MSR_IA32_PMC1 is defined as IA32_PMC1 in SDM.
#         MSR_IA32_PMC2 is defined as IA32_PMC2 in SDM.
#         MSR_IA32_PMC3 is defined as IA32_PMC3 in SDM.
#         MSR_IA32_PMC4 is defined as IA32_PMC4 in SDM.
#         MSR_IA32_PMC5 is defined as IA32_PMC5 in SDM.
#         MSR_IA32_PMC6 is defined as IA32_PMC6 in SDM.
#         MSR_IA32_PMC7 is defined as IA32_PMC7 in SDM.
#   @{
# **/
# #define MSR_IA32_PMC0  0x000000C1
# #define MSR_IA32_PMC1  0x000000C2
# #define MSR_IA32_PMC2  0x000000C3
# #define MSR_IA32_PMC3  0x000000C4
# #define MSR_IA32_PMC4  0x000000C5
# #define MSR_IA32_PMC5  0x000000C6
# #define MSR_IA32_PMC6  0x000000C7
# #define MSR_IA32_PMC7  0x000000C8
MSR_IA32_PMC0  = 0x000000C1
MSR_IA32_PMC1  = 0x000000C2
MSR_IA32_PMC2  = 0x000000C3
MSR_IA32_PMC3  = 0x000000C4
MSR_IA32_PMC4  = 0x000000C5
MSR_IA32_PMC5  = 0x000000C6
MSR_IA32_PMC6  = 0x000000C7
MSR_IA32_PMC7  = 0x000000C8

# /// @}
# 
# /**
#   TSC Frequency Clock Counter (R/Write to clear). If CPUID.06H: ECX[0] = 1.
#   C0_MCNT: C0 TSC Frequency Clock Count Increments at fixed interval (relative
#   to TSC freq.) when the logical processor is in C0. Cleared upon overflow /
#   wrap-around of IA32_APERF.
# 
#   @param  ECX  MSR_IA32_MPERF (0x000000E7)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MPERF);
#   AsmWriteMsr64 (MSR_IA32_MPERF, Msr);
#   @endcode
#   @note MSR_IA32_MPERF is defined as IA32_MPERF in SDM.
# **/
# #define MSR_IA32_MPERF  0x000000E7
MSR_IA32_MPERF                  = 0x000000E7

# 
# /**
#   Actual Performance Clock Counter (R/Write to clear). If CPUID.06H: ECX[0] =
#   1. C0_ACNT: C0 Actual Frequency Clock Count Accumulates core clock counts at
#   the coordinated clock frequency, when the logical processor is in C0.
#   Cleared upon overflow / wrap-around of IA32_MPERF.
# 
#   @param  ECX  MSR_IA32_APERF (0x000000E8)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_APERF);
#   AsmWriteMsr64 (MSR_IA32_APERF, Msr);
#   @endcode
#   @note MSR_IA32_APERF is defined as IA32_APERF in SDM.
# **/
# #define MSR_IA32_APERF  0x000000E8
MSR_IA32_APERF                  = 0x000000E8

# 
# /**
#   MTRR Capability (RO) Section 11.11.2.1, "IA32_MTRR_DEF_TYPE MSR.".
#   Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_MTRRCAP (0x000000FE)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRRCAP_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRRCAP_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MTRRCAP_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MTRRCAP);
#   @endcode
#   @note MSR_IA32_MTRRCAP is defined as IA32_MTRRCAP in SDM.
# **/
# #define MSR_IA32_MTRRCAP  0x000000FE
MSR_IA32_MTRRCAP                = 0x000000FE

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MTRRCAP
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] VCNT: The number of variable memory type ranges in the
#     /// processor.
#     ///
#     UINT32    VCNT      : 8;
#     ///
#     /// [Bit 8] Fixed range MTRRs are supported when set.
#     ///
#     UINT32    FIX       : 1;
#     UINT32    Reserved1 : 1;
#     ///
#     /// [Bit 10] WC Supported when set.
#     ///
#     UINT32    WC        : 1;
#     ///
#     /// [Bit 11] SMRR Supported when set.
#     ///
#     UINT32    SMRR      : 1;
#     UINT32    Reserved2 : 20;
#     UINT32    Reserved3 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MTRRCAP_REGISTER;
class MSR_IA32_MTRRCAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VCNT",        UINT32, 8),
    ("FIX",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("WC",          UINT32, 1),
    ("SMRR",        UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_MTRRCAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRRCAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   SYSENTER_CS_MSR (R/W). Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_SYSENTER_CS (0x00000174)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_SYSENTER_CS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_SYSENTER_CS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_SYSENTER_CS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_SYSENTER_CS);
#   AsmWriteMsr64 (MSR_IA32_SYSENTER_CS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_SYSENTER_CS is defined as IA32_SYSENTER_CS in SDM.
# **/
# #define MSR_IA32_SYSENTER_CS  0x00000174
MSR_IA32_SYSENTER_CS            = 0x00000174

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_SYSENTER_CS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 15:0] CS Selector.
#     ///
#     UINT32    CS        : 16;
#     UINT32    Reserved1 : 16;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_SYSENTER_CS_REGISTER;
class MSR_IA32_SYSENTER_CS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CS",          UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SYSENTER_CS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SYSENTER_CS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   SYSENTER_ESP_MSR (R/W). Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_SYSENTER_ESP (0x00000175)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_SYSENTER_ESP);
#   AsmWriteMsr64 (MSR_IA32_SYSENTER_ESP, Msr);
#   @endcode
#   @note MSR_IA32_SYSENTER_ESP is defined as IA32_SYSENTER_ESP in SDM.
# **/
# #define MSR_IA32_SYSENTER_ESP  0x00000175
MSR_IA32_SYSENTER_ESP           = 0x00000175

# 
# /**
#   SYSENTER_EIP_MSR (R/W). Introduced at Display Family / Display Model 06_01H.
# 
#   @param  ECX  MSR_IA32_SYSENTER_EIP (0x00000176)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_SYSENTER_EIP);
#   AsmWriteMsr64 (MSR_IA32_SYSENTER_EIP, Msr);
#   @endcode
#   @note MSR_IA32_SYSENTER_EIP is defined as IA32_SYSENTER_EIP in SDM.
# **/
# #define MSR_IA32_SYSENTER_EIP  0x00000176
MSR_IA32_SYSENTER_EIP           = 0x00000176

# 
# /**
#   Global Machine Check Capability (RO). Introduced at Display Family / Display
#   Model 06_01H.
# 
#   @param  ECX  MSR_IA32_MCG_CAP (0x00000179)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_CAP_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_CAP_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MCG_CAP_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MCG_CAP);
#   @endcode
#   @note MSR_IA32_MCG_CAP is defined as IA32_MCG_CAP in SDM.
# **/
# #define MSR_IA32_MCG_CAP  0x00000179
MSR_IA32_MCG_CAP                = 0x00000179

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MCG_CAP
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Count: Number of reporting banks.
#     ///
#     UINT32    Count       : 8;
#     ///
#     /// [Bit 8] MCG_CTL_P: IA32_MCG_CTL is present if this bit is set.
#     ///
#     UINT32    MCG_CTL_P   : 1;
#     ///
#     /// [Bit 9] MCG_EXT_P: Extended machine check state registers are present
#     /// if this bit is set.
#     ///
#     UINT32    MCG_EXT_P   : 1;
#     ///
#     /// [Bit 10] MCP_CMCI_P: Support for corrected MC error event is present.
#     /// Introduced at Display Family / Display Model 06_01H.
#     ///
#     UINT32    MCP_CMCI_P  : 1;
#     ///
#     /// [Bit 11] MCG_TES_P: Threshold-based error status register are present
#     /// if this bit is set.
#     ///
#     UINT32    MCG_TES_P   : 1;
#     UINT32    Reserved1   : 4;
#     ///
#     /// [Bits 23:16] MCG_EXT_CNT: Number of extended machine check state
#     /// registers present.
#     ///
#     UINT32    MCG_EXT_CNT : 8;
#     ///
#     /// [Bit 24] MCG_SER_P: The processor supports software error recovery if
#     /// this bit is set.
#     ///
#     UINT32    MCG_SER_P   : 1;
#     UINT32    Reserved2   : 1;
#     ///
#     /// [Bit 26] MCG_ELOG_P: Indicates that the processor allows platform
#     /// firmware to be invoked when an error is detected so that it may
#     /// provide additional platform specific information in an ACPI format
#     /// "Generic Error Data Entry" that augments the data included in machine
#     /// check bank registers. Introduced at Display Family / Display Model
#     /// 06_3EH.
#     ///
#     UINT32    MCG_ELOG_P : 1;
#     ///
#     /// [Bit 27] MCG_LMCE_P: Indicates that the processor support extended
#     /// state in IA32_MCG_STATUS and associated MSR necessary to configure
#     /// Local Machine Check Exception (LMCE). Introduced at Display Family /
#     /// Display Model 06_3EH.
#     ///
#     UINT32    MCG_LMCE_P : 1;
#     UINT32    Reserved3  : 4;
#     UINT32    Reserved4  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MCG_CAP_REGISTER;
class MSR_IA32_MCG_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Count",       UINT32, 8),
    ("MCG_CTL_P",   UINT32, 1),
    ("MCG_EXT_P",   UINT32, 1),
    ("MCP_CMCI_P",  UINT32, 1),
    ("MCG_TES_P",   UINT32, 1),
    ("Reserved1",   UINT32, 4),
    ("MCG_EXT_CNT", UINT32, 8),
    ("MCG_SER_P",   UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("MCG_ELOG_P",  UINT32, 1),
    ("MCG_LMCE_P",  UINT32, 1),
    ("Reserved3",   UINT32, 4),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_IA32_MCG_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Machine Check Status (R/W0). Introduced at Display Family / Display
#   Model 06_01H.
# 
#   @param  ECX  MSR_IA32_MCG_STATUS (0x0000017A)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MCG_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MCG_STATUS);
#   AsmWriteMsr64 (MSR_IA32_MCG_STATUS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MCG_STATUS is defined as IA32_MCG_STATUS in SDM.
# **/
# #define MSR_IA32_MCG_STATUS  0x0000017A
MSR_IA32_MCG_STATUS             = 0x0000017A

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MCG_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] RIPV. Restart IP valid. Introduced at Display Family / Display
#     /// Model 06_01H.
#     ///
#     UINT32    RIPV      : 1;
#     ///
#     /// [Bit 1] EIPV. Error IP valid. Introduced at Display Family / Display
#     /// Model 06_01H.
#     ///
#     UINT32    EIPV      : 1;
#     ///
#     /// [Bit 2] MCIP. Machine check in progress. Introduced at Display Family
#     /// / Display Model 06_01H.
#     ///
#     UINT32    MCIP      : 1;
#     ///
#     /// [Bit 3] LMCE_S. If IA32_MCG_CAP.LMCE_P[2 7] =1.
#     ///
#     UINT32    LMCE_S    : 1;
#     UINT32    Reserved1 : 28;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MCG_STATUS_REGISTER;
class MSR_IA32_MCG_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("RIPV",        UINT32, 1),
    ("EIPV",        UINT32, 1),
    ("MCIP",        UINT32, 1),
    ("LMCE_S",      UINT32, 1),
    ("Reserved1",   UINT32, 28),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_MCG_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Machine Check Control (R/W). If IA32_MCG_CAP.CTL_P[8] =1.
# 
#   @param  ECX  MSR_IA32_MCG_CTL (0x0000017B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MCG_CTL);
#   AsmWriteMsr64 (MSR_IA32_MCG_CTL, Msr);
#   @endcode
#   @note MSR_IA32_MCG_CTL is defined as IA32_MCG_CTL in SDM.
# **/
# #define MSR_IA32_MCG_CTL  0x0000017B
MSR_IA32_MCG_CTL                = 0x0000017B

# 
# /**
#   Performance Event Select Register n (R/W). If CPUID.0AH: EAX[15:8] > n.
# 
#   @param  ECX  MSR_IA32_PERFEVTSELn
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERFEVTSEL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERFEVTSEL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERFEVTSEL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERFEVTSEL0);
#   AsmWriteMsr64 (MSR_IA32_PERFEVTSEL0, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERFEVTSEL0 is defined as IA32_PERFEVTSEL0 in SDM.
#         MSR_IA32_PERFEVTSEL1 is defined as IA32_PERFEVTSEL1 in SDM.
#         MSR_IA32_PERFEVTSEL2 is defined as IA32_PERFEVTSEL2 in SDM.
#         MSR_IA32_PERFEVTSEL3 is defined as IA32_PERFEVTSEL3 in SDM.
#   @{
# **/
# #define MSR_IA32_PERFEVTSEL0  0x00000186
# #define MSR_IA32_PERFEVTSEL1  0x00000187
# #define MSR_IA32_PERFEVTSEL2  0x00000188
# #define MSR_IA32_PERFEVTSEL3  0x00000189
MSR_IA32_PERFEVTSEL0  = 0x00000186
MSR_IA32_PERFEVTSEL1  = 0x00000187
MSR_IA32_PERFEVTSEL2  = 0x00000188
MSR_IA32_PERFEVTSEL3  = 0x00000189

# /// @}
# 
# /**
#   MSR information returned for MSR indexes #MSR_IA32_PERFEVTSEL0 to
#   #MSR_IA32_PERFEVTSEL3
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Event Select: Selects a performance event logic unit.
#     ///
#     UINT32    EventSelect : 8;
#     ///
#     /// [Bits 15:8] UMask: Qualifies the microarchitectural condition to
#     /// detect on the selected event logic.
#     ///
#     UINT32    UMASK       : 8;
#     ///
#     /// [Bit 16] USR: Counts while in privilege level is not ring 0.
#     ///
#     UINT32    USR         : 1;
#     ///
#     /// [Bit 17] OS: Counts while in privilege level is ring 0.
#     ///
#     UINT32    OS          : 1;
#     ///
#     /// [Bit 18] Edge: Enables edge detection if set.
#     ///
#     UINT32    E           : 1;
#     ///
#     /// [Bit 19] PC: enables pin control.
#     ///
#     UINT32    PC          : 1;
#     ///
#     /// [Bit 20] INT: enables interrupt on counter overflow.
#     ///
#     UINT32    INT         : 1;
#     ///
#     /// [Bit 21] AnyThread: When set to 1, it enables counting the associated
#     /// event conditions occurring across all logical processors sharing a
#     /// processor core. When set to 0, the counter only increments the
#     /// associated event conditions occurring in the logical processor which
#     /// programmed the MSR.
#     ///
#     UINT32    ANY         : 1;
#     ///
#     /// [Bit 22] EN: enables the corresponding performance counter to commence
#     /// counting when this bit is set.
#     ///
#     UINT32    EN          : 1;
#     ///
#     /// [Bit 23] INV: invert the CMASK.
#     ///
#     UINT32    INV         : 1;
#     ///
#     /// [Bits 31:24] CMASK: When CMASK is not zero, the corresponding
#     /// performance counter increments each cycle if the event count is
#     /// greater than or equal to the CMASK.
#     ///
#     UINT32    CMASK       : 8;
#     UINT32    Reserved    : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERFEVTSEL_REGISTER;
class MSR_IA32_PERFEVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventSelect", UINT32, 8),
    ("UMASK",       UINT32, 8),
    ("USR",         UINT32, 1),
    ("OS",          UINT32, 1),
    ("E",           UINT32, 1),
    ("PC",          UINT32, 1),
    ("INT",         UINT32, 1),
    ("ANY",         UINT32, 1),
    ("EN",          UINT32, 1),
    ("INV",         UINT32, 1),
    ("CMASK",       UINT32, 8),
    ("Reserved",    UINT32, 32)
  ]

class MSR_IA32_PERFEVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERFEVTSEL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Current performance state(P-State) operating point (RO). Introduced at
#   Display Family / Display Model 0F_03H.
# 
#   @param  ECX  MSR_IA32_PERF_STATUS (0x00000198)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_STATUS);
#   @endcode
#   @note MSR_IA32_PERF_STATUS is defined as IA32_PERF_STATUS in SDM.
# **/
# #define MSR_IA32_PERF_STATUS  0x00000198
# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 15:0] Current performance State Value.
#     ///
#     UINT32    State     : 16;
#     UINT32    Reserved1 : 16;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_STATUS_REGISTER;
class MSR_IA32_PERF_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("State",       UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_PERF_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   (R/W). Introduced at Display Family / Display Model 0F_03H.
# 
#   @param  ECX  MSR_IA32_PERF_CTL (0x00000199)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_CTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_CTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_CTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_CTL);
#   AsmWriteMsr64 (MSR_IA32_PERF_CTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_CTL is defined as IA32_PERF_CTL in SDM.
# **/
# #define MSR_IA32_PERF_CTL  0x00000199
MSR_IA32_PERF_CTL               = 0x00000199

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_CTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 15:0] Target performance State Value.
#     ///
#     UINT32    TargetState : 16;
#     UINT32    Reserved1   : 16;
#     ///
#     /// [Bit 32] IDA Engage. (R/W) When set to 1: disengages IDA. 06_0FH
#     /// (Mobile only).
#     ///
#     UINT32    IDA         : 1;
#     UINT32    Reserved2   : 31;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_CTL_REGISTER;
class MSR_IA32_PERF_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TargetState", UINT32, 16),
    ("Reserved1",   UINT32, 16),
    ("IDA",         UINT32, 1),
    ("Reserved2",   UINT32, 31)
  ]

class MSR_IA32_PERF_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_CTL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Clock Modulation Control (R/W) See Section 14.7.3, "Software Controlled
#   Clock Modulation.". If CPUID.01H:EDX[22] = 1.
# 
#   @param  ECX  MSR_IA32_CLOCK_MODULATION (0x0000019A)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_CLOCK_MODULATION_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_CLOCK_MODULATION_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_CLOCK_MODULATION_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_CLOCK_MODULATION);
#   AsmWriteMsr64 (MSR_IA32_CLOCK_MODULATION, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_CLOCK_MODULATION is defined as IA32_CLOCK_MODULATION in SDM.
# **/
# #define MSR_IA32_CLOCK_MODULATION  0x0000019A
MSR_IA32_CLOCK_MODULATION       = 0x0000019A

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_CLOCK_MODULATION
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Extended On-Demand Clock Modulation Duty Cycle:. If
#     /// CPUID.06H:EAX[5] = 1.
#     ///
#     UINT32    ExtendedOnDemandClockModulationDutyCycle : 1;
#     ///
#     /// [Bits 3:1] On-Demand Clock Modulation Duty Cycle: Specific encoded
#     /// values for target duty cycle modulation. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    OnDemandClockModulationDutyCycle         : 3;
#     ///
#     /// [Bit 4] On-Demand Clock Modulation Enable: Set 1 to enable modulation.
#     /// If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    OnDemandClockModulationEnable            : 1;
#     UINT32    Reserved1                                : 27;
#     UINT32    Reserved2                                : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_CLOCK_MODULATION_REGISTER;
class MSR_IA32_CLOCK_MODULATION_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ExtendedOnDemandClockModulationDutyCycle",    UINT32, 1),
    ("OnDemandClockModulationDutyCycle",            UINT32, 3),
    ("OnDemandClockModulationEnable",               UINT32, 1),
    ("Reserved1",                                   UINT32, 27),
    ("Reserved2",                                   UINT32, 32)
  ]

class MSR_IA32_CLOCK_MODULATION_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_CLOCK_MODULATION_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Thermal Interrupt Control (R/W) Enables and disables the generation of an
#   interrupt on temperature transitions detected with the processor's thermal
#   sensors and thermal monitor. See Section 14.7.2, "Thermal Monitor.".
#   If CPUID.01H:EDX[22] = 1
# 
#   @param  ECX  MSR_IA32_THERM_INTERRUPT (0x0000019B)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_THERM_INTERRUPT_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_THERM_INTERRUPT_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_THERM_INTERRUPT_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_THERM_INTERRUPT);
#   AsmWriteMsr64 (MSR_IA32_THERM_INTERRUPT, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_THERM_INTERRUPT is defined as IA32_THERM_INTERRUPT in SDM.
# **/
# #define MSR_IA32_THERM_INTERRUPT  0x0000019B
MSR_IA32_THERM_INTERRUPT        = 0x0000019B

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_THERM_INTERRUPT
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] High-Temperature Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    HighTempEnable               : 1;
#     ///
#     /// [Bit 1] Low-Temperature Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    LowTempEnable                : 1;
#     ///
#     /// [Bit 2] PROCHOT# Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    PROCHOT_Enable               : 1;
#     ///
#     /// [Bit 3] FORCEPR# Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    FORCEPR_Enable               : 1;
#     ///
#     /// [Bit 4] Critical Temperature Interrupt Enable.
#     /// If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    CriticalTempEnable           : 1;
#     UINT32    Reserved1                    : 3;
#     ///
#     /// [Bits 14:8] Threshold #1 Value. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    Threshold1                   : 7;
#     ///
#     /// [Bit 15] Threshold #1 Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    Threshold1Enable             : 1;
#     ///
#     /// [Bits 22:16] Threshold #2 Value. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    Threshold2                   : 7;
#     ///
#     /// [Bit 23] Threshold #2 Interrupt Enable. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    Threshold2Enable             : 1;
#     ///
#     /// [Bit 24] Power Limit Notification Enable. If CPUID.06H:EAX[4] = 1.
#     ///
#     UINT32    PowerLimitNotificationEnable : 1;
#     UINT32    Reserved2                    : 7;
#     UINT32    Reserved3                    : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_THERM_INTERRUPT_REGISTER;
class MSR_IA32_THERM_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighTempEnable",                  UINT32, 1),
    ("LowTempEnable",                   UINT32, 1),
    ("PROCHOT_Enable",                  UINT32, 1),
    ("FORCEPR_Enable",                  UINT32, 1),
    ("CriticalTempEnable",              UINT32, 1),
    ("Reserved1",                       UINT32, 3),
    ("Threshold1",                      UINT32, 7),
    ("Threshold1Enable",                UINT32, 1),
    ("Threshold2",                      UINT32, 7),
    ("Threshold2Enable",                UINT32, 1),
    ("PowerLimitNotificationEnable",    UINT32, 1),
    ("Reserved2",                       UINT32, 7),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_THERM_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_THERM_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Thermal Status Information (RO) Contains status information about the
#   processor's thermal sensor and automatic thermal monitoring facilities. See
#   Section 14.7.2, "Thermal Monitor". If CPUID.01H:EDX[22] = 1.
# 
#   @param  ECX  MSR_IA32_THERM_STATUS (0x0000019C)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_THERM_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_THERM_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_THERM_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_THERM_STATUS);
#   @endcode
#   @note MSR_IA32_THERM_STATUS is defined as IA32_THERM_STATUS in SDM.
# **/
# #define MSR_IA32_THERM_STATUS  0x0000019C
MSR_IA32_THERM_STATUS           = 0x0000019C

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_THERM_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Thermal Status (RO):. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    ThermalStatus              : 1;
#     ///
#     /// [Bit 1] Thermal Status Log (R/W):. If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    ThermalStatusLog           : 1;
#     ///
#     /// [Bit 2] PROCHOT # or FORCEPR# event (RO). If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    PROCHOT_FORCEPR_Event      : 1;
#     ///
#     /// [Bit 3] PROCHOT # or FORCEPR# log (R/WC0). If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    PROCHOT_FORCEPR_Log        : 1;
#     ///
#     /// [Bit 4] Critical Temperature Status (RO). If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    CriticalTempStatus         : 1;
#     ///
#     /// [Bit 5] Critical Temperature Status log (R/WC0).
#     /// If CPUID.01H:EDX[22] = 1.
#     ///
#     UINT32    CriticalTempStatusLog      : 1;
#     ///
#     /// [Bit 6] Thermal Threshold #1 Status (RO). If CPUID.01H:ECX[8] = 1.
#     ///
#     UINT32    ThermalThreshold1Status    : 1;
#     ///
#     /// [Bit 7] Thermal Threshold #1 log (R/WC0). If CPUID.01H:ECX[8] = 1.
#     ///
#     UINT32    ThermalThreshold1Log       : 1;
#     ///
#     /// [Bit 8] Thermal Threshold #2 Status (RO). If CPUID.01H:ECX[8] = 1.
#     ///
#     UINT32    ThermalThreshold2Status    : 1;
#     ///
#     /// [Bit 9] Thermal Threshold #2 log (R/WC0). If CPUID.01H:ECX[8] = 1.
#     ///
#     UINT32    ThermalThreshold2Log       : 1;
#     ///
#     /// [Bit 10] Power Limitation Status (RO). If CPUID.06H:EAX[4] = 1.
#     ///
#     UINT32    PowerLimitStatus           : 1;
#     ///
#     /// [Bit 11] Power Limitation log (R/WC0). If CPUID.06H:EAX[4] = 1.
#     ///
#     UINT32    PowerLimitLog              : 1;
#     ///
#     /// [Bit 12] Current Limit Status (RO). If CPUID.06H:EAX[7] = 1.
#     ///
#     UINT32    CurrentLimitStatus         : 1;
#     ///
#     /// [Bit 13] Current Limit log (R/WC0). If CPUID.06H:EAX[7] = 1.
#     ///
#     UINT32    CurrentLimitLog            : 1;
#     ///
#     /// [Bit 14] Cross Domain Limit Status (RO). If CPUID.06H:EAX[7] = 1.
#     ///
#     UINT32    CrossDomainLimitStatus     : 1;
#     ///
#     /// [Bit 15] Cross Domain Limit log (R/WC0). If CPUID.06H:EAX[7] = 1.
#     ///
#     UINT32    CrossDomainLimitLog        : 1;
#     ///
#     /// [Bits 22:16] Digital Readout (RO). If CPUID.06H:EAX[0] = 1.
#     ///
#     UINT32    DigitalReadout             : 7;
#     UINT32    Reserved1                  : 4;
#     ///
#     /// [Bits 30:27] Resolution in Degrees Celsius (RO). If CPUID.06H:EAX[0] =
#     /// 1.
#     ///
#     UINT32    ResolutionInDegreesCelsius : 4;
#     ///
#     /// [Bit 31] Reading Valid (RO). If CPUID.06H:EAX[0] = 1.
#     ///
#     UINT32    ReadingValid               : 1;
#     UINT32    Reserved2                  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_THERM_STATUS_REGISTER;
class MSR_IA32_THERM_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalStatus",               UINT32, 1),
    ("ThermalStatusLog",            UINT32, 1),
    ("PROCHOT_FORCEPR_Event",       UINT32, 1),
    ("PROCHOT_FORCEPR_Log",         UINT32, 1),
    ("CriticalTempStatus",          UINT32, 1),
    ("CriticalTempStatusLog",       UINT32, 1),
    ("ThermalThreshold1Status",     UINT32, 1),
    ("ThermalThreshold1Log",        UINT32, 1),
    ("ThermalThreshold2Status",     UINT32, 1),
    ("ThermalThreshold2Log",        UINT32, 1),
    ("PowerLimitStatus",            UINT32, 1),
    ("PowerLimitLog",               UINT32, 1),
    ("CurrentLimitStatus",          UINT32, 1),
    ("CurrentLimitLog",             UINT32, 1),
    ("CrossDomainLimitStatus",      UINT32, 1),
    ("CrossDomainLimitLog",         UINT32, 1),
    ("DigitalReadout",              UINT32, 7),
    ("Reserved1",                   UINT32, 4),
    ("ResolutionInDegreesCelsius",  UINT32, 4),
    ("ReadingValid",                UINT32, 1),
    ("Reserved2",                   UINT32, 32)
  ]

class MSR_IA32_THERM_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_THERM_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Enable Misc. Processor Features (R/W)  Allows a variety of processor
#   functions to be enabled and disabled.
# 
#   @param  ECX  MSR_IA32_MISC_ENABLE (0x000001A0)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MISC_ENABLE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MISC_ENABLE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MISC_ENABLE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MISC_ENABLE);
#   AsmWriteMsr64 (MSR_IA32_MISC_ENABLE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MISC_ENABLE is defined as IA32_MISC_ENABLE in SDM.
# **/
# #define MSR_IA32_MISC_ENABLE  0x000001A0
MSR_IA32_MISC_ENABLE            = 0x000001A0

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MISC_ENABLE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Fast-Strings Enable When set, the fast-strings feature (for
#     /// REP MOVS and REP STORS) is enabled (default); when clear, fast-strings
#     /// are disabled. Introduced at Display Family / Display Model 0F_0H.
#     ///
#     UINT32    FastStrings : 1;
#     UINT32    Reserved1   : 2;
#     ///
#     /// [Bit 3] Automatic Thermal Control Circuit Enable (R/W)  1 = Setting
#     /// this bit enables the thermal control circuit (TCC) portion of the
#     /// Intel Thermal Monitor feature. This allows the processor to
#     /// automatically reduce power consumption in response to TCC activation.
#     /// 0 = Disabled. Note: In some products clearing this bit might be
#     /// ignored in critical thermal conditions, and TM1, TM2 and adaptive
#     /// thermal throttling will still be activated. The default value of this
#     /// field varies with product. See respective tables where default value is
#     /// listed. Introduced at Display Family / Display Model 0F_0H.
#     ///
#     UINT32    AutomaticThermalControlCircuit : 1;
#     UINT32    Reserved2                      : 3;
#     ///
#     /// [Bit 7] Performance Monitoring Available (R)  1 = Performance
#     /// monitoring enabled 0 = Performance monitoring disabled. Introduced at
#     /// Display Family / Display Model 0F_0H.
#     ///
#     UINT32    PerformanceMonitoring          : 1;
#     UINT32    Reserved3                      : 3;
#     ///
#     /// [Bit 11] Branch Trace Storage Unavailable (RO) 1 = Processor doesn't
#     /// support branch trace storage (BTS) 0 = BTS is supported. Introduced at
#     /// Display Family / Display Model 0F_0H.
#     ///
#     UINT32    BTS                            : 1;
#     ///
#     /// [Bit 12] Processor Event Based Sampling (PEBS)  Unavailable (RO)  1 =
#     /// PEBS is not supported; 0 = PEBS is supported. Introduced at Display
#     /// Family / Display Model 06_0FH.
#     ///
#     UINT32    PEBS                           : 1;
#     UINT32    Reserved4                      : 3;
#     ///
#     /// [Bit 16] Enhanced Intel SpeedStep Technology  Enable (R/W) 0= Enhanced
#     /// Intel SpeedStep Technology disabled 1 = Enhanced Intel SpeedStep
#     /// Technology enabled. If CPUID.01H: ECX[7] =1.
#     ///
#     UINT32    EIST                           : 1;
#     UINT32    Reserved5                      : 1;
#     ///
#     /// [Bit 18] ENABLE MONITOR FSM (R/W) When this bit is set to 0, the
#     /// MONITOR feature flag is not set (CPUID.01H:ECX[bit 3] = 0). This
#     /// indicates that MONITOR/MWAIT are not supported. Software attempts to
#     /// execute MONITOR/MWAIT will cause #UD when this bit is 0. When this bit
#     /// is set to 1 (default), MONITOR/MWAIT are supported (CPUID.01H:ECX[bit
#     /// 3] = 1). If the SSE3 feature flag ECX[0] is not set (CPUID.01H:ECX[bit
#     /// 0] = 0), the OS must not attempt to alter this bit. BIOS must leave it
#     /// in the default state. Writing this bit when the SSE3 feature flag is
#     /// set to 0 may generate a #GP exception. Introduced at Display Family /
#     /// Display Model 0F_03H.
#     ///
#     UINT32    MONITOR   : 1;
#     UINT32    Reserved6 : 3;
#     ///
#     /// [Bit 22] Limit CPUID Maxval (R/W) When this bit is set to 1, CPUID.00H
#     /// returns a maximum value in EAX[7:0] of 2. BIOS should contain a setup
#     /// question that allows users to specify when the installed OS does not
#     /// support CPUID functions greater than 2. Before setting this bit, BIOS
#     /// must execute the CPUID.0H and examine the maximum value returned in
#     /// EAX[7:0]. If the maximum value is greater than 2, this bit is
#     /// supported. Otherwise, this bit is not supported. Setting this bit when
#     /// the maximum value is not greater than 2 may generate a #GP exception.
#     /// Setting this bit may cause unexpected behavior in software that
#     /// depends on the availability of CPUID leaves greater than 2. Introduced
#     /// at Display Family / Display Model 0F_03H.
#     ///
#     UINT32    LimitCpuidMaxval     : 1;
#     ///
#     /// [Bit 23] xTPR Message Disable (R/W) When set to 1, xTPR messages are
#     /// disabled. xTPR messages are optional messages that allow the processor
#     /// to inform the chipset of its priority. if CPUID.01H:ECX[14] = 1.
#     ///
#     UINT32    xTPR_Message_Disable : 1;
#     UINT32    Reserved7            : 8;
#     UINT32    Reserved8            : 2;
#     ///
#     /// [Bit 34] XD Bit Disable (R/W) When set to 1, the Execute Disable Bit
#     /// feature (XD Bit) is disabled and the XD Bit extended feature flag will
#     /// be clear (CPUID.80000001H: EDX[20]=0). When set to a 0 (default), the
#     /// Execute Disable Bit feature (if available) allows the OS to enable PAE
#     /// paging and take advantage of data only pages. BIOS must not alter the
#     /// contents of this bit location, if XD bit is not supported. Writing
#     /// this bit to 1 when the XD Bit extended feature flag is set to 0 may
#     /// generate a #GP exception. if CPUID.80000001H:EDX[2 0] = 1.
#     ///
#     UINT32    XD        : 1;
#     UINT32    Reserved9 : 29;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MISC_ENABLE_REGISTER;
class MSR_IA32_MISC_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FastStrings",                     UINT32, 1),
    ("Reserved1",                       UINT32, 2),
    ("AutomaticThermalControlCircuit",  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("PerformanceMonitoring",           UINT32, 1),
    ("Reserved3",                       UINT32, 3),
    ("BTS",                             UINT32, 1),
    ("PEBS",                            UINT32, 1),
    ("Reserved4",                       UINT32, 3),
    ("EIST",                            UINT32, 1),
    ("Reserved5",                       UINT32, 1),
    ("MONITOR",                         UINT32, 1),
    ("Reserved6",                       UINT32, 3),
    ("LimitCpuidMaxval",                UINT32, 1),
    ("xTPR_Message_Disable",            UINT32, 1),
    ("Reserved7",                       UINT32, 8),
    ("Reserved8",                       UINT32, 2),
    ("XD",                              UINT32, 1),
    ("Reserved9",                       UINT32, 29)
  ]

class MSR_IA32_MISC_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MISC_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Performance Energy Bias Hint (R/W). if CPUID.6H:ECX[3] = 1.
# 
#   @param  ECX  MSR_IA32_ENERGY_PERF_BIAS (0x000001B0)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_ENERGY_PERF_BIAS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_ENERGY_PERF_BIAS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_ENERGY_PERF_BIAS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_ENERGY_PERF_BIAS);
#   AsmWriteMsr64 (MSR_IA32_ENERGY_PERF_BIAS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_ENERGY_PERF_BIAS is defined as IA32_ENERGY_PERF_BIAS in SDM.
# **/
# #define MSR_IA32_ENERGY_PERF_BIAS  0x000001B0
MSR_IA32_ENERGY_PERF_BIAS       = 0x000001B0

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_ENERGY_PERF_BIAS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 3:0] Power Policy Preference: 0 indicates preference to highest
#     /// performance. 15 indicates preference to maximize energy saving.
#     ///
#     UINT32    PowerPolicyPreference : 4;
#     UINT32    Reserved1             : 28;
#     UINT32    Reserved2             : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_ENERGY_PERF_BIAS_REGISTER;
class MSR_IA32_ENERGY_PERF_BIAS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PowerPolicyPreference",   UINT32, 4),
    ("Reserved1",               UINT32, 28),
    ("Reserved2",               UINT32, 32)
  ]

class MSR_IA32_ENERGY_PERF_BIAS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_ENERGY_PERF_BIAS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Package Thermal Status Information (RO) Contains status information about
#   the package's thermal sensor. See Section 14.8, "Package Level Thermal
#   Management.". If CPUID.06H: EAX[6] = 1.
# 
#   @param  ECX  MSR_IA32_PACKAGE_THERM_STATUS (0x000001B1)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PACKAGE_THERM_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PACKAGE_THERM_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PACKAGE_THERM_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PACKAGE_THERM_STATUS);
#   @endcode
#   @note MSR_IA32_PACKAGE_THERM_STATUS is defined as IA32_PACKAGE_THERM_STATUS in SDM.
# **/
# #define MSR_IA32_PACKAGE_THERM_STATUS  0x000001B1
MSR_IA32_PACKAGE_THERM_STATUS  = 0x000001B1

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PACKAGE_THERM_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Pkg Thermal Status (RO):.
#     ///
#     UINT32    ThermalStatus           : 1;
#     ///
#     /// [Bit 1] Pkg Thermal Status Log (R/W):.
#     ///
#     UINT32    ThermalStatusLog        : 1;
#     ///
#     /// [Bit 2] Pkg PROCHOT # event (RO).
#     ///
#     UINT32    PROCHOT_Event           : 1;
#     ///
#     /// [Bit 3] Pkg PROCHOT # log (R/WC0).
#     ///
#     UINT32    PROCHOT_Log             : 1;
#     ///
#     /// [Bit 4] Pkg Critical Temperature Status (RO).
#     ///
#     UINT32    CriticalTempStatus      : 1;
#     ///
#     /// [Bit 5] Pkg Critical Temperature Status log (R/WC0).
#     ///
#     UINT32    CriticalTempStatusLog   : 1;
#     ///
#     /// [Bit 6] Pkg Thermal Threshold #1 Status (RO).
#     ///
#     UINT32    ThermalThreshold1Status : 1;
#     ///
#     /// [Bit 7] Pkg Thermal Threshold #1 log (R/WC0).
#     ///
#     UINT32    ThermalThreshold1Log    : 1;
#     ///
#     /// [Bit 8] Pkg Thermal Threshold #2 Status (RO).
#     ///
#     UINT32    ThermalThreshold2Status : 1;
#     ///
#     /// [Bit 9] Pkg Thermal Threshold #1 log (R/WC0).
#     ///
#     UINT32    ThermalThreshold2Log    : 1;
#     ///
#     /// [Bit 10] Pkg Power Limitation Status (RO).
#     ///
#     UINT32    PowerLimitStatus        : 1;
#     ///
#     /// [Bit 11] Pkg Power Limitation log (R/WC0).
#     ///
#     UINT32    PowerLimitLog           : 1;
#     UINT32    Reserved1               : 4;
#     ///
#     /// [Bits 22:16] Pkg Digital Readout (RO).
#     ///
#     UINT32    DigitalReadout          : 7;
#     UINT32    Reserved2               : 9;
#     UINT32    Reserved3               : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PACKAGE_THERM_STATUS_REGISTER;
class MSR_IA32_PACKAGE_THERM_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ThermalStatus",           UINT32, 1),
    ("ThermalStatusLog",        UINT32, 1),
    ("PROCHOT_Event",           UINT32, 1),
    ("PROCHOT_Log",             UINT32, 1),
    ("CriticalTempStatus",      UINT32, 1),
    ("CriticalTempStatusLog",   UINT32, 1),
    ("ThermalThreshold1Status", UINT32, 1),
    ("ThermalThreshold1Log",    UINT32, 1),
    ("ThermalThreshold2Status", UINT32, 1),
    ("ThermalThreshold2Log",    UINT32, 1),
    ("PowerLimitStatus",        UINT32, 1),
    ("PowerLimitLog",           UINT32, 1),
    ("Reserved1",               UINT32, 4),
    ("DigitalReadout",          UINT32, 7),
    ("Reserved2",               UINT32, 9),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_IA32_PACKAGE_THERM_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PACKAGE_THERM_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Pkg Thermal Interrupt Control (R/W) Enables and disables the generation of
#   an interrupt on temperature transitions detected with the package's thermal
#   sensor. See Section 14.8, "Package Level Thermal Management.". If CPUID.06H:
#   EAX[6] = 1.
# 
#   @param  ECX  MSR_IA32_PACKAGE_THERM_INTERRUPT (0x000001B2)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PACKAGE_THERM_INTERRUPT);
#   AsmWriteMsr64 (MSR_IA32_PACKAGE_THERM_INTERRUPT, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PACKAGE_THERM_INTERRUPT is defined as IA32_PACKAGE_THERM_INTERRUPT in SDM.
# **/
# #define MSR_IA32_PACKAGE_THERM_INTERRUPT  0x000001B2
MSR_IA32_PACKAGE_THERM_INTERRUPT  = 0x000001B2

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PACKAGE_THERM_INTERRUPT
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Pkg High-Temperature Interrupt Enable.
#     ///
#     UINT32    HighTempEnable               : 1;
#     ///
#     /// [Bit 1] Pkg Low-Temperature Interrupt Enable.
#     ///
#     UINT32    LowTempEnable                : 1;
#     ///
#     /// [Bit 2] Pkg PROCHOT# Interrupt Enable.
#     ///
#     UINT32    PROCHOT_Enable               : 1;
#     UINT32    Reserved1                    : 1;
#     ///
#     /// [Bit 4] Pkg Overheat Interrupt Enable.
#     ///
#     UINT32    OverheatEnable               : 1;
#     UINT32    Reserved2                    : 3;
#     ///
#     /// [Bits 14:8] Pkg Threshold #1 Value.
#     ///
#     UINT32    Threshold1                   : 7;
#     ///
#     /// [Bit 15] Pkg Threshold #1 Interrupt Enable.
#     ///
#     UINT32    Threshold1Enable             : 1;
#     ///
#     /// [Bits 22:16] Pkg Threshold #2 Value.
#     ///
#     UINT32    Threshold2                   : 7;
#     ///
#     /// [Bit 23] Pkg Threshold #2 Interrupt Enable.
#     ///
#     UINT32    Threshold2Enable             : 1;
#     ///
#     /// [Bit 24] Pkg Power Limit Notification Enable.
#     ///
#     UINT32    PowerLimitNotificationEnable : 1;
#     UINT32    Reserved3                    : 7;
#     UINT32    Reserved4                    : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER;
class MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HighTempEnable",                  UINT32, 1),
    ("LowTempEnable",                   UINT32, 1),
    ("PROCHOT_Enable",                  UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("OverheatEnable",                  UINT32, 1),
    ("Reserved2",                       UINT32, 3),
    ("Threshold1",                      UINT32, 7),
    ("Threshold1Enable",                UINT32, 1),
    ("Threshold2",                      UINT32, 7),
    ("Threshold2Enable",                UINT32, 1),
    ("PowerLimitNotificationEnable",    UINT32, 1),
    ("Reserved3",                       UINT32, 7),
    ("Reserved4",                       UINT32, 32)
  ]

class MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PACKAGE_THERM_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Trace/Profile Resource Control (R/W). Introduced at Display Family / Display
#   Model 06_0EH.
# 
#   @param  ECX  MSR_IA32_DEBUGCTL (0x000001D9)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_DEBUGCTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_DEBUGCTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_DEBUGCTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_DEBUGCTL);
#   AsmWriteMsr64 (MSR_IA32_DEBUGCTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_DEBUGCTL is defined as IA32_DEBUGCTL in SDM.
# **/
# #define MSR_IA32_DEBUGCTL  0x000001D9
MSR_IA32_DEBUGCTL               = 0x000001D9

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_DEBUGCTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] LBR: Setting this bit to 1 enables the processor to record a
#     /// running trace of the most recent branches taken by the processor in
#     /// the LBR stack. Introduced at Display Family / Display Model 06_01H.
#     ///
#     UINT32    LBR                   : 1;
#     ///
#     /// [Bit 1] BTF: Setting this bit to 1 enables the processor to treat
#     /// EFLAGS.TF as single-step on branches instead of single-step on
#     /// instructions. Introduced at Display Family / Display Model 06_01H.
#     ///
#     UINT32    BTF                   : 1;
#     UINT32    Reserved1             : 4;
#     ///
#     /// [Bit 6] TR: Setting this bit to 1 enables branch trace messages to be
#     /// sent. Introduced at Display Family / Display Model 06_0EH.
#     ///
#     UINT32    TR                    : 1;
#     ///
#     /// [Bit 7] BTS: Setting this bit enables branch trace messages (BTMs) to
#     /// be logged in a BTS buffer. Introduced at Display Family / Display
#     /// Model 06_0EH.
#     ///
#     UINT32    BTS                   : 1;
#     ///
#     /// [Bit 8] BTINT: When clear, BTMs are logged in a BTS buffer in circular
#     /// fashion. When this bit is set, an interrupt is generated by the BTS
#     /// facility when the BTS buffer is full. Introduced at Display Family /
#     /// Display Model 06_0EH.
#     ///
#     UINT32    BTINT                 : 1;
#     ///
#     /// [Bit 9] BTS_OFF_OS: When set, BTS or BTM is skipped if CPL = 0.
#     /// Introduced at Display Family / Display Model 06_0FH.
#     ///
#     UINT32    BTS_OFF_OS            : 1;
#     ///
#     /// [Bit 10] BTS_OFF_USR: When set, BTS or BTM is skipped if CPL > 0.
#     /// Introduced at Display Family / Display Model 06_0FH.
#     ///
#     UINT32    BTS_OFF_USR           : 1;
#     ///
#     /// [Bit 11] FREEZE_LBRS_ON_PMI: When set, the LBR stack is frozen on a
#     /// PMI request. If CPUID.01H: ECX[15] = 1 && CPUID.0AH: EAX[7:0] > 1.
#     ///
#     UINT32    FREEZE_LBRS_ON_PMI    : 1;
#     ///
#     /// [Bit 12] FREEZE_PERFMON_ON_PMI: When set, each ENABLE bit of the
#     /// global counter control MSR are frozen (address 38FH) on a PMI request.
#     /// If CPUID.01H: ECX[15] = 1 && CPUID.0AH: EAX[7:0] > 1.
#     ///
#     UINT32    FREEZE_PERFMON_ON_PMI : 1;
#     ///
#     /// [Bit 13] ENABLE_UNCORE_PMI: When set, enables the logical processor to
#     /// receive and generate PMI on behalf of the uncore. Introduced at
#     /// Display Family / Display Model 06_1AH.
#     ///
#     UINT32    ENABLE_UNCORE_PMI     : 1;
#     ///
#     /// [Bit 14] FREEZE_WHILE_SMM: When set, freezes perfmon and trace
#     /// messages while in SMM. If IA32_PERF_CAPABILITIES[ 12] = 1.
#     ///
#     UINT32    FREEZE_WHILE_SMM      : 1;
#     ///
#     /// [Bit 15] RTM_DEBUG: When set, enables DR7 debug bit on XBEGIN. If
#     /// (CPUID.(EAX=07H, ECX=0):EBX[11] = 1).
#     ///
#     UINT32    RTM_DEBUG             : 1;
#     UINT32    Reserved2             : 16;
#     UINT32    Reserved3             : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_DEBUGCTL_REGISTER;
class MSR_IA32_DEBUGCTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR",                     UINT32, 1),
    ("BTF",                     UINT32, 1),
    ("Reserved1",               UINT32, 4),
    ("TR",                      UINT32, 1),
    ("BTS",                     UINT32, 1),
    ("BTINT",                   UINT32, 1),
    ("BTS_OFF_OS",              UINT32, 1),
    ("BTS_OFF_USR",             UINT32, 1),
    ("FREEZE_LBRS_ON_PMI",      UINT32, 1),
    ("FREEZE_PERFMON_ON_PMI",   UINT32, 1),
    ("ENABLE_UNCORE_PMI",       UINT32, 1),
    ("FREEZE_WHILE_SMM",        UINT32, 1),
    ("RTM_DEBUG",               UINT32, 1),
    ("Reserved2",               UINT32, 16),
    ("Reserved3",               UINT32, 32)
  ]

class MSR_IA32_DEBUGCTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DEBUGCTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   SMRR Base Address (Writeable only in SMM)  Base address of SMM memory range.
#   If IA32_MTRRCAP.SMRR[11] = 1.
# 
#   @param  ECX  MSR_IA32_SMRR_PHYSBASE (0x000001F2)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_SMRR_PHYSBASE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_SMRR_PHYSBASE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_SMRR_PHYSBASE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_SMRR_PHYSBASE);
#   AsmWriteMsr64 (MSR_IA32_SMRR_PHYSBASE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_SMRR_PHYSBASE is defined as IA32_SMRR_PHYSBASE in SDM.
# **/
# #define MSR_IA32_SMRR_PHYSBASE  0x000001F2
MSR_IA32_SMRR_PHYSBASE          = 0x000001F2

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_SMRR_PHYSBASE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Type. Specifies memory type of the range.
#     ///
#     UINT32    Type      : 8;
#     UINT32    Reserved1 : 4;
#     ///
#     /// [Bits 31:12] PhysBase.  SMRR physical Base Address.
#     ///
#     UINT32    PhysBase  : 20;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_SMRR_PHYSBASE_REGISTER;
class MSR_IA32_SMRR_PHYSBASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 8),
    ("Reserved1",   UINT32, 4),
    ("PhysBase",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SMRR_PHYSBASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMRR_PHYSBASE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   SMRR Range Mask (Writeable only in SMM) Range Mask of SMM memory range. If
#   IA32_MTRRCAP[SMRR] = 1.
# 
#   @param  ECX  MSR_IA32_SMRR_PHYSMASK (0x000001F3)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_SMRR_PHYSMASK_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_SMRR_PHYSMASK_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_SMRR_PHYSMASK_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_SMRR_PHYSMASK);
#   AsmWriteMsr64 (MSR_IA32_SMRR_PHYSMASK, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_SMRR_PHYSMASK is defined as IA32_SMRR_PHYSMASK in SDM.
# **/
# #define MSR_IA32_SMRR_PHYSMASK  0x000001F3
MSR_IA32_SMRR_PHYSMASK          = 0x000001F3

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_SMRR_PHYSMASK
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved1 : 11;
#     ///
#     /// [Bit 11] Valid Enable range mask.
#     ///
#     UINT32    Valid     : 1;
#     ///
#     /// [Bits 31:12] PhysMask SMRR address range mask.
#     ///
#     UINT32    PhysMask  : 20;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_SMRR_PHYSMASK_REGISTER;
class MSR_IA32_SMRR_PHYSMASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("Valid",       UINT32, 1),
    ("PhysMask",    UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_SMRR_PHYSMASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SMRR_PHYSMASK_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   DCA Capability (R). If CPUID.01H: ECX[18] = 1.
# 
#   @param  ECX  MSR_IA32_PLATFORM_DCA_CAP (0x000001F8)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_PLATFORM_DCA_CAP);
#   @endcode
#   @note MSR_IA32_PLATFORM_DCA_CAP is defined as IA32_PLATFORM_DCA_CAP in SDM.
# **/
# #define MSR_IA32_PLATFORM_DCA_CAP  0x000001F8
MSR_IA32_PLATFORM_DCA_CAP       = 0x000001F8

# 
# /**
#   If set, CPU supports Prefetch-Hint type. If CPUID.01H: ECX[18] = 1.
# 
#   @param  ECX  MSR_IA32_CPU_DCA_CAP (0x000001F9)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_CPU_DCA_CAP);
#   AsmWriteMsr64 (MSR_IA32_CPU_DCA_CAP, Msr);
#   @endcode
#   @note MSR_IA32_CPU_DCA_CAP is defined as IA32_CPU_DCA_CAP in SDM.
# **/
# #define MSR_IA32_CPU_DCA_CAP  0x000001F9
MSR_IA32_CPU_DCA_CAP            = 0x000001F9

# 
# /**
#   DCA type 0 Status and Control register. If CPUID.01H: ECX[18] = 1.
# 
#   @param  ECX  MSR_IA32_DCA_0_CAP (0x000001FA)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_DCA_0_CAP_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_DCA_0_CAP_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_DCA_0_CAP_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_DCA_0_CAP);
#   AsmWriteMsr64 (MSR_IA32_DCA_0_CAP, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_DCA_0_CAP is defined as IA32_DCA_0_CAP in SDM.
# **/
# #define MSR_IA32_DCA_0_CAP  0x000001FA
MSR_IA32_DCA_0_CAP              = 0x000001FA

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_DCA_0_CAP
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] DCA_ACTIVE: Set by HW when DCA is fuseenabled and no
#     /// defeatures are set.
#     ///
#     UINT32    DCA_ACTIVE     : 1;
#     ///
#     /// [Bits 2:1] TRANSACTION.
#     ///
#     UINT32    TRANSACTION    : 2;
#     ///
#     /// [Bits 6:3] DCA_TYPE.
#     ///
#     UINT32    DCA_TYPE       : 4;
#     ///
#     /// [Bits 10:7] DCA_QUEUE_SIZE.
#     ///
#     UINT32    DCA_QUEUE_SIZE : 4;
#     UINT32    Reserved1      : 2;
#     ///
#     /// [Bits 16:13] DCA_DELAY: Writes will update the register but have no HW
#     /// side-effect.
#     ///
#     UINT32    DCA_DELAY      : 4;
#     UINT32    Reserved2      : 7;
#     ///
#     /// [Bit 24] SW_BLOCK: SW can request DCA block by setting this bit.
#     ///
#     UINT32    SW_BLOCK       : 1;
#     UINT32    Reserved3      : 1;
#     ///
#     /// [Bit 26] HW_BLOCK: Set when DCA is blocked by HW (e.g. CR0.CD = 1).
#     ///
#     UINT32    HW_BLOCK       : 1;
#     UINT32    Reserved4      : 5;
#     UINT32    Reserved5      : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_DCA_0_CAP_REGISTER;
class MSR_IA32_DCA_0_CAP_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("DCA_ACTIVE",      UINT32, 1),
    ("TRANSACTION",     UINT32, 2),
    ("DCA_TYPE",        UINT32, 4),
    ("DCA_QUEUE_SIZE",  UINT32, 4),
    ("Reserved1",       UINT32, 2),
    ("DCA_DELAY",       UINT32, 4),
    ("Reserved2",       UINT32, 7),
    ("SW_BLOCK",        UINT32, 1),
    ("Reserved3",       UINT32, 1),
    ("HW_BLOCK",        UINT32, 1),
    ("Reserved4",       UINT32, 5),
    ("Reserved5",       UINT32, 32)
  ]

class MSR_IA32_DCA_0_CAP_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DCA_0_CAP_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MTRRphysBasen.  See Section 11.11.2.3, "Variable Range MTRRs".
#   If CPUID.01H: EDX.MTRR[12] = 1 and IA32_MTRRCAP[7:0] > n.
# 
#   @param  ECX  MSR_IA32_MTRR_PHYSBASEn
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_PHYSBASE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_PHYSBASE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MTRR_PHYSBASE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MTRR_PHYSBASE0);
#   AsmWriteMsr64 (MSR_IA32_MTRR_PHYSBASE0, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MTRR_PHYSBASE0 is defined as IA32_MTRR_PHYSBASE0 in SDM.
#         MSR_IA32_MTRR_PHYSBASE1 is defined as IA32_MTRR_PHYSBASE1 in SDM.
#         MSR_IA32_MTRR_PHYSBASE2 is defined as IA32_MTRR_PHYSBASE2 in SDM.
#         MSR_IA32_MTRR_PHYSBASE3 is defined as IA32_MTRR_PHYSBASE3 in SDM.
#         MSR_IA32_MTRR_PHYSBASE4 is defined as IA32_MTRR_PHYSBASE4 in SDM.
#         MSR_IA32_MTRR_PHYSBASE5 is defined as IA32_MTRR_PHYSBASE5 in SDM.
#         MSR_IA32_MTRR_PHYSBASE6 is defined as IA32_MTRR_PHYSBASE6 in SDM.
#         MSR_IA32_MTRR_PHYSBASE7 is defined as IA32_MTRR_PHYSBASE7 in SDM.
#         MSR_IA32_MTRR_PHYSBASE8 is defined as IA32_MTRR_PHYSBASE8 in SDM.
#         MSR_IA32_MTRR_PHYSBASE9 is defined as IA32_MTRR_PHYSBASE9 in SDM.
#   @{
# **/
# #define MSR_IA32_MTRR_PHYSBASE0  0x00000200
# #define MSR_IA32_MTRR_PHYSBASE1  0x00000202
# #define MSR_IA32_MTRR_PHYSBASE2  0x00000204
# #define MSR_IA32_MTRR_PHYSBASE3  0x00000206
# #define MSR_IA32_MTRR_PHYSBASE4  0x00000208
# #define MSR_IA32_MTRR_PHYSBASE5  0x0000020A
# #define MSR_IA32_MTRR_PHYSBASE6  0x0000020C
# #define MSR_IA32_MTRR_PHYSBASE7  0x0000020E
# #define MSR_IA32_MTRR_PHYSBASE8  0x00000210
# #define MSR_IA32_MTRR_PHYSBASE9  0x00000212
MSR_IA32_MTRR_PHYSBASE0  = 0x00000200
MSR_IA32_MTRR_PHYSBASE1  = 0x00000202
MSR_IA32_MTRR_PHYSBASE2  = 0x00000204
MSR_IA32_MTRR_PHYSBASE3  = 0x00000206
MSR_IA32_MTRR_PHYSBASE4  = 0x00000208
MSR_IA32_MTRR_PHYSBASE5  = 0x0000020A
MSR_IA32_MTRR_PHYSBASE6  = 0x0000020C
MSR_IA32_MTRR_PHYSBASE7  = 0x0000020E
MSR_IA32_MTRR_PHYSBASE8  = 0x00000210
MSR_IA32_MTRR_PHYSBASE9  = 0x00000212

# /// @}
# 
# /**
#   MSR information returned for MSR indexes #MSR_IA32_MTRR_PHYSBASE0 to
#   #MSR_IA32_MTRR_PHYSBASE9
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Type. Specifies memory type of the range.
#     ///
#     UINT32    Type      : 8;
#     UINT32    Reserved1 : 4;
#     ///
#     /// [Bits 31:12] PhysBase.  MTRR physical Base Address.
#     ///
#     UINT32    PhysBase  : 20;
#     ///
#     /// [Bits MAXPHYSADDR:32] PhysBase.  Upper bits of MTRR physical Base Address.
#     /// MAXPHYADDR: The bit position indicated by MAXPHYADDR depends on the
#     /// maximum physical address range supported by the processor. It is
#     /// reported by CPUID leaf function 80000008H. If CPUID does not support
#     /// leaf 80000008H, the processor supports 36-bit physical address size,
#     /// then bit PhysMask consists of bits 35:12, and bits 63:36 are reserved.
#     ///
#     UINT32    PhysBaseHi : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MTRR_PHYSBASE_REGISTER;
class MSR_IA32_MTRR_PHYSBASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 8),
    ("Reserved1",   UINT32, 4),
    ("PhysBase",    UINT32, 20),
    ("PhysBaseHi",  UINT32, 32)
  ]

class MSR_IA32_MTRR_PHYSBASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_PHYSBASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MTRRphysMaskn.  See Section 11.11.2.3, "Variable Range MTRRs".
#   If CPUID.01H: EDX.MTRR[12] = 1 and IA32_MTRRCAP[7:0] > n.
# 
#   @param  ECX  MSR_IA32_MTRR_PHYSMASKn
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_PHYSMASK_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_PHYSMASK_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MTRR_PHYSMASK_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MTRR_PHYSMASK0);
#   AsmWriteMsr64 (MSR_IA32_MTRR_PHYSMASK0, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MTRR_PHYSMASK0 is defined as IA32_MTRR_PHYSMASK0 in SDM.
#         MSR_IA32_MTRR_PHYSMASK1 is defined as IA32_MTRR_PHYSMASK1 in SDM.
#         MSR_IA32_MTRR_PHYSMASK2 is defined as IA32_MTRR_PHYSMASK2 in SDM.
#         MSR_IA32_MTRR_PHYSMASK3 is defined as IA32_MTRR_PHYSMASK3 in SDM.
#         MSR_IA32_MTRR_PHYSMASK4 is defined as IA32_MTRR_PHYSMASK4 in SDM.
#         MSR_IA32_MTRR_PHYSMASK5 is defined as IA32_MTRR_PHYSMASK5 in SDM.
#         MSR_IA32_MTRR_PHYSMASK6 is defined as IA32_MTRR_PHYSMASK6 in SDM.
#         MSR_IA32_MTRR_PHYSMASK7 is defined as IA32_MTRR_PHYSMASK7 in SDM.
#         MSR_IA32_MTRR_PHYSMASK8 is defined as IA32_MTRR_PHYSMASK8 in SDM.
#         MSR_IA32_MTRR_PHYSMASK9 is defined as IA32_MTRR_PHYSMASK9 in SDM.
#   @{
# **/
# #define MSR_IA32_MTRR_PHYSMASK0  0x00000201
# #define MSR_IA32_MTRR_PHYSMASK1  0x00000203
# #define MSR_IA32_MTRR_PHYSMASK2  0x00000205
# #define MSR_IA32_MTRR_PHYSMASK3  0x00000207
# #define MSR_IA32_MTRR_PHYSMASK4  0x00000209
# #define MSR_IA32_MTRR_PHYSMASK5  0x0000020B
# #define MSR_IA32_MTRR_PHYSMASK6  0x0000020D
# #define MSR_IA32_MTRR_PHYSMASK7  0x0000020F
# #define MSR_IA32_MTRR_PHYSMASK8  0x00000211
# #define MSR_IA32_MTRR_PHYSMASK9  0x00000213
MSR_IA32_MTRR_PHYSMASK0  = 0x00000201
MSR_IA32_MTRR_PHYSMASK1  = 0x00000203
MSR_IA32_MTRR_PHYSMASK2  = 0x00000205
MSR_IA32_MTRR_PHYSMASK3  = 0x00000207
MSR_IA32_MTRR_PHYSMASK4  = 0x00000209
MSR_IA32_MTRR_PHYSMASK5  = 0x0000020B
MSR_IA32_MTRR_PHYSMASK6  = 0x0000020D
MSR_IA32_MTRR_PHYSMASK7  = 0x0000020F
MSR_IA32_MTRR_PHYSMASK8  = 0x00000211
MSR_IA32_MTRR_PHYSMASK9  = 0x00000213

# /// @}
# 
# /**
#   MSR information returned for MSR indexes #MSR_IA32_MTRR_PHYSMASK0 to
#   #MSR_IA32_MTRR_PHYSMASK9
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved1 : 11;
#     ///
#     /// [Bit 11] Valid Enable range mask.
#     ///
#     UINT32    V         : 1;
#     ///
#     /// [Bits 31:12] PhysMask.  MTRR address range mask.
#     ///
#     UINT32    PhysMask  : 20;
#     ///
#     /// [Bits MAXPHYSADDR:32] PhysMask.  Upper bits of MTRR address range mask.
#     /// MAXPHYADDR: The bit position indicated by MAXPHYADDR depends on the
#     /// maximum physical address range supported by the processor. It is
#     /// reported by CPUID leaf function 80000008H. If CPUID does not support
#     /// leaf 80000008H, the processor supports 36-bit physical address size,
#     /// then bit PhysMask consists of bits 35:12, and bits 63:36 are reserved.
#     ///
#     UINT32    PhysMaskHi : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MTRR_PHYSMASK_REGISTER;
class MSR_IA32_MTRR_PHYSMASK_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",   UINT32, 11),
    ("V",           UINT32, 1),
    ("PhysMask",    UINT32, 20),
    ("PhysMaskHi",  UINT32, 32)
  ]

class MSR_IA32_MTRR_PHYSMASK_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_PHYSMASK_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MTRRfix64K_00000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX64K_00000 (0x00000250)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX64K_00000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX64K_00000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX64K_00000 is defined as IA32_MTRR_FIX64K_00000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX64K_00000  0x00000250
MSR_IA32_MTRR_FIX64K_00000  = 0x00000250

# 
# /**
#   MTRRfix16K_80000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX16K_80000 (0x00000258)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX16K_80000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX16K_80000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX16K_80000 is defined as IA32_MTRR_FIX16K_80000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX16K_80000  0x00000258
MSR_IA32_MTRR_FIX16K_80000  = 0x00000258

# 
# /**
#   MTRRfix16K_A0000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX16K_A0000 (0x00000259)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX16K_A0000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX16K_A0000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX16K_A0000 is defined as IA32_MTRR_FIX16K_A0000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX16K_A0000  0x00000259
MSR_IA32_MTRR_FIX16K_A0000  = 0x00000259

# 
# /**
#   See Section 11.11.2.2, "Fixed Range MTRRs.". If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_C0000 (0x00000268)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_C0000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_C0000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_C0000 is defined as IA32_MTRR_FIX4K_C0000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_C0000  0x00000268
MSR_IA32_MTRR_FIX4K_C0000   = 0x00000268

# 
# /**
#   MTRRfix4K_C8000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_C8000 (0x00000269)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_C8000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_C8000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_C8000 is defined as IA32_MTRR_FIX4K_C8000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_C8000  0x00000269
MSR_IA32_MTRR_FIX4K_C8000   = 0x00000269

# 
# /**
#   MTRRfix4K_D0000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_D0000 (0x0000026A)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_D0000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_D0000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_D0000 is defined as IA32_MTRR_FIX4K_D0000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_D0000  0x0000026A
MSR_IA32_MTRR_FIX4K_D0000   = 0x0000026A

# 
# /**
#   MTRRfix4K_D8000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_D8000 (0x0000026B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_D8000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_D8000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_D8000 is defined as IA32_MTRR_FIX4K_D8000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_D8000  0x0000026B
MSR_IA32_MTRR_FIX4K_D8000   = 0x0000026B

# 
# /**
#   MTRRfix4K_E0000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_E0000 (0x0000026C)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_E0000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_E0000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_E0000 is defined as IA32_MTRR_FIX4K_E0000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_E0000  0x0000026C
MSR_IA32_MTRR_FIX4K_E0000   = 0x0000026C

# 
# /**
#   MTRRfix4K_E8000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_E8000 (0x0000026D)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_E8000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_E8000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_E8000 is defined as IA32_MTRR_FIX4K_E8000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_E8000  0x0000026D
MSR_IA32_MTRR_FIX4K_E8000   = 0x0000026D

# 
# /**
#   MTRRfix4K_F0000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_F0000 (0x0000026E)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_F0000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_F0000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_F0000 is defined as IA32_MTRR_FIX4K_F0000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_F0000  0x0000026E
MSR_IA32_MTRR_FIX4K_F0000   = 0x0000026E

# 
# /**
#   MTRRfix4K_F8000. If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_FIX4K_F8000 (0x0000026F)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MTRR_FIX4K_F8000);
#   AsmWriteMsr64 (MSR_IA32_MTRR_FIX4K_F8000, Msr);
#   @endcode
#   @note MSR_IA32_MTRR_FIX4K_F8000 is defined as IA32_MTRR_FIX4K_F8000 in SDM.
# **/
# #define MSR_IA32_MTRR_FIX4K_F8000  0x0000026F
MSR_IA32_MTRR_FIX4K_F8000   = 0x0000026F

# 
# /**
#   IA32_PAT (R/W). If CPUID.01H: EDX.MTRR[16] =1.
# 
#   @param  ECX  MSR_IA32_PAT (0x00000277)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PAT_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PAT_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PAT_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PAT);
#   AsmWriteMsr64 (MSR_IA32_PAT, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PAT is defined as IA32_PAT in SDM.
# **/
# #define MSR_IA32_PAT  0x00000277
MSR_IA32_PAT                    = 0x00000277

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PAT
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 2:0] PA0.
#     ///
#     UINT32    PA0       : 3;
#     UINT32    Reserved1 : 5;
#     ///
#     /// [Bits 10:8] PA1.
#     ///
#     UINT32    PA1       : 3;
#     UINT32    Reserved2 : 5;
#     ///
#     /// [Bits 18:16] PA2.
#     ///
#     UINT32    PA2       : 3;
#     UINT32    Reserved3 : 5;
#     ///
#     /// [Bits 26:24] PA3.
#     ///
#     UINT32    PA3       : 3;
#     UINT32    Reserved4 : 5;
#     ///
#     /// [Bits 34:32] PA4.
#     ///
#     UINT32    PA4       : 3;
#     UINT32    Reserved5 : 5;
#     ///
#     /// [Bits 42:40] PA5.
#     ///
#     UINT32    PA5       : 3;
#     UINT32    Reserved6 : 5;
#     ///
#     /// [Bits 50:48] PA6.
#     ///
#     UINT32    PA6       : 3;
#     UINT32    Reserved7 : 5;
#     ///
#     /// [Bits 58:56] PA7.
#     ///
#     UINT32    PA7       : 3;
#     UINT32    Reserved8 : 5;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PAT_REGISTER;
class MSR_IA32_PAT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("PA0",         UINT32, 3),
    ("Reserved1",   UINT32, 5),
    ("PA1",         UINT32, 3),
    ("Reserved2",   UINT32, 5),
    ("PA2",         UINT32, 3),
    ("Reserved3",   UINT32, 5),
    ("PA3",         UINT32, 3),
    ("Reserved4",   UINT32, 5),
    ("PA4",         UINT32, 3),
    ("Reserved5",   UINT32, 5),
    ("PA5",         UINT32, 3),
    ("Reserved6",   UINT32, 5),
    ("PA6",         UINT32, 3),
    ("Reserved7",   UINT32, 5),
    ("PA7",         UINT32, 3),
    ("Reserved8",   UINT32, 5)
  ]

class MSR_IA32_PAT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PAT_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Provides the programming interface to use corrected MC error signaling
#   capability (R/W). If IA32_MCG_CAP[10] = 1 && IA32_MCG_CAP[7:0] > n.
# 
#   @param  ECX  MSR_IA32_MCn_CTL2
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MC_CTL2_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MC_CTL2_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MC_CTL2_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MC0_CTL2);
#   AsmWriteMsr64 (MSR_IA32_MC0_CTL2, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MC0_CTL2  is defined as IA32_MC0_CTL2  in SDM.
#         MSR_IA32_MC1_CTL2  is defined as IA32_MC1_CTL2  in SDM.
#         MSR_IA32_MC2_CTL2  is defined as IA32_MC2_CTL2  in SDM.
#         MSR_IA32_MC3_CTL2  is defined as IA32_MC3_CTL2  in SDM.
#         MSR_IA32_MC4_CTL2  is defined as IA32_MC4_CTL2  in SDM.
#         MSR_IA32_MC5_CTL2  is defined as IA32_MC5_CTL2  in SDM.
#         MSR_IA32_MC6_CTL2  is defined as IA32_MC6_CTL2  in SDM.
#         MSR_IA32_MC7_CTL2  is defined as IA32_MC7_CTL2  in SDM.
#         MSR_IA32_MC8_CTL2  is defined as IA32_MC8_CTL2  in SDM.
#         MSR_IA32_MC9_CTL2  is defined as IA32_MC9_CTL2  in SDM.
#         MSR_IA32_MC10_CTL2 is defined as IA32_MC10_CTL2 in SDM.
#         MSR_IA32_MC11_CTL2 is defined as IA32_MC11_CTL2 in SDM.
#         MSR_IA32_MC12_CTL2 is defined as IA32_MC12_CTL2 in SDM.
#         MSR_IA32_MC13_CTL2 is defined as IA32_MC13_CTL2 in SDM.
#         MSR_IA32_MC14_CTL2 is defined as IA32_MC14_CTL2 in SDM.
#         MSR_IA32_MC15_CTL2 is defined as IA32_MC15_CTL2 in SDM.
#         MSR_IA32_MC16_CTL2 is defined as IA32_MC16_CTL2 in SDM.
#         MSR_IA32_MC17_CTL2 is defined as IA32_MC17_CTL2 in SDM.
#         MSR_IA32_MC18_CTL2 is defined as IA32_MC18_CTL2 in SDM.
#         MSR_IA32_MC19_CTL2 is defined as IA32_MC19_CTL2 in SDM.
#         MSR_IA32_MC20_CTL2 is defined as IA32_MC20_CTL2 in SDM.
#         MSR_IA32_MC21_CTL2 is defined as IA32_MC21_CTL2 in SDM.
#         MSR_IA32_MC22_CTL2 is defined as IA32_MC22_CTL2 in SDM.
#         MSR_IA32_MC23_CTL2 is defined as IA32_MC23_CTL2 in SDM.
#         MSR_IA32_MC24_CTL2 is defined as IA32_MC24_CTL2 in SDM.
#         MSR_IA32_MC25_CTL2 is defined as IA32_MC25_CTL2 in SDM.
#         MSR_IA32_MC26_CTL2 is defined as IA32_MC26_CTL2 in SDM.
#         MSR_IA32_MC27_CTL2 is defined as IA32_MC27_CTL2 in SDM.
#         MSR_IA32_MC28_CTL2 is defined as IA32_MC28_CTL2 in SDM.
#         MSR_IA32_MC29_CTL2 is defined as IA32_MC29_CTL2 in SDM.
#         MSR_IA32_MC30_CTL2 is defined as IA32_MC30_CTL2 in SDM.
#         MSR_IA32_MC31_CTL2 is defined as IA32_MC31_CTL2 in SDM.
#   @{
# **/
# #define MSR_IA32_MC0_CTL2   0x00000280
# #define MSR_IA32_MC1_CTL2   0x00000281
# #define MSR_IA32_MC2_CTL2   0x00000282
# #define MSR_IA32_MC3_CTL2   0x00000283
# #define MSR_IA32_MC4_CTL2   0x00000284
# #define MSR_IA32_MC5_CTL2   0x00000285
# #define MSR_IA32_MC6_CTL2   0x00000286
# #define MSR_IA32_MC7_CTL2   0x00000287
# #define MSR_IA32_MC8_CTL2   0x00000288
# #define MSR_IA32_MC9_CTL2   0x00000289
# #define MSR_IA32_MC10_CTL2  0x0000028A
# #define MSR_IA32_MC11_CTL2  0x0000028B
# #define MSR_IA32_MC12_CTL2  0x0000028C
# #define MSR_IA32_MC13_CTL2  0x0000028D
# #define MSR_IA32_MC14_CTL2  0x0000028E
# #define MSR_IA32_MC15_CTL2  0x0000028F
# #define MSR_IA32_MC16_CTL2  0x00000290
# #define MSR_IA32_MC17_CTL2  0x00000291
# #define MSR_IA32_MC18_CTL2  0x00000292
# #define MSR_IA32_MC19_CTL2  0x00000293
# #define MSR_IA32_MC20_CTL2  0x00000294
# #define MSR_IA32_MC21_CTL2  0x00000295
# #define MSR_IA32_MC22_CTL2  0x00000296
# #define MSR_IA32_MC23_CTL2  0x00000297
# #define MSR_IA32_MC24_CTL2  0x00000298
# #define MSR_IA32_MC25_CTL2  0x00000299
# #define MSR_IA32_MC26_CTL2  0x0000029A
# #define MSR_IA32_MC27_CTL2  0x0000029B
# #define MSR_IA32_MC28_CTL2  0x0000029C
# #define MSR_IA32_MC29_CTL2  0x0000029D
# #define MSR_IA32_MC30_CTL2  0x0000029E
# #define MSR_IA32_MC31_CTL2  0x0000029F
MSR_IA32_MC0_CTL2   = 0x00000280
MSR_IA32_MC1_CTL2   = 0x00000281
MSR_IA32_MC2_CTL2   = 0x00000282
MSR_IA32_MC3_CTL2   = 0x00000283
MSR_IA32_MC4_CTL2   = 0x00000284
MSR_IA32_MC5_CTL2   = 0x00000285
MSR_IA32_MC6_CTL2   = 0x00000286
MSR_IA32_MC7_CTL2   = 0x00000287
MSR_IA32_MC8_CTL2   = 0x00000288
MSR_IA32_MC9_CTL2   = 0x00000289
MSR_IA32_MC10_CTL2  = 0x0000028A
MSR_IA32_MC11_CTL2  = 0x0000028B
MSR_IA32_MC12_CTL2  = 0x0000028C
MSR_IA32_MC13_CTL2  = 0x0000028D
MSR_IA32_MC14_CTL2  = 0x0000028E
MSR_IA32_MC15_CTL2  = 0x0000028F
MSR_IA32_MC16_CTL2  = 0x00000290
MSR_IA32_MC17_CTL2  = 0x00000291
MSR_IA32_MC18_CTL2  = 0x00000292
MSR_IA32_MC19_CTL2  = 0x00000293
MSR_IA32_MC20_CTL2  = 0x00000294
MSR_IA32_MC21_CTL2  = 0x00000295
MSR_IA32_MC22_CTL2  = 0x00000296
MSR_IA32_MC23_CTL2  = 0x00000297
MSR_IA32_MC24_CTL2  = 0x00000298
MSR_IA32_MC25_CTL2  = 0x00000299
MSR_IA32_MC26_CTL2  = 0x0000029A
MSR_IA32_MC27_CTL2  = 0x0000029B
MSR_IA32_MC28_CTL2  = 0x0000029C
MSR_IA32_MC29_CTL2  = 0x0000029D
MSR_IA32_MC30_CTL2  = 0x0000029E
MSR_IA32_MC31_CTL2  = 0x0000029F

# /// @}
# 
# /**
#   MSR information returned for MSR indexes #MSR_IA32_MC0_CTL2
#   to #MSR_IA32_MC31_CTL2
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 14:0] Corrected error count threshold.
#     ///
#     UINT32    CorrectedErrorCountThreshold : 15;
#     UINT32    Reserved1                    : 15;
#     ///
#     /// [Bit 30] CMCI_EN.
#     ///
#     UINT32    CMCI_EN                      : 1;
#     UINT32    Reserved2                    : 1;
#     UINT32    Reserved3                    : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MC_CTL2_REGISTER;
class MSR_IA32_MC_CTL2_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("CorrectedErrorCountThreshold",    UINT32, 15),
    ("Reserved1",                       UINT32, 15),
    ("CMCI_EN",                         UINT32, 1),
    ("Reserved2",                       UINT32, 1),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_MC_CTL2_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MC_CTL2_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MTRRdefType (R/W). If CPUID.01H: EDX.MTRR[12] =1.
# 
#   @param  ECX  MSR_IA32_MTRR_DEF_TYPE (0x000002FF)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_DEF_TYPE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MTRR_DEF_TYPE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MTRR_DEF_TYPE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MTRR_DEF_TYPE);
#   AsmWriteMsr64 (MSR_IA32_MTRR_DEF_TYPE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MTRR_DEF_TYPE is defined as IA32_MTRR_DEF_TYPE in SDM.
# **/
# #define MSR_IA32_MTRR_DEF_TYPE  0x000002FF
MSR_IA32_MTRR_DEF_TYPE          = 0x000002FF

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MTRR_DEF_TYPE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 2:0] Default Memory Type.
#     ///
#     UINT32    Type      : 3;
#     UINT32    Reserved1 : 7;
#     ///
#     /// [Bit 10] Fixed Range MTRR Enable.
#     ///
#     UINT32    FE        : 1;
#     ///
#     /// [Bit 11] MTRR Enable.
#     ///
#     UINT32    E         : 1;
#     UINT32    Reserved2 : 20;
#     UINT32    Reserved3 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MTRR_DEF_TYPE_REGISTER;
class MSR_IA32_MTRR_DEF_TYPE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT32, 3),
    ("Reserved1",   UINT32, 7),
    ("FE",          UINT32, 1),
    ("E",           UINT32, 1),
    ("Reserved2",   UINT32, 20),
    ("Reserved3",   UINT32, 32)
  ]

class MSR_IA32_MTRR_DEF_TYPE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MTRR_DEF_TYPE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Fixed-Function Performance Counter 0 (R/W): Counts Instr_Retired.Any. If
#   CPUID.0AH: EDX[4:0] > 0.
# 
#   @param  ECX  MSR_IA32_FIXED_CTR0 (0x00000309)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_FIXED_CTR0);
#   AsmWriteMsr64 (MSR_IA32_FIXED_CTR0, Msr);
#   @endcode
#   @note MSR_IA32_FIXED_CTR0 is defined as IA32_FIXED_CTR0 in SDM.
# **/
# #define MSR_IA32_FIXED_CTR0  0x00000309
MSR_IA32_FIXED_CTR0             = 0x00000309

# 
# /**
#   Fixed-Function Performance Counter 1 (R/W): Counts CPU_CLK_Unhalted.Core. If
#   CPUID.0AH: EDX[4:0] > 1.
# 
#   @param  ECX  MSR_IA32_FIXED_CTR1 (0x0000030A)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_FIXED_CTR1);
#   AsmWriteMsr64 (MSR_IA32_FIXED_CTR1, Msr);
#   @endcode
#   @note MSR_IA32_FIXED_CTR1 is defined as IA32_FIXED_CTR1 in SDM.
# **/
# #define MSR_IA32_FIXED_CTR1  0x0000030A
MSR_IA32_FIXED_CTR1             = 0x0000030A

# 
# /**
#   Fixed-Function Performance Counter 2 (R/W): Counts CPU_CLK_Unhalted.Ref. If
#   CPUID.0AH: EDX[4:0] > 2.
# 
#   @param  ECX  MSR_IA32_FIXED_CTR2 (0x0000030B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_FIXED_CTR2);
#   AsmWriteMsr64 (MSR_IA32_FIXED_CTR2, Msr);
#   @endcode
#   @note MSR_IA32_FIXED_CTR2 is defined as IA32_FIXED_CTR2 in SDM.
# **/
# #define MSR_IA32_FIXED_CTR2  0x0000030B
MSR_IA32_FIXED_CTR2             = 0x0000030B

# 
# /**
#   RO. If CPUID.01H: ECX[15] = 1.
# 
#   @param  ECX  MSR_IA32_PERF_CAPABILITIES (0x00000345)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_CAPABILITIES_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_CAPABILITIES_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_CAPABILITIES_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_CAPABILITIES);
#   AsmWriteMsr64 (MSR_IA32_PERF_CAPABILITIES, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_CAPABILITIES is defined as IA32_PERF_CAPABILITIES in SDM.
# **/
# #define MSR_IA32_PERF_CAPABILITIES  0x00000345
MSR_IA32_PERF_CAPABILITIES      = 0x00000345

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_CAPABILITIES
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 5:0] LBR format.
#     ///
#     UINT32    LBR_FMT       : 6;
#     ///
#     /// [Bit 6] PEBS Trap.
#     ///
#     UINT32    PEBS_TRAP     : 1;
#     ///
#     /// [Bit 7] PEBSSaveArchRegs.
#     ///
#     UINT32    PEBS_ARCH_REG : 1;
#     ///
#     /// [Bits 11:8] PEBS Record Format.
#     ///
#     UINT32    PEBS_REC_FMT  : 4;
#     ///
#     /// [Bit 12] 1: Freeze while SMM is supported.
#     ///
#     UINT32    SMM_FREEZE    : 1;
#     ///
#     /// [Bit 13] 1: Full width of counter writable via IA32_A_PMCx.
#     ///
#     UINT32    FW_WRITE      : 1;
#     UINT32    Reserved1     : 18;
#     UINT32    Reserved2     : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_CAPABILITIES_REGISTER;
class MSR_IA32_PERF_CAPABILITIES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LBR_FMT",         UINT32, 6),
    ("PEBS_TRAP",       UINT32, 1),
    ("PEBS_ARCH_REG",   UINT32, 1),
    ("PEBS_REC_FMT",    UINT32, 4),
    ("SMM_FREEZE",      UINT32, 1),
    ("FW_WRITE",        UINT32, 1),
    ("Reserved1",       UINT32, 18),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PERF_CAPABILITIES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_CAPABILITIES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Fixed-Function Performance Counter Control (R/W) Counter increments while
#   the results of ANDing respective enable bit in IA32_PERF_GLOBAL_CTRL with
#   the corresponding OS or USR bits in this MSR is true. If CPUID.0AH: EAX[7:0]
#   > 1.
# 
#   @param  ECX  MSR_IA32_FIXED_CTR_CTRL (0x0000038D)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_FIXED_CTR_CTRL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_FIXED_CTR_CTRL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_FIXED_CTR_CTRL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_FIXED_CTR_CTRL);
#   AsmWriteMsr64 (MSR_IA32_FIXED_CTR_CTRL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_FIXED_CTR_CTRL is defined as IA32_FIXED_CTR_CTRL in SDM.
# **/
# #define MSR_IA32_FIXED_CTR_CTRL  0x0000038D
MSR_IA32_FIXED_CTR_CTRL         = 0x0000038D

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_FIXED_CTR_CTRL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] EN0_OS: Enable Fixed Counter 0 to count while CPL = 0.
#     ///
#     UINT32    EN0_OS     : 1;
#     ///
#     /// [Bit 1] EN0_Usr: Enable Fixed Counter 0 to count while CPL > 0.
#     ///
#     UINT32    EN0_Usr    : 1;
#     ///
#     /// [Bit 2] AnyThread: When set to 1, it enables counting the associated
#     /// event conditions occurring across all logical processors sharing a
#     /// processor core. When set to 0, the counter only increments the
#     /// associated event conditions occurring in the logical processor which
#     /// programmed the MSR. If CPUID.0AH: EAX[7:0] > 2.
#     ///
#     UINT32    AnyThread0 : 1;
#     ///
#     /// [Bit 3] EN0_PMI: Enable PMI when fixed counter 0 overflows.
#     ///
#     UINT32    EN0_PMI    : 1;
#     ///
#     /// [Bit 4] EN1_OS: Enable Fixed Counter 1 to count while CPL = 0.
#     ///
#     UINT32    EN1_OS     : 1;
#     ///
#     /// [Bit 5] EN1_Usr: Enable Fixed Counter 1 to count while CPL > 0.
#     ///
#     UINT32    EN1_Usr    : 1;
#     ///
#     /// [Bit 6] AnyThread: When set to 1, it enables counting the associated
#     /// event conditions occurring across all logical processors sharing a
#     /// processor core. When set to 0, the counter only increments the
#     /// associated event conditions occurring in the logical processor which
#     /// programmed the MSR. If CPUID.0AH: EAX[7:0] > 2.
#     ///
#     UINT32    AnyThread1 : 1;
#     ///
#     /// [Bit 7] EN1_PMI: Enable PMI when fixed counter 1 overflows.
#     ///
#     UINT32    EN1_PMI    : 1;
#     ///
#     /// [Bit 8] EN2_OS: Enable Fixed Counter 2 to count while CPL = 0.
#     ///
#     UINT32    EN2_OS     : 1;
#     ///
#     /// [Bit 9] EN2_Usr: Enable Fixed Counter 2 to count while CPL > 0.
#     ///
#     UINT32    EN2_Usr    : 1;
#     ///
#     /// [Bit 10] AnyThread: When set to 1, it enables counting the associated
#     /// event conditions occurring across all logical processors sharing a
#     /// processor core. When set to 0, the counter only increments the
#     /// associated event conditions occurring in the logical processor which
#     /// programmed the MSR. If CPUID.0AH: EAX[7:0] > 2.
#     ///
#     UINT32    AnyThread2 : 1;
#     ///
#     /// [Bit 11] EN2_PMI: Enable PMI when fixed counter 2 overflows.
#     ///
#     UINT32    EN2_PMI    : 1;
#     UINT32    Reserved1  : 20;
#     UINT32    Reserved2  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_FIXED_CTR_CTRL_REGISTER;
class MSR_IA32_FIXED_CTR_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN0_OS",      UINT32, 1),
    ("EN0_Usr",     UINT32, 1),
    ("AnyThread0",  UINT32, 1),
    ("EN0_PMI",     UINT32, 1),
    ("EN1_OS",      UINT32, 1),
    ("EN1_Usr",     UINT32, 1),
    ("AnyThread1",  UINT32, 1),
    ("EN1_PMI",     UINT32, 1),
    ("EN2_OS",      UINT32, 1),
    ("EN2_Usr",     UINT32, 1),
    ("AnyThread2",  UINT32, 1),
    ("EN2_PMI",     UINT32, 1),
    ("Reserved1",   UINT32, 20),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_FIXED_CTR_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_FIXED_CTR_CTRL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Performance Counter Status (RO). If CPUID.0AH: EAX[7:0] > 0.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_STATUS (0x0000038E)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_STATUS);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_STATUS is defined as IA32_PERF_GLOBAL_STATUS in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_STATUS  0x0000038E
MSR_IA32_PERF_GLOBAL_STATUS     = 0x0000038E

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Ovf_PMC0: Overflow status of IA32_PMC0. If CPUID.0AH:
#     /// EAX[15:8] > 0.
#     ///
#     UINT32    Ovf_PMC0       : 1;
#     ///
#     /// [Bit 1] Ovf_PMC1: Overflow status of IA32_PMC1. If CPUID.0AH:
#     /// EAX[15:8] > 1.
#     ///
#     UINT32    Ovf_PMC1       : 1;
#     ///
#     /// [Bit 2] Ovf_PMC2: Overflow status of IA32_PMC2. If CPUID.0AH:
#     /// EAX[15:8] > 2.
#     ///
#     UINT32    Ovf_PMC2       : 1;
#     ///
#     /// [Bit 3] Ovf_PMC3: Overflow status of IA32_PMC3. If CPUID.0AH:
#     /// EAX[15:8] > 3.
#     ///
#     UINT32    Ovf_PMC3       : 1;
#     UINT32    Reserved1      : 28;
#     ///
#     /// [Bit 32] Ovf_FixedCtr0: Overflow status of IA32_FIXED_CTR0. If
#     /// CPUID.0AH: EAX[7:0] > 1.
#     ///
#     UINT32    Ovf_FixedCtr0  : 1;
#     ///
#     /// [Bit 33] Ovf_FixedCtr1: Overflow status of IA32_FIXED_CTR1. If
#     /// CPUID.0AH: EAX[7:0] > 1.
#     ///
#     UINT32    Ovf_FixedCtr1  : 1;
#     ///
#     /// [Bit 34] Ovf_FixedCtr2: Overflow status of IA32_FIXED_CTR2. If
#     /// CPUID.0AH: EAX[7:0] > 1.
#     ///
#     UINT32    Ovf_FixedCtr2  : 1;
#     UINT32    Reserved2      : 20;
#     ///
#     /// [Bit 55] Trace_ToPA_PMI: A PMI occurred due to a ToPA entry memory
#     /// buffer was completely filled. If (CPUID.(EAX=07H, ECX=0):EBX[25] = 1)
#     /// && IA32_RTIT_CTL.ToPA = 1.
#     ///
#     UINT32    Trace_ToPA_PMI : 1;
#     UINT32    Reserved3      : 2;
#     ///
#     /// [Bit 58] LBR_Frz: LBRs are frozen due to -
#     /// IA32_DEBUGCTL.FREEZE_LBR_ON_PMI=1, -  The LBR stack overflowed. If
#     /// CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    LBR_Frz        : 1;
#     ///
#     /// [Bit 59] CTR_Frz: Performance counters in the core PMU are frozen due
#     /// to -  IA32_DEBUGCTL.FREEZE_PERFMON_ON_ PMI=1, -  one or more core PMU
#     /// counters overflowed. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    CTR_Frz        : 1;
#     ///
#     /// [Bit 60] ASCI: Data in the performance counters in the core PMU may
#     /// include contributions from the direct or indirect operation intel SGX
#     /// to protect an enclave. If CPUID.(EAX=07H, ECX=0):EBX[2] = 1.
#     ///
#     UINT32    ASCI           : 1;
#     ///
#     /// [Bit 61] Ovf_Uncore: Uncore counter overflow status. If CPUID.0AH:
#     /// EAX[7:0] > 2.
#     ///
#     UINT32    Ovf_Uncore     : 1;
#     ///
#     /// [Bit 62] OvfBuf: DS SAVE area Buffer overflow status. If CPUID.0AH:
#     /// EAX[7:0] > 0.
#     ///
#     UINT32    OvfBuf         : 1;
#     ///
#     /// [Bit 63] CondChgd: status bits of this register has changed. If
#     /// CPUID.0AH: EAX[7:0] > 0.
#     ///
#     UINT32    CondChgd       : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_STATUS_REGISTER;
class MSR_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMC0",        UINT32, 1),
    ("Ovf_PMC1",        UINT32, 1),
    ("Ovf_PMC2",        UINT32, 1),
    ("Ovf_PMC3",        UINT32, 1),
    ("Reserved1",       UINT32, 28),
    ("Ovf_FixedCtr0",   UINT32, 1),
    ("Ovf_FixedCtr1",   UINT32, 1),
    ("Ovf_FixedCtr2",   UINT32, 1),
    ("Reserved2",       UINT32, 20),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved3",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Performance Counter Control (R/W) Counter increments while the result
#   of ANDing respective enable bit in this MSR with the corresponding OS or USR
#   bits in the general-purpose or fixed counter control MSR is true. If
#   CPUID.0AH: EAX[7:0] > 0.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_CTRL (0x0000038F)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_CTRL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_CTRL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_CTRL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_CTRL);
#   AsmWriteMsr64 (MSR_IA32_PERF_GLOBAL_CTRL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_CTRL is defined as IA32_PERF_GLOBAL_CTRL in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_CTRL  0x0000038F
MSR_IA32_PERF_GLOBAL_CTRL       = 0x0000038F

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_CTRL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] EN_PMCn. If CPUID.0AH: EAX[15:8] > n.
#     /// Enable bitmask.  Only the first n-1 bits are valid.
#     /// Bits n..31 are reserved.
#     ///
#     UINT32    EN_PMCn       : 32;
#     ///
#     /// [Bits 63:32] EN_FIXED_CTRn. If CPUID.0AH: EDX[4:0] > n.
#     /// Enable bitmask.  Only the first n-1 bits are valid.
#     /// Bits 31:n are reserved.
#     ///
#     UINT32    EN_FIXED_CTRn : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_CTRL_REGISTER;
class MSR_IA32_PERF_GLOBAL_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN_PMCn",         UINT32, 32),
    ("EN_FIXED_CTRn",   UINT32, 32)
  ]

class MSR_IA32_PERF_GLOBAL_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_CTRL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Performance Counter Overflow Control (R/W). If CPUID.0AH: EAX[7:0] >
#   0 && CPUID.0AH: EAX[7:0] <= 3.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_OVF_CTRL (0x00000390)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_OVF_CTRL);
#   AsmWriteMsr64 (MSR_IA32_PERF_GLOBAL_OVF_CTRL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_OVF_CTRL is defined as IA32_PERF_GLOBAL_OVF_CTRL in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_OVF_CTRL  0x00000390
MSR_IA32_PERF_GLOBAL_OVF_CTRL   = 0x00000390

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_OVF_CTRL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Set 1 to Clear Ovf_PMC0 bit. If CPUID.0AH: EAX[15:8] > n.
#     /// Clear bitmask.  Only the first n-1 bits are valid.
#     /// Bits 31:n are reserved.
#     ///
#     UINT32    Ovf_PMCn       : 32;
#     ///
#     /// [Bits 54:32] Set 1 to Clear Ovf_FIXED_CTR0 bit.
#     /// If CPUID.0AH: EDX[4:0] > n.
#     /// Clear bitmask.  Only the first n-1 bits are valid.
#     /// Bits 22:n are reserved.
#     ///
#     UINT32    Ovf_FIXED_CTRn : 23;
#     ///
#     /// [Bit 55] Set 1 to Clear Trace_ToPA_PMI bit. If (CPUID.(EAX=07H,
#     /// ECX=0):EBX[25] = 1) && IA32_RTIT_CTL.ToPA = 1.
#     ///
#     UINT32    Trace_ToPA_PMI : 1;
#     UINT32    Reserved2      : 5;
#     ///
#     /// [Bit 61] Set 1 to Clear Ovf_Uncore bit. Introduced at Display Family /
#     /// Display Model 06_2EH.
#     ///
#     UINT32    Ovf_Uncore     : 1;
#     ///
#     /// [Bit 62] Set 1 to Clear OvfBuf: bit. If CPUID.0AH: EAX[7:0] > 0.
#     ///
#     UINT32    OvfBuf         : 1;
#     ///
#     /// [Bit 63] Set to 1to clear CondChgd: bit. If CPUID.0AH: EAX[7:0] > 0.
#     ///
#     UINT32    CondChgd       : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER;
class MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 5),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_OVF_CTRL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Performance Counter Overflow Reset Control (R/W). If CPUID.0AH:
#   EAX[7:0] > 3.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_STATUS_RESET (0x00000390)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_STATUS_RESET);
#   AsmWriteMsr64 (MSR_IA32_PERF_GLOBAL_STATUS_RESET, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_STATUS_RESET is defined as IA32_PERF_GLOBAL_STATUS_RESET in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_STATUS_RESET  0x00000390
MSR_IA32_PERF_GLOBAL_STATUS_RESET  = 0x00000390

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_STATUS_RESET
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Set 1 to Clear Ovf_PMC0 bit. If CPUID.0AH: EAX[15:8] > n.
#     /// Clear bitmask.  Only the first n-1 bits are valid.
#     /// Bits 31:n are reserved.
#     ///
#     UINT32    Ovf_PMCn       : 32;
#     ///
#     /// [Bits 54:32] Set 1 to Clear Ovf_FIXED_CTR0 bit.
#     /// If CPUID.0AH: EDX[4:0] > n.
#     /// Clear bitmask.  Only the first n-1 bits are valid.
#     /// Bits 22:n are reserved.
#     ///
#     UINT32    Ovf_FIXED_CTRn : 23;
#     ///
#     /// [Bit 55] Set 1 to Clear Trace_ToPA_PMI bit. If (CPUID.(EAX=07H,
#     /// ECX=0):EBX[25] = 1) && IA32_RTIT_CTL.ToPA[8] = 1.
#     ///
#     UINT32    Trace_ToPA_PMI : 1;
#     UINT32    Reserved2      : 2;
#     ///
#     /// [Bit 58] Set 1 to Clear LBR_Frz bit. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    LBR_Frz        : 1;
#     ///
#     /// [Bit 59] Set 1 to Clear CTR_Frz bit. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    CTR_Frz        : 1;
#     ///
#     /// [Bit 60] Set 1 to Clear ASCI bit. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    ASCI           : 1;
#     ///
#     /// [Bit 61] Set 1 to Clear Ovf_Uncore bit. Introduced at Display Family /
#     /// Display Model 06_2EH.
#     ///
#     UINT32    Ovf_Uncore     : 1;
#     ///
#     /// [Bit 62] Set 1 to Clear OvfBuf: bit. If CPUID.0AH: EAX[7:0] > 0.
#     ///
#     UINT32    OvfBuf         : 1;
#     ///
#     /// [Bit 63] Set to 1to clear CondChgd: bit. If CPUID.0AH: EAX[7:0] > 0.
#     ///
#     UINT32    CondChgd       : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER;
class MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("CondChgd",        UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_RESET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Global Performance Counter Overflow Set Control (R/W). If CPUID.0AH:
#   EAX[7:0] > 3.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_STATUS_SET (0x00000391)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_STATUS_SET);
#   AsmWriteMsr64 (MSR_IA32_PERF_GLOBAL_STATUS_SET, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_STATUS_SET is defined as IA32_PERF_GLOBAL_STATUS_SET in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_STATUS_SET  0x00000391
MSR_IA32_PERF_GLOBAL_STATUS_SET  = 0x00000391

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_STATUS_SET
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Set 1 to cause Ovf_PMCn = 1. If CPUID.0AH: EAX[7:0] > n.
#     /// Set bitmask.  Only the first n-1 bits are valid.
#     /// Bits 31:n are reserved.
#     ///
#     UINT32    Ovf_PMCn       : 32;
#     ///
#     /// [Bits 54:32] Set 1 to cause Ovf_FIXED_CTRn = 1.
#     /// If CPUID.0AH: EAX[7:0] > n.
#     /// Set bitmask.  Only the first n-1 bits are valid.
#     /// Bits 22:n are reserved.
#     ///
#     UINT32    Ovf_FIXED_CTRn : 23;
#     ///
#     /// [Bit 55] Set 1 to cause Trace_ToPA_PMI = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    Trace_ToPA_PMI : 1;
#     UINT32    Reserved2      : 2;
#     ///
#     /// [Bit 58] Set 1 to cause LBR_Frz = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    LBR_Frz        : 1;
#     ///
#     /// [Bit 59] Set 1 to cause CTR_Frz = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    CTR_Frz        : 1;
#     ///
#     /// [Bit 60] Set 1 to cause ASCI = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    ASCI           : 1;
#     ///
#     /// [Bit 61] Set 1 to cause Ovf_Uncore = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    Ovf_Uncore     : 1;
#     ///
#     /// [Bit 62] Set 1 to cause OvfBuf = 1. If CPUID.0AH: EAX[7:0] > 3.
#     ///
#     UINT32    OvfBuf         : 1;
#     UINT32    Reserved3      : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER;
class MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Ovf_PMCn",        UINT32, 32),
    ("Ovf_FIXED_CTRn",  UINT32, 23),
    ("Trace_ToPA_PMI",  UINT32, 1),
    ("Reserved2",       UINT32, 2),
    ("LBR_Frz",         UINT32, 1),
    ("CTR_Frz",         UINT32, 1),
    ("ASCI",            UINT32, 1),
    ("Ovf_Uncore",      UINT32, 1),
    ("OvfBuf",          UINT32, 1),
    ("Reserved3",       UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_STATUS_SET_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Indicator of core perfmon interface is in use (RO). If CPUID.0AH: EAX[7:0] >
#   3.
# 
#   @param  ECX  MSR_IA32_PERF_GLOBAL_INUSE (0x00000392)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_INUSE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PERF_GLOBAL_INUSE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PERF_GLOBAL_INUSE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PERF_GLOBAL_INUSE);
#   @endcode
#   @note MSR_IA32_PERF_GLOBAL_INUSE is defined as IA32_PERF_GLOBAL_INUSE in SDM.
# **/
# #define MSR_IA32_PERF_GLOBAL_INUSE  0x00000392
# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PERF_GLOBAL_INUSE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] IA32_PERFEVTSELn in use.  If CPUID.0AH: EAX[7:0] > n.
#     /// Status bitmask.  Only the first n-1 bits are valid.
#     /// Bits 31:n are reserved.
#     ///
#     UINT32    IA32_PERFEVTSELn : 32;
#     ///
#     /// [Bits 62:32] IA32_FIXED_CTRn in use.
#     /// If CPUID.0AH: EAX[7:0] > n.
#     /// Status bitmask.  Only the first n-1 bits are valid.
#     /// Bits 30:n are reserved.
#     ///
#     UINT32    IA32_FIXED_CTRn  : 31;
#     ///
#     /// [Bit 63] PMI in use.
#     ///
#     UINT32    PMI              : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PERF_GLOBAL_INUSE_REGISTER;
class MSR_IA32_PERF_GLOBAL_INUSE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("IA32_PERFEVTSELn",    UINT32, 32),
    ("IA32_FIXED_CTRn",     UINT32, 31),
    ("PMI",                 UINT32, 1)
  ]

class MSR_IA32_PERF_GLOBAL_INUSE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PERF_GLOBAL_INUSE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   PEBS Control (R/W).
# 
#   @param  ECX  MSR_IA32_PEBS_ENABLE (0x000003F1)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PEBS_ENABLE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PEBS_ENABLE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PEBS_ENABLE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PEBS_ENABLE);
#   AsmWriteMsr64 (MSR_IA32_PEBS_ENABLE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PEBS_ENABLE is defined as IA32_PEBS_ENABLE in SDM.
# **/
# #define MSR_IA32_PEBS_ENABLE  0x000003F1
MSR_IA32_PEBS_ENABLE            = 0x000003F1

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PEBS_ENABLE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Enable PEBS on IA32_PMC0. Introduced at Display Family /
#     /// Display Model 06_0FH.
#     ///
#     UINT32    Enable    : 1;
#     ///
#     /// [Bits 3:1] Reserved or Model specific.
#     ///
#     UINT32    Reserved1 : 3;
#     UINT32    Reserved2 : 28;
#     ///
#     /// [Bits 35:32] Reserved or Model specific.
#     ///
#     UINT32    Reserved3 : 4;
#     UINT32    Reserved4 : 28;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PEBS_ENABLE_REGISTER;
class MSR_IA32_PEBS_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",      UINT32, 1),
    ("Reserved1",   UINT32, 3),
    ("Reserved2",   UINT32, 28),
    ("Reserved3",   UINT32, 4),
    ("Reserved4",   UINT32, 28)
  ]

class MSR_IA32_PEBS_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PEBS_ENABLE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   MCn_CTL. If IA32_MCG_CAP.CNT > n.
# 
#   @param  ECX  MSR_IA32_MCn_CTL
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MC0_CTL);
#   AsmWriteMsr64 (MSR_IA32_MC0_CTL, Msr);
#   @endcode
#   @note MSR_IA32_MC0_CTL  is defined as IA32_MC0_CTL  in SDM.
#         MSR_IA32_MC1_CTL  is defined as IA32_MC1_CTL  in SDM.
#         MSR_IA32_MC2_CTL  is defined as IA32_MC2_CTL  in SDM.
#         MSR_IA32_MC3_CTL  is defined as IA32_MC3_CTL  in SDM.
#         MSR_IA32_MC4_CTL  is defined as IA32_MC4_CTL  in SDM.
#         MSR_IA32_MC5_CTL  is defined as IA32_MC5_CTL  in SDM.
#         MSR_IA32_MC6_CTL  is defined as IA32_MC6_CTL  in SDM.
#         MSR_IA32_MC7_CTL  is defined as IA32_MC7_CTL  in SDM.
#         MSR_IA32_MC8_CTL  is defined as IA32_MC8_CTL  in SDM.
#         MSR_IA32_MC9_CTL  is defined as IA32_MC9_CTL  in SDM.
#         MSR_IA32_MC10_CTL is defined as IA32_MC10_CTL in SDM.
#         MSR_IA32_MC11_CTL is defined as IA32_MC11_CTL in SDM.
#         MSR_IA32_MC12_CTL is defined as IA32_MC12_CTL in SDM.
#         MSR_IA32_MC13_CTL is defined as IA32_MC13_CTL in SDM.
#         MSR_IA32_MC14_CTL is defined as IA32_MC14_CTL in SDM.
#         MSR_IA32_MC15_CTL is defined as IA32_MC15_CTL in SDM.
#         MSR_IA32_MC16_CTL is defined as IA32_MC16_CTL in SDM.
#         MSR_IA32_MC17_CTL is defined as IA32_MC17_CTL in SDM.
#         MSR_IA32_MC18_CTL is defined as IA32_MC18_CTL in SDM.
#         MSR_IA32_MC19_CTL is defined as IA32_MC19_CTL in SDM.
#         MSR_IA32_MC20_CTL is defined as IA32_MC20_CTL in SDM.
#         MSR_IA32_MC21_CTL is defined as IA32_MC21_CTL in SDM.
#         MSR_IA32_MC22_CTL is defined as IA32_MC22_CTL in SDM.
#         MSR_IA32_MC23_CTL is defined as IA32_MC23_CTL in SDM.
#         MSR_IA32_MC24_CTL is defined as IA32_MC24_CTL in SDM.
#         MSR_IA32_MC25_CTL is defined as IA32_MC25_CTL in SDM.
#         MSR_IA32_MC26_CTL is defined as IA32_MC26_CTL in SDM.
#         MSR_IA32_MC27_CTL is defined as IA32_MC27_CTL in SDM.
#         MSR_IA32_MC28_CTL is defined as IA32_MC28_CTL in SDM.
#   @{
# **/
# #define MSR_IA32_MC0_CTL   0x00000400
# #define MSR_IA32_MC1_CTL   0x00000404
# #define MSR_IA32_MC2_CTL   0x00000408
# #define MSR_IA32_MC3_CTL   0x0000040C
# #define MSR_IA32_MC4_CTL   0x00000410
# #define MSR_IA32_MC5_CTL   0x00000414
# #define MSR_IA32_MC6_CTL   0x00000418
# #define MSR_IA32_MC7_CTL   0x0000041C
# #define MSR_IA32_MC8_CTL   0x00000420
# #define MSR_IA32_MC9_CTL   0x00000424
# #define MSR_IA32_MC10_CTL  0x00000428
# #define MSR_IA32_MC11_CTL  0x0000042C
# #define MSR_IA32_MC12_CTL  0x00000430
# #define MSR_IA32_MC13_CTL  0x00000434
# #define MSR_IA32_MC14_CTL  0x00000438
# #define MSR_IA32_MC15_CTL  0x0000043C
# #define MSR_IA32_MC16_CTL  0x00000440
# #define MSR_IA32_MC17_CTL  0x00000444
# #define MSR_IA32_MC18_CTL  0x00000448
# #define MSR_IA32_MC19_CTL  0x0000044C
# #define MSR_IA32_MC20_CTL  0x00000450
# #define MSR_IA32_MC21_CTL  0x00000454
# #define MSR_IA32_MC22_CTL  0x00000458
# #define MSR_IA32_MC23_CTL  0x0000045C
# #define MSR_IA32_MC24_CTL  0x00000460
# #define MSR_IA32_MC25_CTL  0x00000464
# #define MSR_IA32_MC26_CTL  0x00000468
# #define MSR_IA32_MC27_CTL  0x0000046C
# #define MSR_IA32_MC28_CTL  0x00000470
MSR_IA32_MC0_CTL   = 0x00000400
MSR_IA32_MC1_CTL   = 0x00000404
MSR_IA32_MC2_CTL   = 0x00000408
MSR_IA32_MC3_CTL   = 0x0000040C
MSR_IA32_MC4_CTL   = 0x00000410
MSR_IA32_MC5_CTL   = 0x00000414
MSR_IA32_MC6_CTL   = 0x00000418
MSR_IA32_MC7_CTL   = 0x0000041C
MSR_IA32_MC8_CTL   = 0x00000420
MSR_IA32_MC9_CTL   = 0x00000424
MSR_IA32_MC10_CTL  = 0x00000428
MSR_IA32_MC11_CTL  = 0x0000042C
MSR_IA32_MC12_CTL  = 0x00000430
MSR_IA32_MC13_CTL  = 0x00000434
MSR_IA32_MC14_CTL  = 0x00000438
MSR_IA32_MC15_CTL  = 0x0000043C
MSR_IA32_MC16_CTL  = 0x00000440
MSR_IA32_MC17_CTL  = 0x00000444
MSR_IA32_MC18_CTL  = 0x00000448
MSR_IA32_MC19_CTL  = 0x0000044C
MSR_IA32_MC20_CTL  = 0x00000450
MSR_IA32_MC21_CTL  = 0x00000454
MSR_IA32_MC22_CTL  = 0x00000458
MSR_IA32_MC23_CTL  = 0x0000045C
MSR_IA32_MC24_CTL  = 0x00000460
MSR_IA32_MC25_CTL  = 0x00000464
MSR_IA32_MC26_CTL  = 0x00000468
MSR_IA32_MC27_CTL  = 0x0000046C
MSR_IA32_MC28_CTL  = 0x00000470

# /// @}
# 
# /**
#   MCn_STATUS. If IA32_MCG_CAP.CNT > n.
# 
#   @param  ECX  MSR_IA32_MCn_STATUS
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MC0_STATUS);
#   AsmWriteMsr64 (MSR_IA32_MC0_STATUS, Msr);
#   @endcode
#   @note MSR_IA32_MC0_STATUS  is defined as IA32_MC0_STATUS  in SDM.
#         MSR_IA32_MC1_STATUS  is defined as IA32_MC1_STATUS  in SDM.
#         MSR_IA32_MC2_STATUS  is defined as IA32_MC2_STATUS  in SDM.
#         MSR_IA32_MC3_STATUS  is defined as IA32_MC3_STATUS  in SDM.
#         MSR_IA32_MC4_STATUS  is defined as IA32_MC4_STATUS  in SDM.
#         MSR_IA32_MC5_STATUS  is defined as IA32_MC5_STATUS  in SDM.
#         MSR_IA32_MC6_STATUS  is defined as IA32_MC6_STATUS  in SDM.
#         MSR_IA32_MC7_STATUS  is defined as IA32_MC7_STATUS  in SDM.
#         MSR_IA32_MC8_STATUS  is defined as IA32_MC8_STATUS  in SDM.
#         MSR_IA32_MC9_STATUS  is defined as IA32_MC9_STATUS  in SDM.
#         MSR_IA32_MC10_STATUS is defined as IA32_MC10_STATUS in SDM.
#         MSR_IA32_MC11_STATUS is defined as IA32_MC11_STATUS in SDM.
#         MSR_IA32_MC12_STATUS is defined as IA32_MC12_STATUS in SDM.
#         MSR_IA32_MC13_STATUS is defined as IA32_MC13_STATUS in SDM.
#         MSR_IA32_MC14_STATUS is defined as IA32_MC14_STATUS in SDM.
#         MSR_IA32_MC15_STATUS is defined as IA32_MC15_STATUS in SDM.
#         MSR_IA32_MC16_STATUS is defined as IA32_MC16_STATUS in SDM.
#         MSR_IA32_MC17_STATUS is defined as IA32_MC17_STATUS in SDM.
#         MSR_IA32_MC18_STATUS is defined as IA32_MC18_STATUS in SDM.
#         MSR_IA32_MC19_STATUS is defined as IA32_MC19_STATUS in SDM.
#         MSR_IA32_MC20_STATUS is defined as IA32_MC20_STATUS in SDM.
#         MSR_IA32_MC21_STATUS is defined as IA32_MC21_STATUS in SDM.
#         MSR_IA32_MC22_STATUS is defined as IA32_MC22_STATUS in SDM.
#         MSR_IA32_MC23_STATUS is defined as IA32_MC23_STATUS in SDM.
#         MSR_IA32_MC24_STATUS is defined as IA32_MC24_STATUS in SDM.
#         MSR_IA32_MC25_STATUS is defined as IA32_MC25_STATUS in SDM.
#         MSR_IA32_MC26_STATUS is defined as IA32_MC26_STATUS in SDM.
#         MSR_IA32_MC27_STATUS is defined as IA32_MC27_STATUS in SDM.
#         MSR_IA32_MC28_STATUS is defined as IA32_MC28_STATUS in SDM.
#   @{
# **/
# #define MSR_IA32_MC0_STATUS   0x00000401
# #define MSR_IA32_MC1_STATUS   0x00000405
# #define MSR_IA32_MC2_STATUS   0x00000409
# #define MSR_IA32_MC3_STATUS   0x0000040D
# #define MSR_IA32_MC4_STATUS   0x00000411
# #define MSR_IA32_MC5_STATUS   0x00000415
# #define MSR_IA32_MC6_STATUS   0x00000419
# #define MSR_IA32_MC7_STATUS   0x0000041D
# #define MSR_IA32_MC8_STATUS   0x00000421
# #define MSR_IA32_MC9_STATUS   0x00000425
# #define MSR_IA32_MC10_STATUS  0x00000429
# #define MSR_IA32_MC11_STATUS  0x0000042D
# #define MSR_IA32_MC12_STATUS  0x00000431
# #define MSR_IA32_MC13_STATUS  0x00000435
# #define MSR_IA32_MC14_STATUS  0x00000439
# #define MSR_IA32_MC15_STATUS  0x0000043D
# #define MSR_IA32_MC16_STATUS  0x00000441
# #define MSR_IA32_MC17_STATUS  0x00000445
# #define MSR_IA32_MC18_STATUS  0x00000449
# #define MSR_IA32_MC19_STATUS  0x0000044D
# #define MSR_IA32_MC20_STATUS  0x00000451
# #define MSR_IA32_MC21_STATUS  0x00000455
# #define MSR_IA32_MC22_STATUS  0x00000459
# #define MSR_IA32_MC23_STATUS  0x0000045D
# #define MSR_IA32_MC24_STATUS  0x00000461
# #define MSR_IA32_MC25_STATUS  0x00000465
# #define MSR_IA32_MC26_STATUS  0x00000469
# #define MSR_IA32_MC27_STATUS  0x0000046D
# #define MSR_IA32_MC28_STATUS  0x00000471
MSR_IA32_MC0_STATUS   = 0x00000401
MSR_IA32_MC1_STATUS   = 0x00000405
MSR_IA32_MC2_STATUS   = 0x00000409
MSR_IA32_MC3_STATUS   = 0x0000040D
MSR_IA32_MC4_STATUS   = 0x00000411
MSR_IA32_MC5_STATUS   = 0x00000415
MSR_IA32_MC6_STATUS   = 0x00000419
MSR_IA32_MC7_STATUS   = 0x0000041D
MSR_IA32_MC8_STATUS   = 0x00000421
MSR_IA32_MC9_STATUS   = 0x00000425
MSR_IA32_MC10_STATUS  = 0x00000429
MSR_IA32_MC11_STATUS  = 0x0000042D
MSR_IA32_MC12_STATUS  = 0x00000431
MSR_IA32_MC13_STATUS  = 0x00000435
MSR_IA32_MC14_STATUS  = 0x00000439
MSR_IA32_MC15_STATUS  = 0x0000043D
MSR_IA32_MC16_STATUS  = 0x00000441
MSR_IA32_MC17_STATUS  = 0x00000445
MSR_IA32_MC18_STATUS  = 0x00000449
MSR_IA32_MC19_STATUS  = 0x0000044D
MSR_IA32_MC20_STATUS  = 0x00000451
MSR_IA32_MC21_STATUS  = 0x00000455
MSR_IA32_MC22_STATUS  = 0x00000459
MSR_IA32_MC23_STATUS  = 0x0000045D
MSR_IA32_MC24_STATUS  = 0x00000461
MSR_IA32_MC25_STATUS  = 0x00000465
MSR_IA32_MC26_STATUS  = 0x00000469
MSR_IA32_MC27_STATUS  = 0x0000046D
MSR_IA32_MC28_STATUS  = 0x00000471

# /// @}
# 
# /**
#   MCn_ADDR. If IA32_MCG_CAP.CNT > n.
# 
#   @param  ECX  MSR_IA32_MCn_ADDR
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MC0_ADDR);
#   AsmWriteMsr64 (MSR_IA32_MC0_ADDR, Msr);
#   @endcode
#   @note MSR_IA32_MC0_ADDR  is defined as IA32_MC0_ADDR  in SDM.
#         MSR_IA32_MC1_ADDR  is defined as IA32_MC1_ADDR  in SDM.
#         MSR_IA32_MC2_ADDR  is defined as IA32_MC2_ADDR  in SDM.
#         MSR_IA32_MC3_ADDR  is defined as IA32_MC3_ADDR  in SDM.
#         MSR_IA32_MC4_ADDR  is defined as IA32_MC4_ADDR  in SDM.
#         MSR_IA32_MC5_ADDR  is defined as IA32_MC5_ADDR  in SDM.
#         MSR_IA32_MC6_ADDR  is defined as IA32_MC6_ADDR  in SDM.
#         MSR_IA32_MC7_ADDR  is defined as IA32_MC7_ADDR  in SDM.
#         MSR_IA32_MC8_ADDR  is defined as IA32_MC8_ADDR  in SDM.
#         MSR_IA32_MC9_ADDR  is defined as IA32_MC9_ADDR  in SDM.
#         MSR_IA32_MC10_ADDR is defined as IA32_MC10_ADDR in SDM.
#         MSR_IA32_MC11_ADDR is defined as IA32_MC11_ADDR in SDM.
#         MSR_IA32_MC12_ADDR is defined as IA32_MC12_ADDR in SDM.
#         MSR_IA32_MC13_ADDR is defined as IA32_MC13_ADDR in SDM.
#         MSR_IA32_MC14_ADDR is defined as IA32_MC14_ADDR in SDM.
#         MSR_IA32_MC15_ADDR is defined as IA32_MC15_ADDR in SDM.
#         MSR_IA32_MC16_ADDR is defined as IA32_MC16_ADDR in SDM.
#         MSR_IA32_MC17_ADDR is defined as IA32_MC17_ADDR in SDM.
#         MSR_IA32_MC18_ADDR is defined as IA32_MC18_ADDR in SDM.
#         MSR_IA32_MC19_ADDR is defined as IA32_MC19_ADDR in SDM.
#         MSR_IA32_MC20_ADDR is defined as IA32_MC20_ADDR in SDM.
#         MSR_IA32_MC21_ADDR is defined as IA32_MC21_ADDR in SDM.
#         MSR_IA32_MC22_ADDR is defined as IA32_MC22_ADDR in SDM.
#         MSR_IA32_MC23_ADDR is defined as IA32_MC23_ADDR in SDM.
#         MSR_IA32_MC24_ADDR is defined as IA32_MC24_ADDR in SDM.
#         MSR_IA32_MC25_ADDR is defined as IA32_MC25_ADDR in SDM.
#         MSR_IA32_MC26_ADDR is defined as IA32_MC26_ADDR in SDM.
#         MSR_IA32_MC27_ADDR is defined as IA32_MC27_ADDR in SDM.
#         MSR_IA32_MC28_ADDR is defined as IA32_MC28_ADDR in SDM.
#   @{
# **/
# #define MSR_IA32_MC0_ADDR   0x00000402
# #define MSR_IA32_MC1_ADDR   0x00000406
# #define MSR_IA32_MC2_ADDR   0x0000040A
# #define MSR_IA32_MC3_ADDR   0x0000040E
# #define MSR_IA32_MC4_ADDR   0x00000412
# #define MSR_IA32_MC5_ADDR   0x00000416
# #define MSR_IA32_MC6_ADDR   0x0000041A
# #define MSR_IA32_MC7_ADDR   0x0000041E
# #define MSR_IA32_MC8_ADDR   0x00000422
# #define MSR_IA32_MC9_ADDR   0x00000426
# #define MSR_IA32_MC10_ADDR  0x0000042A
# #define MSR_IA32_MC11_ADDR  0x0000042E
# #define MSR_IA32_MC12_ADDR  0x00000432
# #define MSR_IA32_MC13_ADDR  0x00000436
# #define MSR_IA32_MC14_ADDR  0x0000043A
# #define MSR_IA32_MC15_ADDR  0x0000043E
# #define MSR_IA32_MC16_ADDR  0x00000442
# #define MSR_IA32_MC17_ADDR  0x00000446
# #define MSR_IA32_MC18_ADDR  0x0000044A
# #define MSR_IA32_MC19_ADDR  0x0000044E
# #define MSR_IA32_MC20_ADDR  0x00000452
# #define MSR_IA32_MC21_ADDR  0x00000456
# #define MSR_IA32_MC22_ADDR  0x0000045A
# #define MSR_IA32_MC23_ADDR  0x0000045E
# #define MSR_IA32_MC24_ADDR  0x00000462
# #define MSR_IA32_MC25_ADDR  0x00000466
# #define MSR_IA32_MC26_ADDR  0x0000046A
# #define MSR_IA32_MC27_ADDR  0x0000046E
# #define MSR_IA32_MC28_ADDR  0x00000472
MSR_IA32_MC0_ADDR   = 0x00000402
MSR_IA32_MC1_ADDR   = 0x00000406
MSR_IA32_MC2_ADDR   = 0x0000040A
MSR_IA32_MC3_ADDR   = 0x0000040E
MSR_IA32_MC4_ADDR   = 0x00000412
MSR_IA32_MC5_ADDR   = 0x00000416
MSR_IA32_MC6_ADDR   = 0x0000041A
MSR_IA32_MC7_ADDR   = 0x0000041E
MSR_IA32_MC8_ADDR   = 0x00000422
MSR_IA32_MC9_ADDR   = 0x00000426
MSR_IA32_MC10_ADDR  = 0x0000042A
MSR_IA32_MC11_ADDR  = 0x0000042E
MSR_IA32_MC12_ADDR  = 0x00000432
MSR_IA32_MC13_ADDR  = 0x00000436
MSR_IA32_MC14_ADDR  = 0x0000043A
MSR_IA32_MC15_ADDR  = 0x0000043E
MSR_IA32_MC16_ADDR  = 0x00000442
MSR_IA32_MC17_ADDR  = 0x00000446
MSR_IA32_MC18_ADDR  = 0x0000044A
MSR_IA32_MC19_ADDR  = 0x0000044E
MSR_IA32_MC20_ADDR  = 0x00000452
MSR_IA32_MC21_ADDR  = 0x00000456
MSR_IA32_MC22_ADDR  = 0x0000045A
MSR_IA32_MC23_ADDR  = 0x0000045E
MSR_IA32_MC24_ADDR  = 0x00000462
MSR_IA32_MC25_ADDR  = 0x00000466
MSR_IA32_MC26_ADDR  = 0x0000046A
MSR_IA32_MC27_ADDR  = 0x0000046E
MSR_IA32_MC28_ADDR  = 0x00000472

# /// @}
# 
# /**
#   MCn_MISC. If IA32_MCG_CAP.CNT > n.
# 
#   @param  ECX  MSR_IA32_MCn_MISC
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_MC0_MISC);
#   AsmWriteMsr64 (MSR_IA32_MC0_MISC, Msr);
#   @endcode
#   @note MSR_IA32_MC0_MISC  is defined as IA32_MC0_MISC  in SDM.
#         MSR_IA32_MC1_MISC  is defined as IA32_MC1_MISC  in SDM.
#         MSR_IA32_MC2_MISC  is defined as IA32_MC2_MISC  in SDM.
#         MSR_IA32_MC3_MISC  is defined as IA32_MC3_MISC  in SDM.
#         MSR_IA32_MC4_MISC  is defined as IA32_MC4_MISC  in SDM.
#         MSR_IA32_MC5_MISC  is defined as IA32_MC5_MISC  in SDM.
#         MSR_IA32_MC6_MISC  is defined as IA32_MC6_MISC  in SDM.
#         MSR_IA32_MC7_MISC  is defined as IA32_MC7_MISC  in SDM.
#         MSR_IA32_MC8_MISC  is defined as IA32_MC8_MISC  in SDM.
#         MSR_IA32_MC9_MISC  is defined as IA32_MC9_MISC  in SDM.
#         MSR_IA32_MC10_MISC is defined as IA32_MC10_MISC in SDM.
#         MSR_IA32_MC11_MISC is defined as IA32_MC11_MISC in SDM.
#         MSR_IA32_MC12_MISC is defined as IA32_MC12_MISC in SDM.
#         MSR_IA32_MC13_MISC is defined as IA32_MC13_MISC in SDM.
#         MSR_IA32_MC14_MISC is defined as IA32_MC14_MISC in SDM.
#         MSR_IA32_MC15_MISC is defined as IA32_MC15_MISC in SDM.
#         MSR_IA32_MC16_MISC is defined as IA32_MC16_MISC in SDM.
#         MSR_IA32_MC17_MISC is defined as IA32_MC17_MISC in SDM.
#         MSR_IA32_MC18_MISC is defined as IA32_MC18_MISC in SDM.
#         MSR_IA32_MC19_MISC is defined as IA32_MC19_MISC in SDM.
#         MSR_IA32_MC20_MISC is defined as IA32_MC20_MISC in SDM.
#         MSR_IA32_MC21_MISC is defined as IA32_MC21_MISC in SDM.
#         MSR_IA32_MC22_MISC is defined as IA32_MC22_MISC in SDM.
#         MSR_IA32_MC23_MISC is defined as IA32_MC23_MISC in SDM.
#         MSR_IA32_MC24_MISC is defined as IA32_MC24_MISC in SDM.
#         MSR_IA32_MC25_MISC is defined as IA32_MC25_MISC in SDM.
#         MSR_IA32_MC26_MISC is defined as IA32_MC26_MISC in SDM.
#         MSR_IA32_MC27_MISC is defined as IA32_MC27_MISC in SDM.
#         MSR_IA32_MC28_MISC is defined as IA32_MC28_MISC in SDM.
#   @{
# **/
# #define MSR_IA32_MC0_MISC   0x00000403
# #define MSR_IA32_MC1_MISC   0x00000407
# #define MSR_IA32_MC2_MISC   0x0000040B
# #define MSR_IA32_MC3_MISC   0x0000040F
# #define MSR_IA32_MC4_MISC   0x00000413
# #define MSR_IA32_MC5_MISC   0x00000417
# #define MSR_IA32_MC6_MISC   0x0000041B
# #define MSR_IA32_MC7_MISC   0x0000041F
# #define MSR_IA32_MC8_MISC   0x00000423
# #define MSR_IA32_MC9_MISC   0x00000427
# #define MSR_IA32_MC10_MISC  0x0000042B
# #define MSR_IA32_MC11_MISC  0x0000042F
# #define MSR_IA32_MC12_MISC  0x00000433
# #define MSR_IA32_MC13_MISC  0x00000437
# #define MSR_IA32_MC14_MISC  0x0000043B
# #define MSR_IA32_MC15_MISC  0x0000043F
# #define MSR_IA32_MC16_MISC  0x00000443
# #define MSR_IA32_MC17_MISC  0x00000447
# #define MSR_IA32_MC18_MISC  0x0000044B
# #define MSR_IA32_MC19_MISC  0x0000044F
# #define MSR_IA32_MC20_MISC  0x00000453
# #define MSR_IA32_MC21_MISC  0x00000457
# #define MSR_IA32_MC22_MISC  0x0000045B
# #define MSR_IA32_MC23_MISC  0x0000045F
# #define MSR_IA32_MC24_MISC  0x00000463
# #define MSR_IA32_MC25_MISC  0x00000467
# #define MSR_IA32_MC26_MISC  0x0000046B
# #define MSR_IA32_MC27_MISC  0x0000046F
# #define MSR_IA32_MC28_MISC  0x00000473
MSR_IA32_MC0_MISC   = 0x00000403
MSR_IA32_MC1_MISC   = 0x00000407
MSR_IA32_MC2_MISC   = 0x0000040B
MSR_IA32_MC3_MISC   = 0x0000040F
MSR_IA32_MC4_MISC   = 0x00000413
MSR_IA32_MC5_MISC   = 0x00000417
MSR_IA32_MC6_MISC   = 0x0000041B
MSR_IA32_MC7_MISC   = 0x0000041F
MSR_IA32_MC8_MISC   = 0x00000423
MSR_IA32_MC9_MISC   = 0x00000427
MSR_IA32_MC10_MISC  = 0x0000042B
MSR_IA32_MC11_MISC  = 0x0000042F
MSR_IA32_MC12_MISC  = 0x00000433
MSR_IA32_MC13_MISC  = 0x00000437
MSR_IA32_MC14_MISC  = 0x0000043B
MSR_IA32_MC15_MISC  = 0x0000043F
MSR_IA32_MC16_MISC  = 0x00000443
MSR_IA32_MC17_MISC  = 0x00000447
MSR_IA32_MC18_MISC  = 0x0000044B
MSR_IA32_MC19_MISC  = 0x0000044F
MSR_IA32_MC20_MISC  = 0x00000453
MSR_IA32_MC21_MISC  = 0x00000457
MSR_IA32_MC22_MISC  = 0x0000045B
MSR_IA32_MC23_MISC  = 0x0000045F
MSR_IA32_MC24_MISC  = 0x00000463
MSR_IA32_MC25_MISC  = 0x00000467
MSR_IA32_MC26_MISC  = 0x0000046B
MSR_IA32_MC27_MISC  = 0x0000046F
MSR_IA32_MC28_MISC  = 0x00000473

# /// @}
# 
# /**
#   Reporting Register of Basic VMX  Capabilities (R/O) See Appendix A.1, "Basic
#   VMX Information.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_BASIC (0x00000480)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_VMX_BASIC_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_VMX_BASIC);
#   @endcode
#   @note MSR_IA32_VMX_BASIC is defined as IA32_VMX_BASIC in SDM.
# **/
# #define MSR_IA32_VMX_BASIC  0x00000480
MSR_IA32_VMX_BASIC  = 0x00000480

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_VMX_BASIC
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 30:0] VMCS revision identifier used by the processor.  Processors
#     /// that use the same VMCS revision identifier use the same size for VMCS
#     /// regions (see subsequent item on bits 44:32).
#     ///
#     /// @note Earlier versions of this manual specified that the VMCS revision
#     /// identifier was a 32-bit field in bits 31:0 of this MSR. For all
#     /// processors produced prior to this change, bit 31 of this MSR was read
#     /// as 0.
#     ///
#     UINT32    VmcsRevisonId : 31;
#     UINT32    MustBeZero    : 1;
#     ///
#     /// [Bit 44:32] Reports the number of bytes that software should allocate
#     /// for the VMXON region and any VMCS region.  It is a value greater than
#     /// 0 and at most 4096(bit 44 is set if and only if bits 43:32 are clear).
#     ///
#     UINT32    VmcsSize      : 13;
#     UINT32    Reserved1     : 3;
#     ///
#     /// [Bit 48] Indicates the width of the physical addresses that may be used
#     /// for the VMXON region, each VMCS, and data structures referenced by
#     /// pointers in a VMCS (I/O bitmaps, virtual-APIC page, MSR areas for VMX
#     /// transitions).  If the bit is 0, these addresses are limited to the
#     /// processor's physical-address width.  If the bit is 1, these addresses
#     /// are limited to 32 bits. This bit is always 0 for processors that
#     /// support Intel 64 architecture.
#     ///
#     /// @note On processors that support Intel 64 architecture, the pointer
#     /// must not set bits beyond the processor's physical address width.
#     ///
#     UINT32    VmcsAddressWidth : 1;
#     ///
#     /// [Bit 49] If bit 49 is read as 1, the logical processor supports the
#     /// dual-monitor treatment of system-management interrupts and
#     /// system-management mode. See Section 34.15 for details of this treatment.
#     ///
#     UINT32    DualMonitor      : 1;
#     ///
#     /// [Bit 53:50] report the memory type that should be used for the VMCS,
#     /// for data structures referenced by pointers in the VMCS (I/O bitmaps,
#     /// virtual-APIC page, MSR areas for VMX transitions), and for the MSEG
#     /// header. If software needs to access these data structures (e.g., to
#     /// modify the contents of the MSR bitmaps), it can configure the paging
#     /// structures to map them into the linear-address space. If it does so,
#     /// it should establish mappings that use the memory type reported bits
#     /// 53:50 in this MSR.
#     ///
#     /// As of this writing, all processors that support VMX operation indicate
#     /// the write-back type.
#     ///
#     /// If software needs to access these data structures (e.g., to modify
#     /// the contents of the MSR bitmaps), it can configure the paging
#     /// structures to map them into the linear-address space. If it does so,
#     /// it should establish mappings that use the memory type reported in this
#     /// MSR.
#     ///
#     /// @note Alternatively, software may map any of these regions or
#     /// structures with the UC memory type. (This may be necessary for the MSEG
#     /// header.) Doing so is discouraged unless necessary as it will cause the
#     /// performance of software accesses to those structures to suffer.
#     ///
#     ///
#     UINT32    MemoryType       : 4;
#     ///
#     /// [Bit 54] If bit 54 is read as 1, the processor reports information in
#     /// the VM-exit instruction-information field on VM exitsdue to execution
#     /// of the INS and OUTS instructions (see Section 27.2.4). This reporting
#     /// is done only if this bit is read as 1.
#     ///
#     UINT32    InsOutsReporting : 1;
#     ///
#     /// [Bit 55] Bit 55 is read as 1 if any VMX controls that default to 1 may
#     /// be cleared to 0. See Appendix A.2 for details. It also reports support
#     /// for the VMX capability MSRs IA32_VMX_TRUE_PINBASED_CTLS,
#     /// IA32_VMX_TRUE_PROCBASED_CTLS, IA32_VMX_TRUE_EXIT_CTLS, and
#     /// IA32_VMX_TRUE_ENTRY_CTLS. See Appendix A.3.1, Appendix A.3.2,
#     /// Appendix A.4, and Appendix A.5 for details.
#     ///
#     UINT32    VmxControls : 1;
#     UINT32    Reserved2   : 8;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_VMX_BASIC_REGISTER;
class MSR_IA32_VMX_BASIC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmcsRevisonId",       UINT32, 31),
    ("MustBeZero",          UINT32, 1),
    ("VmcsSize",            UINT32, 13),
    ("Reserved1",           UINT32, 3),
    ("VmcsAddressWidth",    UINT32, 1),
    ("DualMonitor",         UINT32, 1),
    ("MemoryType",          UINT32, 4),
    ("InsOutsReporting",    UINT32, 1),
    ("VmxControls",         UINT32, 1),
    ("Reserved2",           UINT32, 8)
  ]

class MSR_IA32_VMX_BASIC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_VMX_BASIC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# ///
# /// @{ Define value for bit field MSR_IA32_VMX_BASIC_REGISTER.MemoryType
# ///
# #define MSR_IA32_VMX_BASIC_REGISTER_MEMORY_TYPE_UNCACHEABLE  0x00
# #define MSR_IA32_VMX_BASIC_REGISTER_MEMORY_TYPE_WRITE_BACK   0x06
# ///
# /// @}
# ///
# 
# /**
#   Capability Reporting Register of Pinbased VM-execution Controls (R/O) See
#   Appendix A.3.1, "Pin-Based VMExecution Controls.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_PINBASED_CTLS (0x00000481)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_PINBASED_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_PINBASED_CTLS is defined as IA32_VMX_PINBASED_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_PINBASED_CTLS  0x00000481
MSR_IA32_VMX_PINBASED_CTLS      = 0x00000481

# 
# /**
#   Capability Reporting Register of Primary  Processor-based VM-execution
#   Controls (R/O) See Appendix A.3.2, "Primary Processor- Based VM-Execution
#   Controls.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_PROCBASED_CTLS (0x00000482)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_PROCBASED_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_PROCBASED_CTLS is defined as IA32_VMX_PROCBASED_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_PROCBASED_CTLS  0x00000482
MSR_IA32_VMX_PROCBASED_CTLS     = 0x00000482

# 
# /**
#   Capability Reporting Register of VM-exit  Controls (R/O) See Appendix A.4,
#   "VM-Exit Controls.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_EXIT_CTLS (0x00000483)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_EXIT_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_EXIT_CTLS is defined as IA32_VMX_EXIT_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_EXIT_CTLS  0x00000483
MSR_IA32_VMX_EXIT_CTLS          = 0x00000483

# 
# /**
#   Capability Reporting Register of VMentry Controls (R/O) See Appendix A.5,
#   "VM-Entry Controls.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_ENTRY_CTLS (0x00000484)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_ENTRY_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_ENTRY_CTLS is defined as IA32_VMX_ENTRY_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_ENTRY_CTLS  0x00000484
MSR_IA32_VMX_ENTRY_CTLS         = 0x00000484

# 
# /**
#   Reporting Register of Miscellaneous VMX Capabilities (R/O) See Appendix A.6,
#   "Miscellaneous Data.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_MISC (0x00000485)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   IA32_VMX_MISC_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_VMX_MISC);
#   @endcode
#   @note MSR_IA32_VMX_MISC is defined as IA32_VMX_MISC in SDM.
# **/
# #define MSR_IA32_VMX_MISC  0x00000485
MSR_IA32_VMX_MISC               = 0x00000485

# 
# /**
#   MSR information returned for MSR index #IA32_VMX_MISC
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 4:0] Reports a value X that specifies the relationship between the
#     /// rate of the VMX-preemption timer and that of the timestamp counter (TSC).
#     /// Specifically, the VMX-preemption timer (if it is active) counts down by
#     /// 1 every time bit X in the TSC changes due to a TSC increment.
#     ///
#     UINT32    VmxTimerRatio                     : 5;
#     ///
#     /// [Bit 5] If bit 5 is read as 1, VM exits store the value of IA32_EFER.LMA
#     /// into the "IA-32e mode guest" VM-entry control;see Section 27.2 for more
#     /// details. This bit is read as 1 on any logical processor that supports
#     /// the 1-setting of the "unrestricted guest" VM-execution control.
#     ///
#     UINT32    VmExitEferLma                     : 1;
#     ///
#     /// [Bit 6] reports (if set) the support for activity state 1 (HLT).
#     ///
#     UINT32    HltActivityStateSupported         : 1;
#     ///
#     /// [Bit 7] reports (if set) the support for activity state 2 (shutdown).
#     ///
#     UINT32    ShutdownActivityStateSupported    : 1;
#     ///
#     /// [Bit 8] reports (if set) the support for activity state 3 (wait-for-SIPI).
#     ///
#     UINT32    WaitForSipiActivityStateSupported : 1;
#     UINT32    Reserved1                         : 5;
#     ///
#     /// [Bit 14] If read as 1, Intel(R) Processor Trace (Intel PT) can be used
#     /// in VMX operation. If the processor supports Intel PT but does not allow
#     /// it to be used in VMX operation, execution of VMXON clears
#     /// IA32_RTIT_CTL.TraceEn (see "VMXON-Enter VMX Operation" in Chapter 30);
#     /// any attempt to set that bit while in VMX operation (including VMX root
#     /// operation) using the WRMSR instruction causes a general-protection
#     /// exception.
#     ///
#     UINT32    ProcessorTraceSupported : 1;
#     ///
#     /// [Bit 15] If read as 1, the RDMSR instruction can be used in system-
#     /// management mode (SMM) to read the IA32_SMBASE MSR (MSR address 9EH).
#     /// See Section 34.15.6.3.
#     ///
#     UINT32    SmBaseMsrSupported      : 1;
#     ///
#     /// [Bits 24:16] Indicate the number of CR3-target values supported by the
#     /// processor. This number is a value between 0 and 256, inclusive (bit 24
#     /// is set if and only if bits 23:16 are clear).
#     ///
#     UINT32    NumberOfCr3TargetValues : 9;
#     ///
#     /// [Bit 27:25] Bits 27:25 is used to compute the recommended maximum
#     /// number of MSRs that should appear in the VM-exit MSR-store list, the
#     /// VM-exit MSR-load list, or the VM-entry MSR-load list. Specifically, if
#     /// the value bits 27:25 of IA32_VMX_MISC is N, then 512 * (N + 1) is the
#     /// recommended maximum number of MSRs to be included in each list. If the
#     /// limit is exceeded, undefined processor behavior may result (including a
#     /// machine check during the VMX transition).
#     ///
#     UINT32    MsrStoreListMaximum    : 3;
#     ///
#     /// [Bit 28] If read as 1, bit 2 of the IA32_SMM_MONITOR_CTL can be set
#     /// to 1. VMXOFF unblocks SMIs unless IA32_SMM_MONITOR_CTL[bit 2] is 1
#     /// (see Section 34.14.4).
#     ///
#     UINT32    BlockSmiSupported      : 1;
#     ///
#     /// [Bit 29] read as 1, software can use VMWRITE to write to any supported
#     /// field in the VMCS; otherwise, VMWRITE cannot be used to modify VM-exit
#     /// information fields.
#     ///
#     UINT32    VmWriteSupported       : 1;
#     ///
#     /// [Bit 30] If read as 1, VM entry allows injection of a software
#     /// interrupt, software exception, or privileged software exception with an
#     /// instruction length of 0.
#     ///
#     UINT32    VmInjectSupported      : 1;
#     UINT32    Reserved2              : 1;
#     ///
#     /// [Bits 63:32] Reports the 32-bit MSEG revision identifier used by the
#     /// processor.
#     ///
#     UINT32    MsegRevisionIdentifier : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } IA32_VMX_MISC_REGISTER;
class IA32_VMX_MISC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VmxTimerRatio",                       UINT32, 5),
    ("VmExitEferLma",                       UINT32, 1),
    ("HltActivityStateSupported",           UINT32, 1),
    ("ShutdownActivityStateSupported",      UINT32, 1),
    ("WaitForSipiActivityStateSupported",   UINT32, 1),
    ("Reserved1",                           UINT32, 5),
    ("ProcessorTraceSupported",             UINT32, 1),
    ("SmBaseMsrSupported",                  UINT32, 1),
    ("NumberOfCr3TargetValues",             UINT32, 9),
    ("MsrStoreListMaximum",                 UINT32, 3),
    ("BlockSmiSupported",                   UINT32, 1),
    ("VmWriteSupported",                    UINT32, 1),
    ("VmInjectSupported",                   UINT32, 1),
    ("Reserved2",                           UINT32, 1),
    ("MsegRevisionIdentifier",              UINT32, 32)
  ]

class IA32_VMX_MISC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    IA32_VMX_MISC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Capability Reporting Register of CR0 Bits Fixed to 0 (R/O) See Appendix A.7,
#   "VMX-Fixed Bits in CR0.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_CR0_FIXED0 (0x00000486)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_CR0_FIXED0);
#   @endcode
#   @note MSR_IA32_VMX_CR0_FIXED0 is defined as IA32_VMX_CR0_FIXED0 in SDM.
# **/
# #define MSR_IA32_VMX_CR0_FIXED0  0x00000486
MSR_IA32_VMX_CR0_FIXED0             = 0x00000486

# 
# /**
#   Capability Reporting Register of CR0 Bits Fixed to 1 (R/O) See Appendix A.7,
#   "VMX-Fixed Bits in CR0.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_CR0_FIXED1 (0x00000487)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_CR0_FIXED1);
#   @endcode
#   @note MSR_IA32_VMX_CR0_FIXED1 is defined as IA32_VMX_CR0_FIXED1 in SDM.
# **/
# #define MSR_IA32_VMX_CR0_FIXED1  0x00000487
# 
# /**
#   Capability Reporting Register of CR4 Bits Fixed to 0 (R/O) See Appendix A.8,
#   "VMX-Fixed Bits in CR4.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_CR4_FIXED0 (0x00000488)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_CR4_FIXED0);
#   @endcode
#   @note MSR_IA32_VMX_CR4_FIXED0 is defined as IA32_VMX_CR4_FIXED0 in SDM.
# **/
# #define MSR_IA32_VMX_CR4_FIXED0  0x00000488
MSR_IA32_VMX_CR4_FIXED0             = 0x00000488

# 
# /**
#   Capability Reporting Register of CR4 Bits Fixed to 1 (R/O) See Appendix A.8,
#   "VMX-Fixed Bits in CR4.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_CR4_FIXED1 (0x00000489)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_CR4_FIXED1);
#   @endcode
#   @note MSR_IA32_VMX_CR4_FIXED1 is defined as IA32_VMX_CR4_FIXED1 in SDM.
# **/
# #define MSR_IA32_VMX_CR4_FIXED1  0x00000489
MSR_IA32_VMX_CR4_FIXED1             = 0x00000489

# 
# /**
#   Capability Reporting Register of VMCS Field Enumeration (R/O) See Appendix
#   A.9, "VMCS Enumeration.". If CPUID.01H:ECX.[5] = 1.
# 
#   @param  ECX  MSR_IA32_VMX_VMCS_ENUM (0x0000048A)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_VMCS_ENUM);
#   @endcode
#   @note MSR_IA32_VMX_VMCS_ENUM is defined as IA32_VMX_VMCS_ENUM in SDM.
# **/
# #define MSR_IA32_VMX_VMCS_ENUM  0x0000048A
MSR_IA32_VMX_VMCS_ENUM              = 0x0000048A

# 
# /**
#   Capability Reporting Register of  Secondary Processor-based  VM-execution
#   Controls (R/O) See Appendix A.3.3, "Secondary Processor- Based VM-Execution
#   Controls.". If ( CPUID.01H:ECX.[5] && IA32_VMX_PROCBASED_C TLS[63]).
# 
#   @param  ECX  MSR_IA32_VMX_PROCBASED_CTLS2 (0x0000048B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_PROCBASED_CTLS2);
#   @endcode
#   @note MSR_IA32_VMX_PROCBASED_CTLS2 is defined as IA32_VMX_PROCBASED_CTLS2 in SDM.
# **/
# #define MSR_IA32_VMX_PROCBASED_CTLS2  0x0000048B
MSR_IA32_VMX_PROCBASED_CTLS2        = 0x0000048B

# 
# /**
#   Capability Reporting Register of EPT and  VPID (R/O) See Appendix A.10,
#   "VPID and EPT Capabilities.". If ( CPUID.01H:ECX.[5] && IA32_VMX_PROCBASED_C
#   TLS[63] && ( IA32_VMX_PROCBASED_C TLS2[33] IA32_VMX_PROCBASED_C TLS2[37]) ).
# 
#   @param  ECX  MSR_IA32_VMX_EPT_VPID_CAP (0x0000048C)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_EPT_VPID_CAP);
#   @endcode
#   @note MSR_IA32_VMX_EPT_VPID_CAP is defined as IA32_VMX_EPT_VPID_CAP in SDM.
# **/
# #define MSR_IA32_VMX_EPT_VPID_CAP  0x0000048C
MSR_IA32_VMX_EPT_VPID_CAP           = 0x0000048C

# 
# /**
#   Capability Reporting Register of Pinbased VM-execution Flex Controls (R/O)
#   See Appendix A.3.1, "Pin-Based VMExecution Controls.". If (
#   CPUID.01H:ECX.[5] = 1 && IA32_VMX_BASIC[55] ).
# 
#   @param  ECX  MSR_IA32_VMX_TRUE_PINBASED_CTLS (0x0000048D)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_TRUE_PINBASED_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_TRUE_PINBASED_CTLS is defined as IA32_VMX_TRUE_PINBASED_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_TRUE_PINBASED_CTLS  0x0000048D
MSR_IA32_VMX_TRUE_PINBASED_CTLS     = 0x0000048D

# 
# /**
#   Capability Reporting Register of Primary  Processor-based VM-execution Flex
#   Controls (R/O) See Appendix A.3.2, "Primary Processor- Based VM-Execution
#   Controls.". If( CPUID.01H:ECX.[5] = 1 && IA32_VMX_BASIC[55] ).
# 
#   @param  ECX  MSR_IA32_VMX_TRUE_PROCBASED_CTLS (0x0000048E)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_TRUE_PROCBASED_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_TRUE_PROCBASED_CTLS is defined as IA32_VMX_TRUE_PROCBASED_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_TRUE_PROCBASED_CTLS  0x0000048E
MSR_IA32_VMX_TRUE_PROCBASED_CTLS    = 0x0000048E

# 
# /**
#   Capability Reporting Register of VM-exit  Flex Controls (R/O) See Appendix
#   A.4, "VM-Exit Controls.". If( CPUID.01H:ECX.[5] = 1 && IA32_VMX_BASIC[55] ).
# 
#   @param  ECX  MSR_IA32_VMX_TRUE_EXIT_CTLS (0x0000048F)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_TRUE_EXIT_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_TRUE_EXIT_CTLS is defined as IA32_VMX_TRUE_EXIT_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_TRUE_EXIT_CTLS  0x0000048F
MSR_IA32_VMX_TRUE_EXIT_CTLS         = 0x0000048F

# 
# /**
#   Capability Reporting Register of VMentry Flex Controls (R/O) See Appendix
#   A.5, "VM-Entry Controls.". If( CPUID.01H:ECX.[5] = 1 && IA32_VMX_BASIC[55] ).
# 
#   @param  ECX  MSR_IA32_VMX_TRUE_ENTRY_CTLS (0x00000490)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_TRUE_ENTRY_CTLS);
#   @endcode
#   @note MSR_IA32_VMX_TRUE_ENTRY_CTLS is defined as IA32_VMX_TRUE_ENTRY_CTLS in SDM.
# **/
# #define MSR_IA32_VMX_TRUE_ENTRY_CTLS  0x00000490
MSR_IA32_VMX_TRUE_ENTRY_CTLS        = 0x00000490

# 
# /**
#   Capability Reporting Register of VMfunction Controls (R/O). If(
#   CPUID.01H:ECX.[5] = 1 && IA32_VMX_BASIC[55] ).
# 
#   @param  ECX  MSR_IA32_VMX_VMFUNC (0x00000491)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_VMX_VMFUNC);
#   @endcode
#   @note MSR_IA32_VMX_VMFUNC is defined as IA32_VMX_VMFUNC in SDM.
# **/
# #define MSR_IA32_VMX_VMFUNC  0x00000491
MSR_IA32_VMX_VMFUNC                 = 0x00000491

# 
# /**
#   Full Width Writable IA32_PMCn Alias (R/W). (If CPUID.0AH: EAX[15:8] > n) &&
#   IA32_PERF_CAPABILITIES[ 13] = 1.
# 
#   @param  ECX  MSR_IA32_A_PMCn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_A_PMC0);
#   AsmWriteMsr64 (MSR_IA32_A_PMC0, Msr);
#   @endcode
#   @note MSR_IA32_A_PMC0 is defined as IA32_A_PMC0 in SDM.
#         MSR_IA32_A_PMC1 is defined as IA32_A_PMC1 in SDM.
#         MSR_IA32_A_PMC2 is defined as IA32_A_PMC2 in SDM.
#         MSR_IA32_A_PMC3 is defined as IA32_A_PMC3 in SDM.
#         MSR_IA32_A_PMC4 is defined as IA32_A_PMC4 in SDM.
#         MSR_IA32_A_PMC5 is defined as IA32_A_PMC5 in SDM.
#         MSR_IA32_A_PMC6 is defined as IA32_A_PMC6 in SDM.
#         MSR_IA32_A_PMC7 is defined as IA32_A_PMC7 in SDM.
#   @{
# **/
# #define MSR_IA32_A_PMC0  0x000004C1
# #define MSR_IA32_A_PMC1  0x000004C2
# #define MSR_IA32_A_PMC2  0x000004C3
# #define MSR_IA32_A_PMC3  0x000004C4
# #define MSR_IA32_A_PMC4  0x000004C5
# #define MSR_IA32_A_PMC5  0x000004C6
# #define MSR_IA32_A_PMC6  0x000004C7
# #define MSR_IA32_A_PMC7  0x000004C8
MSR_IA32_A_PMC0  = 0x000004C1
MSR_IA32_A_PMC1  = 0x000004C2
MSR_IA32_A_PMC2  = 0x000004C3
MSR_IA32_A_PMC3  = 0x000004C4
MSR_IA32_A_PMC4  = 0x000004C5
MSR_IA32_A_PMC5  = 0x000004C6
MSR_IA32_A_PMC6  = 0x000004C7
MSR_IA32_A_PMC7  = 0x000004C8

# /// @}
# 
# /**
#   (R/W). If IA32_MCG_CAP.LMCE_P =1.
# 
#   @param  ECX  MSR_IA32_MCG_EXT_CTL (0x000004D0)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_EXT_CTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_MCG_EXT_CTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_MCG_EXT_CTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_MCG_EXT_CTL);
#   AsmWriteMsr64 (MSR_IA32_MCG_EXT_CTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_MCG_EXT_CTL is defined as IA32_MCG_EXT_CTL in SDM.
# **/
# #define MSR_IA32_MCG_EXT_CTL  0x000004D0
MSR_IA32_MCG_EXT_CTL            = 0x000004D0

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_MCG_EXT_CTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] LMCE_EN.
#     ///
#     UINT32    LMCE_EN   : 1;
#     UINT32    Reserved1 : 31;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_MCG_EXT_CTL_REGISTER;
class MSR_IA32_MCG_EXT_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("LMCE_EN",     UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_MCG_EXT_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_MCG_EXT_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Status and SVN Threshold of SGX Support for ACM (RO). If CPUID.(EAX=07H,
#   ECX=0H): EBX[2] = 1.
# 
#   @param  ECX  MSR_IA32_SGX_SVN_STATUS (0x00000500)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_SGX_SVN_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_SGX_SVN_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_SGX_SVN_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_SGX_SVN_STATUS);
#   @endcode
#   @note MSR_IA32_SGX_SVN_STATUS is defined as IA32_SGX_SVN_STATUS in SDM.
# **/
# #define MSR_IA32_SGX_SVN_STATUS  0x00000500
MSR_IA32_SGX_SVN_STATUS         = 0x00000500

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_SGX_SVN_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Lock. See Section 41.11.3, "Interactions with Authenticated
#     /// Code Modules (ACMs)".
#     ///
#     UINT32    Lock          : 1;
#     UINT32    Reserved1     : 15;
#     ///
#     /// [Bits 23:16] SGX_SVN_SINIT. See Section 41.11.3, "Interactions with
#     /// Authenticated Code Modules (ACMs)".
#     ///
#     UINT32    SGX_SVN_SINIT : 8;
#     UINT32    Reserved2     : 8;
#     UINT32    Reserved3     : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_SGX_SVN_STATUS_REGISTER;
class MSR_IA32_SGX_SVN_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",            UINT32, 1),
    ("Reserved1",       UINT32, 15),
    ("SGX_SVN_SINIT",   UINT32, 8),
    ("Reserved2",       UINT32, 8),
    ("Reserved3",       UINT32, 32)
  ]

class MSR_IA32_SGX_SVN_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_SGX_SVN_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Trace Output Base Register (R/W). If ((CPUID.(EAX=07H, ECX=0):EBX[25] = 1)
#   && ( (CPUID.(EAX=14H,ECX=0): ECX[0] = 1) (CPUID.(EAX=14H,ECX=0): ECX[2] = 1)
#   ) ).
# 
#   @param  ECX  MSR_IA32_RTIT_OUTPUT_BASE (0x00000560)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_OUTPUT_BASE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_OUTPUT_BASE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_OUTPUT_BASE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_OUTPUT_BASE);
#   AsmWriteMsr64 (MSR_IA32_RTIT_OUTPUT_BASE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_OUTPUT_BASE is defined as IA32_RTIT_OUTPUT_BASE in SDM.
# **/
# #define MSR_IA32_RTIT_OUTPUT_BASE  0x00000560
MSR_IA32_RTIT_OUTPUT_BASE       = 0x00000560

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_RTIT_OUTPUT_BASE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved : 7;
#     ///
#     /// [Bits 31:7] Base physical address.
#     ///
#     UINT32    Base     : 25;
#     ///
#     /// [Bits 63:32] Base physical address.
#     ///
#     UINT32    BaseHi   : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_OUTPUT_BASE_REGISTER;
class MSR_IA32_RTIT_OUTPUT_BASE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 7),
    ("Base",        UINT32, 25),
    ("BaseHi",      UINT32, 32)
  ]

class MSR_IA32_RTIT_OUTPUT_BASE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_OUTPUT_BASE_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Trace Output Mask Pointers Register (R/W). If ((CPUID.(EAX=07H,
#   ECX=0):EBX[25] = 1) && ( (CPUID.(EAX=14H,ECX=0): ECX[0] = 1)
#   (CPUID.(EAX=14H,ECX=0): ECX[2] = 1) ) ).
# 
#   @param  ECX  MSR_IA32_RTIT_OUTPUT_MASK_PTRS (0x00000561)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_OUTPUT_MASK_PTRS);
#   AsmWriteMsr64 (MSR_IA32_RTIT_OUTPUT_MASK_PTRS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_OUTPUT_MASK_PTRS is defined as IA32_RTIT_OUTPUT_MASK_PTRS in SDM.
# **/
# #define MSR_IA32_RTIT_OUTPUT_MASK_PTRS  0x00000561
MSR_IA32_RTIT_OUTPUT_MASK_PTRS  = 0x00000561

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_RTIT_OUTPUT_MASK_PTRS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved          : 7;
#     ///
#     /// [Bits 31:7] MaskOrTableOffset.
#     ///
#     UINT32    MaskOrTableOffset : 25;
#     ///
#     /// [Bits 63:32] Output Offset.
#     ///
#     UINT32    OutputOffset      : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER;
class MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",            UINT32, 7),
    ("MaskOrTableOffset",   UINT32, 25),
    ("OutputOffset",        UINT32, 32)
  ]

class MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_OUTPUT_MASK_PTRS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Format of ToPA table entries.
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] END. See Section 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    END       : 1;
#     UINT32    Reserved1 : 1;
#     ///
#     /// [Bit 2] INT. See Section 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    INT       : 1;
#     UINT32    Reserved2 : 1;
#     ///
#     /// [Bit 4] STOP. See Section 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    STOP      : 1;
#     UINT32    Reserved3 : 1;
#     ///
#     /// [Bit 6:9] Indicates the size of the associated output region. See Section
#     /// 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    Size      : 4;
#     UINT32    Reserved4 : 2;
#     ///
#     /// [Bit 12:31] Output Region Base Physical Address low part.
#     /// [Bit 12:31] Output Region Base Physical Address [12:63] value to match.
#     /// ATTENTION: The size of the address field is determined by the processor's
#     /// physical-address width (MAXPHYADDR) in bits, as reported in
#     /// CPUID.80000008H:EAX[7:0]. the above part of address reserved.
#     /// True address field is [12:MAXPHYADDR-1], [MAXPHYADDR:63] is reserved part.
#     /// Detail see Section 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    Base : 20;
#     ///
#     /// [Bit 32:63] Output Region Base Physical Address high part.
#     /// [Bit 32:63] Output Region Base Physical Address [12:63] value to match.
#     /// ATTENTION: The size of the address field is determined by the processor's
#     /// physical-address width (MAXPHYADDR) in bits, as reported in
#     /// CPUID.80000008H:EAX[7:0]. the above part of address reserved.
#     /// True address field is [12:MAXPHYADDR-1], [MAXPHYADDR:63] is reserved part.
#     /// Detail see Section 35.2.6.2, "Table of Physical Addresses (ToPA)".
#     ///
#     UINT32    BaseHi : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } RTIT_TOPA_TABLE_ENTRY;
class RTIT_TOPA_TABLE_ENTRY_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("END",         UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("INT",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("STOP",        UINT32, 1),
    ("Reserved3",   UINT32, 1),
    ("Size",        UINT32, 4),
    ("Reserved4",   UINT32, 2),
    ("Base",        UINT32, 20),
    ("BaseHi",      UINT32, 32)
  ]

class RTIT_TOPA_TABLE_ENTRY (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    RTIT_TOPA_TABLE_ENTRY_Bits),
    ("Uint64",  UINT64)
  ]

# 
# ///
# /// The size of the associated output region usd by Topa.
# ///
# typedef enum {
#   RtitTopaMemorySize4K = 0,
#   RtitTopaMemorySize8K,
#   RtitTopaMemorySize16K,
#   RtitTopaMemorySize32K,
#   RtitTopaMemorySize64K,
#   RtitTopaMemorySize128K,
#   RtitTopaMemorySize256K,
#   RtitTopaMemorySize512K,
#   RtitTopaMemorySize1M,
#   RtitTopaMemorySize2M,
#   RtitTopaMemorySize4M,
#   RtitTopaMemorySize8M,
#   RtitTopaMemorySize16M,
#   RtitTopaMemorySize32M,
#   RtitTopaMemorySize64M,
#   RtitTopaMemorySize128M
# } RTIT_TOPA_MEMORY_SIZE;
RtitTopaMemorySize4K    = 0
RtitTopaMemorySize8K    = 1 
RtitTopaMemorySize16K   = 2 
RtitTopaMemorySize32K   = 3 
RtitTopaMemorySize64K   = 4 
RtitTopaMemorySize128K  = 5 
RtitTopaMemorySize256K  = 6 
RtitTopaMemorySize512K  = 7 
RtitTopaMemorySize1M    = 8 
RtitTopaMemorySize2M    = 9 
RtitTopaMemorySize4M    = 10
RtitTopaMemorySize8M    = 11
RtitTopaMemorySize16M   = 12
RtitTopaMemorySize32M   = 13
RtitTopaMemorySize64M   = 14
RtitTopaMemorySize128M  = 15
RTIT_TOPA_MEMORY_SIZE   = ENUM

# 
# /**
#   Trace Control Register (R/W). If (CPUID.(EAX=07H, ECX=0):EBX[25] = 1).
# 
#   @param  ECX  MSR_IA32_RTIT_CTL (0x00000570)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_CTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_CTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_CTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_CTL);
#   AsmWriteMsr64 (MSR_IA32_RTIT_CTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_CTL is defined as IA32_RTIT_CTL in SDM.
# **/
# #define MSR_IA32_RTIT_CTL  0x00000570
MSR_IA32_RTIT_CTL               = 0x00000570

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_RTIT_CTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] TraceEn.
#     ///
#     UINT32    TraceEn   : 1;
#     ///
#     /// [Bit 1] CYCEn. If (CPUID.(EAX=07H, ECX=0):EBX[1] = 1).
#     ///
#     UINT32    CYCEn     : 1;
#     ///
#     /// [Bit 2] OS.
#     ///
#     UINT32    OS        : 1;
#     ///
#     /// [Bit 3] User.
#     ///
#     UINT32    User      : 1;
#     ///
#     /// [Bit 4] PwrEvtEn.
#     ///
#     UINT32    PwrEvtEn  : 1;
#     ///
#     /// [Bit 5] FUPonPTW.
#     ///
#     UINT32    FUPonPTW  : 1;
#     ///
#     /// [Bit 6] FabricEn. If (CPUID.(EAX=07H, ECX=0):ECX[3] = 1).
#     ///
#     UINT32    FabricEn  : 1;
#     ///
#     /// [Bit 7] CR3 filter.
#     ///
#     UINT32    CR3       : 1;
#     ///
#     /// [Bit 8] ToPA.
#     ///
#     UINT32    ToPA      : 1;
#     ///
#     /// [Bit 9] MTCEn. If (CPUID.(EAX=07H, ECX=0):EBX[3] = 1).
#     ///
#     UINT32    MTCEn     : 1;
#     ///
#     /// [Bit 10] TSCEn.
#     ///
#     UINT32    TSCEn     : 1;
#     ///
#     /// [Bit 11] DisRETC.
#     ///
#     UINT32    DisRETC   : 1;
#     ///
#     /// [Bit 12] PTWEn.
#     ///
#     UINT32    PTWEn     : 1;
#     ///
#     /// [Bit 13] BranchEn.
#     ///
#     UINT32    BranchEn  : 1;
#     ///
#     /// [Bits 17:14] MTCFreq. If (CPUID.(EAX=07H, ECX=0):EBX[3] = 1).
#     ///
#     UINT32    MTCFreq   : 4;
#     UINT32    Reserved3 : 1;
#     ///
#     /// [Bits 22:19] CYCThresh. If (CPUID.(EAX=07H, ECX=0):EBX[1] = 1).
#     ///
#     UINT32    CYCThresh : 4;
#     UINT32    Reserved4 : 1;
#     ///
#     /// [Bits 27:24] PSBFreq. If (CPUID.(EAX=07H, ECX=0):EBX[1] = 1).
#     ///
#     UINT32    PSBFreq   : 4;
#     UINT32    Reserved5 : 4;
#     ///
#     /// [Bits 35:32] ADDR0_CFG. If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > 0).
#     ///
#     UINT32    ADDR0_CFG : 4;
#     ///
#     /// [Bits 39:36] ADDR1_CFG. If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > 1).
#     ///
#     UINT32    ADDR1_CFG : 4;
#     ///
#     /// [Bits 43:40] ADDR2_CFG. If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > 2).
#     ///
#     UINT32    ADDR2_CFG : 4;
#     ///
#     /// [Bits 47:44] ADDR3_CFG. If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > 3).
#     ///
#     UINT32    ADDR3_CFG : 4;
#     UINT32    Reserved6 : 16;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_CTL_REGISTER;
class MSR_IA32_RTIT_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("TraceEn",     UINT32, 1),
    ("CYCEn",       UINT32, 1),
    ("OS",          UINT32, 1),
    ("User",        UINT32, 1),
    ("PwrEvtEn",    UINT32, 1),
    ("FUPonPTW",    UINT32, 1),
    ("FabricEn",    UINT32, 1),
    ("CR3",         UINT32, 1),
    ("ToPA",        UINT32, 1),
    ("MTCEn",       UINT32, 1),
    ("TSCEn",       UINT32, 1),
    ("DisRETC",     UINT32, 1),
    ("PTWEn",       UINT32, 1),
    ("BranchEn",    UINT32, 1),
    ("MTCFreq",     UINT32, 4),
    ("Reserved3",   UINT32, 1),
    ("CYCThresh",   UINT32, 4),
    ("Reserved4",   UINT32, 1),
    ("PSBFreq",     UINT32, 4),
    ("Reserved5",   UINT32, 4),
    ("ADDR0_CFG",   UINT32, 4),
    ("ADDR1_CFG",   UINT32, 4),
    ("ADDR2_CFG",   UINT32, 4),
    ("ADDR3_CFG",   UINT32, 4),
    ("Reserved6",   UINT32, 16)
  ]

class MSR_IA32_RTIT_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_CTL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Tracing Status Register (R/W). If (CPUID.(EAX=07H, ECX=0):EBX[25] = 1).
# 
#   @param  ECX  MSR_IA32_RTIT_STATUS (0x00000571)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_STATUS);
#   AsmWriteMsr64 (MSR_IA32_RTIT_STATUS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_STATUS is defined as IA32_RTIT_STATUS in SDM.
# **/
# #define MSR_IA32_RTIT_STATUS  0x00000571
# 
# /**
#   MSR information returned for MSR index #MSR_IA32_RTIT_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] FilterEn, (writes ignored).
#     /// If (CPUID.(EAX=07H, ECX=0):EBX[2] = 1).
#     ///
#     UINT32    FilterEn      : 1;
#     ///
#     /// [Bit 1] ContexEn, (writes ignored).
#     ///
#     UINT32    ContexEn      : 1;
#     ///
#     /// [Bit 2] TriggerEn, (writes ignored).
#     ///
#     UINT32    TriggerEn     : 1;
#     UINT32    Reserved1     : 1;
#     ///
#     /// [Bit 4] Error.
#     ///
#     UINT32    Error         : 1;
#     ///
#     /// [Bit 5] Stopped.
#     ///
#     UINT32    Stopped       : 1;
#     UINT32    Reserved2     : 26;
#     ///
#     /// [Bits 48:32] PacketByteCnt. If (CPUID.(EAX=07H, ECX=0):EBX[1] > 3).
#     ///
#     UINT32    PacketByteCnt : 17;
#     UINT32    Reserved3     : 15;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_STATUS_REGISTER;
class MSR_IA32_RTIT_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("FilterEn",        UINT32, 1),
    ("ContexEn",        UINT32, 1),
    ("TriggerEn",       UINT32, 1),
    ("Reserved1",       UINT32, 1),
    ("Error",           UINT32, 1),
    ("Stopped",         UINT32, 1),
    ("Reserved2",       UINT32, 26),
    ("PacketByteCnt",   UINT32, 17),
    ("Reserved3",       UINT32, 15)
  ]

class MSR_IA32_RTIT_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_STATUS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Trace Filter CR3 Match Register (R/W).
#   If (CPUID.(EAX=07H, ECX=0):EBX[25] = 1).
# 
#   @param  ECX  MSR_IA32_RTIT_CR3_MATCH (0x00000572)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_CR3_MATCH_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_CR3_MATCH_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_CR3_MATCH_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_CR3_MATCH);
#   AsmWriteMsr64 (MSR_IA32_RTIT_CR3_MATCH, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_CR3_MATCH is defined as IA32_RTIT_CR3_MATCH in SDM.
# **/
# #define MSR_IA32_RTIT_CR3_MATCH  0x00000572
MSR_IA32_RTIT_CR3_MATCH         = 0x00000572

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_RTIT_CR3_MATCH
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved : 5;
#     ///
#     /// [Bits 31:5] CR3[63:5] value to match.
#     ///
#     UINT32    Cr3      : 27;
#     ///
#     /// [Bits 63:32] CR3[63:5] value to match.
#     ///
#     UINT32    Cr3Hi    : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_CR3_MATCH_REGISTER;
class MSR_IA32_RTIT_CR3_MATCH_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved",    UINT32, 5),
    ("Cr3",         UINT32, 27),
    ("Cr3Hi",       UINT32, 32)
  ]

class MSR_IA32_RTIT_CR3_MATCH_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_CR3_MATCH_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Region n Start Address (R/W). If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > n).
# 
#   @param  ECX  MSR_IA32_RTIT_ADDRn_A
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_ADDR_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_ADDR_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_ADDR_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_ADDR0_A);
#   AsmWriteMsr64 (MSR_IA32_RTIT_ADDR0_A, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_ADDR0_A is defined as IA32_RTIT_ADDR0_A in SDM.
#         MSR_IA32_RTIT_ADDR1_A is defined as IA32_RTIT_ADDR1_A in SDM.
#         MSR_IA32_RTIT_ADDR2_A is defined as IA32_RTIT_ADDR2_A in SDM.
#         MSR_IA32_RTIT_ADDR3_A is defined as IA32_RTIT_ADDR3_A in SDM.
#   @{
# **/
# #define MSR_IA32_RTIT_ADDR0_A  0x00000580
# #define MSR_IA32_RTIT_ADDR1_A  0x00000582
# #define MSR_IA32_RTIT_ADDR2_A  0x00000584
# #define MSR_IA32_RTIT_ADDR3_A  0x00000586
MSR_IA32_RTIT_ADDR0_A  = 0x00000580
MSR_IA32_RTIT_ADDR1_A  = 0x00000582
MSR_IA32_RTIT_ADDR2_A  = 0x00000584
MSR_IA32_RTIT_ADDR3_A  = 0x00000586

# /// @}
# 
# /**
#   Region n End Address (R/W). If (CPUID.(EAX=07H, ECX=1):EAX[2:0] > n).
# 
#   @param  ECX  MSR_IA32_RTIT_ADDRn_B
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_ADDR_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_RTIT_ADDR_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_RTIT_ADDR_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_RTIT_ADDR0_B);
#   AsmWriteMsr64 (MSR_IA32_RTIT_ADDR0_B, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_RTIT_ADDR0_B is defined as IA32_RTIT_ADDR0_B in SDM.
#         MSR_IA32_RTIT_ADDR1_B is defined as IA32_RTIT_ADDR1_B in SDM.
#         MSR_IA32_RTIT_ADDR2_B is defined as IA32_RTIT_ADDR2_B in SDM.
#         MSR_IA32_RTIT_ADDR3_B is defined as IA32_RTIT_ADDR3_B in SDM.
#   @{
# **/
# #define MSR_IA32_RTIT_ADDR0_B  0x00000581
# #define MSR_IA32_RTIT_ADDR1_B  0x00000583
# #define MSR_IA32_RTIT_ADDR2_B  0x00000585
# #define MSR_IA32_RTIT_ADDR3_B  0x00000587
MSR_IA32_RTIT_ADDR0_B  = 0x00000581
MSR_IA32_RTIT_ADDR1_B  = 0x00000583
MSR_IA32_RTIT_ADDR2_B  = 0x00000585
MSR_IA32_RTIT_ADDR3_B  = 0x00000587

# /// @}
# 
# /**
#   MSR information returned for MSR indexes
#   #MSR_IA32_RTIT_ADDR0_A to #MSR_IA32_RTIT_ADDR3_A and
#   #MSR_IA32_RTIT_ADDR0_B to #MSR_IA32_RTIT_ADDR3_B
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Virtual Address.
#     ///
#     UINT32    VirtualAddress   : 32;
#     ///
#     /// [Bits 47:32] Virtual Address.
#     ///
#     UINT32    VirtualAddressHi : 16;
#     ///
#     /// [Bits 63:48] SignExt_VA.
#     ///
#     UINT32    SignExt_VA       : 16;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_RTIT_ADDR_REGISTER;
class MSR_IA32_RTIT_ADDR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("VirtualAddress",      UINT32, 32),
    ("VirtualAddressHi",    UINT32, 16),
    ("SignExt_VA",          UINT32, 16)
  ]

class MSR_IA32_RTIT_ADDR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_RTIT_ADDR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   DS Save Area (R/W) Points to the linear address of the first byte of the DS
#   buffer management area, which is used to manage the BTS and PEBS buffers.
#   See Section 18.6.3.4, "Debug Store (DS) Mechanism.". If(
#   CPUID.01H:EDX.DS[21] = 1. The linear address of the first byte of the DS
#   buffer management area, if IA-32e mode is active.
# 
#   @param  ECX  MSR_IA32_DS_AREA (0x00000600)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_DS_AREA_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_DS_AREA_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_DS_AREA);
#   AsmWriteMsr64 (MSR_IA32_DS_AREA, Msr);
#   @endcode
#   @note MSR_IA32_DS_AREA is defined as IA32_DS_AREA in SDM.
# **/
# #define MSR_IA32_DS_AREA  0x00000600
MSR_IA32_DS_AREA                = 0x00000600

# 
# /**
#   TSC Target of Local APIC's TSC Deadline Mode (R/W). If CPUID.01H:ECX.[24] =
#   1.
# 
#   @param  ECX  MSR_IA32_TSC_DEADLINE (0x000006E0)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_TSC_DEADLINE);
#   AsmWriteMsr64 (MSR_IA32_TSC_DEADLINE, Msr);
#   @endcode
#   @note MSR_IA32_TSC_DEADLINE is defined as IA32_TSC_DEADLINE in SDM.
# **/
# #define MSR_IA32_TSC_DEADLINE  0x000006E0
MSR_IA32_TSC_DEADLINE           = 0x000006E0

# 
# /**
#   Enable/disable HWP (R/W). If CPUID.06H:EAX.[7] = 1.
# 
#   @param  ECX  MSR_IA32_PM_ENABLE (0x00000770)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PM_ENABLE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PM_ENABLE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PM_ENABLE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PM_ENABLE);
#   AsmWriteMsr64 (MSR_IA32_PM_ENABLE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PM_ENABLE is defined as IA32_PM_ENABLE in SDM.
# **/
# #define MSR_IA32_PM_ENABLE  0x00000770
MSR_IA32_PM_ENABLE              = 0x00000770

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PM_ENABLE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] HWP_ENABLE (R/W1-Once). See Section 14.4.2, "Enabling HWP". If
#     /// CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    HWP_ENABLE : 1;
#     UINT32    Reserved1  : 31;
#     UINT32    Reserved2  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PM_ENABLE_REGISTER;
class MSR_IA32_PM_ENABLE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HWP_ENABLE",  UINT32, 1),
    ("Reserved1",   UINT32, 31),
    ("Reserved2",   UINT32, 32)
  ]

class MSR_IA32_PM_ENABLE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PM_ENABLE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   HWP Performance Range Enumeration (RO). If CPUID.06H:EAX.[7] = 1.
# 
#   @param  ECX  MSR_IA32_HWP_CAPABILITIES (0x00000771)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_CAPABILITIES_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_CAPABILITIES_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_HWP_CAPABILITIES_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_HWP_CAPABILITIES);
#   @endcode
#   @note MSR_IA32_HWP_CAPABILITIES is defined as IA32_HWP_CAPABILITIES in SDM.
# **/
# #define MSR_IA32_HWP_CAPABILITIES  0x00000771
MSR_IA32_HWP_CAPABILITIES       = 0x00000771

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_HWP_CAPABILITIES
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Highest_Performance See Section 14.4.3, "HWP Performance
#     /// Range and Dynamic Capabilities". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Highest_Performance        : 8;
#     ///
#     /// [Bits 15:8] Guaranteed_Performance See Section 14.4.3, "HWP
#     /// Performance Range and Dynamic Capabilities". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Guaranteed_Performance     : 8;
#     ///
#     /// [Bits 23:16] Most_Efficient_Performance See Section 14.4.3, "HWP
#     /// Performance Range and Dynamic Capabilities". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Most_Efficient_Performance : 8;
#     ///
#     /// [Bits 31:24] Lowest_Performance See Section 14.4.3, "HWP Performance
#     /// Range and Dynamic Capabilities". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Lowest_Performance         : 8;
#     UINT32    Reserved                   : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_HWP_CAPABILITIES_REGISTER;
class MSR_IA32_HWP_CAPABILITIES_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Highest_Performance",         UINT32, 8),
    ("Guaranteed_Performance",      UINT32, 8),
    ("Most_Efficient_Performance",  UINT32, 8),
    ("Lowest_Performance",          UINT32, 8),
    ("Reserved",                    UINT32, 32)
  ]

class MSR_IA32_HWP_CAPABILITIES_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_CAPABILITIES_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Power Management Control Hints for All Logical Processors in a Package
#   (R/W). If CPUID.06H:EAX.[11] = 1.
# 
#   @param  ECX  MSR_IA32_HWP_REQUEST_PKG (0x00000772)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_REQUEST_PKG_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_REQUEST_PKG_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_HWP_REQUEST_PKG_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_HWP_REQUEST_PKG);
#   AsmWriteMsr64 (MSR_IA32_HWP_REQUEST_PKG, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_HWP_REQUEST_PKG is defined as IA32_HWP_REQUEST_PKG in SDM.
# **/
# #define MSR_IA32_HWP_REQUEST_PKG  0x00000772
MSR_IA32_HWP_REQUEST_PKG        = 0x00000772

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_HWP_REQUEST_PKG
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Minimum_Performance See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[11] = 1.
#     ///
#     UINT32    Minimum_Performance           : 8;
#     ///
#     /// [Bits 15:8] Maximum_Performance See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[11] = 1.
#     ///
#     UINT32    Maximum_Performance           : 8;
#     ///
#     /// [Bits 23:16] Desired_Performance See Section 14.4.4, "Managing HWP".
#     /// If CPUID.06H:EAX.[11] = 1.
#     ///
#     UINT32    Desired_Performance           : 8;
#     ///
#     /// [Bits 31:24] Energy_Performance_Preference See Section 14.4.4,
#     /// "Managing HWP". If CPUID.06H:EAX.[11] = 1 && CPUID.06H:EAX.[10] = 1.
#     ///
#     UINT32    Energy_Performance_Preference : 8;
#     ///
#     /// [Bits 41:32] Activity_Window See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[11] = 1 && CPUID.06H:EAX.[9] = 1.
#     ///
#     UINT32    Activity_Window               : 10;
#     UINT32    Reserved                      : 22;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_HWP_REQUEST_PKG_REGISTER;
class MSR_IA32_HWP_REQUEST_PKG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Minimum_Performance",             UINT32, 8),
    ("Maximum_Performance",             UINT32, 8),
    ("Desired_Performance",             UINT32, 8),
    ("Energy_Performance_Preference",   UINT32, 8),
    ("Activity_Window",                 UINT32, 10),
    ("Reserved",                        UINT32, 22)
  ]

class MSR_IA32_HWP_REQUEST_PKG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_REQUEST_PKG_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Control HWP Native Interrupts (R/W). If CPUID.06H:EAX.[8] = 1.
# 
#   @param  ECX  MSR_IA32_HWP_INTERRUPT (0x00000773)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_INTERRUPT_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_INTERRUPT_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_HWP_INTERRUPT_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_HWP_INTERRUPT);
#   AsmWriteMsr64 (MSR_IA32_HWP_INTERRUPT, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_HWP_INTERRUPT is defined as IA32_HWP_INTERRUPT in SDM.
# **/
# #define MSR_IA32_HWP_INTERRUPT  0x00000773
MSR_IA32_HWP_INTERRUPT          = 0x00000773

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_HWP_INTERRUPT
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] EN_Guaranteed_Performance_Change. See Section 14.4.6, "HWP
#     /// Notifications". If CPUID.06H:EAX.[8] = 1.
#     ///
#     UINT32    EN_Guaranteed_Performance_Change : 1;
#     ///
#     /// [Bit 1] EN_Excursion_Minimum. See Section 14.4.6, "HWP Notifications".
#     /// If CPUID.06H:EAX.[8] = 1.
#     ///
#     UINT32    EN_Excursion_Minimum             : 1;
#     UINT32    Reserved1                        : 30;
#     UINT32    Reserved2                        : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_HWP_INTERRUPT_REGISTER;
class MSR_IA32_HWP_INTERRUPT_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN_Guaranteed_Performance_Change",    UINT32, 1),
    ("EN_Excursion_Minimum",                UINT32, 1),
    ("Reserved1",                           UINT32, 30),
    ("Reserved2",                           UINT32, 32)
  ]

class MSR_IA32_HWP_INTERRUPT_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_INTERRUPT_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Power Management Control Hints to a Logical Processor (R/W). If
#   CPUID.06H:EAX.[7] = 1.
# 
#   @param  ECX  MSR_IA32_HWP_REQUEST (0x00000774)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_REQUEST_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_REQUEST_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_HWP_REQUEST_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_HWP_REQUEST);
#   AsmWriteMsr64 (MSR_IA32_HWP_REQUEST, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_HWP_REQUEST is defined as IA32_HWP_REQUEST in SDM.
# **/
# #define MSR_IA32_HWP_REQUEST  0x00000774
MSR_IA32_HWP_REQUEST            = 0x00000774

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_HWP_REQUEST
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Minimum_Performance See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Minimum_Performance           : 8;
#     ///
#     /// [Bits 15:8] Maximum_Performance See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Maximum_Performance           : 8;
#     ///
#     /// [Bits 23:16] Desired_Performance See Section 14.4.4, "Managing HWP".
#     /// If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Desired_Performance           : 8;
#     ///
#     /// [Bits 31:24] Energy_Performance_Preference See Section 14.4.4,
#     /// "Managing HWP". If CPUID.06H:EAX.[7] = 1 && CPUID.06H:EAX.[10] = 1.
#     ///
#     UINT32    Energy_Performance_Preference : 8;
#     ///
#     /// [Bits 41:32] Activity_Window See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[7] = 1 && CPUID.06H:EAX.[9] = 1.
#     ///
#     UINT32    Activity_Window               : 10;
#     ///
#     /// [Bit 42] Package_Control See Section 14.4.4, "Managing HWP". If
#     /// CPUID.06H:EAX.[7] = 1 && CPUID.06H:EAX.[11] = 1.
#     ///
#     UINT32    Package_Control               : 1;
#     UINT32    Reserved                      : 21;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_HWP_REQUEST_REGISTER;
class MSR_IA32_HWP_REQUEST_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Minimum_Performance",             UINT32, 8),
    ("Maximum_Performance",             UINT32, 8),
    ("Desired_Performance",             UINT32, 8),
    ("Energy_Performance_Preference",   UINT32, 8),
    ("Activity_Window",                 UINT32, 10),
    ("Package_Control",                 UINT32, 1),
    ("Reserved",                        UINT32, 21)
  ]

class MSR_IA32_HWP_REQUEST_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_REQUEST_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Log bits indicating changes to  Guaranteed & excursions to Minimum (R/W). If
#   CPUID.06H:EAX.[7] = 1.
# 
#   @param  ECX  MSR_IA32_HWP_STATUS (0x00000777)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_STATUS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_HWP_STATUS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_HWP_STATUS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_HWP_STATUS);
#   AsmWriteMsr64 (MSR_IA32_HWP_STATUS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_HWP_STATUS is defined as IA32_HWP_STATUS in SDM.
# **/
# #define MSR_IA32_HWP_STATUS  0x00000777
MSR_IA32_HWP_STATUS             = 0x00000777

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_HWP_STATUS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Guaranteed_Performance_Change (R/WC0). See Section 14.4.5,
#     /// "HWP Feedback". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Guaranteed_Performance_Change : 1;
#     UINT32    Reserved1                     : 1;
#     ///
#     /// [Bit 2] Excursion_To_Minimum (R/WC0). See Section 14.4.5, "HWP
#     /// Feedback". If CPUID.06H:EAX.[7] = 1.
#     ///
#     UINT32    Excursion_To_Minimum          : 1;
#     UINT32    Reserved2                     : 29;
#     UINT32    Reserved3                     : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_HWP_STATUS_REGISTER;
class MSR_IA32_HWP_STATUS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Guaranteed_Performance_Change",   UINT32, 1),
    ("Reserved1",                       UINT32, 1),
    ("Excursion_To_Minimum",            UINT32, 1),
    ("Reserved2",                       UINT32, 29),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_HWP_STATUS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_HWP_STATUS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   x2APIC ID Register (R/O) See x2APIC Specification. If CPUID.01H:ECX[21] = 1
#   && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_APICID (0x00000802)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_APICID);
#   @endcode
#   @note MSR_IA32_X2APIC_APICID is defined as IA32_X2APIC_APICID in SDM.
# **/
# #define MSR_IA32_X2APIC_APICID  0x00000802
MSR_IA32_X2APIC_APICID      = 0x00000802

# 
# /**
#   x2APIC Version Register (R/O). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_VERSION (0x00000803)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_VERSION);
#   @endcode
#   @note MSR_IA32_X2APIC_VERSION is defined as IA32_X2APIC_VERSION in SDM.
# **/
# #define MSR_IA32_X2APIC_VERSION  0x00000803
MSR_IA32_X2APIC_VERSION     = 0x00000803

# 
# /**
#   x2APIC Task Priority Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_TPR (0x00000808)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_TPR);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_TPR, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_TPR is defined as IA32_X2APIC_TPR in SDM.
# **/
# #define MSR_IA32_X2APIC_TPR  0x00000808
MSR_IA32_X2APIC_TPR         = 0x00000808

# 
# /**
#   x2APIC Processor Priority Register (R/O). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_PPR (0x0000080A)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_PPR);
#   @endcode
#   @note MSR_IA32_X2APIC_PPR is defined as IA32_X2APIC_PPR in SDM.
# **/
# #define MSR_IA32_X2APIC_PPR  0x0000080A
MSR_IA32_X2APIC_PPR         = 0x0000080A

# 
# /**
#   x2APIC EOI Register (W/O). If CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10]
#   = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_EOI (0x0000080B)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = 0;
#   AsmWriteMsr64 (MSR_IA32_X2APIC_EOI, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_EOI is defined as IA32_X2APIC_EOI in SDM.
# **/
# #define MSR_IA32_X2APIC_EOI  0x0000080B
MSR_IA32_X2APIC_EOI         = 0x0000080B

# 
# /**
#   x2APIC Logical Destination Register (R/O). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LDR (0x0000080D)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LDR);
#   @endcode
#   @note MSR_IA32_X2APIC_LDR is defined as IA32_X2APIC_LDR in SDM.
# **/
# #define MSR_IA32_X2APIC_LDR  0x0000080D
MSR_IA32_X2APIC_LDR         = 0x0000080D

# 
# /**
#   x2APIC Spurious Interrupt Vector Register (R/W). If CPUID.01H:ECX.[21] = 1
#   && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_SIVR (0x0000080F)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_SIVR);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_SIVR, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_SIVR is defined as IA32_X2APIC_SIVR in SDM.
# **/
# #define MSR_IA32_X2APIC_SIVR  0x0000080F
MSR_IA32_X2APIC_SIVR        = 0x0000080F

# 
# /**
#   x2APIC In-Service Register Bits (n * 32 + 31):(n * 32) (R/O).
#   If CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_ISRn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_ISR0);
#   @endcode
#   @note MSR_IA32_X2APIC_ISR0 is defined as IA32_X2APIC_ISR0 in SDM.
#         MSR_IA32_X2APIC_ISR1 is defined as IA32_X2APIC_ISR1 in SDM.
#         MSR_IA32_X2APIC_ISR2 is defined as IA32_X2APIC_ISR2 in SDM.
#         MSR_IA32_X2APIC_ISR3 is defined as IA32_X2APIC_ISR3 in SDM.
#         MSR_IA32_X2APIC_ISR4 is defined as IA32_X2APIC_ISR4 in SDM.
#         MSR_IA32_X2APIC_ISR5 is defined as IA32_X2APIC_ISR5 in SDM.
#         MSR_IA32_X2APIC_ISR6 is defined as IA32_X2APIC_ISR6 in SDM.
#         MSR_IA32_X2APIC_ISR7 is defined as IA32_X2APIC_ISR7 in SDM.
#   @{
# **/
# #define MSR_IA32_X2APIC_ISR0  0x00000810
# #define MSR_IA32_X2APIC_ISR1  0x00000811
# #define MSR_IA32_X2APIC_ISR2  0x00000812
# #define MSR_IA32_X2APIC_ISR3  0x00000813
# #define MSR_IA32_X2APIC_ISR4  0x00000814
# #define MSR_IA32_X2APIC_ISR5  0x00000815
# #define MSR_IA32_X2APIC_ISR6  0x00000816
# #define MSR_IA32_X2APIC_ISR7  0x00000817
MSR_IA32_X2APIC_ISR0  = 0x00000810
MSR_IA32_X2APIC_ISR1  = 0x00000811
MSR_IA32_X2APIC_ISR2  = 0x00000812
MSR_IA32_X2APIC_ISR3  = 0x00000813
MSR_IA32_X2APIC_ISR4  = 0x00000814
MSR_IA32_X2APIC_ISR5  = 0x00000815
MSR_IA32_X2APIC_ISR6  = 0x00000816
MSR_IA32_X2APIC_ISR7  = 0x00000817

# /// @}
# 
# /**
#   x2APIC Trigger Mode Register Bits (n * 32 + ):(n * 32) (R/O).
#   If CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_TMRn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_TMR0);
#   @endcode
#   @note MSR_IA32_X2APIC_TMR0 is defined as IA32_X2APIC_TMR0 in SDM.
#         MSR_IA32_X2APIC_TMR1 is defined as IA32_X2APIC_TMR1 in SDM.
#         MSR_IA32_X2APIC_TMR2 is defined as IA32_X2APIC_TMR2 in SDM.
#         MSR_IA32_X2APIC_TMR3 is defined as IA32_X2APIC_TMR3 in SDM.
#         MSR_IA32_X2APIC_TMR4 is defined as IA32_X2APIC_TMR4 in SDM.
#         MSR_IA32_X2APIC_TMR5 is defined as IA32_X2APIC_TMR5 in SDM.
#         MSR_IA32_X2APIC_TMR6 is defined as IA32_X2APIC_TMR6 in SDM.
#         MSR_IA32_X2APIC_TMR7 is defined as IA32_X2APIC_TMR7 in SDM.
#   @{
# **/
# #define MSR_IA32_X2APIC_TMR0  0x00000818
# #define MSR_IA32_X2APIC_TMR1  0x00000819
# #define MSR_IA32_X2APIC_TMR2  0x0000081A
# #define MSR_IA32_X2APIC_TMR3  0x0000081B
# #define MSR_IA32_X2APIC_TMR4  0x0000081C
# #define MSR_IA32_X2APIC_TMR5  0x0000081D
# #define MSR_IA32_X2APIC_TMR6  0x0000081E
# #define MSR_IA32_X2APIC_TMR7  0x0000081F
MSR_IA32_X2APIC_TMR0  = 0x00000818
MSR_IA32_X2APIC_TMR1  = 0x00000819
MSR_IA32_X2APIC_TMR2  = 0x0000081A
MSR_IA32_X2APIC_TMR3  = 0x0000081B
MSR_IA32_X2APIC_TMR4  = 0x0000081C
MSR_IA32_X2APIC_TMR5  = 0x0000081D
MSR_IA32_X2APIC_TMR6  = 0x0000081E
MSR_IA32_X2APIC_TMR7  = 0x0000081F

# /// @}
# 
# /**
#   x2APIC Interrupt Request Register Bits (n* 32 + 31):(n * 32) (R/O).
#   If CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_IRRn
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_IRR0);
#   @endcode
#   @note MSR_IA32_X2APIC_IRR0 is defined as IA32_X2APIC_IRR0 in SDM.
#         MSR_IA32_X2APIC_IRR1 is defined as IA32_X2APIC_IRR1 in SDM.
#         MSR_IA32_X2APIC_IRR2 is defined as IA32_X2APIC_IRR2 in SDM.
#         MSR_IA32_X2APIC_IRR3 is defined as IA32_X2APIC_IRR3 in SDM.
#         MSR_IA32_X2APIC_IRR4 is defined as IA32_X2APIC_IRR4 in SDM.
#         MSR_IA32_X2APIC_IRR5 is defined as IA32_X2APIC_IRR5 in SDM.
#         MSR_IA32_X2APIC_IRR6 is defined as IA32_X2APIC_IRR6 in SDM.
#         MSR_IA32_X2APIC_IRR7 is defined as IA32_X2APIC_IRR7 in SDM.
#   @{
# **/
# #define MSR_IA32_X2APIC_IRR0  0x00000820
# #define MSR_IA32_X2APIC_IRR1  0x00000821
# #define MSR_IA32_X2APIC_IRR2  0x00000822
# #define MSR_IA32_X2APIC_IRR3  0x00000823
# #define MSR_IA32_X2APIC_IRR4  0x00000824
# #define MSR_IA32_X2APIC_IRR5  0x00000825
# #define MSR_IA32_X2APIC_IRR6  0x00000826
# #define MSR_IA32_X2APIC_IRR7  0x00000827
MSR_IA32_X2APIC_IRR0  = 0x00000820
MSR_IA32_X2APIC_IRR1  = 0x00000821
MSR_IA32_X2APIC_IRR2  = 0x00000822
MSR_IA32_X2APIC_IRR3  = 0x00000823
MSR_IA32_X2APIC_IRR4  = 0x00000824
MSR_IA32_X2APIC_IRR5  = 0x00000825
MSR_IA32_X2APIC_IRR6  = 0x00000826
MSR_IA32_X2APIC_IRR7  = 0x00000827

# /// @}
# 
# /**
#   x2APIC Error Status Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_ESR (0x00000828)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_ESR);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_ESR, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_ESR is defined as IA32_X2APIC_ESR in SDM.
# **/
# #define MSR_IA32_X2APIC_ESR  0x00000828
MSR_IA32_X2APIC_ESR             = 0x00000828

# 
# /**
#   x2APIC LVT Corrected Machine Check Interrupt Register (R/W). If
#   CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_CMCI (0x0000082F)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_CMCI);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_CMCI, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_CMCI is defined as IA32_X2APIC_LVT_CMCI in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_CMCI  0x0000082F
MSR_IA32_X2APIC_LVT_CMCI        = 0x0000082F

# 
# /**
#   x2APIC Interrupt Command Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_ICR (0x00000830)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_ICR);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_ICR, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_ICR is defined as IA32_X2APIC_ICR in SDM.
# **/
# #define MSR_IA32_X2APIC_ICR  0x00000830
MSR_IA32_X2APIC_ICR             = 0x00000830

# 
# /**
#   x2APIC LVT Timer Interrupt Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_TIMER (0x00000832)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_TIMER);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_TIMER, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_TIMER is defined as IA32_X2APIC_LVT_TIMER in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_TIMER  0x00000832
MSR_IA32_X2APIC_LVT_TIMER       = 0x00000832

# 
# /**
#   x2APIC LVT Thermal Sensor Interrupt Register (R/W). If CPUID.01H:ECX.[21] =
#   1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_THERMAL (0x00000833)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_THERMAL);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_THERMAL, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_THERMAL is defined as IA32_X2APIC_LVT_THERMAL in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_THERMAL  0x00000833
MSR_IA32_X2APIC_LVT_THERMAL     = 0x00000833

# 
# /**
#   x2APIC LVT Performance Monitor Interrupt Register (R/W). If
#   CPUID.01H:ECX.[21] = 1 && IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_PMI (0x00000834)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_PMI);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_PMI, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_PMI is defined as IA32_X2APIC_LVT_PMI in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_PMI  0x00000834
MSR_IA32_X2APIC_LVT_PMI         = 0x00000834

# 
# /**
#   x2APIC LVT LINT0 Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_LINT0 (0x00000835)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_LINT0);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_LINT0, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_LINT0 is defined as IA32_X2APIC_LVT_LINT0 in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_LINT0  0x00000835
MSR_IA32_X2APIC_LVT_LINT0       = 0x00000835

# 
# /**
#   x2APIC LVT LINT1 Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_LINT1 (0x00000836)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_LINT1);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_LINT1, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_LINT1 is defined as IA32_X2APIC_LVT_LINT1 in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_LINT1  0x00000836
MSR_IA32_X2APIC_LVT_LINT1       = 0x00000836

# 
# /**
#   x2APIC LVT Error Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_LVT_ERROR (0x00000837)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_LVT_ERROR);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_LVT_ERROR, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_LVT_ERROR is defined as IA32_X2APIC_LVT_ERROR in SDM.
# **/
# #define MSR_IA32_X2APIC_LVT_ERROR  0x00000837
MSR_IA32_X2APIC_LVT_ERROR       = 0x00000837

# 
# /**
#   x2APIC Initial Count Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_INIT_COUNT (0x00000838)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_INIT_COUNT);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_INIT_COUNT, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_INIT_COUNT is defined as IA32_X2APIC_INIT_COUNT in SDM.
# **/
# #define MSR_IA32_X2APIC_INIT_COUNT  0x00000838
MSR_IA32_X2APIC_INIT_COUNT      = 0x00000838

# 
# /**
#   x2APIC Current Count Register (R/O). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_CUR_COUNT (0x00000839)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_CUR_COUNT);
#   @endcode
#   @note MSR_IA32_X2APIC_CUR_COUNT is defined as IA32_X2APIC_CUR_COUNT in SDM.
# **/
# #define MSR_IA32_X2APIC_CUR_COUNT  0x00000839
MSR_IA32_X2APIC_CUR_COUNT       = 0x00000839

# 
# /**
#   x2APIC Divide Configuration Register (R/W). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_DIV_CONF (0x0000083E)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_X2APIC_DIV_CONF);
#   AsmWriteMsr64 (MSR_IA32_X2APIC_DIV_CONF, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_DIV_CONF is defined as IA32_X2APIC_DIV_CONF in SDM.
# **/
# #define MSR_IA32_X2APIC_DIV_CONF  0x0000083E
MSR_IA32_X2APIC_DIV_CONF        = 0x0000083E

# 
# /**
#   x2APIC Self IPI Register (W/O). If CPUID.01H:ECX.[21] = 1 &&
#   IA32_APIC_BASE.[10] = 1.
# 
#   @param  ECX  MSR_IA32_X2APIC_SELF_IPI (0x0000083F)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = 0;
#   AsmWriteMsr64 (MSR_IA32_X2APIC_SELF_IPI, Msr);
#   @endcode
#   @note MSR_IA32_X2APIC_SELF_IPI is defined as IA32_X2APIC_SELF_IPI in SDM.
# **/
# #define MSR_IA32_X2APIC_SELF_IPI  0x0000083F
MSR_IA32_X2APIC_SELF_IPI        = 0x0000083F

# 
# /**
#   Memory Encryption Activation MSR. If CPUID.07H:ECX.[13] = 1.
# 
#   @param  ECX  MSR_IA32_TME_ACTIVATE (0x00000982)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_TME_ACTIVATE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_TME_ACTIVATE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_TME_ACTIVATE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_TME_ACTIVATE);
#   AsmWriteMsr64 (MSR_IA32_TME_ACTIVATE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_TME_ACTIVATE is defined as IA32_TME_ACTIVATE in SDM.
# **/
# #define MSR_IA32_TME_ACTIVATE  0x00000982
MSR_IA32_TME_ACTIVATE           = 0x00000982

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_TME_ACTIVATE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Lock R/O: Will be set upon successful WRMSR (or first SMI);
#     /// written value ignored..
#     ///
#     UINT32    Lock              : 1;
#     ///
#     /// [Bit 1] Hardware Encryption Enable: This bit also enables MKTME; MKTME
#     /// cannot be enabled without enabling encryption hardware.
#     ///
#     UINT32    TmeEnable         : 1;
#     ///
#     /// [Bit 2] Key Select:
#     /// 0: Create a new TME key (expected cold/warm boot).
#     /// 1: Restore the TME key from storage (Expected when resume from standby).
#     ///
#     UINT32    KeySelect         : 1;
#     ///
#     /// [Bit 3] Save TME Key for Standby: Save key into storage to be used when
#     /// resume from standby.
#     /// Note: This may not be supported in all processors.
#     ///
#     UINT32    SaveKeyForStandby : 1;
#     ///
#     /// [Bit 7:4] TME Policy/Encryption Algorithm: Only algorithms enumerated in
#     /// IA32_TME_CAPABILITY are allowed.
#     /// For example:
#     ///   0000 – AES-XTS-128.
#     ///   0001 – AES-XTS-128 with integrity.
#     ///   0010 – AES-XTS-256.
#     ///   Other values are invalid.
#     ///
#     UINT32    TmePolicy : 4;
#     UINT32    Reserved  : 23;
#     ///
#     /// [Bit 31] TME Encryption Bypass Enable: When encryption hardware is enabled:
#     /// * Total Memory Encryption is enabled using a CPU generated ephemeral key
#     ///   based on a hardware random number generator when this bit is set to 0.
#     /// * Total Memory Encryption is bypassed (no encryption/decryption for KeyID0)
#     ///   when this bit is set to 1.
#     /// Software must inspect Hardware Encryption Enable (bit 1) and TME encryption
#     /// bypass Enable (bit 31) to determine if TME encryption is enabled.
#     ///
#     UINT32    TmeBypassMode : 1;
#     ///
#     /// [Bit 35:32] MK_TME_KEYID_BITS: Reserved if MKTME is not enumerated, otherwise:
#     /// The number of key identifier bits to allocate to MKTME usage.
#     /// Similar to enumeration, this is an encoded value.
#     /// Writing a value greater than MK_TME_MAX_KEYID_BITS will result in #GP.
#     /// Writing a non-zero value to this field will #GP if bit 1 of EAX (Hardware
#     /// Encryption Enable) is not also set to ‘1, as encryption hardware must be
#     /// enabled to use MKTME.
#     /// Example: To support 255 keys, this field would be set to a value of 8.
#     ///
#     UINT32    MkTmeKeyidBits : 4;
#     UINT32    Reserved2      : 12;
#     ///
#     /// [Bit 63:48] MK_TME_CRYPTO_ALGS: Reserved if MKTME is not enumerated, otherwise:
#     ///   Bit 48: AES-XTS 128.
#     ///   Bit 49: AES-XTS 128 with integrity.
#     ///   Bit 50: AES-XTS 256.
#     ///   Bit 63:51: Reserved (#GP)
#     /// Bitmask for BIOS to set which encryption algorithms are allowed for MKTME, would
#     /// be later enforced by the key loading ISA ('1= allowed)
#     ///
#     UINT32    MkTmeCryptoAlgs : 16;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32[2];
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_TME_ACTIVATE_REGISTER;
class MSR_IA32_TME_ACTIVATE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Lock",                UINT32, 1),
    ("TmeEnable",           UINT32, 1),
    ("KeySelect",           UINT32, 1),
    ("SaveKeyForStandby",   UINT32, 1),
    ("TmePolicy",           UINT32, 4),
    ("Reserved",            UINT32, 23),
    ("TmeBypassMode",       UINT32, 1),
    ("MkTmeKeyidBits",      UINT32, 4),
    ("Reserved2",           UINT32, 12),
    ("MkTmeCryptoAlgs",     UINT32, 16),
  ]

class MSR_IA32_TME_ACTIVATE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_TME_ACTIVATE_REGISTER_Bits),
    ("Uint32",  UINT32 * 2),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Silicon Debug Feature Control (R/W). If CPUID.01H:ECX.[11] = 1.
# 
#   @param  ECX  MSR_IA32_DEBUG_INTERFACE (0x00000C80)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_DEBUG_INTERFACE_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_DEBUG_INTERFACE_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_DEBUG_INTERFACE_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_DEBUG_INTERFACE);
#   AsmWriteMsr64 (MSR_IA32_DEBUG_INTERFACE, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_DEBUG_INTERFACE is defined as IA32_DEBUG_INTERFACE in SDM.
# **/
# #define MSR_IA32_DEBUG_INTERFACE  0x00000C80
MSR_IA32_DEBUG_INTERFACE        = 0x00000C80

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_DEBUG_INTERFACE
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Enable (R/W) BIOS set 1 to enable Silicon debug features.
#     /// Default is 0. If CPUID.01H:ECX.[11] = 1.
#     ///
#     UINT32    Enable        : 1;
#     UINT32    Reserved1     : 29;
#     ///
#     /// [Bit 30] Lock (R/W): If 1, locks any further change to the MSR. The
#     /// lock bit is set automatically on the first SMI assertion even if not
#     /// explicitly set by BIOS. Default is 0. If CPUID.01H:ECX.[11] = 1.
#     ///
#     UINT32    Lock          : 1;
#     ///
#     /// [Bit 31] Debug Occurred (R/O): This "sticky bit" is set by hardware to
#     /// indicate the status of bit 0. Default is 0. If CPUID.01H:ECX.[11] = 1.
#     ///
#     UINT32    DebugOccurred : 1;
#     UINT32    Reserved2     : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_DEBUG_INTERFACE_REGISTER;
class MSR_IA32_DEBUG_INTERFACE_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 29),
    ("Lock",            UINT32, 1),
    ("DebugOccurred",   UINT32, 1),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_DEBUG_INTERFACE_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_DEBUG_INTERFACE_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   L3 QOS Configuration (R/W). If ( CPUID.(EAX=10H, ECX=1):ECX.[2] = 1 ).
# 
#   @param  ECX  MSR_IA32_L3_QOS_CFG (0x00000C81)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_L3_QOS_CFG_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_L3_QOS_CFG_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_L3_QOS_CFG_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_L3_QOS_CFG);
#   AsmWriteMsr64 (MSR_IA32_L3_QOS_CFG, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_L3_QOS_CFG is defined as IA32_L3_QOS_CFG in SDM.
# **/
# #define MSR_IA32_L3_QOS_CFG  0x00000C81
MSR_IA32_L3_QOS_CFG             = 0x00000C81

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_L3_QOS_CFG
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Enable (R/W) Set 1 to enable L3 CAT masks and COS to operate
#     /// in Code and Data Prioritization (CDP) mode.
#     ///
#     UINT32    Enable    : 1;
#     UINT32    Reserved1 : 31;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_L3_QOS_CFG_REGISTER;
class MSR_IA32_L3_QOS_CFG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_L3_QOS_CFG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_L3_QOS_CFG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   L2 QOS Configuration (R/W). If ( CPUID.(EAX=10H, ECX=2):ECX.[2] = 1 ).
# 
#   @param  ECX  MSR_IA32_L2_QOS_CFG (0x00000C82)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_L2_QOS_CFG_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_L2_QOS_CFG_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_L2_QOS_CFG_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_L2_QOS_CFG);
#   AsmWriteMsr64 (MSR_IA32_L2_QOS_CFG, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_L2_QOS_CFG is defined as IA32_L2_QOS_CFG in SDM.
# **/
# #define MSR_IA32_L2_QOS_CFG  0x00000C82
MSR_IA32_L2_QOS_CFG             = 0x00000C82

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_L2_QOS_CFG
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] Enable (R/W) Set 1 to enable L2 CAT masks and COS to operate
#     /// in Code and Data Prioritization (CDP) mode.
#     ///
#     UINT32    Enable    : 1;
#     UINT32    Reserved1 : 31;
#     UINT32    Reserved2 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_L2_QOS_CFG_REGISTER;
class MSR_IA32_L2_QOS_CFG_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Enable",          UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_L2_QOS_CFG_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_L2_QOS_CFG_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Monitoring Event Select Register (R/W). If ( CPUID.(EAX=07H, ECX=0):EBX.[12]
#   = 1 ).
# 
#   @param  ECX  MSR_IA32_QM_EVTSEL (0x00000C8D)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_QM_EVTSEL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_QM_EVTSEL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_QM_EVTSEL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_QM_EVTSEL);
#   AsmWriteMsr64 (MSR_IA32_QM_EVTSEL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_QM_EVTSEL is defined as IA32_QM_EVTSEL in SDM.
# **/
# #define MSR_IA32_QM_EVTSEL  0x00000C8D
MSR_IA32_QM_EVTSEL              = 0x00000C8D

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_QM_EVTSEL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 7:0] Event ID: ID of a supported monitoring event to report via
#     /// IA32_QM_CTR.
#     ///
#     UINT32    EventID              : 8;
#     UINT32    Reserved             : 24;
#     ///
#     /// [Bits 63:32] Resource Monitoring ID: ID for monitoring hardware to
#     /// report monitored data via IA32_QM_CTR. N = Ceil (Log:sub:`2` (
#     /// CPUID.(EAX= 0FH, ECX=0H).EBX[31:0] +1)).
#     ///
#     UINT32    ResourceMonitoringID : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_QM_EVTSEL_REGISTER;
class MSR_IA32_QM_EVTSEL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EventID",                 UINT32, 8),
    ("Reserved",                UINT32, 24),
    ("ResourceMonitoringID",    UINT32, 32)
  ]

class MSR_IA32_QM_EVTSEL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_QM_EVTSEL_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Monitoring Counter Register (R/O). If ( CPUID.(EAX=07H, ECX=0):EBX.[12] = 1
#   ).
# 
#   @param  ECX  MSR_IA32_QM_CTR (0x00000C8E)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_QM_CTR_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_QM_CTR_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_QM_CTR_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_QM_CTR);
#   @endcode
#   @note MSR_IA32_QM_CTR is defined as IA32_QM_CTR in SDM.
# **/
# #define MSR_IA32_QM_CTR  0x00000C8E
MSR_IA32_QM_CTR                 = 0x00000C8E

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_QM_CTR
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Resource Monitored Data.
#     ///
#     UINT32    ResourceMonitoredData   : 32;
#     ///
#     /// [Bits 61:32] Resource Monitored Data.
#     ///
#     UINT32    ResourceMonitoredDataHi : 30;
#     ///
#     /// [Bit 62] Unavailable: If 1, indicates data for this RMID is not
#     /// available or not monitored for this resource or RMID.
#     ///
#     UINT32    Unavailable             : 1;
#     ///
#     /// [Bit 63] Error: If 1, indicates and unsupported RMID or event type was
#     /// written to IA32_PQR_QM_EVTSEL.
#     ///
#     UINT32    Error                   : 1;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_QM_CTR_REGISTER;
class MSR_IA32_QM_CTR_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResourceMonitoredData",   UINT32, 32),
    ("ResourceMonitoredDataHi", UINT32, 30),
    ("Unavailable",             UINT32, 1),
    ("Error",                   UINT32, 1)
  ]

class MSR_IA32_QM_CTR_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_QM_CTR_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Resource Association Register (R/W). If ( (CPUID.(EAX=07H, ECX=0):EBX[12]
#   =1) or (CPUID.(EAX=07H, ECX=0):EBX[15] =1 ) ).
# 
#   @param  ECX  MSR_IA32_PQR_ASSOC (0x00000C8F)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PQR_ASSOC_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PQR_ASSOC_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PQR_ASSOC_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PQR_ASSOC);
#   AsmWriteMsr64 (MSR_IA32_PQR_ASSOC, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PQR_ASSOC is defined as IA32_PQR_ASSOC in SDM.
# **/
# #define MSR_IA32_PQR_ASSOC  0x00000C8F
MSR_IA32_PQR_ASSOC              = 0x00000C8F

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PQR_ASSOC
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] Resource Monitoring ID (R/W): ID for monitoring hardware
#     /// to track internal operation, e.g. memory access. N = Ceil (Log:sub:`2`
#     /// ( CPUID.(EAX= 0FH, ECX=0H).EBX[31:0] +1)).
#     ///
#     UINT32    ResourceMonitoringID : 32;
#     ///
#     /// [Bits 63:32] COS (R/W). The class of service (COS) to enforce (on
#     /// writes); returns the current COS when read. If ( CPUID.(EAX=07H,
#     /// ECX=0):EBX.[15] = 1 ).
#     ///
#     UINT32    COS                  : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PQR_ASSOC_REGISTER;
class MSR_IA32_PQR_ASSOC_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("ResourceMonitoringID",    UINT32, 32),
    ("COS",                     UINT32, 30)
  ]

class MSR_IA32_PQR_ASSOC_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PQR_ASSOC_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Supervisor State of MPX Configuration. (R/W). If (CPUID.(EAX=07H,
#   ECX=0H):EBX[14] = 1).
# 
#   @param  ECX  MSR_IA32_BNDCFGS (0x00000D90)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_BNDCFGS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_BNDCFGS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_BNDCFGS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_BNDCFGS);
#   AsmWriteMsr64 (MSR_IA32_BNDCFGS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_BNDCFGS is defined as IA32_BNDCFGS in SDM.
# **/
# #define MSR_IA32_BNDCFGS  0x00000D90
MSR_IA32_BNDCFGS                = 0x00000D90

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_BNDCFGS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] EN: Enable Intel MPX in supervisor mode.
#     ///
#     UINT32    EN          : 1;
#     ///
#     /// [Bit 1] BNDPRESERVE: Preserve the bounds registers for near branch
#     /// instructions in the absence of the BND prefix.
#     ///
#     UINT32    BNDPRESERVE : 1;
#     UINT32    Reserved    : 10;
#     ///
#     /// [Bits 31:12] Base Address of Bound Directory.
#     ///
#     UINT32    Base        : 20;
#     ///
#     /// [Bits 63:32] Base Address of Bound Directory.
#     ///
#     UINT32    BaseHi      : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_BNDCFGS_REGISTER;
class MSR_IA32_BNDCFGS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("EN",          UINT32, 1),
    ("BNDPRESERVE", UINT32, 1),
    ("Reserved",    UINT32, 10),
    ("Base",        UINT32, 20),
    ("BaseHi",      UINT32, 32)
  ]

class MSR_IA32_BNDCFGS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_BNDCFGS_REGISTER_Bits),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Extended Supervisor State Mask (R/W). If( CPUID.(0DH, 1):EAX.[3] = 1.
# 
#   @param  ECX  MSR_IA32_XSS (0x00000DA0)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_XSS_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_XSS_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_XSS_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_XSS);
#   AsmWriteMsr64 (MSR_IA32_XSS, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_XSS is defined as IA32_XSS in SDM.
# **/
# #define MSR_IA32_XSS  0x00000DA0
MSR_IA32_XSS                    = 0x00000DA0

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_XSS
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     UINT32    Reserved1                     : 8;
#     ///
#     /// [Bit 8] Trace Packet Configuration State (R/W).
#     ///
#     UINT32    TracePacketConfigurationState : 1;
#     UINT32    Reserved2                     : 23;
#     UINT32    Reserved3                     : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_XSS_REGISTER;
class MSR_IA32_XSS_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("Reserved1",                       UINT32, 8),
    ("TracePacketConfigurationState",   UINT32, 1),
    ("Reserved2",                       UINT32, 23),
    ("Reserved3",                       UINT32, 32)
  ]

class MSR_IA32_XSS_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_XSS_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Package Level Enable/disable HDC (R/W). If CPUID.06H:EAX.[13] = 1.
# 
#   @param  ECX  MSR_IA32_PKG_HDC_CTL (0x00000DB0)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PKG_HDC_CTL_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PKG_HDC_CTL_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PKG_HDC_CTL_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PKG_HDC_CTL);
#   AsmWriteMsr64 (MSR_IA32_PKG_HDC_CTL, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PKG_HDC_CTL is defined as IA32_PKG_HDC_CTL in SDM.
# **/
# #define MSR_IA32_PKG_HDC_CTL  0x00000DB0
MSR_IA32_PKG_HDC_CTL            = 0x00000DB0

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PKG_HDC_CTL
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] HDC_Pkg_Enable (R/W) Force HDC idling or wake up HDC-idled
#     /// logical processors in the package. See Section 14.5.2, "Package level
#     /// Enabling HDC". If CPUID.06H:EAX.[13] = 1.
#     ///
#     UINT32    HDC_Pkg_Enable : 1;
#     UINT32    Reserved1      : 31;
#     UINT32    Reserved2      : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PKG_HDC_CTL_REGISTER;
class MSR_IA32_PKG_HDC_CTL_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HDC_Pkg_Enable",  UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PKG_HDC_CTL_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PKG_HDC_CTL_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Enable/disable HWP (R/W). If CPUID.06H:EAX.[13] = 1.
# 
#   @param  ECX  MSR_IA32_PM_CTL1 (0x00000DB1)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_PM_CTL1_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_PM_CTL1_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_PM_CTL1_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_PM_CTL1);
#   AsmWriteMsr64 (MSR_IA32_PM_CTL1, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_PM_CTL1 is defined as IA32_PM_CTL1 in SDM.
# **/
# #define MSR_IA32_PM_CTL1  0x00000DB1
MSR_IA32_PM_CTL1                = 0x00000DB1

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_PM_CTL1
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] HDC_Allow_Block (R/W) Allow/Block this logical processor for
#     /// package level HDC control. See Section 14.5.3.
#     /// If CPUID.06H:EAX.[13] = 1.
#     ///
#     UINT32    HDC_Allow_Block : 1;
#     UINT32    Reserved1       : 31;
#     UINT32    Reserved2       : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_PM_CTL1_REGISTER;
class MSR_IA32_PM_CTL1_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("HDC_Allow_Block", UINT32, 1),
    ("Reserved1",       UINT32, 31),
    ("Reserved2",       UINT32, 32)
  ]

class MSR_IA32_PM_CTL1_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_PM_CTL1_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   Per-Logical_Processor HDC Idle Residency (R/0). If CPUID.06H:EAX.[13] = 1.
#   Stall_Cycle_Cnt (R/W) Stalled cycles due to HDC forced idle on this logical
#   processor. See Section 14.5.4.1. If CPUID.06H:EAX.[13] = 1.
# 
#   @param  ECX  MSR_IA32_THREAD_STALL (0x00000DB2)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_THREAD_STALL);
#   @endcode
#   @note MSR_IA32_THREAD_STALL is defined as IA32_THREAD_STALL in SDM.
# **/
# #define MSR_IA32_THREAD_STALL  0x00000DB2
MSR_IA32_THREAD_STALL           = 0x00000DB2

# 
# /**
#   Extended Feature Enables. If ( CPUID.80000001H:EDX.[2 0]
#   CPUID.80000001H:EDX.[2 9]).
# 
#   @param  ECX  MSR_IA32_EFER (0xC0000080)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_EFER_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_EFER_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_EFER_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_EFER);
#   AsmWriteMsr64 (MSR_IA32_EFER, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_EFER is defined as IA32_EFER in SDM.
# **/
# #define MSR_IA32_EFER  0xC0000080
MSR_IA32_EFER                   = 0xC0000080

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_EFER
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bit 0] SYSCALL Enable: IA32_EFER.SCE (R/W) Enables SYSCALL/SYSRET
#     /// instructions in 64-bit mode.
#     ///
#     UINT32    SCE       : 1;
#     UINT32    Reserved1 : 7;
#     ///
#     /// [Bit 8] IA-32e Mode Enable: IA32_EFER.LME (R/W) Enables IA-32e mode
#     /// operation.
#     ///
#     UINT32    LME       : 1;
#     UINT32    Reserved2 : 1;
#     ///
#     /// [Bit 10] IA-32e Mode Active: IA32_EFER.LMA (R) Indicates IA-32e mode
#     /// is active when set.
#     ///
#     UINT32    LMA       : 1;
#     ///
#     /// [Bit 11] Execute Disable Bit Enable: IA32_EFER.NXE (R/W).
#     ///
#     UINT32    NXE       : 1;
#     UINT32    Reserved3 : 20;
#     UINT32    Reserved4 : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_EFER_REGISTER;
class MSR_IA32_EFER_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("SCE",         UINT32, 1),
    ("Reserved1",   UINT32, 7),
    ("LME",         UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("LMA",         UINT32, 1),
    ("NXE",         UINT32, 1),
    ("Reserved3",   UINT32, 20),
    ("Reserved4",   UINT32, 32)
  ]

class MSR_IA32_EFER_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_EFER_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# /**
#   System Call Target Address (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_STAR (0xC0000081)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_STAR);
#   AsmWriteMsr64 (MSR_IA32_STAR, Msr);
#   @endcode
#   @note MSR_IA32_STAR is defined as IA32_STAR in SDM.
# **/
# #define MSR_IA32_STAR  0xC0000081
MSR_IA32_STAR                   = 0xC0000081

# 
# /**
#   IA-32e Mode System Call Target Address (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_LSTAR (0xC0000082)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_LSTAR);
#   AsmWriteMsr64 (MSR_IA32_LSTAR, Msr);
#   @endcode
#   @note MSR_IA32_LSTAR is defined as IA32_LSTAR in SDM.
# **/
# #define MSR_IA32_LSTAR  0xC0000082
MSR_IA32_LSTAR                  = 0xC0000082

# 
# /**
#   IA-32e Mode System Call Target Address (R/W) Not used, as the SYSCALL
#   instruction is not recognized in compatibility mode. If
#   CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_CSTAR (0xC0000083)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_CSTAR);
#   AsmWriteMsr64 (MSR_IA32_CSTAR, Msr);
#   @endcode
#   @note MSR_IA32_CSTAR is defined as IA32_CSTAR in SDM.
# **/
# #define MSR_IA32_CSTAR  0xC0000083
MSR_IA32_CSTAR                  = 0xC0000083

# 
# /**
#   System Call Flag Mask (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_FMASK (0xC0000084)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_FMASK);
#   AsmWriteMsr64 (MSR_IA32_FMASK, Msr);
#   @endcode
#   @note MSR_IA32_FMASK is defined as IA32_FMASK in SDM.
# **/
# #define MSR_IA32_FMASK  0xC0000084
MSR_IA32_FMASK                  = 0xC0000084

# 
# /**
#   Map of BASE Address of FS (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_FS_BASE (0xC0000100)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_FS_BASE);
#   AsmWriteMsr64 (MSR_IA32_FS_BASE, Msr);
#   @endcode
#   @note MSR_IA32_FS_BASE is defined as IA32_FS_BASE in SDM.
# **/
# #define MSR_IA32_FS_BASE  0xC0000100
MSR_IA32_FS_BASE                = 0xC0000100

# 
# /**
#   Map of BASE Address of GS (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_GS_BASE (0xC0000101)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_GS_BASE);
#   AsmWriteMsr64 (MSR_IA32_GS_BASE, Msr);
#   @endcode
#   @note MSR_IA32_GS_BASE is defined as IA32_GS_BASE in SDM.
# **/
# #define MSR_IA32_GS_BASE  0xC0000101
MSR_IA32_GS_BASE                = 0xC0000101

# 
# /**
#   Swap Target of BASE Address of GS (R/W). If CPUID.80000001:EDX.[29] = 1.
# 
#   @param  ECX  MSR_IA32_KERNEL_GS_BASE (0xC0000102)
#   @param  EAX  Lower 32-bits of MSR value.
#   @param  EDX  Upper 32-bits of MSR value.
# 
#   <b>Example usage</b>
#   @code
#   UINT64  Msr;
# 
#   Msr = AsmReadMsr64 (MSR_IA32_KERNEL_GS_BASE);
#   AsmWriteMsr64 (MSR_IA32_KERNEL_GS_BASE, Msr);
#   @endcode
#   @note MSR_IA32_KERNEL_GS_BASE is defined as IA32_KERNEL_GS_BASE in SDM.
# **/
# #define MSR_IA32_KERNEL_GS_BASE  0xC0000102
MSR_IA32_KERNEL_GS_BASE         = 0xC0000102

# 
# /**
#   Auxiliary TSC (RW). If CPUID.80000001H: EDX[27] = 1.
# 
#   @param  ECX  MSR_IA32_TSC_AUX (0xC0000103)
#   @param  EAX  Lower 32-bits of MSR value.
#                Described by the type MSR_IA32_TSC_AUX_REGISTER.
#   @param  EDX  Upper 32-bits of MSR value.
#                Described by the type MSR_IA32_TSC_AUX_REGISTER.
# 
#   <b>Example usage</b>
#   @code
#   MSR_IA32_TSC_AUX_REGISTER  Msr;
# 
#   Msr.Uint64 = AsmReadMsr64 (MSR_IA32_TSC_AUX);
#   AsmWriteMsr64 (MSR_IA32_TSC_AUX, Msr.Uint64);
#   @endcode
#   @note MSR_IA32_TSC_AUX is defined as IA32_TSC_AUX in SDM.
# **/
# #define MSR_IA32_TSC_AUX  0xC0000103
MSR_IA32_TSC_AUX                = 0xC0000103

# 
# /**
#   MSR information returned for MSR index #MSR_IA32_TSC_AUX
# **/
# typedef union {
#   ///
#   /// Individual bit fields
#   ///
#   struct {
#     ///
#     /// [Bits 31:0] AUX: Auxiliary signature of TSC.
#     ///
#     UINT32    AUX      : 32;
#     UINT32    Reserved : 32;
#   } Bits;
#   ///
#   /// All bit fields as a 32-bit value
#   ///
#   UINT32    Uint32;
#   ///
#   /// All bit fields as a 64-bit value
#   ///
#   UINT64    Uint64;
# } MSR_IA32_TSC_AUX_REGISTER;
class MSR_IA32_TSC_AUX_REGISTER_Bits (Structure):
  _pack_   = 1
  _fields_ = [
    ("AUX",         UINT32, 32),
    ("Reserved",    UINT32, 32)
  ]

class MSR_IA32_TSC_AUX_REGISTER (Union):
  _pack_   = 1
  _fields_ = [
    ("Bits",    MSR_IA32_TSC_AUX_REGISTER_Bits),
    ("Uint32",  UINT32),
    ("Uint64",  UINT64)
  ]

# 
# #endif
# 