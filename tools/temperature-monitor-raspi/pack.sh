# 处理其他名称
archname=$(uname -m|tr A-Z a-z)
version=$(git describe --tags `git rev-list --tags --max-count=1`)
dirname=temper-monitor-$archname-$version
echo "Packing $dirname"
# 编译打包
# 移动文件
echo "Moving files..."
mkdir $dirname
cp -rv ./src $dirname/
cp -rv ./default-config $dirname/
cp -rv ./service $dirname/
cp -v {install,uninstall,start.sh,readme.md} $dirname
# 移除无需的内容
rm -v $dirname/src/*.conf
rm -v $dirname/src/.gitignore
# 压缩
echo "Compress files..."
tar -czf $dirname.tar.gz $dirname
# rm -r $dirname
# 移动文件夹
echo "Moving tar file..."
if [ ! -d ./release]; then
	mkdir ./release
fi
if [ ! -d ./release/$version ]; then
	mkdir ./release/$version
fi
# rm -r ../release/$1/$dirname
mv $dirname.tar.gz ./release/$version/$dirname.tar.gz