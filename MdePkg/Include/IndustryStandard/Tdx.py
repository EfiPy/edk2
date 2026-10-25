# /** @file
#   Intel Trust Domain Extension definitions
#   Detailed information is in below document:
#   https://software.intel.com/content/dam/develop/external/us/en/documents
#   /tdx-module-1eas-v0.85.039.pdf
# 
#   Copyright (c) 2020 - 2021, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Tdx.py
#
# EfiPy2.MdePkg.IndustryStandard.Tdx
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef MDE_PKG_TDX_H_
# #define MDE_PKG_TDX_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #define EXIT_REASON_EXTERNAL_INTERRUPT  1
# #define EXIT_REASON_TRIPLE_FAULT        2
EXIT_REASON_EXTERNAL_INTERRUPT  = 1
EXIT_REASON_TRIPLE_FAULT        = 2

# 
# #define EXIT_REASON_PENDING_INTERRUPT    7
# #define EXIT_REASON_NMI_WINDOW           8
# #define EXIT_REASON_TASK_SWITCH          9
# #define EXIT_REASON_CPUID                10
# #define EXIT_REASON_HLT                  12
# #define EXIT_REASON_INVD                 13
# #define EXIT_REASON_INVLPG               14
# #define EXIT_REASON_RDPMC                15
# #define EXIT_REASON_RDTSC                16
# #define EXIT_REASON_VMCALL               18
# #define EXIT_REASON_VMCLEAR              19
# #define EXIT_REASON_VMLAUNCH             20
# #define EXIT_REASON_VMPTRLD              21
# #define EXIT_REASON_VMPTRST              22
# #define EXIT_REASON_VMREAD               23
# #define EXIT_REASON_VMRESUME             24
# #define EXIT_REASON_VMWRITE              25
# #define EXIT_REASON_VMOFF                26
# #define EXIT_REASON_VMON                 27
# #define EXIT_REASON_CR_ACCESS            28
# #define EXIT_REASON_DR_ACCESS            29
# #define EXIT_REASON_IO_INSTRUCTION       30
# #define EXIT_REASON_MSR_READ             31
# #define EXIT_REASON_MSR_WRITE            32
# #define EXIT_REASON_INVALID_STATE        33
# #define EXIT_REASON_MSR_LOAD_FAIL        34
# #define EXIT_REASON_MWAIT_INSTRUCTION    36
# #define EXIT_REASON_MONITOR_TRAP_FLAG    37
# #define EXIT_REASON_MONITOR_INSTRUCTION  39
# #define EXIT_REASON_PAUSE_INSTRUCTION    40
# #define EXIT_REASON_MCE_DURING_VMENTRY   41
# #define EXIT_REASON_TPR_BELOW_THRESHOLD  43
# #define EXIT_REASON_APIC_ACCESS          44
# #define EXIT_REASON_EOI_INDUCED          45
# #define EXIT_REASON_GDTR_IDTR            46
# #define EXIT_REASON_LDTR_TR              47
# #define EXIT_REASON_EPT_VIOLATION        48
# #define EXIT_REASON_EPT_MISCONFIG        49
# #define EXIT_REASON_INVEPT               50
# #define EXIT_REASON_RDTSCP               51
# #define EXIT_REASON_PREEMPTION_TIMER     52
# #define EXIT_REASON_INVVPID              53
# #define EXIT_REASON_WBINVD               54
# #define EXIT_REASON_XSETBV               55
# #define EXIT_REASON_APIC_WRITE           56
# #define EXIT_REASON_RDRAND               57
# #define EXIT_REASON_INVPCID              58
# #define EXIT_REASON_VMFUNC               59
# #define EXIT_REASON_ENCLS                60
# #define EXIT_REASON_RDSEED               61
# #define EXIT_REASON_PML_FULL             62
# #define EXIT_REASON_XSAVES               63
# #define EXIT_REASON_XRSTORS              64
EXIT_REASON_PENDING_INTERRUPT    = 7
EXIT_REASON_NMI_WINDOW           = 8
EXIT_REASON_TASK_SWITCH          = 9
EXIT_REASON_CPUID                = 10
EXIT_REASON_HLT                  = 12
EXIT_REASON_INVD                 = 13
EXIT_REASON_INVLPG               = 14
EXIT_REASON_RDPMC                = 15
EXIT_REASON_RDTSC                = 16
EXIT_REASON_VMCALL               = 18
EXIT_REASON_VMCLEAR              = 19
EXIT_REASON_VMLAUNCH             = 20
EXIT_REASON_VMPTRLD              = 21
EXIT_REASON_VMPTRST              = 22
EXIT_REASON_VMREAD               = 23
EXIT_REASON_VMRESUME             = 24
EXIT_REASON_VMWRITE              = 25
EXIT_REASON_VMOFF                = 26
EXIT_REASON_VMON                 = 27
EXIT_REASON_CR_ACCESS            = 28
EXIT_REASON_DR_ACCESS            = 29
EXIT_REASON_IO_INSTRUCTION       = 30
EXIT_REASON_MSR_READ             = 31
EXIT_REASON_MSR_WRITE            = 32
EXIT_REASON_INVALID_STATE        = 33
EXIT_REASON_MSR_LOAD_FAIL        = 34
EXIT_REASON_MWAIT_INSTRUCTION    = 36
EXIT_REASON_MONITOR_TRAP_FLAG    = 37
EXIT_REASON_MONITOR_INSTRUCTION  = 39
EXIT_REASON_PAUSE_INSTRUCTION    = 40
EXIT_REASON_MCE_DURING_VMENTRY   = 41
EXIT_REASON_TPR_BELOW_THRESHOLD  = 43
EXIT_REASON_APIC_ACCESS          = 44
EXIT_REASON_EOI_INDUCED          = 45
EXIT_REASON_GDTR_IDTR            = 46
EXIT_REASON_LDTR_TR              = 47
EXIT_REASON_EPT_VIOLATION        = 48
EXIT_REASON_EPT_MISCONFIG        = 49
EXIT_REASON_INVEPT               = 50
EXIT_REASON_RDTSCP               = 51
EXIT_REASON_PREEMPTION_TIMER     = 52
EXIT_REASON_INVVPID              = 53
EXIT_REASON_WBINVD               = 54
EXIT_REASON_XSETBV               = 55
EXIT_REASON_APIC_WRITE           = 56
EXIT_REASON_RDRAND               = 57
EXIT_REASON_INVPCID              = 58
EXIT_REASON_VMFUNC               = 59
EXIT_REASON_ENCLS                = 60
EXIT_REASON_RDSEED               = 61
EXIT_REASON_PML_FULL             = 62
EXIT_REASON_XSAVES               = 63
EXIT_REASON_XRSTORS              = 64
EXIT_REASON_PENDING_INTERRUPT    = 7
EXIT_REASON_NMI_WINDOW           = 8
EXIT_REASON_TASK_SWITCH          = 9
EXIT_REASON_CPUID                = 10
EXIT_REASON_HLT                  = 12
EXIT_REASON_INVD                 = 13
EXIT_REASON_INVLPG               = 14
EXIT_REASON_RDPMC                = 15
EXIT_REASON_RDTSC                = 16
EXIT_REASON_VMCALL               = 18
EXIT_REASON_VMCLEAR              = 19
EXIT_REASON_VMLAUNCH             = 20
EXIT_REASON_VMPTRLD              = 21
EXIT_REASON_VMPTRST              = 22
EXIT_REASON_VMREAD               = 23
EXIT_REASON_VMRESUME             = 24
EXIT_REASON_VMWRITE              = 25
EXIT_REASON_VMOFF                = 26
EXIT_REASON_VMON                 = 27
EXIT_REASON_CR_ACCESS            = 28
EXIT_REASON_DR_ACCESS            = 29
EXIT_REASON_IO_INSTRUCTION       = 30
EXIT_REASON_MSR_READ             = 31
EXIT_REASON_MSR_WRITE            = 32
EXIT_REASON_INVALID_STATE        = 33
EXIT_REASON_MSR_LOAD_FAIL        = 34
EXIT_REASON_MWAIT_INSTRUCTION    = 36
EXIT_REASON_MONITOR_TRAP_FLAG    = 37
EXIT_REASON_MONITOR_INSTRUCTION  = 39
EXIT_REASON_PAUSE_INSTRUCTION    = 40
EXIT_REASON_MCE_DURING_VMENTRY   = 41
EXIT_REASON_TPR_BELOW_THRESHOLD  = 43
EXIT_REASON_APIC_ACCESS          = 44
EXIT_REASON_EOI_INDUCED          = 45
EXIT_REASON_GDTR_IDTR            = 46
EXIT_REASON_LDTR_TR              = 47
EXIT_REASON_EPT_VIOLATION        = 48
EXIT_REASON_EPT_MISCONFIG        = 49
EXIT_REASON_INVEPT               = 50
EXIT_REASON_RDTSCP               = 51
EXIT_REASON_PREEMPTION_TIMER     = 52
EXIT_REASON_INVVPID              = 53
EXIT_REASON_WBINVD               = 54
EXIT_REASON_XSETBV               = 55
EXIT_REASON_APIC_WRITE           = 56
EXIT_REASON_RDRAND               = 57
EXIT_REASON_INVPCID              = 58
EXIT_REASON_VMFUNC               = 59
EXIT_REASON_ENCLS                = 60
EXIT_REASON_RDSEED               = 61
EXIT_REASON_PML_FULL             = 62
EXIT_REASON_XSAVES               = 63
EXIT_REASON_XRSTORS              = 64

# 
# // TDCALL API Function Completion Status Codes
# #define TDX_EXIT_REASON_SUCCESS                0x0000000000000000
# #define TDX_EXIT_REASON_PAGE_ALREADY_ACCEPTED  0x00000B0A00000000
# #define TDX_EXIT_REASON_PAGE_SIZE_MISMATCH     0xC0000B0B00000000
# #define TDX_EXIT_REASON_OPERAND_INVALID        0xC000010000000000
# #define TDX_EXIT_REASON_OPERAND_BUSY           0x8000020000000000
TDX_EXIT_REASON_SUCCESS                = 0x0000000000000000
TDX_EXIT_REASON_PAGE_ALREADY_ACCEPTED  = 0x00000B0A00000000
TDX_EXIT_REASON_PAGE_SIZE_MISMATCH     = 0xC0000B0B00000000
TDX_EXIT_REASON_OPERAND_INVALID        = 0xC000010000000000
TDX_EXIT_REASON_OPERAND_BUSY           = 0x8000020000000000

# 
# // TDCALL [TDG.MEM.PAGE.ACCEPT] page size
# #define TDCALL_ACCEPT_PAGE_SIZE_4K  0
# #define TDCALL_ACCEPT_PAGE_SIZE_2M  1
# #define TDCALL_ACCEPT_PAGE_SIZE_1G  2
TDCALL_ACCEPT_PAGE_SIZE_4K  = 0
TDCALL_ACCEPT_PAGE_SIZE_2M  = 1
TDCALL_ACCEPT_PAGE_SIZE_1G  = 2

# 
# #define TDCALL_TDVMCALL      0
# #define TDCALL_TDINFO        1
# #define TDCALL_TDEXTENDRTMR  2
# #define TDCALL_TDGETVEINFO   3
# #define TDCALL_TDREPORT      4
# #define TDCALL_TDSETCPUIDVE  5
# #define TDCALL_TDACCEPTPAGE  6
TDCALL_TDVMCALL      = 0
TDCALL_TDINFO        = 1
TDCALL_TDEXTENDRTMR  = 2
TDCALL_TDGETVEINFO   = 3
TDCALL_TDREPORT      = 4
TDCALL_TDSETCPUIDVE  = 5
TDCALL_TDACCEPTPAGE  = 6

# 
# #define TDVMCALL_CPUID    0x0000a
# #define TDVMCALL_HALT     0x0000c
# #define TDVMCALL_IO       0x0001e
# #define TDVMCALL_RDMSR    0x0001f
# #define TDVMCALL_WRMSR    0x00020
# #define TDVMCALL_MMIO     0x00030
# #define TDVMCALL_PCONFIG  0x00041
TDVMCALL_CPUID    = 0x0000a
TDVMCALL_HALT     = 0x0000c
TDVMCALL_IO       = 0x0001e
TDVMCALL_RDMSR    = 0x0001f
TDVMCALL_WRMSR    = 0x00020
TDVMCALL_MMIO     = 0x00030
TDVMCALL_PCONFIG  = 0x00041

# 
# #define TDVMCALL_GET_TDVMCALL_INFO   0x10000
# #define TDVMCALL_MAPGPA              0x10001
# #define TDVMCALL_GET_QUOTE           0x10002
# #define TDVMCALL_REPORT_FATAL_ERR    0x10003
# #define TDVMCALL_SETUP_EVENT_NOTIFY  0x10004
TDVMCALL_GET_TDVMCALL_INFO   = 0x10000
TDVMCALL_MAPGPA              = 0x10001
TDVMCALL_GET_QUOTE           = 0x10002
TDVMCALL_REPORT_FATAL_ERR    = 0x10003
TDVMCALL_SETUP_EVENT_NOTIFY  = 0x10004

# 
# #pragma pack(1)
# typedef struct {
#   UINT64    Data[6];
# } TDCALL_GENERIC_RETURN_DATA;
class TDCALL_GENERIC_RETURN_DATA (Structure):
  _fields_ = [
    ("Data",    UINT64 * 6)
    ]

# 
# typedef struct {
#   UINT64    Gpaw;
#   UINT64    Attributes;
#   UINT32    MaxVcpus;
#   UINT32    NumVcpus;
#   UINT64    Resv[3];
# } TDCALL_INFO_RETURN_DATA;
class TDCALL_INFO_RETURN_DATA (Structure):
  _fields_ = [
    ("Gpaw",        UINT64),
    ("Attributes",  UINT64),
    ("MaxVcpus",    UINT32),
    ("NumVcpus",    UINT32),
    ("Resv",        UINT64 * 3)
    ]

# 
# typedef union {
#   UINT64    Val;
#   struct {
#     UINT32    Size      : 3;
#     UINT32    Direction : 1;
#     UINT32    String    : 1;
#     UINT32    Rep       : 1;
#     UINT32    Encoding  : 1;
#     UINT32    Resv      : 9;
#     UINT32    Port      : 16;
#     UINT32    Resv2;
#   } Io;
# } VMX_EXIT_QUALIFICATION;
class VMX_EXIT_QUALIFICATION_Io (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Size",        UINT32, 3),
    ("Direction",   UINT32, 1),
    ("String",      UINT32, 1),
    ("Rep",         UINT32, 1),
    ("Encoding",    UINT32, 1),
    ("Resv",        UINT32, 9),
    ("Port",        UINT32, 16),
    ("Resv2",       UINT32)
    ]

class VMX_EXIT_QUALIFICATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Val",     UINT64),
    ("Bits",    VMX_EXIT_QUALIFICATION_Io),
    ]

# 
# typedef struct {
#   UINT32                    ExitReason;
#   UINT32                    Resv;
#   VMX_EXIT_QUALIFICATION    ExitQualification;
#   UINT64                    GuestLA;
#   UINT64                    GuestPA;
#   UINT32                    ExitInstructionLength;
#   UINT32                    ExitInstructionInfo;
#   UINT32                    Resv1;
# } TDCALL_VEINFO_RETURN_DATA;
class TDCALL_VEINFO_RETURN_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExitReason",              UINT32                ),
    ("Resv",                    UINT32                ),
    ("ExitQualification",       VMX_EXIT_QUALIFICATION),
    ("GuestLA",                 UINT64                ),
    ("GuestPA",                 UINT64                ),
    ("ExitInstructionLength",   UINT32                ),
    ("ExitInstructionInfo",     UINT32                ),
    ("Resv1",                   UINT32                )
    ]

# 
# typedef union {
#   TDCALL_GENERIC_RETURN_DATA    Generic;
#   TDCALL_INFO_RETURN_DATA       TdInfo;
#   TDCALL_VEINFO_RETURN_DATA     VeInfo;
# } TD_RETURN_DATA;
class TD_RETURN_DATA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Generic", TDCALL_GENERIC_RETURN_DATA),
    ("TdInfo",  TDCALL_INFO_RETURN_DATA),
    ("VeInfo",  TDCALL_VEINFO_RETURN_DATA)
    ]

# 
# /* data structure used in TDREPORT_STRUCT */
# typedef struct {
#   UINT8    Type;
#   UINT8    Subtype;
#   UINT8    Version;
#   UINT8    Rsvd;
# } TD_REPORT_TYPE;
class TD_REPORT_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8),
    ("Subtype", UINT8),
    ("Version", UINT8),
    ("Rsvd",    UINT8)
    ]

# 
# typedef struct {
#   TD_REPORT_TYPE    ReportType;
#   UINT8             Rsvd1[12];
#   UINT8             CpuSvn[16];
#   UINT8             TeeTcbInfoHash[48];
#   UINT8             TeeInfoHash[48];
#   UINT8             ReportData[64];
#   UINT8             Rsvd2[32];
#   UINT8             Mac[32];
# } REPORTMACSTRUCT;
class REPORTMACSTRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReportType",      TD_REPORT_TYPE),
    ("Rsvd1",           UINT8 * 12),
    ("CpuSvn",          UINT8 * 16),
    ("TeeTcbInfoHash",  UINT8 * 48),
    ("TeeInfoHash",     UINT8 * 48),
    ("ReportData",      UINT8 * 64),
    ("Rsvd2",           UINT8 * 32),
    ("Mac",             UINT8 * 32)
    ]

# 
# typedef struct {
#   UINT8    Seam[2];
#   UINT8    Rsvd[14];
# } TEE_TCB_SVN;
class TEE_TCB_SVN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Seam",    UINT8 * 2),
    ("Rsvd",    UINT8 * 14)
    ]

# 
# typedef struct {
#   UINT8          Valid[8];
#   TEE_TCB_SVN    TeeTcbSvn;
#   UINT8          Mrseam[48];
#   UINT8          Mrsignerseam[48];
#   UINT8          Attributes[8];
#   UINT8          Rsvd[111];
# } TEE_TCB_INFO;
class TEE_TCB_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Valid",           UINT8       * 8),
    ("TeeTcbSvn",       TEE_TCB_SVN),
    ("Mrseam",          UINT8       * 48),
    ("Mrsignerseam",    UINT8       * 48),
    ("Attributes",      UINT8       * 8),
    ("Rsvd",            UINT8       * 111)
    ]

# 
# typedef struct {
#   UINT8    Attributes[8];
#   UINT8    Xfam[8];
#   UINT8    Mrtd[48];
#   UINT8    Mrconfigid[48];
#   UINT8    Mrowner[48];
#   UINT8    Mrownerconfig[48];
#   UINT8    Rtmrs[4][48];
#   UINT8    Rsvd[112];
# } TDINFO;
class TDINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Attributes",      UINT8 * 8),
    ("Xfam",            UINT8 * 8),
    ("Mrtd",            UINT8 * 48),
    ("Mrconfigid",      UINT8 * 48),
    ("Mrowner",         UINT8 * 48),
    ("Mrownerconfig",   UINT8 * 48),
    ("Rtmrs",          (UINT8 * 48) * 4),
    ("Rsvd",            UINT8 * 112)
    ]

# 
# typedef struct {
#   REPORTMACSTRUCT    ReportMacStruct;
#   TEE_TCB_INFO       TeeTcbInfo;
#   UINT8              Rsvd[17];
#   TDINFO             Tdinfo;
# } TDREPORT_STRUCT;
class TDREPORT_STRUCT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReportMacStruct", REPORTMACSTRUCT),
    ("TeeTcbInfo",      TEE_TCB_INFO),
    ("Rsvd",            UINT8 * 17),
    ("Tdinfo",          TDINFO)
    ]

# 
# #pragma pack()
# 
# #endif
# 