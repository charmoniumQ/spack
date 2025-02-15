# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyNbclient(PythonPackage):
    """A client library for executing notebooks.

    Formally nbconvert's ExecutePreprocessor."""

    homepage = "https://jupyter.org/"
    pypi = "nbclient/nbclient-0.5.0.tar.gz"

    version("0.6.7", sha256="3c5a7fc6bb74be7d31edf2817b44501a65caa99e5e56363bc359649b97cd24b9")
    version("0.6.6", sha256="0df76a7961d99a681b4796c74a1f2553b9f998851acc01896dce064ad19a9027")
    version("0.5.13", sha256="40c52c9b5e3c31faecaee69f202b3f53e38d7c1c563de0fadde9d7eda0fdafe8")
    version("0.5.5", sha256="ed7d18431393750d29a64da432e0b7889274eb5a5056682be5691b1b1dc8f755")
    version("0.5.0", sha256="8ad52d27ba144fca1402db014857e53c5a864a2f407be66ca9d74c3a56d6591d")

    depends_on("python@3.7:", when="@0.5.13:", type=("build", "run"))
    depends_on("python@3.6.1:", when="@0.5.5:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-jupyter-client@6.1.5:", type=("build", "run"))
    depends_on("py-nbformat@5.0:", type=("build", "run"))
    depends_on("py-async-generator", type=("build", "run"), when="@0.5.0")
    depends_on("py-nest-asyncio", type=("build", "run"))
    depends_on("py-traitlets@5.2.2:", when="@0.6:", type=("build", "run"))
    depends_on("py-traitlets@5:", when="@0.5.13:", type=("build", "run"))
    depends_on("py-traitlets@4.2:", type=("build", "run"))
