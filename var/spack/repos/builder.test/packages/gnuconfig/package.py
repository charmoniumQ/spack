# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class Gnuconfig(Package):
    """This package is needed to allow mocking AutotoolsPackage objects"""

    homepage = "http://www.example.com"
    url = "http://www.example.com/a-1.0.tar.gz"

    version("2.0", "abcdef0123456789abcdef0123456789")
    version("1.0", "0123456789abcdef0123456789abcdef")
