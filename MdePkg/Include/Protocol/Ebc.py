# /** @file
#   Describes the protocol interface to the EBC interpreter.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# Ebc.py
#
# EfiPy2.MdePkg.Protocol.Ebc
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __EFI_EBC_PROTOCOL_H__
# #define __EFI_EBC_PROTOCOL_H__
from EfiPy2 import *

# 
# #define EFI_EBC_INTERPRETER_PROTOCOL_GUID \
#   { \
#     0x13AC6DD1, 0x73D0, 0x11D4, {0xB0, 0x6B, 0x00, 0xAA, 0x00, 0xBD, 0x6D, 0xE7 } \
#   }
gEfiEbcProtocolGuid   = \
  EFI_GUID (0x13AC6DD1, 0x73D0, 0x11D4, (0xB0, 0x6B, 0x00, 0xAA, 0x00, 0xBD, 0x6D, 0xE7 ))

# 
# //
# // Define OPCODES
# //
# #define OPCODE_BREAK    0x00
# #define OPCODE_JMP      0x01
# #define OPCODE_JMP8     0x02
# #define OPCODE_CALL     0x03
# #define OPCODE_RET      0x04
# #define OPCODE_CMPEQ    0x05
# #define OPCODE_CMPLTE   0x06
# #define OPCODE_CMPGTE   0x07
# #define OPCODE_CMPULTE  0x08
# #define OPCODE_CMPUGTE  0x09
# #define OPCODE_NOT      0x0A
# #define OPCODE_NEG      0x0B
# #define OPCODE_ADD      0x0C
# #define OPCODE_SUB      0x0D
# #define OPCODE_MUL      0x0E
# #define OPCODE_MULU     0x0F
# #define OPCODE_DIV      0x10
# #define OPCODE_DIVU     0x11
# #define OPCODE_MOD      0x12
# #define OPCODE_MODU     0x13
# #define OPCODE_AND      0x14
# #define OPCODE_OR       0x15
# #define OPCODE_XOR      0x16
# #define OPCODE_SHL      0x17
# #define OPCODE_SHR      0x18
# #define OPCODE_ASHR     0x19
# #define OPCODE_EXTNDB   0x1A
# #define OPCODE_EXTNDW   0x1B
# #define OPCODE_EXTNDD   0x1C
# #define OPCODE_MOVBW    0x1D
# #define OPCODE_MOVWW    0x1E
# #define OPCODE_MOVDW    0x1F
# #define OPCODE_MOVQW    0x20
# #define OPCODE_MOVBD    0x21
# #define OPCODE_MOVWD    0x22
# #define OPCODE_MOVDD    0x23
# #define OPCODE_MOVQD    0x24
# #define OPCODE_MOVSNW   0x25  // Move signed natural with word index
# #define OPCODE_MOVSND   0x26  // Move signed natural with dword index
# //
# // #define OPCODE_27         0x27
# //
# #define OPCODE_MOVQQ     0x28 // Does this go away?
# #define OPCODE_LOADSP    0x29
# #define OPCODE_STORESP   0x2A
# #define OPCODE_PUSH      0x2B
# #define OPCODE_POP       0x2C
# #define OPCODE_CMPIEQ    0x2D
# #define OPCODE_CMPILTE   0x2E
# #define OPCODE_CMPIGTE   0x2F
# #define OPCODE_CMPIULTE  0x30
# #define OPCODE_CMPIUGTE  0x31
# #define OPCODE_MOVNW     0x32
# #define OPCODE_MOVND     0x33
# //
# // #define OPCODE_34         0x34
# //
# #define OPCODE_PUSHN   0x35
# #define OPCODE_POPN    0x36
# #define OPCODE_MOVI    0x37
# #define OPCODE_MOVIN   0x38
# #define OPCODE_MOVREL  0x39
OPCODE_BREAK    = 0x00
OPCODE_JMP      = 0x01
OPCODE_JMP8     = 0x02
OPCODE_CALL     = 0x03
OPCODE_RET      = 0x04
OPCODE_CMPEQ    = 0x05
OPCODE_CMPLTE   = 0x06
OPCODE_CMPGTE   = 0x07
OPCODE_CMPULTE  = 0x08
OPCODE_CMPUGTE  = 0x09
OPCODE_NOT      = 0x0A
OPCODE_NEG      = 0x0B
OPCODE_ADD      = 0x0C
OPCODE_SUB      = 0x0D
OPCODE_MUL      = 0x0E
OPCODE_MULU     = 0x0F
OPCODE_DIV      = 0x10
OPCODE_DIVU     = 0x11
OPCODE_MOD      = 0x12
OPCODE_MODU     = 0x13
OPCODE_AND      = 0x14
OPCODE_OR       = 0x15
OPCODE_XOR      = 0x16
OPCODE_SHL      = 0x17
OPCODE_SHR      = 0x18
OPCODE_ASHR     = 0x19
OPCODE_EXTNDB   = 0x1A
OPCODE_EXTNDW   = 0x1B
OPCODE_EXTNDD   = 0x1C
OPCODE_MOVBW    = 0x1D
OPCODE_MOVWW    = 0x1E
OPCODE_MOVDW    = 0x1F
OPCODE_MOVQW    = 0x20
OPCODE_MOVBD    = 0x21
OPCODE_MOVWD    = 0x22
OPCODE_MOVDD    = 0x23
OPCODE_MOVQD    = 0x24
OPCODE_MOVSNW   = 0x25
OPCODE_MOVSND   = 0x26
#
# OPCODE_27         = 0x27
#
OPCODE_MOVQQ     = 0x28
OPCODE_LOADSP    = 0x29
OPCODE_STORESP   = 0x2A
OPCODE_PUSH      = 0x2B
OPCODE_POP       = 0x2C
OPCODE_CMPIEQ    = 0x2D
OPCODE_CMPILTE   = 0x2E
OPCODE_CMPIGTE   = 0x2F
OPCODE_CMPIULTE  = 0x30
OPCODE_CMPIUGTE  = 0x31
OPCODE_MOVNW     = 0x32
OPCODE_MOVND     = 0x33
# 
# OPCODE_34         = 0x34
# 
OPCODE_PUSHN   = 0x35
OPCODE_POPN    = 0x36
OPCODE_MOVI    = 0x37
OPCODE_MOVIN   = 0x38
OPCODE_MOVREL  = 0x39

# 
# //
# // Bit masks for opcode encodings
# //
# #define OPCODE_M_OPCODE       0x3F  // bits of interest for first level decode
# #define OPCODE_M_IMMDATA      0x80
# #define OPCODE_M_IMMDATA64    0x40
# #define OPCODE_M_64BIT        0x40  // for CMP
# #define OPCODE_M_RELADDR      0x10  // for CALL instruction
# #define OPCODE_M_CMPI32_DATA  0x80  // for CMPI
# #define OPCODE_M_CMPI64       0x40  // for CMPI 32 or 64 bit comparison
# #define OPERAND_M_MOVIN_N     0x80
# #define OPERAND_M_CMPI_INDEX  0x10
OPCODE_M_OPCODE       = 0x3F  # bits of interest for first level decode
OPCODE_M_IMMDATA      = 0x80
OPCODE_M_IMMDATA64    = 0x40
OPCODE_M_64BIT        = 0x40  # for CMP
OPCODE_M_RELADDR      = 0x10  # for CALL instruction
OPCODE_M_CMPI32_DATA  = 0x80  # for CMPI
OPCODE_M_CMPI64       = 0x40  # for CMPI 32 or 64 bit comparison
OPERAND_M_MOVIN_N     = 0x80
OPERAND_M_CMPI_INDEX  = 0x10

# 
# //
# // Masks for instructions that encode presence of indexes for operand1 and/or
# // operand2.
# //
# #define OPCODE_M_IMMED_OP1  0x80
# #define OPCODE_M_IMMED_OP2  0x40
OPCODE_M_IMMED_OP1  = 0x80
OPCODE_M_IMMED_OP2  = 0x40

# 
# //
# // Bit masks for operand encodings
# //
# #define OPERAND_M_INDIRECT1  0x08
# #define OPERAND_M_INDIRECT2  0x80
# #define OPERAND_M_OP1        0x07
# #define OPERAND_M_OP2        0x70
OPERAND_M_INDIRECT1  = 0x08
OPERAND_M_INDIRECT2  = 0x80
OPERAND_M_OP1        = 0x07
OPERAND_M_OP2        = 0x70

# 
# //
# // Masks for data manipulation instructions
# //
# #define DATAMANIP_M_64       0x40 // 64-bit width operation
# #define DATAMANIP_M_IMMDATA  0x80
DATAMANIP_M_64       = 0x40 # 64-bit width operation
DATAMANIP_M_IMMDATA  = 0x80

# 
# //
# // For MOV instructions, need a mask for the opcode when immediate
# // data applies to R2.
# //
# #define OPCODE_M_IMMED_OP2  0x40
OPCODE_M_IMMED_OP2  = 0x40

# 
# //
# // The MOVI/MOVIn instructions use bit 6 of operands byte to indicate
# // if an index is present. Then bits 4 and 5 are used to indicate the width
# // of the move.
# //
# #define MOVI_M_IMMDATA    0x40
# #define MOVI_M_DATAWIDTH  0xC0
# #define MOVI_DATAWIDTH16  0x40
# #define MOVI_DATAWIDTH32  0x80
# #define MOVI_DATAWIDTH64  0xC0
# #define MOVI_M_MOVEWIDTH  0x30
# #define MOVI_MOVEWIDTH8   0x00
# #define MOVI_MOVEWIDTH16  0x10
# #define MOVI_MOVEWIDTH32  0x20
# #define MOVI_MOVEWIDTH64  0x30
MOVI_M_IMMDATA    = 0x40
MOVI_M_DATAWIDTH  = 0xC0
MOVI_DATAWIDTH16  = 0x40
MOVI_DATAWIDTH32  = 0x80
MOVI_DATAWIDTH64  = 0xC0
MOVI_M_MOVEWIDTH  = 0x30
MOVI_MOVEWIDTH8   = 0x00
MOVI_MOVEWIDTH16  = 0x10
MOVI_MOVEWIDTH32  = 0x20
MOVI_MOVEWIDTH64  = 0x30

# 
# //
# // Masks for CALL instruction encodings
# //
# #define OPERAND_M_RELATIVE_ADDR  0x10
# #define OPERAND_M_NATIVE_CALL    0x20
OPERAND_M_RELATIVE_ADDR  = 0x10
OPERAND_M_NATIVE_CALL    = 0x20

# 
# //
# // Masks for decoding push/pop instructions
# //
# #define PUSHPOP_M_IMMDATA  0x80 // opcode bit indicating immediate data
# #define PUSHPOP_M_64       0x40 // opcode bit indicating 64-bit operation
PUSHPOP_M_IMMDATA  = 0x80 # opcode bit indicating immediate data
PUSHPOP_M_64       = 0x40 # opcode bit indicating 64-bit operation

# //
# // Mask for operand of JMP instruction
# //
# #define JMP_M_RELATIVE     0x10
# #define JMP_M_CONDITIONAL  0x80
# #define JMP_M_CS           0x40
JMP_M_RELATIVE     = 0x10
JMP_M_CONDITIONAL  = 0x80
JMP_M_CS           = 0x40

# 
# //
# // Macros to determine if a given operand is indirect
# //
# #define OPERAND1_INDIRECT(op)  ((op) & OPERAND_M_INDIRECT1)
def OPERAND1_INDIRECT(op):
  return ((op) & OPERAND_M_INDIRECT1)

# #define OPERAND2_INDIRECT(op)  ((op) & OPERAND_M_INDIRECT2)
def OPERAND2_INDIRECT(op):
  return ((op) & OPERAND_M_INDIRECT2)

# 
# //
# // Macros to extract the operands from second byte of instructions
# //
# #define OPERAND1_REGNUM(op)  ((op) & OPERAND_M_OP1)
def OPERAND1_REGNUM(op):
  return ((op) & OPERAND_M_OP1)
  
# #define OPERAND2_REGNUM(op)  (((op) & OPERAND_M_OP2) >> 4)
def OPERAND2_REGNUM(op):
  return (((op) & OPERAND_M_OP2) >> 4)

# 
# #define OPERAND1_CHAR(op)  ('0' + OPERAND1_REGNUM (op))
def OPERAND1_CHAR(op):
  return chr (ord ('0') + OPERAND1_REGNUM (op))

# #define OPERAND2_CHAR(op)  ('0' + OPERAND2_REGNUM (op))
def OPERAND2_CHAR(op):
  return chr (ord ('0') + OPERAND2_REGNUM (op))

# 
# //
# // Condition masks usually for byte 1 encodings of code
# //
# #define CONDITION_M_CONDITIONAL  0x80
# #define CONDITION_M_CS           0x40
# 
# ///
# /// Protocol Guid Name defined in spec.
# ///
# #define EFI_EBC_PROTOCOL_GUID  EFI_EBC_INTERPRETER_PROTOCOL_GUID
EFI_EBC_PROTOCOL_GUID = gEfiEbcProtocolGuid

# 
# ///
# /// Define for forward reference.
# ///
# typedef struct _EFI_EBC_PROTOCOL EFI_EBC_PROTOCOL;
class EFI_EBC_PROTOCOL (Structure):
  pass

# 
# /**
#   Creates a thunk for an EBC entry point, returning the address of the thunk.
# 
#   A PE32+ EBC image, like any other PE32+ image, contains an optional header that specifies the
#   entry point for image execution. However, for EBC images, this is the entry point of EBC
#   instructions, so is not directly executable by the native processor. Therefore, when an EBC image is
#   loaded, the loader must call this service to get a pointer to native code (thunk) that can be executed,
#   which will invoke the interpreter to begin execution at the original EBC entry point.
# 
#   @param  This          A pointer to the EFI_EBC_PROTOCOL instance.
#   @param  ImageHandle   Handle of image for which the thunk is being created.
#   @param  EbcEntryPoint Address of the actual EBC entry point or protocol service the thunk should call.
#   @param  Thunk         Returned pointer to a thunk created.
# 
#   @retval EFI_SUCCESS            The function completed successfully.
#   @retval EFI_INVALID_PARAMETER  Image entry point is not 2-byte aligned.
#   @retval EFI_OUT_OF_RESOURCES   Memory could not be allocated for the thunk.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EBC_CREATE_THUNK)(
#   IN EFI_EBC_PROTOCOL           *This,
#   IN EFI_HANDLE                 ImageHandle,
#   IN VOID                       *EbcEntryPoint,
#   OUT VOID                      **Thunk
#   );
EFI_EBC_CREATE_THUNK = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EFI_HANDLE,                 # IN  ImageHandle,
  PVOID,                      # IN  *EbcEntryPoint,
  POINTER(PVOID)              # OUT **Thunk
  )

# 
# /**
#   Called prior to unloading an EBC image from memory.
# 
#   This function is called after an EBC image has exited, but before the image is actually unloaded. It
#   is intended to provide the interpreter with the opportunity to perform any cleanup that may be
#   necessary as a result of loading and executing the image.
# 
#   @param  This          A pointer to the EFI_EBC_PROTOCOL instance.
#   @param  ImageHandle   Image handle of the EBC image that is being unloaded from memory.
# 
#   @retval EFI_SUCCESS            The function completed successfully.
#   @retval EFI_INVALID_PARAMETER  Image handle is not recognized as belonging
#                                  to an EBC image that has been executed.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EBC_UNLOAD_IMAGE)(
#   IN EFI_EBC_PROTOCOL           *This,
#   IN EFI_HANDLE                 ImageHandle
#   );
EFI_EBC_UNLOAD_IMAGE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EFI_HANDLE                  # IN  ImageHandle
  )

# 
# /**
#   This is the prototype for the Flush callback routine. A pointer to a routine
#   of this type is passed to the EBC EFI_EBC_REGISTER_ICACHE_FLUSH protocol service.
# 
#   @param  Start  The beginning physical address to flush from the processor's instruction cache.
#   @param  Length The number of bytes to flush from the processor's instruction cache.
# 
#   @retval EFI_SUCCESS            The function completed successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EBC_ICACHE_FLUSH)(
#   IN EFI_PHYSICAL_ADDRESS     Start,
#   IN UINT64                   Length
#   );
EBC_ICACHE_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  EFI_PHYSICAL_ADDRESS, # IN  Start
  UINT64                # IN  Length
  )

# 
# /**
#   Registers a callback function that the EBC interpreter calls to flush
#   the processor instruction cache following creation of thunks.
# 
#   @param  This       A pointer to the EFI_EBC_PROTOCOL instance.
#   @param  Flush      Pointer to a function of type EBC_ICACH_FLUSH.
# 
#   @retval EFI_SUCCESS            The function completed successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EBC_REGISTER_ICACHE_FLUSH)(
#   IN EFI_EBC_PROTOCOL           *This,
#   IN EBC_ICACHE_FLUSH           Flush
#   );
EFI_EBC_REGISTER_ICACHE_FLUSH = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  EBC_ICACHE_FLUSH            # IN  Flush
  )

# 
# /**
#   Called to get the version of the interpreter.
# 
#   This function is called to get the version of the loaded EBC interpreter. The value and format of the
#   returned version is identical to that returned by the EBC BREAK 1 instruction.
# 
#   @param  This       A pointer to the EFI_EBC_PROTOCOL instance.
#   @param  Version    Pointer to where to store the returned version of the interpreter.
# 
#   @retval EFI_SUCCESS            The function completed successfully.
#   @retval EFI_INVALID_PARAMETER  Version pointer is NULL.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_EBC_GET_VERSION)(
#   IN EFI_EBC_PROTOCOL           *This,
#   IN OUT UINT64                 *Version
#   );
EFI_EBC_GET_VERSION = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_EBC_PROTOCOL),  # IN  *This
  POINTER(UINT64)             # IN  *Version
  )

# 
# ///
# /// The EFI EBC protocol provides services to load and execute EBC images, which will typically be
# /// loaded into option ROMs. The image loader will load the EBC image, perform standard relocations,
# /// and invoke the CreateThunk() service to create a thunk for the EBC image's entry point. The
# /// image can then be run using the standard EFI start image services.
# ///
# struct _EFI_EBC_PROTOCOL {
#   EFI_EBC_CREATE_THUNK             CreateThunk;
#   EFI_EBC_UNLOAD_IMAGE             UnloadImage;
#   EFI_EBC_REGISTER_ICACHE_FLUSH    RegisterICacheFlush;
#   EFI_EBC_GET_VERSION              GetVersion;
# };
EFI_EBC_PROTOCOL._fields_ = [
    ("CreateThunk",         EFI_EBC_CREATE_THUNK),
    ("UnloadImage",         EFI_EBC_UNLOAD_IMAGE),
    ("RegisterICacheFlush", EFI_EBC_REGISTER_ICACHE_FLUSH),
    ("GetVersion",          EFI_EBC_GET_VERSION)
  ]

# 
# //
# // Extern the global EBC protocol GUID
# //
# extern EFI_GUID  gEfiEbcProtocolGuid;
# 
# #endif
# 