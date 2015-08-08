from spack import *

class PyJinja2(Package):
    """template engine written in pure Python"""
    homepage = "http://jinja.pocoo.org/"
    url      = "https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.8.tar.gz"

    version('2.8', 'edb51693fe22c53cee5403775c71a99e')

    extends('python')
    depends_on("py-setuptools@18.1")

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)

