#!/bin/bash

revision=2908
i686=/usr/i686-w64-mingw32/sys-root/mingw/
x64=/usr/x86_64-w64-mingw32/sys-root/mingw/

mkdir -p r${revision}/{debug,release}/{32,64}

# Copy the files
cp ${i686}bin/{libexpat-1.dll,gdb.exe} r${revision}/debug/32/
cp ${x64}bin/{libexpat-1.dll,gdb.exe} r${revision}/debug/64/

echo "Copying and stripping files"
for f in imp2ld.exe addld.exe mod2zmod.exe imp2gbs.exe xml2gbs.exe imp2vs.exe vpl2mod.exe mkfastmod.exe mod2vpl.exe tei2mod.exe osis2mod.exe mod2osis.exe mod2imp.exe \
	installmgr.exe  diatheke.exe vs2osisreftxt.exe \
	uconv.exe icui18n48.dll icuuc48.dll icudata48.dll \
	libclucene-core.dll libclucene-shared.dll \
	libgcc_s_sjlj-1.dll libstdc++-6.dll \
	libsword.dll libcurl-4.dll libgnurx-0.dll zlib1.dll libidn-11.dll libssh2-1.dll libintl-8.dll \
	libcrypto-10.dll libssl-10.dll iconv.dll
do
	cp ${i686}bin/${f} r${revision}/debug/32/
	cp ${i686}bin/${f}.debug r${revision}/debug/32/
	cp ${x64}bin/${f} r${revision}/debug/64/
	cp ${x64}bin/${f}.debug r${revision}/debug/64/
	
	strip -o r${revision}/release/32/${f} ${i686}bin/${f}
	strip -o r${revision}/release/64/${f} ${x64}bin/${f}
done

# Create the zip files
echo "Creating zip files"
pushd r${revision}/debug/32/
zip ../../../sword-utils-${revision}-debug-i686.zip *
popd

pushd r${revision}/debug/64/
zip ../../../sword-utils-${revision}-debug-x64.zip *
popd

pushd r${revision}/release/32/
zip ../../../sword-utils-${revision}-release-i686.zip *
popd

pushd r${revision}/release/64/
zip ../../../sword-utils-${revision}-release-x64.zip *
popd
