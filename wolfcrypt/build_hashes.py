# build_hashes.py
#
# Copyright (C) 2006-2016 wolfSSL Inc.
#
# This file is part of wolfSSL. (formerly known as CyaSSL)
#
# wolfSSL is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# wolfSSL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
import os

from cffi import FFI

ffi = FFI()

ffi.set_source("wolfcrypt._hashes",
    """
        #include <wolfssl/options.h>
        #include <wolfssl/wolfcrypt/sha.h>
        #include <wolfssl/wolfcrypt/sha256.h>
        #include <wolfssl/wolfcrypt/sha512.h>
    """,
    include_dirs=["/usr/local/include"],
    library_dirs=["/usr/local/lib"],
    libraries=["wolfssl"],
)

ffi.cdef(
"""

    typedef unsigned char byte;
    typedef unsigned int  word32;

    typedef struct { ...; } Sha;

    int wc_InitSha(Sha* sha);
    int wc_ShaUpdate(Sha* sha, const byte* data, word32 length);
    int wc_ShaFinal(Sha* sha, byte* digest);


    typedef struct { ...; } Sha256;

    int wc_InitSha256(Sha256* sha);
    int wc_Sha256Update(Sha256* sha, const byte* data, word32 length);
    int wc_Sha256Final(Sha256* sha, byte* digest);


    typedef struct { ...; } Sha384;

    int wc_InitSha384(Sha384* sha);
    int wc_Sha384Update(Sha384* sha, const byte* data, word32 length);
    int wc_Sha384Final(Sha384* sha, byte* digest);


    typedef struct { ...; } Sha512;

    int wc_InitSha512(Sha512* sha);
    int wc_Sha512Update(Sha512* sha, const byte* data, word32 length);
    int wc_Sha512Final(Sha512* sha, byte* digest);

"""
)

if __name__ == "__main__":
    ffi.compile(verbose=1)