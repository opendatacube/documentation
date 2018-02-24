#!python3

import re,sys,os
import yaml
import subprocess

if len(sys.argv) < 2:
    print('Parse the Open Data Cube .travis/envionment.yaml python module',
          'requirements from Travis/Anaconda format to standard Pip format.')
    print('')
    print('Python modules are installed with,')
    print('    pip3 install --upgrade [module]')
    print('If --dry-run then the module names and versions are printed to stdout in pip format.')
    print('')
    print('Usage:',
          'python3 pip_from_travis.py3 path/to/.travis/environment.yaml',
          '[--dry-run]')
    sys.exit(0)

yml = sys.argv[1]
if not os.path.isfile(yml):
    print('YAML file not found:', yml)
    sys.exit(1)

dryrun = False
if len(sys.argv) > 2:
    if re.match('--dry-run', sys.argv[2]):
        dryrun = True
    else:
        print('Unknown option:', sys.argv[2])
        sys.exit(1)

# Skip these regexs
skip = {}
skip['^gdal'] = 'Do separately for version matching with system GDAL'
# Rename these modules (after regex)
rename = {}
rename['redis-py'] = 'redispy'  # Anaconda to pip rename

# Store pip modules and versions, in pip format (strings)
pips = []

def parse_list(lst):
    """Parse a list of travis / anaconda modules and versions"""
    for k in lst:
        if isinstance(k, dict):
            for j in k.keys(): parse_list(k[j])
        else:
            parse_item(k)

def parse_item(k):
    """Parse a module with optional version item"""
    m = re.search('^(\S+)\s*(([>=]+)\s*(\S+))?', k)
    if not m:
       print('Could not parse item:', k)
       return
    mod = m.group(1)
    fn = ''
    ver = ''
    if m.group(2) is not None:
        fn = m.group(3)
        ver = m.group(4)
    # Skips
    for s in skip.keys():
        if re.search(s, mod):
            print('Skip:', k, '|', skip[s])
            return
    # Rename
    if mod in rename: mod = rename[mod]
    if fn == '=': fn = '=='
    # Save
    pips.append('{:s}{:s}{:s}'.format(mod, fn, ver))

# Main
with open(yml, 'r') as F:
    cfg = yaml.load(F)
    parse_list(cfg['dependencies'])

for p in pips:
    if dryrun:
        print(p)
        continue
    cmd = ['pip3', 'install', '--upgrade', p]
    if subprocess.call(cmd):
        print('Error in cmd:', cmd)
        sys.exit(1)
        
