# /** @file
#   DebugSupport protocol and supporting definitions as defined in the UEFI2.4
#   specification.
# 
#   The DebugSupport protocol is used by source level debuggers to abstract the
#   processor and handle context save and restore operations.
# 
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# Portions copyright (c) 2011 - 2013, ARM Ltd. All rights reserved.<BR>
# Copyright (c) 2020, Hewlett Packard Enterprise Development LP. All rights reserved.<BR>
# 
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# DebugSupport.py
#
# EfiPy2.MdePkg.Protocol.DebugSupport
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __DEBUG_SUPPORT_H__
# #define __DEBUG_SUPPORT_H__
from EfiPy2 import *

# 
# #include <IndustryStandard/PeImage.h>
from EfiPy2.MdePkg.IndustryStandard  import PeImage

# 
# typedef struct _EFI_DEBUG_SUPPORT_PROTOCOL EFI_DEBUG_SUPPORT_PROTOCOL;
class EFI_DEBUG_SUPPORT_PROTOCOL (Structure):
  pass

# 
# ///
# /// Debug Support protocol {2755590C-6F3C-42FA-9EA4-A3BA543CDA25}.
# ///
# #define EFI_DEBUG_SUPPORT_PROTOCOL_GUID \
#   { \
#     0x2755590C, 0x6F3C, 0x42FA, {0x9E, 0xA4, 0xA3, 0xBA, 0x54, 0x3C, 0xDA, 0x25 } \
#   }
gEfiDebugSupportProtocolGuid            = \
  EFI_GUID (0x2755590C, 0x6F3C, 0x42FA, (0x9E, 0xA4, 0xA3, 0xBA, 0x54, 0x3C, 0xDA, 0x25 ))

# 
# ///
# /// Processor exception to be hooked.
# /// All exception types for IA32, X64, Itanium and EBC processors are defined.
# ///
# typedef INTN EFI_EXCEPTION_TYPE;
EFI_EXCEPTION_TYPE  = INTN

# 
# ///
# ///  IA-32 processor exception types.
# ///
# #define EXCEPT_IA32_DIVIDE_ERROR     0
# #define EXCEPT_IA32_DEBUG            1
# #define EXCEPT_IA32_NMI              2
# #define EXCEPT_IA32_BREAKPOINT       3
# #define EXCEPT_IA32_OVERFLOW         4
# #define EXCEPT_IA32_BOUND            5
# #define EXCEPT_IA32_INVALID_OPCODE   6
# #define EXCEPT_IA32_DOUBLE_FAULT     8
# #define EXCEPT_IA32_INVALID_TSS      10
# #define EXCEPT_IA32_SEG_NOT_PRESENT  11
# #define EXCEPT_IA32_STACK_FAULT      12
# #define EXCEPT_IA32_GP_FAULT         13
# #define EXCEPT_IA32_PAGE_FAULT       14
# #define EXCEPT_IA32_FP_ERROR         16
# #define EXCEPT_IA32_ALIGNMENT_CHECK  17
# #define EXCEPT_IA32_MACHINE_CHECK    18
# #define EXCEPT_IA32_SIMD             19
EXCEPT_IA32_DIVIDE_ERROR    = 0
EXCEPT_IA32_DEBUG           = 1
EXCEPT_IA32_NMI             = 2
EXCEPT_IA32_BREAKPOINT      = 3
EXCEPT_IA32_OVERFLOW        = 4
EXCEPT_IA32_BOUND           = 5
EXCEPT_IA32_INVALID_OPCODE  = 6
EXCEPT_IA32_DOUBLE_FAULT    = 8
EXCEPT_IA32_INVALID_TSS     = 10
EXCEPT_IA32_SEG_NOT_PRESENT = 11
EXCEPT_IA32_STACK_FAULT     = 12
EXCEPT_IA32_GP_FAULT        = 13
EXCEPT_IA32_PAGE_FAULT      = 14
EXCEPT_IA32_FP_ERROR        = 16
EXCEPT_IA32_ALIGNMENT_CHECK = 17
EXCEPT_IA32_MACHINE_CHECK   = 18
EXCEPT_IA32_SIMD            = 19

# 
# ///
# /// FXSAVE_STATE.
# /// FP / MMX / XMM registers (see fxrstor instruction definition).
# ///
# typedef struct {
#   UINT16    Fcw;
#   UINT16    Fsw;
#   UINT16    Ftw;
#   UINT16    Opcode;
#   UINT32    Eip;
#   UINT16    Cs;
#   UINT16    Reserved1;
#   UINT32    DataOffset;
#   UINT16    Ds;
#   UINT8     Reserved2[10];
#   UINT8     St0Mm0[10], Reserved3[6];
#   UINT8     St1Mm1[10], Reserved4[6];
#   UINT8     St2Mm2[10], Reserved5[6];
#   UINT8     St3Mm3[10], Reserved6[6];
#   UINT8     St4Mm4[10], Reserved7[6];
#   UINT8     St5Mm5[10], Reserved8[6];
#   UINT8     St6Mm6[10], Reserved9[6];
#   UINT8     St7Mm7[10], Reserved10[6];
#   UINT8     Xmm0[16];
#   UINT8     Xmm1[16];
#   UINT8     Xmm2[16];
#   UINT8     Xmm3[16];
#   UINT8     Xmm4[16];
#   UINT8     Xmm5[16];
#   UINT8     Xmm6[16];
#   UINT8     Xmm7[16];
#   UINT8     Reserved11[14 * 16];
# } EFI_FX_SAVE_STATE_IA32;
class EFI_FX_SAVE_STATE_IA32 (Structure):
  _fields_ = [
    ("Fcw",         UINT16),
    ("Fsw",         UINT16),
    ("Ftw",         UINT16),
    ("Opcode",      UINT16),
    ("Eip",         UINT32),
    ("Cs",          UINT16),
    ("Reserved1",   UINT16),
    ("DataOffset",  UINT32),
    ("Ds",          UINT16),
    ("Reserved2",   UINT8 * 10),
    ("St0Mm0",      UINT8 * 10),
    ("Reserved3",   UINT8 * 6),
    ("St1Mm1",      UINT8 * 10),
    ("Reserved4",   UINT8 * 6),
    ("St2Mm2",      UINT8 * 10),
    ("Reserved5",   UINT8 * 6),
    ("St3Mm3",      UINT8 * 10),
    ("Reserved6",   UINT8 * 6),
    ("St4Mm4",      UINT8 * 10),
    ("Reserved7",   UINT8 * 6),
    ("St5Mm5",      UINT8 * 10),
    ("Reserved8",   UINT8 * 6),
    ("St6Mm6",      UINT8 * 10),
    ("Reserved9",   UINT8 * 6),
    ("St7Mm7",      UINT8 * 10),
    ("Reserved10",  UINT8 * 6),
    ("Xmm0",        UINT8 * 16),
    ("Xmm1",        UINT8 * 16),
    ("Xmm2",        UINT8 * 16),
    ("Xmm3",        UINT8 * 16),
    ("Xmm4",        UINT8 * 16),
    ("Xmm5",        UINT8 * 16),
    ("Xmm6",        UINT8 * 16),
    ("Xmm7",        UINT8 * 16),
    ("Reserved11",  UINT8 * (14 * 16))
  ]

# 
# ///
# ///  IA-32 processor context definition.
# ///
# typedef struct {
#   UINT32                    ExceptionData;
#   EFI_FX_SAVE_STATE_IA32    FxSaveState;
#   UINT32                    Dr0;
#   UINT32                    Dr1;
#   UINT32                    Dr2;
#   UINT32                    Dr3;
#   UINT32                    Dr6;
#   UINT32                    Dr7;
#   UINT32                    Cr0;
#   UINT32                    Cr1; /* Reserved */
#   UINT32                    Cr2;
#   UINT32                    Cr3;
#   UINT32                    Cr4;
#   UINT32                    Eflags;
#   UINT32                    Ldtr;
#   UINT32                    Tr;
#   UINT32                    Gdtr[2];
#   UINT32                    Idtr[2];
#   UINT32                    Eip;
#   UINT32                    Gs;
#   UINT32                    Fs;
#   UINT32                    Es;
#   UINT32                    Ds;
#   UINT32                    Cs;
#   UINT32                    Ss;
#   UINT32                    Edi;
#   UINT32                    Esi;
#   UINT32                    Ebp;
#   UINT32                    Esp;
#   UINT32                    Ebx;
#   UINT32                    Edx;
#   UINT32                    Ecx;
#   UINT32                    Eax;
# } EFI_SYSTEM_CONTEXT_IA32;
class EFI_SYSTEM_CONTEXT_IA32 (Structure):
  _fields_ = [
    ("ExceptionData", UINT32),
    ("FxSaveState",   EFI_FX_SAVE_STATE_IA32),
    ("Dr0",           UINT32),
    ("Dr1",           UINT32),
    ("Dr2",           UINT32),
    ("Dr3",           UINT32),
    ("Dr6",           UINT32),
    ("Dr7",           UINT32),
    ("Cr0",           UINT32),
    ("Cr1",           UINT32),
    ("Cr2",           UINT32),
    ("Cr3",           UINT32),
    ("Cr4",           UINT32),
    ("Eflags",        UINT32),
    ("Ldtr",          UINT32),
    ("Tr",            UINT32),
    ("Gdtr",          UINT32 * 2),
    ("Idtr",          UINT32 * 2),
    ("Eip",           UINT32),
    ("Gs",            UINT32),
    ("Fs",            UINT32),
    ("Es",            UINT32),
    ("Ds",            UINT32),
    ("Cs",            UINT32),
    ("Ss",            UINT32),
    ("Edi",           UINT32),
    ("Esi",           UINT32),
    ("Ebp",           UINT32),
    ("Esp",           UINT32),
    ("Ebx",           UINT32),
    ("Edx",           UINT32),
    ("Ecx",           UINT32),
    ("Eax",           UINT32)
  ]           

# 
# ///
# ///  x64 processor exception types.
# ///
# #define EXCEPT_X64_DIVIDE_ERROR     0
# #define EXCEPT_X64_DEBUG            1
# #define EXCEPT_X64_NMI              2
# #define EXCEPT_X64_BREAKPOINT       3
# #define EXCEPT_X64_OVERFLOW         4
# #define EXCEPT_X64_BOUND            5
# #define EXCEPT_X64_INVALID_OPCODE   6
# #define EXCEPT_X64_DOUBLE_FAULT     8
# #define EXCEPT_X64_INVALID_TSS      10
# #define EXCEPT_X64_SEG_NOT_PRESENT  11
# #define EXCEPT_X64_STACK_FAULT      12
# #define EXCEPT_X64_GP_FAULT         13
# #define EXCEPT_X64_PAGE_FAULT       14
# #define EXCEPT_X64_FP_ERROR         16
# #define EXCEPT_X64_ALIGNMENT_CHECK  17
# #define EXCEPT_X64_MACHINE_CHECK    18
# #define EXCEPT_X64_SIMD             19
EXCEPT_X64_DIVIDE_ERROR    = 0
EXCEPT_X64_DEBUG           = 1
EXCEPT_X64_NMI             = 2
EXCEPT_X64_BREAKPOINT      = 3
EXCEPT_X64_OVERFLOW        = 4
EXCEPT_X64_BOUND           = 5
EXCEPT_X64_INVALID_OPCODE  = 6
EXCEPT_X64_DOUBLE_FAULT    = 8
EXCEPT_X64_INVALID_TSS     = 10
EXCEPT_X64_SEG_NOT_PRESENT = 11
EXCEPT_X64_STACK_FAULT     = 12
EXCEPT_X64_GP_FAULT        = 13
EXCEPT_X64_PAGE_FAULT      = 14
EXCEPT_X64_FP_ERROR        = 16
EXCEPT_X64_ALIGNMENT_CHECK = 17
EXCEPT_X64_MACHINE_CHECK   = 18
EXCEPT_X64_SIMD            = 19

# 
# ///
# /// FXSAVE_STATE.
# /// FP / MMX / XMM registers (see fxrstor instruction definition).
# ///
# typedef struct {
#   UINT16    Fcw;
#   UINT16    Fsw;
#   UINT16    Ftw;
#   UINT16    Opcode;
#   UINT64    Rip;
#   UINT64    DataOffset;
#   UINT8     Reserved1[8];
#   UINT8     St0Mm0[10], Reserved2[6];
#   UINT8     St1Mm1[10], Reserved3[6];
#   UINT8     St2Mm2[10], Reserved4[6];
#   UINT8     St3Mm3[10], Reserved5[6];
#   UINT8     St4Mm4[10], Reserved6[6];
#   UINT8     St5Mm5[10], Reserved7[6];
#   UINT8     St6Mm6[10], Reserved8[6];
#   UINT8     St7Mm7[10], Reserved9[6];
#   UINT8     Xmm0[16];
#   UINT8     Xmm1[16];
#   UINT8     Xmm2[16];
#   UINT8     Xmm3[16];
#   UINT8     Xmm4[16];
#   UINT8     Xmm5[16];
#   UINT8     Xmm6[16];
#   UINT8     Xmm7[16];
#   //
#   // NOTE: UEFI 2.0 spec definition as follows.
#   //
#   UINT8     Reserved11[14 * 16];
# } EFI_FX_SAVE_STATE_X64;
class EFI_FX_SAVE_STATE_X64 (Structure):
  _fields_ = [
    ("Fcw",         UINT16),
    ("Fsw",         UINT16),
    ("Ftw",         UINT16),
    ("Opcode",      UINT16),
    ("Rip",         UINT64),
    ("DataOffset",  UINT64),
    ("Reserved1",   UINT8 *  8),
    ("St0Mm0",      UINT8 * 10),
    ("Reserved2",   UINT8 *  6),
    ("St1Mm1",      UINT8 * 10),
    ("Reserved3",   UINT8 *  6),
    ("St2Mm2",      UINT8 * 10),
    ("Reserved4",   UINT8 *  6),
    ("St3Mm3",      UINT8 * 10),
    ("Reserved5",   UINT8 *  6),
    ("St4Mm4",      UINT8 * 10),
    ("Reserved6",   UINT8 *  6),
    ("St5Mm5",      UINT8 * 10),
    ("Reserved7",   UINT8 *  6),
    ("St6Mm6",      UINT8 * 10),
    ("Reserved8",   UINT8 *  6),
    ("St7Mm7",      UINT8 * 10),
    ("Reserved9",   UINT8 *  6),
    ("Xmm0",        UINT8 * 16),
    ("Xmm1",        UINT8 * 16),
    ("Xmm2",        UINT8 * 16),
    ("Xmm3",        UINT8 * 16),
    ("Xmm4",        UINT8 * 16),
    ("Xmm5",        UINT8 * 16),
    ("Xmm6",        UINT8 * 16),
    ("Xmm7",        UINT8 * 16),
    ("Reserved11",  UINT8 * (14 * 16))
  ]

# 
# ///
# ///  x64 processor context definition.
# ///
# typedef struct {
#   UINT64                   ExceptionData;
#   EFI_FX_SAVE_STATE_X64    FxSaveState;
#   UINT64                   Dr0;
#   UINT64                   Dr1;
#   UINT64                   Dr2;
#   UINT64                   Dr3;
#   UINT64                   Dr6;
#   UINT64                   Dr7;
#   UINT64                   Cr0;
#   UINT64                   Cr1; /* Reserved */
#   UINT64                   Cr2;
#   UINT64                   Cr3;
#   UINT64                   Cr4;
#   UINT64                   Cr8;
#   UINT64                   Rflags;
#   UINT64                   Ldtr;
#   UINT64                   Tr;
#   UINT64                   Gdtr[2];
#   UINT64                   Idtr[2];
#   UINT64                   Rip;
#   UINT64                   Gs;
#   UINT64                   Fs;
#   UINT64                   Es;
#   UINT64                   Ds;
#   UINT64                   Cs;
#   UINT64                   Ss;
#   UINT64                   Rdi;
#   UINT64                   Rsi;
#   UINT64                   Rbp;
#   UINT64                   Rsp;
#   UINT64                   Rbx;
#   UINT64                   Rdx;
#   UINT64                   Rcx;
#   UINT64                   Rax;
#   UINT64                   R8;
#   UINT64                   R9;
#   UINT64                   R10;
#   UINT64                   R11;
#   UINT64                   R12;
#   UINT64                   R13;
#   UINT64                   R14;
#   UINT64                   R15;
# } EFI_SYSTEM_CONTEXT_X64;
class EFI_SYSTEM_CONTEXT_X64 (Structure):
  _fields_ = [
    ("ExceptionData", UINT64),
    ("FxSaveState",   EFI_FX_SAVE_STATE_X64),
    ("Dr0",           UINT64),
    ("Dr1",           UINT64),
    ("Dr2",           UINT64),
    ("Dr3",           UINT64),
    ("Dr6",           UINT64),
    ("Dr7",           UINT64),
    ("Cr0",           UINT64),
    ("Cr1",           UINT64),
    ("Cr2",           UINT64),
    ("Cr3",           UINT64),
    ("Cr4",           UINT64),
    ("Cr8",           UINT64),
    ("Rflags",        UINT64),
    ("Ldtr",          UINT64),
    ("Tr",            UINT64),
    ("Gdtr",          UINT64 * 2),
    ("Idtr",          UINT64 * 2),
    ("Rip",           UINT64),
    ("Gs",            UINT64),
    ("Fs",            UINT64),
    ("Es",            UINT64),
    ("Ds",            UINT64),
    ("Cs",            UINT64),
    ("Ss",            UINT64),
    ("Rdi",           UINT64),
    ("Rsi",           UINT64),
    ("Rbp",           UINT64),
    ("Rsp",           UINT64),
    ("Rbx",           UINT64),
    ("Rdx",           UINT64),
    ("Rcx",           UINT64),
    ("Rax",           UINT64),
    ("R8",            UINT64),
    ("R9",            UINT64),
    ("R10",           UINT64),
    ("R11",           UINT64),
    ("R12",           UINT64),
    ("R13",           UINT64),
    ("R14",           UINT64),
    ("R15",           UINT64)
  ]
# 
# ///
# ///  Itanium Processor Family Exception types.
# ///
# #define EXCEPT_IPF_VHTP_TRANSLATION        0
# #define EXCEPT_IPF_INSTRUCTION_TLB         1
# #define EXCEPT_IPF_DATA_TLB                2
# #define EXCEPT_IPF_ALT_INSTRUCTION_TLB     3
# #define EXCEPT_IPF_ALT_DATA_TLB            4
# #define EXCEPT_IPF_DATA_NESTED_TLB         5
# #define EXCEPT_IPF_INSTRUCTION_KEY_MISSED  6
# #define EXCEPT_IPF_DATA_KEY_MISSED         7
# #define EXCEPT_IPF_DIRTY_BIT               8
# #define EXCEPT_IPF_INSTRUCTION_ACCESS_BIT  9
# #define EXCEPT_IPF_DATA_ACCESS_BIT         10
# #define EXCEPT_IPF_BREAKPOINT              11
# #define EXCEPT_IPF_EXTERNAL_INTERRUPT      12
EXCEPT_IPF_VHTP_TRANSLATION       = 0
EXCEPT_IPF_INSTRUCTION_TLB        = 1
EXCEPT_IPF_DATA_TLB               = 2
EXCEPT_IPF_ALT_INSTRUCTION_TLB    = 3
EXCEPT_IPF_ALT_DATA_TLB           = 4
EXCEPT_IPF_DATA_NESTED_TLB        = 5
EXCEPT_IPF_INSTRUCTION_KEY_MISSED = 6
EXCEPT_IPF_DATA_KEY_MISSED        = 7
EXCEPT_IPF_DIRTY_BIT              = 8
EXCEPT_IPF_INSTRUCTION_ACCESS_BIT = 9
EXCEPT_IPF_DATA_ACCESS_BIT        = 10
EXCEPT_IPF_BREAKPOINT             = 11
EXCEPT_IPF_EXTERNAL_INTERRUPT     = 12

# //
# // 13 - 19 reserved
# //
# #define EXCEPT_IPF_PAGE_NOT_PRESENT           20
# #define EXCEPT_IPF_KEY_PERMISSION             21
# #define EXCEPT_IPF_INSTRUCTION_ACCESS_RIGHTS  22
# #define EXCEPT_IPF_DATA_ACCESS_RIGHTS         23
# #define EXCEPT_IPF_GENERAL_EXCEPTION          24
# #define EXCEPT_IPF_DISABLED_FP_REGISTER       25
# #define EXCEPT_IPF_NAT_CONSUMPTION            26
# #define EXCEPT_IPF_SPECULATION                27
EXCEPT_IPF_PAGE_NOT_PRESENT           = 20
EXCEPT_IPF_KEY_PERMISSION             = 21
EXCEPT_IPF_INSTRUCTION_ACCESS_RIGHTS  = 22
EXCEPT_IPF_DATA_ACCESS_RIGHTS         = 23
EXCEPT_IPF_GENERAL_EXCEPTION          = 24
EXCEPT_IPF_DISABLED_FP_REGISTER       = 25
EXCEPT_IPF_NAT_CONSUMPTION            = 26
EXCEPT_IPF_SPECULATION                = 27

# //
# // 28 reserved
# //
# #define EXCEPT_IPF_DEBUG                          29
# #define EXCEPT_IPF_UNALIGNED_REFERENCE            30
# #define EXCEPT_IPF_UNSUPPORTED_DATA_REFERENCE     31
# #define EXCEPT_IPF_FP_FAULT                       32
# #define EXCEPT_IPF_FP_TRAP                        33
# #define EXCEPT_IPF_LOWER_PRIVILEGE_TRANSFER_TRAP  34
# #define EXCEPT_IPF_TAKEN_BRANCH                   35
# #define EXCEPT_IPF_SINGLE_STEP                    36
EXCEPT_IPF_DEBUG                          = 29
EXCEPT_IPF_UNALIGNED_REFERENCE            = 30
EXCEPT_IPF_UNSUPPORTED_DATA_REFERENCE     = 31
EXCEPT_IPF_FP_FAULT                       = 32
EXCEPT_IPF_FP_TRAP                        = 33
EXCEPT_IPF_LOWER_PRIVILEGE_TRANSFER_TRAP  = 34
EXCEPT_IPF_TAKEN_BRANCH                   = 35
EXCEPT_IPF_SINGLE_STEP                    = 36

# //
# // 37 - 44 reserved
# //
# #define EXCEPT_IPF_IA32_EXCEPTION  45
# #define EXCEPT_IPF_IA32_INTERCEPT  46
# #define EXCEPT_IPF_IA32_INTERRUPT  47
EXCEPT_IPF_IA32_EXCEPTION = 45
EXCEPT_IPF_IA32_INTERCEPT = 46
EXCEPT_IPF_IA32_INTERRUPT = 47

# 
# ///
# ///  IPF processor context definition.
# ///
# typedef struct {
#   //
#   // The first reserved field is necessary to preserve alignment for the correct
#   // bits in UNAT and to insure F2 is 16 byte aligned.
#   //
#   UINT64    Reserved;
#   UINT64    R1;
#   UINT64    R2;
#   UINT64    R3;
#   UINT64    R4;
#   UINT64    R5;
#   UINT64    R6;
#   UINT64    R7;
#   UINT64    R8;
#   UINT64    R9;
#   UINT64    R10;
#   UINT64    R11;
#   UINT64    R12;
#   UINT64    R13;
#   UINT64    R14;
#   UINT64    R15;
#   UINT64    R16;
#   UINT64    R17;
#   UINT64    R18;
#   UINT64    R19;
#   UINT64    R20;
#   UINT64    R21;
#   UINT64    R22;
#   UINT64    R23;
#   UINT64    R24;
#   UINT64    R25;
#   UINT64    R26;
#   UINT64    R27;
#   UINT64    R28;
#   UINT64    R29;
#   UINT64    R30;
#   UINT64    R31;
# 
#   UINT64    F2[2];
#   UINT64    F3[2];
#   UINT64    F4[2];
#   UINT64    F5[2];
#   UINT64    F6[2];
#   UINT64    F7[2];
#   UINT64    F8[2];
#   UINT64    F9[2];
#   UINT64    F10[2];
#   UINT64    F11[2];
#   UINT64    F12[2];
#   UINT64    F13[2];
#   UINT64    F14[2];
#   UINT64    F15[2];
#   UINT64    F16[2];
#   UINT64    F17[2];
#   UINT64    F18[2];
#   UINT64    F19[2];
#   UINT64    F20[2];
#   UINT64    F21[2];
#   UINT64    F22[2];
#   UINT64    F23[2];
#   UINT64    F24[2];
#   UINT64    F25[2];
#   UINT64    F26[2];
#   UINT64    F27[2];
#   UINT64    F28[2];
#   UINT64    F29[2];
#   UINT64    F30[2];
#   UINT64    F31[2];
# 
#   UINT64    Pr;
# 
#   UINT64    B0;
#   UINT64    B1;
#   UINT64    B2;
#   UINT64    B3;
#   UINT64    B4;
#   UINT64    B5;
#   UINT64    B6;
#   UINT64    B7;
# 
#   //
#   // application registers
#   //
#   UINT64    ArRsc;
#   UINT64    ArBsp;
#   UINT64    ArBspstore;
#   UINT64    ArRnat;
# 
#   UINT64    ArFcr;
# 
#   UINT64    ArEflag;
#   UINT64    ArCsd;
#   UINT64    ArSsd;
#   UINT64    ArCflg;
#   UINT64    ArFsr;
#   UINT64    ArFir;
#   UINT64    ArFdr;
# 
#   UINT64    ArCcv;
# 
#   UINT64    ArUnat;
# 
#   UINT64    ArFpsr;
# 
#   UINT64    ArPfs;
#   UINT64    ArLc;
#   UINT64    ArEc;
# 
#   //
#   // control registers
#   //
#   UINT64    CrDcr;
#   UINT64    CrItm;
#   UINT64    CrIva;
#   UINT64    CrPta;
#   UINT64    CrIpsr;
#   UINT64    CrIsr;
#   UINT64    CrIip;
#   UINT64    CrIfa;
#   UINT64    CrItir;
#   UINT64    CrIipa;
#   UINT64    CrIfs;
#   UINT64    CrIim;
#   UINT64    CrIha;
# 
#   //
#   // debug registers
#   //
#   UINT64    Dbr0;
#   UINT64    Dbr1;
#   UINT64    Dbr2;
#   UINT64    Dbr3;
#   UINT64    Dbr4;
#   UINT64    Dbr5;
#   UINT64    Dbr6;
#   UINT64    Dbr7;
# 
#   UINT64    Ibr0;
#   UINT64    Ibr1;
#   UINT64    Ibr2;
#   UINT64    Ibr3;
#   UINT64    Ibr4;
#   UINT64    Ibr5;
#   UINT64    Ibr6;
#   UINT64    Ibr7;
# 
#   //
#   // virtual registers - nat bits for R1-R31
#   //
#   UINT64    IntNat;
# } EFI_SYSTEM_CONTEXT_IPF;
class EFI_SYSTEM_CONTEXT_IPF (Structure):
  _fields_ = [
    ("Reserved",    UINT64),
    ("R1",          UINT64),
    ("R2",          UINT64),
    ("R3",          UINT64),
    ("R4",          UINT64),
    ("R5",          UINT64),
    ("R6",          UINT64),
    ("R7",          UINT64),
    ("R8",          UINT64),
    ("R9",          UINT64),
    ("R10",         UINT64),
    ("R11",         UINT64),
    ("R12",         UINT64),
    ("R13",         UINT64),
    ("R14",         UINT64),
    ("R15",         UINT64),
    ("R16",         UINT64),
    ("R17",         UINT64),
    ("R18",         UINT64),
    ("R19",         UINT64),
    ("R20",         UINT64),
    ("R21",         UINT64),
    ("R22",         UINT64),
    ("R23",         UINT64),
    ("R24",         UINT64),
    ("R25",         UINT64),
    ("R26",         UINT64),
    ("R27",         UINT64),
    ("R28",         UINT64),
    ("R29",         UINT64),
    ("R30",         UINT64),
    ("R31",         UINT64),
    ("F2",          UINT64 * 2),
    ("F3",          UINT64 * 2),
    ("F4",          UINT64 * 2),
    ("F5",          UINT64 * 2),
    ("F6",          UINT64 * 2),
    ("F7",          UINT64 * 2),
    ("F8",          UINT64 * 2),
    ("F9",          UINT64 * 2),
    ("F10",         UINT64 * 2),
    ("F11",         UINT64 * 2),
    ("F12",         UINT64 * 2),
    ("F13",         UINT64 * 2),
    ("F14",         UINT64 * 2),
    ("F15",         UINT64 * 2),
    ("F16",         UINT64 * 2),
    ("F17",         UINT64 * 2),
    ("F18",         UINT64 * 2),
    ("F19",         UINT64 * 2),
    ("F20",         UINT64 * 2),
    ("F21",         UINT64 * 2),
    ("F22",         UINT64 * 2),
    ("F23",         UINT64 * 2),
    ("F24",         UINT64 * 2),
    ("F25",         UINT64 * 2),
    ("F26",         UINT64 * 2),
    ("F27",         UINT64 * 2),
    ("F28",         UINT64 * 2),
    ("F29",         UINT64 * 2),
    ("F30",         UINT64 * 2),
    ("F31",         UINT64 * 2),
    ("Pr",          UINT64),
    ("B0",          UINT64),
    ("B1",          UINT64),
    ("B2",          UINT64),
    ("B3",          UINT64),
    ("B4",          UINT64),
    ("B5",          UINT64),
    ("B6",          UINT64),
    ("B7",          UINT64),
    ("ArRsc",       UINT64),
    ("ArBsp",       UINT64),
    ("ArBspstore",  UINT64),
    ("ArRnat",      UINT64),
    ("ArFcr",       UINT64),
    ("ArEflag",     UINT64),
    ("ArCsd",       UINT64),
    ("ArSsd",       UINT64),
    ("ArCflg",      UINT64),
    ("ArFsr",       UINT64),
    ("ArFir",       UINT64),
    ("ArFdr",       UINT64),
    ("ArCcv",       UINT64),
    ("ArUnat",      UINT64),
    ("ArFpsr",      UINT64),
    ("ArPfs",       UINT64),
    ("ArLc",        UINT64),
    ("ArEc",        UINT64),
    ("CrDcr",       UINT64),
    ("CrItm",       UINT64),
    ("CrIva",       UINT64),
    ("CrPta",       UINT64),
    ("CrIpsr",      UINT64),
    ("CrIsr",       UINT64),
    ("CrIip",       UINT64),
    ("CrIfa",       UINT64),
    ("CrItir",      UINT64),
    ("CrIipa",      UINT64),
    ("CrIfs",       UINT64),
    ("CrIim",       UINT64),
    ("CrIha",       UINT64),
    ("Dbr0",        UINT64),
    ("Dbr1",        UINT64),
    ("Dbr2",        UINT64),
    ("Dbr3",        UINT64),
    ("Dbr4",        UINT64),
    ("Dbr5",        UINT64),
    ("Dbr6",        UINT64),
    ("Dbr7",        UINT64),
    ("Ibr0",        UINT64),
    ("Ibr1",        UINT64),
    ("Ibr2",        UINT64),
    ("Ibr3",        UINT64),
    ("Ibr4",        UINT64),
    ("Ibr5",        UINT64),
    ("Ibr6",        UINT64),
    ("Ibr7",        UINT64),
    ("IntNat",      UINT64)
  ]

# 
# ///
# ///  EBC processor exception types.
# ///
# #define EXCEPT_EBC_UNDEFINED             0
# #define EXCEPT_EBC_DIVIDE_ERROR          1
# #define EXCEPT_EBC_DEBUG                 2
# #define EXCEPT_EBC_BREAKPOINT            3
# #define EXCEPT_EBC_OVERFLOW              4
# #define EXCEPT_EBC_INVALID_OPCODE        5  ///< Opcode out of range.
# #define EXCEPT_EBC_STACK_FAULT           6
# #define EXCEPT_EBC_ALIGNMENT_CHECK       7
# #define EXCEPT_EBC_INSTRUCTION_ENCODING  8  ///< Malformed instruction.
# #define EXCEPT_EBC_BAD_BREAK             9  ///< BREAK 0 or undefined BREAK.
# #define EXCEPT_EBC_STEP                  10 ///< To support debug stepping.
EXCEPT_EBC_UNDEFINED             = 0
EXCEPT_EBC_DIVIDE_ERROR          = 1
EXCEPT_EBC_DEBUG                 = 2
EXCEPT_EBC_BREAKPOINT            = 3
EXCEPT_EBC_OVERFLOW              = 4
EXCEPT_EBC_INVALID_OPCODE        = 5
EXCEPT_EBC_STACK_FAULT           = 6
EXCEPT_EBC_ALIGNMENT_CHECK       = 7
EXCEPT_EBC_INSTRUCTION_ENCODING  = 8
EXCEPT_EBC_BAD_BREAK             = 9
EXCEPT_EBC_STEP                  = 10

# ///
# /// For coding convenience, define the maximum valid EBC exception.
# ///
# #define MAX_EBC_EXCEPTION  EXCEPT_EBC_STEP
MAX_EBC_EXCEPTION = EXCEPT_EBC_STEP

# 
# ///
# ///  EBC processor context definition.
# ///
# typedef struct {
#   UINT64    R0;
#   UINT64    R1;
#   UINT64    R2;
#   UINT64    R3;
#   UINT64    R4;
#   UINT64    R5;
#   UINT64    R6;
#   UINT64    R7;
#   UINT64    Flags;
#   UINT64    ControlFlags;
#   UINT64    Ip;
# } EFI_SYSTEM_CONTEXT_EBC;
class EFI_SYSTEM_CONTEXT_EBC (Structure):
  _fields_ = [
    ("R0",            UINT64),
    ("R1",            UINT64),
    ("R2",            UINT64),
    ("R3",            UINT64),
    ("R4",            UINT64),
    ("R5",            UINT64),
    ("R6",            UINT64),
    ("R7",            UINT64),
    ("Flags",         UINT64),
    ("ControlFlags",  UINT64),
    ("Ip",            UINT64)
  ]

# 
# ///
# ///  ARM processor exception types.
# ///
# #define EXCEPT_ARM_RESET                  0
# #define EXCEPT_ARM_UNDEFINED_INSTRUCTION  1
# #define EXCEPT_ARM_SOFTWARE_INTERRUPT     2
# #define EXCEPT_ARM_PREFETCH_ABORT         3
# #define EXCEPT_ARM_DATA_ABORT             4
# #define EXCEPT_ARM_RESERVED               5
# #define EXCEPT_ARM_IRQ                    6
# #define EXCEPT_ARM_FIQ                    7
EXCEPT_ARM_RESET                    = 0
EXCEPT_ARM_UNDEFINED_INSTRUCTION    = 1
EXCEPT_ARM_SOFTWARE_INTERRUPT       = 2
EXCEPT_ARM_PREFETCH_ABORT           = 3
EXCEPT_ARM_DATA_ABORT               = 4
EXCEPT_ARM_RESERVED                 = 5
EXCEPT_ARM_IRQ                      = 6
EXCEPT_ARM_FIQ                      = 7

# 
# ///
# /// For coding convenience, define the maximum valid ARM exception.
# ///
# #define MAX_ARM_EXCEPTION  EXCEPT_ARM_FIQ
MAX_ARM_EXCEPTION = EXCEPT_ARM_FIQ

# 
# ///
# ///  ARM processor context definition.
# ///
# typedef struct {
#   UINT32    R0;
#   UINT32    R1;
#   UINT32    R2;
#   UINT32    R3;
#   UINT32    R4;
#   UINT32    R5;
#   UINT32    R6;
#   UINT32    R7;
#   UINT32    R8;
#   UINT32    R9;
#   UINT32    R10;
#   UINT32    R11;
#   UINT32    R12;
#   UINT32    SP;
#   UINT32    LR;
#   UINT32    PC;
#   UINT32    CPSR;
#   UINT32    DFSR;
#   UINT32    DFAR;
#   UINT32    IFSR;
#   UINT32    IFAR;
# } EFI_SYSTEM_CONTEXT_ARM;
class EFI_SYSTEM_CONTEXT_ARM (Structure):
  _fields_ = [
    ("R0",    UINT32),
    ("R1",    UINT32),
    ("R2",    UINT32),
    ("R3",    UINT32),
    ("R4",    UINT32),
    ("R5",    UINT32),
    ("R6",    UINT32),
    ("R7",    UINT32),
    ("R8",    UINT32),
    ("R9",    UINT32),
    ("R10",   UINT32),
    ("R11",   UINT32),
    ("R12",   UINT32),
    ("SP",    UINT32),
    ("LR",    UINT32),
    ("PC",    UINT32),
    ("CPSR",  UINT32),
    ("DFSR",  UINT32),
    ("DFAR",  UINT32),
    ("IFSR",  UINT32),
    ("IFAR",  UINT32)
  ]


# 
# ///
# ///  AARCH64 processor exception types.
# ///
# #define EXCEPT_AARCH64_SYNCHRONOUS_EXCEPTIONS  0
# #define EXCEPT_AARCH64_IRQ                     1
# #define EXCEPT_AARCH64_FIQ                     2
# #define EXCEPT_AARCH64_SERROR                  3
EXCEPT_AARCH64_SYNCHRONOUS_EXCEPTIONS    = 0
EXCEPT_AARCH64_IRQ                       = 1
EXCEPT_AARCH64_FIQ                       = 2
EXCEPT_AARCH64_SERROR                    = 3

# 
# ///
# /// For coding convenience, define the maximum valid ARM exception.
# ///
# #define MAX_AARCH64_EXCEPTION  EXCEPT_AARCH64_SERROR
MAX_AARCH64_EXCEPTION = EXCEPT_AARCH64_SERROR

# 
# typedef struct {
#   // General Purpose Registers
#   UINT64    X0;
#   UINT64    X1;
#   UINT64    X2;
#   UINT64    X3;
#   UINT64    X4;
#   UINT64    X5;
#   UINT64    X6;
#   UINT64    X7;
#   UINT64    X8;
#   UINT64    X9;
#   UINT64    X10;
#   UINT64    X11;
#   UINT64    X12;
#   UINT64    X13;
#   UINT64    X14;
#   UINT64    X15;
#   UINT64    X16;
#   UINT64    X17;
#   UINT64    X18;
#   UINT64    X19;
#   UINT64    X20;
#   UINT64    X21;
#   UINT64    X22;
#   UINT64    X23;
#   UINT64    X24;
#   UINT64    X25;
#   UINT64    X26;
#   UINT64    X27;
#   UINT64    X28;
#   UINT64    FP; // x29 - Frame pointer
#   UINT64    LR; // x30 - Link Register
#   UINT64    SP; // x31 - Stack pointer
# 
#   // FP/SIMD Registers
#   UINT64    V0[2];
#   UINT64    V1[2];
#   UINT64    V2[2];
#   UINT64    V3[2];
#   UINT64    V4[2];
#   UINT64    V5[2];
#   UINT64    V6[2];
#   UINT64    V7[2];
#   UINT64    V8[2];
#   UINT64    V9[2];
#   UINT64    V10[2];
#   UINT64    V11[2];
#   UINT64    V12[2];
#   UINT64    V13[2];
#   UINT64    V14[2];
#   UINT64    V15[2];
#   UINT64    V16[2];
#   UINT64    V17[2];
#   UINT64    V18[2];
#   UINT64    V19[2];
#   UINT64    V20[2];
#   UINT64    V21[2];
#   UINT64    V22[2];
#   UINT64    V23[2];
#   UINT64    V24[2];
#   UINT64    V25[2];
#   UINT64    V26[2];
#   UINT64    V27[2];
#   UINT64    V28[2];
#   UINT64    V29[2];
#   UINT64    V30[2];
#   UINT64    V31[2];
# 
#   UINT64    ELR;  // Exception Link Register
#   UINT64    SPSR; // Saved Processor Status Register
#   UINT64    FPSR; // Floating Point Status Register
#   UINT64    ESR;  // Exception syndrome register
#   UINT64    FAR;  // Fault Address Register
# } EFI_SYSTEM_CONTEXT_AARCH64;
class EFI_SYSTEM_CONTEXT_AARCH64 (Structure):
  _fields_ = [
    ("X0",    UINT64),
    ("X1",    UINT64),
    ("X2",    UINT64),
    ("X3",    UINT64),
    ("X4",    UINT64),
    ("X5",    UINT64),
    ("X6",    UINT64),
    ("X7",    UINT64),
    ("X8",    UINT64),
    ("X9",    UINT64),
    ("X10",   UINT64),
    ("X11",   UINT64),
    ("X12",   UINT64),
    ("X13",   UINT64),
    ("X14",   UINT64),
    ("X15",   UINT64),
    ("X16",   UINT64),
    ("X17",   UINT64),
    ("X18",   UINT64),
    ("X19",   UINT64),
    ("X20",   UINT64),
    ("X21",   UINT64),
    ("X22",   UINT64),
    ("X23",   UINT64),
    ("X24",   UINT64),
    ("X25",   UINT64),
    ("X26",   UINT64),
    ("X27",   UINT64),
    ("X28",   UINT64),
    ("FP",    UINT64),
    ("LR",    UINT64),
    ("SP",    UINT64),
    ("V0",    UINT64 * 2),
    ("V1",    UINT64 * 2),
    ("V2",    UINT64 * 2),
    ("V3",    UINT64 * 2),
    ("V4",    UINT64 * 2),
    ("V5",    UINT64 * 2),
    ("V6",    UINT64 * 2),
    ("V7",    UINT64 * 2),
    ("V8",    UINT64 * 2),
    ("V9",    UINT64 * 2),
    ("V10",   UINT64 * 2),
    ("V11",   UINT64 * 2),
    ("V12",   UINT64 * 2),
    ("V13",   UINT64 * 2),
    ("V14",   UINT64 * 2),
    ("V15",   UINT64 * 2),
    ("V16",   UINT64 * 2),
    ("V17",   UINT64 * 2),
    ("V18",   UINT64 * 2),
    ("V19",   UINT64 * 2),
    ("V20",   UINT64 * 2),
    ("V21",   UINT64 * 2),
    ("V22",   UINT64 * 2),
    ("V23",   UINT64 * 2),
    ("V24",   UINT64 * 2),
    ("V25",   UINT64 * 2),
    ("V26",   UINT64 * 2),
    ("V27",   UINT64 * 2),
    ("V28",   UINT64 * 2),
    ("V29",   UINT64 * 2),
    ("V30",   UINT64 * 2),
    ("V31",   UINT64 * 2),
    ("ELR",   UINT64),
    ("SPSR",  UINT64),
    ("FPSR",  UINT64),
    ("ESR",   UINT64),
    ("FAR",   UINT64)
  ]

# 
# ///
# /// RISC-V processor exception types.
# ///
# #define EXCEPT_RISCV_INST_MISALIGNED               0
# #define EXCEPT_RISCV_INST_ACCESS_FAULT             1
# #define EXCEPT_RISCV_ILLEGAL_INST                  2
# #define EXCEPT_RISCV_BREAKPOINT                    3
# #define EXCEPT_RISCV_LOAD_ADDRESS_MISALIGNED       4
# #define EXCEPT_RISCV_LOAD_ACCESS_FAULT             5
# #define EXCEPT_RISCV_STORE_AMO_ADDRESS_MISALIGNED  6
# #define EXCEPT_RISCV_STORE_AMO_ACCESS_FAULT        7
# #define EXCEPT_RISCV_ENV_CALL_FROM_UMODE           8
# #define EXCEPT_RISCV_ENV_CALL_FROM_SMODE           9
# #define EXCEPT_RISCV_ENV_CALL_FROM_VS_MODE         10
# #define EXCEPT_RISCV_ENV_CALL_FROM_MMODE           11
# #define EXCEPT_RISCV_INST_ACCESS_PAGE_FAULT        12
# #define EXCEPT_RISCV_LOAD_ACCESS_PAGE_FAULT        13
# #define EXCEPT_RISCV_14                            14
# #define EXCEPT_RISCV_STORE_ACCESS_PAGE_FAULT       15
# #define EXCEPT_RISCV_16                            16
# #define EXCEPT_RISCV_17                            17
# #define EXCEPT_RISCV_18                            18
# #define EXCEPT_RISCV_19                            19
# #define EXCEPT_RISCV_INST_GUEST_PAGE_FAULT         20
# #define EXCEPT_RISCV_LOAD_GUEST_PAGE_FAULT         21
# #define EXCEPT_RISCV_VIRTUAL_INSTRUCTION           22
# #define EXCEPT_RISCV_STORE_GUEST_PAGE_FAULT        23
# #define EXCEPT_RISCV_MAX_EXCEPTIONS                (EXCEPT_RISCV_STORE_GUEST_PAGE_FAULT)
EXCEPT_RISCV_INST_MISALIGNED               = 0
EXCEPT_RISCV_INST_ACCESS_FAULT             = 1
EXCEPT_RISCV_ILLEGAL_INST                  = 2
EXCEPT_RISCV_BREAKPOINT                    = 3
EXCEPT_RISCV_LOAD_ADDRESS_MISALIGNED       = 4
EXCEPT_RISCV_LOAD_ACCESS_FAULT             = 5
EXCEPT_RISCV_STORE_AMO_ADDRESS_MISALIGNED  = 6
EXCEPT_RISCV_STORE_AMO_ACCESS_FAULT        = 7
EXCEPT_RISCV_ENV_CALL_FROM_UMODE           = 8
EXCEPT_RISCV_ENV_CALL_FROM_SMODE           = 9
EXCEPT_RISCV_ENV_CALL_FROM_VS_MODE         = 10
EXCEPT_RISCV_ENV_CALL_FROM_MMODE           = 11
EXCEPT_RISCV_INST_ACCESS_PAGE_FAULT        = 12
EXCEPT_RISCV_LOAD_ACCESS_PAGE_FAULT        = 13
EXCEPT_RISCV_14                            = 14
EXCEPT_RISCV_STORE_ACCESS_PAGE_FAULT       = 15
EXCEPT_RISCV_16                            = 16
EXCEPT_RISCV_17                            = 17
EXCEPT_RISCV_18                            = 18
EXCEPT_RISCV_19                            = 19
EXCEPT_RISCV_INST_GUEST_PAGE_FAULT         = 20
EXCEPT_RISCV_LOAD_GUEST_PAGE_FAULT         = 21
EXCEPT_RISCV_VIRTUAL_INSTRUCTION           = 22
EXCEPT_RISCV_STORE_GUEST_PAGE_FAULT        = 23
EXCEPT_RISCV_MAX_EXCEPTIONS                = EXCEPT_RISCV_STORE_GUEST_PAGE_FAULT

# 
# ///
# /// RISC-V processor exception types for interrupts.
# ///
# #define EXCEPT_RISCV_IS_IRQ(x)     ((x & 0x8000000000000000UL) != 0)
def EXCEPT_RISCV_IS_IRQ (x):
  return (x & 0x8000000000000000) != 0

# #define EXCEPT_RISCV_IRQ_INDEX(x)  (x & 0x7FFFFFFFFFFFFFFFUL)
def EXCEPT_RISCV_IRQ_INDEX (x):
  return x & 0x7FFFFFFFFFFFFFFF

# #define EXCEPT_RISCV_IRQ_0                 0x8000000000000000UL
# #define EXCEPT_RISCV_IRQ_SOFT_FROM_SMODE   0x8000000000000001UL
# #define EXCEPT_RISCV_IRQ_SOFT_FROM_VSMODE  0x8000000000000002UL
# #define EXCEPT_RISCV_IRQ_SOFT_FROM_MMODE   0x8000000000000003UL
# #define EXCEPT_RISCV_IRQ_4                 0x8000000000000004UL
# #define EXCEPT_RISCV_IRQ_TIMER_FROM_SMODE  0x8000000000000005UL
# #define EXCEPT_RISCV_MAX_IRQS              (EXCEPT_RISCV_IRQ_INDEX(EXCEPT_RISCV_IRQ_TIMER_FROM_SMODE))
EXCEPT_RISCV_IRQ_0                 = 0x8000000000000000
EXCEPT_RISCV_IRQ_SOFT_FROM_SMODE   = 0x8000000000000001
EXCEPT_RISCV_IRQ_SOFT_FROM_VSMODE  = 0x8000000000000002
EXCEPT_RISCV_IRQ_SOFT_FROM_MMODE   = 0x8000000000000003
EXCEPT_RISCV_IRQ_4                 = 0x8000000000000004
EXCEPT_RISCV_IRQ_TIMER_FROM_SMODE  = 0x8000000000000005
EXCEPT_RISCV_MAX_IRQS              = EXCEPT_RISCV_IRQ_INDEX(EXCEPT_RISCV_IRQ_TIMER_FROM_SMODE)

# 
# typedef struct {
#   UINT64    X0;
#   UINT64    X1;
#   UINT64    X2;
#   UINT64    X3;
#   UINT64    X4;
#   UINT64    X5;
#   UINT64    X6;
#   UINT64    X7;
#   UINT64    X8;
#   UINT64    X9;
#   UINT64    X10;
#   UINT64    X11;
#   UINT64    X12;
#   UINT64    X13;
#   UINT64    X14;
#   UINT64    X15;
#   UINT64    X16;
#   UINT64    X17;
#   UINT64    X18;
#   UINT64    X19;
#   UINT64    X20;
#   UINT64    X21;
#   UINT64    X22;
#   UINT64    X23;
#   UINT64    X24;
#   UINT64    X25;
#   UINT64    X26;
#   UINT64    X27;
#   UINT64    X28;
#   UINT64    X29;
#   UINT64    X30;
#   UINT64    X31;
#   UINT64    SEPC;
#   UINT32    SSTATUS;
#   UINT32    STVAL;
# } EFI_SYSTEM_CONTEXT_RISCV64;
class EFI_SYSTEM_CONTEXT_RISCV64 (Structure):
  _fields_ = [
    ("X0",      UINT64),
    ("X1",      UINT64),
    ("X2",      UINT64),
    ("X3",      UINT64),
    ("X4",      UINT64),
    ("X5",      UINT64),
    ("X6",      UINT64),
    ("X7",      UINT64),
    ("X8",      UINT64),
    ("X9",      UINT64),
    ("X10",     UINT64),
    ("X11",     UINT64),
    ("X12",     UINT64),
    ("X13",     UINT64),
    ("X14",     UINT64),
    ("X15",     UINT64),
    ("X16",     UINT64),
    ("X17",     UINT64),
    ("X18",     UINT64),
    ("X19",     UINT64),
    ("X20",     UINT64),
    ("X21",     UINT64),
    ("X22",     UINT64),
    ("X23",     UINT64),
    ("X24",     UINT64),
    ("X25",     UINT64),
    ("X26",     UINT64),
    ("X27",     UINT64),
    ("X28",     UINT64),
    ("X29",     UINT64),
    ("X30",     UINT64),
    ("X31",     UINT64),
    ("SEPC",    UINT64),
    ("SSTATUS", UINT32),
    ("STVAL",   UINT32)
  ]

# 
# //
# // LoongArch processor exception types.
# //
# #define EXCEPT_LOONGARCH_INT   0
# #define EXCEPT_LOONGARCH_PIL   1
# #define EXCEPT_LOONGARCH_PIS   2
# #define EXCEPT_LOONGARCH_PIF   3
# #define EXCEPT_LOONGARCH_PME   4
# #define EXCEPT_LOONGARCH_PNR   5
# #define EXCEPT_LOONGARCH_PNX   6
# #define EXCEPT_LOONGARCH_PPI   7
# #define EXCEPT_LOONGARCH_ADE   8
# #define EXCEPT_LOONGARCH_ALE   9
# #define EXCEPT_LOONGARCH_BCE   10
# #define EXCEPT_LOONGARCH_SYS   11
# #define EXCEPT_LOONGARCH_BRK   12
# #define EXCEPT_LOONGARCH_INE   13
# #define EXCEPT_LOONGARCH_IPE   14
# #define EXCEPT_LOONGARCH_FPD   15
# #define EXCEPT_LOONGARCH_SXD   16
# #define EXCEPT_LOONGARCH_ASXD  17
# #define EXCEPT_LOONGARCH_FPE   18
# #define EXCEPT_LOONGARCH_TBR   64 // For code only, there is no such type in the ISA spec, the TLB refill is defined for an independent exception.
EXCEPT_LOONGARCH_INT   = 0
EXCEPT_LOONGARCH_PIL   = 1
EXCEPT_LOONGARCH_PIS   = 2
EXCEPT_LOONGARCH_PIF   = 3
EXCEPT_LOONGARCH_PME   = 4
EXCEPT_LOONGARCH_PNR   = 5
EXCEPT_LOONGARCH_PNX   = 6
EXCEPT_LOONGARCH_PPI   = 7
EXCEPT_LOONGARCH_ADE   = 8
EXCEPT_LOONGARCH_ALE   = 9
EXCEPT_LOONGARCH_BCE   = 10
EXCEPT_LOONGARCH_SYS   = 11
EXCEPT_LOONGARCH_BRK   = 12
EXCEPT_LOONGARCH_INE   = 13
EXCEPT_LOONGARCH_IPE   = 14
EXCEPT_LOONGARCH_FPD   = 15
EXCEPT_LOONGARCH_SXD   = 16
EXCEPT_LOONGARCH_ASXD  = 17
EXCEPT_LOONGARCH_FPE   = 18
EXCEPT_LOONGARCH_TBR   = 64

# 
# //
# // LoongArch processor Interrupt types.
# //
# #define EXCEPT_LOONGARCH_INT_SIP0   0
# #define EXCEPT_LOONGARCH_INT_SIP1   1
# #define EXCEPT_LOONGARCH_INT_IP0    2
# #define EXCEPT_LOONGARCH_INT_IP1    3
# #define EXCEPT_LOONGARCH_INT_IP2    4
# #define EXCEPT_LOONGARCH_INT_IP3    5
# #define EXCEPT_LOONGARCH_INT_IP4    6
# #define EXCEPT_LOONGARCH_INT_IP5    7
# #define EXCEPT_LOONGARCH_INT_IP6    8
# #define EXCEPT_LOONGARCH_INT_IP7    9
# #define EXCEPT_LOONGARCH_INT_PMC    10
# #define EXCEPT_LOONGARCH_INT_TIMER  11
# #define EXCEPT_LOONGARCH_INT_IPI    12
EXCEPT_LOONGARCH_INT_SIP0   = 0
EXCEPT_LOONGARCH_INT_SIP1   = 1
EXCEPT_LOONGARCH_INT_IP0    = 2
EXCEPT_LOONGARCH_INT_IP1    = 3
EXCEPT_LOONGARCH_INT_IP2    = 4
EXCEPT_LOONGARCH_INT_IP3    = 5
EXCEPT_LOONGARCH_INT_IP4    = 6
EXCEPT_LOONGARCH_INT_IP5    = 7
EXCEPT_LOONGARCH_INT_IP6    = 8
EXCEPT_LOONGARCH_INT_IP7    = 9
EXCEPT_LOONGARCH_INT_PMC    = 10
EXCEPT_LOONGARCH_INT_TIMER  = 11
EXCEPT_LOONGARCH_INT_IPI    = 12

# 
# //
# // For coding convenience, define the maximum valid
# // LoongArch interrupt.
# //
# #define MAX_LOONGARCH_INTERRUPT  14
MAX_LOONGARCH_INTERRUPT  = 14

# 
# typedef struct {
#   UINT64    R0;
#   UINT64    R1;
#   UINT64    R2;
#   UINT64    R3;
#   UINT64    R4;
#   UINT64    R5;
#   UINT64    R6;
#   UINT64    R7;
#   UINT64    R8;
#   UINT64    R9;
#   UINT64    R10;
#   UINT64    R11;
#   UINT64    R12;
#   UINT64    R13;
#   UINT64    R14;
#   UINT64    R15;
#   UINT64    R16;
#   UINT64    R17;
#   UINT64    R18;
#   UINT64    R19;
#   UINT64    R20;
#   UINT64    R21;
#   UINT64    R22;
#   UINT64    R23;
#   UINT64    R24;
#   UINT64    R25;
#   UINT64    R26;
#   UINT64    R27;
#   UINT64    R28;
#   UINT64    R29;
#   UINT64    R30;
#   UINT64    R31;
# 
#   UINT64    CRMD;  // CuRrent MoDe information
#   UINT64    PRMD;  // PRe-exception MoDe information
#   UINT64    EUEN;  // Extended component Unit ENable
#   UINT64    MISC;  // MISCellaneous controller
#   UINT64    ECFG;  // Exception ConFiGuration
#   UINT64    ESTAT; // Exception STATus
#   UINT64    ERA;   // Exception Return Address
#   UINT64    BADV;  // BAD Virtual address
#   UINT64    BADI;  // BAD Instruction
# } EFI_SYSTEM_CONTEXT_LOONGARCH64;
class EFI_SYSTEM_CONTEXT_LOONGARCH64 (Structure):
  _fields_ = [
    ("R0",      UINT64),
    ("R1",      UINT64),
    ("R2",      UINT64),
    ("R3",      UINT64),
    ("R4",      UINT64),
    ("R5",      UINT64),
    ("R6",      UINT64),
    ("R7",      UINT64),
    ("R8",      UINT64),
    ("R9",      UINT64),
    ("R10",     UINT64),
    ("R11",     UINT64),
    ("R12",     UINT64),
    ("R13",     UINT64),
    ("R14",     UINT64),
    ("R15",     UINT64),
    ("R16",     UINT64),
    ("R17",     UINT64),
    ("R18",     UINT64),
    ("R19",     UINT64),
    ("R20",     UINT64),
    ("R21",     UINT64),
    ("R22",     UINT64),
    ("R23",     UINT64),
    ("R24",     UINT64),
    ("R25",     UINT64),
    ("R26",     UINT64),
    ("R27",     UINT64),
    ("R28",     UINT64),
    ("R29",     UINT64),
    ("R30",     UINT64),
    ("R31",     UINT64),
    ("CRMD",    UINT64),
    ("PRMD",    UINT64),
    ("EUEN",    UINT64),
    ("MISC",    UINT64),
    ("ECFG",    UINT64),
    ("ESTAT",   UINT64),
    ("ERA",     UINT64),
    ("BADV",    UINT64),
    ("BADI",    UINT64)
  ]

# 
# ///
# /// Universal EFI_SYSTEM_CONTEXT definition.
# ///
# typedef union {
#   EFI_SYSTEM_CONTEXT_EBC            *SystemContextEbc;
#   EFI_SYSTEM_CONTEXT_IA32           *SystemContextIa32;
#   EFI_SYSTEM_CONTEXT_X64            *SystemContextX64;
#   EFI_SYSTEM_CONTEXT_IPF            *SystemContextIpf;
#   EFI_SYSTEM_CONTEXT_ARM            *SystemContextArm;
#   EFI_SYSTEM_CONTEXT_AARCH64        *SystemContextAArch64;
#   EFI_SYSTEM_CONTEXT_RISCV64        *SystemContextRiscV64;
#   EFI_SYSTEM_CONTEXT_LOONGARCH64    *SystemContextLoongArch64;
# } EFI_SYSTEM_CONTEXT;
class EFI_SYSTEM_CONTEXT (Union):
  _fields_ = [
    ("SystemContextEbc",            POINTER (EFI_SYSTEM_CONTEXT_EBC)),
    ("SystemContextIa32",           POINTER (EFI_SYSTEM_CONTEXT_IA32)),
    ("SystemContextX64",            POINTER (EFI_SYSTEM_CONTEXT_X64)),
    ("SystemContextIpf",            POINTER (EFI_SYSTEM_CONTEXT_IPF)),
    ("SystemContextArm",            POINTER (EFI_SYSTEM_CONTEXT_ARM)),
    ("SystemContextAArch64",        POINTER (EFI_SYSTEM_CONTEXT_AARCH64)),
    ("SystemContextRiscV64",        POINTER (EFI_SYSTEM_CONTEXT_RISCV64)),
    ("SystemContextLoongArch64",    POINTER (EFI_SYSTEM_CONTEXT_LOONGARCH64))
  ]

# 
# //
# // DebugSupport callback function prototypes
# //
# 
# /**
#   Registers and enables an exception callback function for the specified exception.
# 
#   @param  ExceptionType         Exception types in EBC, IA-32, x64, or IPF.
#   @param  SystemContext         Exception content.
# 
# **/
# typedef
# VOID
# (EFIAPI *EFI_EXCEPTION_CALLBACK)(
#   IN     EFI_EXCEPTION_TYPE               ExceptionType,
#   IN OUT EFI_SYSTEM_CONTEXT               SystemContext
#   );
EFI_EXCEPTION_CALLBACK = CFUNCTYPE (
  VOID,
  EFI_EXCEPTION_TYPE, # IN     ExceptionType,              
  EFI_SYSTEM_CONTEXT  # IN OUT SystemContext         
  )

# 
# /**
#   Registers and enables the on-target debug agent's periodic entry point.
# 
#   @param  SystemContext         Exception content.
# 
# **/
# typedef
# VOID
# (EFIAPI *EFI_PERIODIC_CALLBACK)(
#   IN OUT EFI_SYSTEM_CONTEXT               SystemContext
#   );
EFI_PERIODIC_CALLBACK = CFUNCTYPE (
  VOID,
  EFI_SYSTEM_CONTEXT  # IN OUT SystemContext         
  )

# 
# ///
# /// Machine type definition
# ///
# typedef enum {
#   IsaIa32    = IMAGE_FILE_MACHINE_I386,           ///< 0x014C
#   IsaX64     = IMAGE_FILE_MACHINE_X64,            ///< 0x8664
#   IsaIpf     = IMAGE_FILE_MACHINE_IA64,           ///< 0x0200
#   IsaEbc     = IMAGE_FILE_MACHINE_EBC,            ///< 0x0EBC
#   IsaArm     = IMAGE_FILE_MACHINE_ARMTHUMB_MIXED, ///< 0x01c2
#   IsaAArch64 = IMAGE_FILE_MACHINE_ARM64           ///< 0xAA64
# } EFI_INSTRUCTION_SET_ARCHITECTURE;
IsaIa32 = PeImage.IMAGE_FILE_MACHINE_I386
IsaX64  = PeImage.IMAGE_FILE_MACHINE_X64
IsaIpf  = PeImage.IMAGE_FILE_MACHINE_IA64
IsaEbc  = PeImage.IMAGE_FILE_MACHINE_EBC
IsaArm  = PeImage.IMAGE_FILE_MACHINE_ARMTHUMB_MIXED
IsaAArch64  = PeImage.IMAGE_FILE_MACHINE_ARM64
EFI_INSTRUCTION_SET_ARCHITECTURE  = ENUM

# 
# //
# // DebugSupport member function definitions
# //
# 
# /**
#   Returns the maximum value that may be used for the ProcessorIndex parameter in
#   RegisterPeriodicCallback() and RegisterExceptionCallback().
# 
#   @param  This                  A pointer to the EFI_DEBUG_SUPPORT_PROTOCOL instance.
#   @param  MaxProcessorIndex     Pointer to a caller-allocated UINTN in which the maximum supported
#                                 processor index is returned.
# 
#   @retval EFI_SUCCESS           The function completed successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_GET_MAXIMUM_PROCESSOR_INDEX)(
#   IN EFI_DEBUG_SUPPORT_PROTOCOL          *This,
#   OUT UINTN                              *MaxProcessorIndex
#   );
EFI_GET_MAXIMUM_PROCESSOR_INDEX = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN     *This
  POINTER (UINTN)                       #    OUT *MaxProcessorIndex
  )

# 
# /**
#   Registers a function to be called back periodically in interrupt context.
# 
#   @param  This                  A pointer to the EFI_DEBUG_SUPPORT_PROTOCOL instance.
#   @param  ProcessorIndex        Specifies which processor the callback function applies to.
#   @param  PeriodicCallback      A pointer to a function of type PERIODIC_CALLBACK that is the main
#                                 periodic entry point of the debug agent.
# 
#   @retval EFI_SUCCESS           The function completed successfully.
#   @retval EFI_ALREADY_STARTED   Non-NULL PeriodicCallback parameter when a callback
#                                 function was previously registered.
#   @retval EFI_OUT_OF_RESOURCES  System has insufficient memory resources to register new callback
#                                 function.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REGISTER_PERIODIC_CALLBACK)(
#   IN EFI_DEBUG_SUPPORT_PROTOCOL          *This,
#   IN UINTN                               ProcessorIndex,
#   IN EFI_PERIODIC_CALLBACK               PeriodicCallback
#   );
EFI_REGISTER_PERIODIC_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  EFI_PERIODIC_CALLBACK                 # IN    PeriodicCallback
  )

# 
# /**
#   Registers a function to be called when a given processor exception occurs.
# 
#   @param  This                  A pointer to the EFI_DEBUG_SUPPORT_PROTOCOL instance.
#   @param  ProcessorIndex        Specifies which processor the callback function applies to.
#   @param  ExceptionCallback     A pointer to a function of type EXCEPTION_CALLBACK that is called
#                                 when the processor exception specified by ExceptionType occurs.
#   @param  ExceptionType         Specifies which processor exception to hook.
# 
#   @retval EFI_SUCCESS           The function completed successfully.
#   @retval EFI_ALREADY_STARTED   Non-NULL PeriodicCallback parameter when a callback
#                                 function was previously registered.
#   @retval EFI_OUT_OF_RESOURCES  System has insufficient memory resources to register new callback
#                                 function.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REGISTER_EXCEPTION_CALLBACK)(
#   IN EFI_DEBUG_SUPPORT_PROTOCOL          *This,
#   IN UINTN                               ProcessorIndex,
#   IN EFI_EXCEPTION_CALLBACK              ExceptionCallback,
#   IN EFI_EXCEPTION_TYPE                  ExceptionType
#   );
EFI_REGISTER_EXCEPTION_CALLBACK = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  EFI_EXCEPTION_CALLBACK,               # IN    ExceptionCallback
  EFI_EXCEPTION_TYPE                    # IN    ExceptionType
  )

# 
# /**
#   Invalidates processor instruction cache for a memory range. Subsequent execution in this range
#   causes a fresh memory fetch to retrieve code to be executed.
# 
#   @param  This                  A pointer to the EFI_DEBUG_SUPPORT_PROTOCOL instance.
#   @param  ProcessorIndex        Specifies which processor's instruction cache is to be invalidated.
#   @param  Start                 Specifies the physical base of the memory range to be invalidated.
#   @param  Length                Specifies the minimum number of bytes in the processor's instruction
#                                 cache to invalidate.
# 
#   @retval EFI_SUCCESS           The function completed successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_INVALIDATE_INSTRUCTION_CACHE)(
#   IN EFI_DEBUG_SUPPORT_PROTOCOL          *This,
#   IN UINTN                               ProcessorIndex,
#   IN VOID                                *Start,
#   IN UINT64                              Length
#   );
EFI_INVALIDATE_INSTRUCTION_CACHE = CFUNCTYPE (
  EFI_STATUS,
  POINTER (EFI_DEBUG_SUPPORT_PROTOCOL), # IN    *This
  UINTN,                                # IN    MaxProcessorIndex
  PVOID,                                # IN    *Start
  UINT64                                # IN    Length
  )

# 
# ///
# /// This protocol provides the services to allow the debug agent to register
# /// callback functions that are called either periodically or when specific
# /// processor exceptions occur.
# ///
# struct _EFI_DEBUG_SUPPORT_PROTOCOL {
#   ///
#   /// Declares the processor architecture for this instance of the EFI Debug Support protocol.
#   ///
#   EFI_INSTRUCTION_SET_ARCHITECTURE    Isa;
#   EFI_GET_MAXIMUM_PROCESSOR_INDEX     GetMaximumProcessorIndex;
#   EFI_REGISTER_PERIODIC_CALLBACK      RegisterPeriodicCallback;
#   EFI_REGISTER_EXCEPTION_CALLBACK     RegisterExceptionCallback;
#   EFI_INVALIDATE_INSTRUCTION_CACHE    InvalidateInstructionCache;
# };
EFI_DEBUG_SUPPORT_PROTOCOL._fields_ = [
    ("Isa",                         EFI_INSTRUCTION_SET_ARCHITECTURE),
    ("GetMaximumProcessorIndex",    EFI_GET_MAXIMUM_PROCESSOR_INDEX),
    ("RegisterPeriodicCallback",    EFI_REGISTER_PERIODIC_CALLBACK),
    ("RegisterExceptionCallback",   EFI_REGISTER_EXCEPTION_CALLBACK),
    ("InvalidateInstructionCache",  EFI_INVALIDATE_INSTRUCTION_CACHE)
  ]
# 
# extern EFI_GUID  gEfiDebugSupportProtocolGuid;
# 
# #endif
# 