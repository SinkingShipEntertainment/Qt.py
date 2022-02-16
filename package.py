name = 'qtpy'

version = '1.3.6'

authors = [
	'Mottosso',
]

description = '''Qt wrapper'''

with scope('config') as c:
	# Determine location to release: internal (int) vs external (ext)
	# NOTE: Modify this variable to reflect the current package situation
	release_as = 'ext'

	# The 'c' variable here is actually rezconfig.py
	# 'release_packages_path' is a variable defined inside rezconfig.py

	import os
	if release_as == 'int':
		c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_INT']
	elif release_as == 'ext':
		c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
]

private_build_requires = [
]

variants = [
	['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

def commands():
	env.REZ_QTPY_ROOT = '{root}'

	env.PYTHONPATH.append('{root}')

build_command = 'rez python {root}/rez_build.py'

uuid = 'repository.Qt.py'

