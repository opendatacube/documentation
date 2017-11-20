# Mac and Homebrew build and install instructions

## Xcode command line tools
1. http://developer.apple.com
2. Downloads link
3. More downloads link
4. Search 'command line tools'
5. Select latest version for the OS
6. Download and Install

Which version of CLT are installed?
```bash
pkgutil --pkgs | grep -i tools
pkgutil --pkg-info=com.apple.pkg.CLTools_Executables
```

## Homebrew
https://brew.sh

1. Install as per install instructions, like
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Get a github token for Homebrew
  * No github scopes required
  * https://github.com/settings/tokens/new?scopes=&description=Homebrew
```bash
echo 'export HOMEBREW_GITHUB_API_TOKEN="your_new_token"' >> ~/.bash_profile
source ~/.bash_profile
```

3. Set directory permissions (optional)
  * Not critical for brew install but handy for apps that need to write to /usr/local
```bash
[optional, may require https://apple.stackexchange.com/questions/208478]
sudo chown <user>:admin /usr/local
```

4. Get homebrew to a happy place
```bash
brew update
brew update  # a second time
brew doctor  # best to fix any concerns before continuing
```

5. Set paths
  * Mac OS X environment checks .bash_profile, .bash_login, .profile in this order. It will run whichever is the highest in the hierarchy so if you have .bash_profile it will not check .profile. https://stackoverflow.com/a/7376412
  * If /etc/paths adds /usr/local/bin, put /usr/local/sbin here too.
  * If /etc/paths and path_helper aren't valid then use this export:
```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH >> ~/.bash_profile
```
  * Also note that Homebrew defines python2 and python3. Both can be used. 'python' will default to the system python. See https://docs.brew.sh/Homebrew-and-Python.html and https://github.com/Homebrew/homebrew-core/issues/15746.
  * To make 'python' be one of the homebrew pythons use this export:
```bash
[optional]
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```

## Packages
Not all of these are critical but they are handy.
```bash
brew install python3 (and/or python2, you can have both)
brew install zlib
brew install hdf5
brew install netcdf
brew install geos
brew install proj
brew install imagemagick
brew install homebrew/science/nco  # requires java
#brew install gdal  # version 1.11.5
brew install libyaml
brew install wget  # or curl if you prefer
```
To brew GDAL2, see https://www.karambelkar.info/2016/10/gdal-2-on-mac-with-homebrew/
```bash
mkdir -p /usr/local/lib/gdalplugins/2.2
chmod -R 0777 /usr/local/lib/gdalplugins
brew unlink gdal
brew tap osgeo/osgeo4mac && brew tap --repair
brew install jasper netcdf # gdal dependencies
brew install gdal2 --with-armadillo --with-complete --with-libkml
brew link --force gdal2
gdal-config --version
```

To Pip or Brew? Pip is preferred for python libs
```bash
# pip3 or pip2
# packages can be combined into one line but its then harder to isolate and fix any errors
# --upgrade is for convenience only
pip3 install --upgrade setuptools
pip3 install --upgrade nose
pip3 install --upgrade numpy
pip3 install --upgrade scipy
pip3 install --upgrade h5py
pip3 install --upgrade netCDF4
pip3 install --upgrade gdal==2.2.2  # version needs to match brew version, e.g. 1.11.5 if using standard brew
pip3 install --upgrade matplotlib

wget https://downloads.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz
tar xzf basemap-1.0.7.tar.gz
cd basemap-1.0.7
pip3 install .

pip3 install --upgrade pyproj
pip3 install --upgrade pyshp
pip3 install --upgrade pydap
pip3 install --upgrade glueviz  # includes pandas
pip3 install --upgrade pillow
pip3 install --upgrade shapely

pip3 install --upgrade jupyter jupyterdrive
pip3 install --upgrade rasterio numexpr

# For data cube
pip3 install --upgrade pep8 pylint fiona pycodestyle
pip3 install --upgrade pytest ptest-cov hypothesis mock
```

Postgresql.app vs Brew? Both do a similar job > stick with brew
```bash
brew install postgresql

  To have launchd start postgresql now and restart at login:
    brew services start postgresql
  Or, if you don't want/need a background service you can just run:
    postgres -D /usr/local/var/postgres
    (or similarly .. pg_ctl -D /usr/local/var/postgres start)

brew install postgis

  To create a spatially-enabled database, see the documentation:
    http://postgis.net/docs/manual-2.2/postgis_installation.html#create_new_db_extensions
  PostGIS SQL scripts installed to:
    /usr/local/opt/postgis/share/postgis
  PostGIS plugin libraries installed to:
    /usr/local/lib
  PostGIS extension modules installed to:
    /usr/local/share/postgresql/extension

pip3 install psycopg2
```

## Virtual env
* https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments
```bash
# Do once to set up the environment (target-dir)
python3 -m venv --clear --system-site-packages [target-dir]

# Do as required to connect and disconnect from the environment
source [target-dir]/bin/activate
...
deactivate
```

## Datacube from pip
```bash
pip3 install datacube -U gdal=2.2.2  # use gdal version that matches the brew version, e.g. 1.11.5 if using standard brew
```

If there are errors that relate to uninstalling a package from /Library/Python/2.7/site-packages, then either:
  * Use the [package]==[installed version] parameter to the datacube install command
  * Alternatively, use root to upgrade the package:
```bash
sudo pip3 install [package] -U
```
   This will have the side effect of removing it from /Library/Python/2.7/site-packages and putting it in /usr/local/ (for brew), but this is no problem if you’re using brew for most things (could symlink it back to /Library/Python/2.7/site-packages)

```bash
sudo chown -R [username] /usr/local/lib/python2.7/site-packages/  # so you don’t need to be root for future pip updates.
```

## Datacube from source
```bash
cd [your-working-dir-for-code-repositories]/
git clone https://github.com/opendatacube/datacube-core.git
cd datacube-core/

python3 setup.py develop

./check_code.sh
```

# Configure DB
Follow instructions in readthedocs
