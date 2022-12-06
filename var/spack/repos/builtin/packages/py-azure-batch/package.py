# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyAzureBatch(PythonPackage):
    """Microsoft Azure Batch Client Library for Python."""

    homepage = "https://github.com/Azure/azure-sdk-for-python"
    pypi = "azure-batch/azure-batch-9.0.0.zip"

    version("10.0.0", sha256="83d7a2b0be42ca456ac2b56fa3dc6ce704c130e888d37d924072c1d3718f32d0")
    version("9.0.0", sha256="47ca6f50a640915e1cdc5ce3c1307abe5fa3a636236e561119cf62d9df384d84")

    depends_on("py-setuptools", type="build")
    # https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/batch/azure-batch/setup.py#L69
    depends_on("py-msrest@0.5.0:", type=("build", "run"))
    depends_on("py-msrestazure@0.4.32:1", type=("build", "run"))
    depends_on("py-azure-common@1.1:1", type=("build", "run"))
