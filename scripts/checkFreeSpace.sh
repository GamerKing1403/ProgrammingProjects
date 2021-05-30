used=$(df -h /dev/sdb3 --output=used | sed -n '2p')
size=$(df -h /dev/sdb3 --output=size | sed -n '2p')
echo used+'\'+size
