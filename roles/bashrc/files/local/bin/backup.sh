external="/run/media/greg/My Book/ManualBackups"
local="/shared/Backup"
local="${external}"

# First, backup the server's config
echo "Backing up server config"
cd "${local}/thehellings.com"
if [ ! -d etc ]; then
	git clone ssh://root@thehellings.com/etc/
fi
pushd etc
git pull
popd

# Next, backup the server's sites
echo "Backing up server site data"
if [ ! -d home ]; then
	mkdir -p home;
fi
pushd home
rsync -az --delete-delay --progress thehellings.com:/home/greg .
rsync -az --delete-delay --progress thehellings.com:/home/sites .
popd
rsync -az --delete-delay --progress --exclude='.cache' thehellings.com:/srv .


# Next, we backup things from my local machine
echo "Backing up local configuration"
cd "${local}/home.thehellings.com"
if [ ! -d etc ]; then
	git clone home.thehellings.com:/etc/;
fi
pushd etc
git pull
popd

# And, of course, my home directory
mkdir -p "${local}/desktop.home.thehellings.com"
cd "${local}/desktop.home.thehellings.com"
echo "Backing up my home drive"
rsync -az --delete-delay --progress --exclude='.cache,lost+found' /home .

echo "Backing up Files"
rsync -azv --delete-delay --progress /shared/Files "${external}/.."
echo "Backing up Videos"
rsync -azv --delete-delay --progress /shared/Videos "${external}/.."

# Now, copy the whole thing to the backup drive as well
#echo "Copying all data to the external device"
#rsync -azv --progress "${local}/" "${external}/"
#rm -rf "${external}/*"
#cp -R "${local}/thehellings.com" "${external}"
#cp -R "${local}/home.thehellings.com" "${external}"
