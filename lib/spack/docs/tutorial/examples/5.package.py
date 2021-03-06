##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Mpileaks(Package):
    """Tool to detect and report MPI objects like MPI_Requests and
    MPI_Datatypes."""

    homepage = "https://github.com/hpc/mpileaks"
    url      = "https://github.com/hpc/mpileaks/releases/download/v1.0/mpileaks-1.0.tar.gz"

    version('1.0', '8838c574b39202a57d7c2d68692718aa')

    variant('stackstart', values=int, default=0, description='Specify the number of stack frames to truncate.')

    depends_on('mpi')
    depends_on('adept-utils')
    depends_on('callpath')

    def install(self, spec, prefix):
        stackstart = int(self.spec.variants['stackstart'].value)
        confargs = ['--with-adept-utils=%s' % self.spec['adept-utils'].prefix,
                    '--with-callpath=%s' % self.spec['callpath'].prefix,
                    '--prefix=%s' % self.spec.prefix]
        if stackstart:
            confargs.extend(['--with-stack-start-c=%s' % stackstart,
                             '--with-stack-start-fortran=%s' % stackstart])
        configure(*confargs)
        make()
        make('install')
