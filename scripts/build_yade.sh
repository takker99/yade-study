#!/usr/bin/env bash
set -e

# Script to build YADE from source and prepare a local Python package in yade/
WORKDIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

echo "=== Installing build dependencies ==="
sudo apt-get update
sudo apt-get install -y cmake git freeglut3-dev libboost-all-dev fakeroot \
dpkg-dev build-essential g++ python3-dev python3-ipython python3-matplotlib \
libsqlite3-dev python3-numpy python3-tk gnuplot libgts-dev python3-pygraphviz \
libvtk9-dev libeigen3-dev python3-xlib python3-pyqt5 pyqt5-dev-tools python3-mpi4py \
python3-pyqt5.qtwebkit gtk2-engines-pixbuf python3-pyqt5.qtsvg libqglviewer-dev-qt5 \
python3-pil libjs-jquery python3-sphinx python3-git libxmu-dev libxi-dev libcgal-dev \
help2man libbz2-dev zlib1g-dev libopenblas-dev libsuitesparse-dev \
libmetis-dev python3-bibtexparser python3-future coinor-clp coinor-libclp-dev \
python3-mpmath libmpfr-dev libmpfrc++-dev libmpc-dev texlive-xetex python3-pickleshare python3-ipython-genutils

echo "=== Cloning YADE source ==="
cd "$WORKDIR"
if [ ! -d yade-source ]; then
    git clone https://gitlab.com/yade-dev/trunk.git yade-source
else
    echo "yade-source already exists, pulling latest changes"
    cd yade-source
    git pull
    cd "$WORKDIR"
fi

echo "=== Building YADE ==="
PREFIX="$WORKDIR/yade/install"
mkdir -p yade-source/build
cd yade-source/build
cmake .. -DCMAKE_INSTALL_PREFIX="$PREFIX" -DUSE_CXX17=ON -DCMAKE_BUILD_TYPE=Release
# JOBS=$(( ($(nproc) + 3) / 4 ))
# make -j"$JOBS"
make -j16
make install

echo "=== Preparing local YADE package ==="
SITE_PKG=$(find "$PREFIX/lib" -type d -path "*/site-packages" | head -n1)
rm -rf "$WORKDIR/yade/yade"
mkdir -p "$WORKDIR/yade"
rsync -av --exclude '__pycache__' "$SITE_PKG/yade/" "$WORKDIR/yade/"

echo "YADE build and local package preparation complete."
