from spack import *

class PyTornado(Package):
    """Python web framework and asynchronous networking library"""
    homepage = "http://www.tornadoweb.org/"
    url      = "https://github.com/tornadoweb/tornado/archive/v4.2.1.tar.gz"

    version('4.2.1', '74e7c4a61e40226e6c50f11bcef75af1')

    extends('python')
    depends_on('py-setuptools@18.1')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
