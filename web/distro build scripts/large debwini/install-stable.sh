mount none -t proc /proc
mount none -t sysfs /sys
mount none -t devpts /dev/pts
export HOME=/root
export LC_ALL=C
apt-get update
apt-get install udev sudo nano man-db dialog dbus --yes --force-yes # try taking out udev
dbus-uuidgen > /var/lib/dbus/machine-id
/etc/init.d/udev start
echo "Debwini" > /etc/hostname
apt-get upgrade --yes && apt-get dist-upgrade --yes
apt-get install --no-install-recommends --yes --force-yes linux-image-amd64 live-boot \
net-tools wireless-tools network-manager tcpdump wget openssh-client pciutils usbutils \
gparted ntfsprogs hfsprogs dosfstools firmware-linux-free firmware-linux-nonfree flashplayer-nonfree banshee \
xfce4 lightdm g++ python3 google-chrome-stable openjdk-7-jdk transmission-gtk git
chmod 1777 /dev/shm
alsactl init
passwd root
adduser schwinn
adduser schwinn sudo
dpkg-reconfigure lightdm
nano /etc/lightdm/lightdm.conf

# LAMP
# wallpaper
# network manager to toolbar (maybe take out wpagui?)
# Install IDE (IntelliJ, Eclilpse, Netbeans) with plugins
