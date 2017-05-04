# Mac and Hobrew build and install instructions

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
echo 'export HOMEBREW_GITHUB_API_TOKEN="your_new_token"' >> ~/.bashrc
source ~/.bashrc
```

3. Set directory permissions (optional)
  * Not critical for brew install but handy for apps that need to write to /usr/local
```bash
sudo chown <user>:admin /usr/local
```

4. Get homebrew to a happy place
```bash
brew update
brew update  # a second time
brew doctor  # best to fix any concerns before continuing
```

## Packages
Not all of these are critical bu they are handy.
```bash
brew install python
brew install homebrew/dupes/zlib
brew install homebrew/science/hdf5
brew install homebrew/science/netcdf
brew install geos
brew install proj
brew install imagemagick
brew install homebrew/science/nco
brew install gdal
brew install libyaml
```

To Pip or Brew? Pip is preferred for python libs
```bash
pip install --upgrade pip setuptools
pip install nose
pip install numpy
pip install scipy
pip install h5py
pip install netCDF4
pip install gdal=1.11.5  # version needs to match brew version
pip install matplotlib

wget https://downloads.sourceforge.net/project/matplotlib/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz
tar xzf basemap-1.0.7.tar.gz
cd basemap-1.0.7
pip install .

pip install pyproj
pip install pyshp
pip install pydap
pip install glueviz -- includes pands
pip install pillow
pip install shapely

pip install jupyter jupyterdrive
pip install rasterio numexpr
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

pip install psycopg2
```

## Datacube from pip
```bash
pip install datacube -U gdal=1.11.5  # use gdal version that matches the brew version
```

If there are errors that relate to uninstalling a package from /Library/Python/2.7/site-packages, then either:
  * Use the [package]==[installed version] parameter to the datacube install command
  * Alternatively, use root to upgrade the package:
```bash
sudo pip install [package] -U
```
   This will have the side effect of removing it from /Library/Python/2.7/site-packages and putting it in /usr/local/ (for brew), but this is no problem if you’re using brew for most things (could symlink it back to /Library/Python/2.7/site-packages)

```bash
sudo chown -R [username] /usr/local/lib/python2.7/site-packages/  # so you don’t need to be root for future pip updates.
```

## Datacube from source
```bash
cd /usr/local
git clone https://github.com/data-cube/agdc-v2.git
cd agdc-v2/

python setup.py develop

pip install pep8 pylint fiona
./check_code.sh
```

# Configure DB
Follow instructions in readthedocs
