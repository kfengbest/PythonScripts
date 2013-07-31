import os
import os.path
import sys
import shutil

import subprocess

# TODO: Must be changed every time before do a new integration
# Change before integration:
embPreviousName = "July_26_2013"
embTargetName = "July_27_2013"
# Change above before integration

# TODO: Define this variable in your Mac OS system:
embSrc = "/Users/fengka/Documents/Src/Materials/"
emb3P = "/Users/fengka/Documents/Src/NeutronP4/Neutron/3p/EMB/"
embAutoCopy = "//eptbuild/epstore/3rdParties/AutoCopy/Neutron/EMB/"
zip7Path = "/Users/fengka/Documents/Src/NeutronP4/Neutron/main/src/Build/Mac/Tools/7zip/7za"
# Define this variable in your Mac OS system:


embPreviousRootPath = os.path.join(emb3P,embPreviousName)
embRootPath = os.path.join(emb3P,embTargetName)

embProject = os.path.join(embSrc, "source/Solutions")
srcIncludePath = os.path.join(embSrc, "include")
srcPathDebug = os.path.join(embSrc, "Toolkit/binary/bin/osx_clang_4.0/x64/Debug/")
srcPathRelease = os.path.join(embSrc, "Toolkit/binary/bin/osx_clang_4.0/x64/Release/")

destIncludePath = os.path.join(embRootPath,"Mac64/include")
destPathFrameworkDebug = os.path.join(embRootPath,"MAC64/Frameworks/Debug/EMB.framework/")
destPathFrameworkRelease = os.path.join(embRootPath,"MAC64/Frameworks/Release/EMB.framework/")

destPathBinaryDebug = os.path.join(embRootPath,"MAC64/binary/bin/osx_clang_4.0/x64/Debug/")
destPathBinaryRelease = os.path.join(embRootPath,"MAC64/binary/bin/osx_clang_4.0/x64/Release/")

curWDir = os.getcwd()


def CleanDir( Dir ):
    if os.path.isdir( Dir ):
        paths = os.listdir( Dir )
        for path in paths:
            filePath = os.path.join( Dir, path )
            if os.path.isfile( filePath ):
                try:
                    os.remove( filePath )
                except os.error:
                    autoRun.exception( "remove %s error." %filePath )
            elif os.path.isdir( filePath ):
                shutil.rmtree(filePath,True)
    return True


def SyncCode() :
	print "Pulling source code"
	os.chdir(embSrc)
	os.system("git pull")
	print "Pull code finished."

def BuildCode() :
	print "Clean Toolkit folder"
	os.chdir(embSrc)
	CleanDir(os.path.join(embSrc, "Toolkit"))

	print "building debug."
	os.chdir(embProject)
	os.system("xcodebuild -target \"AdExMatSample\" -project ExMaterials.xcodeproj -configuration Debug") 

	print "building release."
	os.system("xcodebuild -target \"AdExMatSample\" -project ExMaterials.xcodeproj -configuration Release") 


def CopyFiles() :
	print "Copying files..."

	if os.path.exists(embRootPath) == False :
		shutil.copytree(embPreviousRootPath, embRootPath)

	# Copy include folder:
	if os.path.exists(destIncludePath):
		shutil.rmtree(destIncludePath)
	shutil.copytree(srcIncludePath, destIncludePath)

	# Copy to debug framework
	shutil.copy(os.path.join(srcPathDebug,"AdExMatSample"), 				os.path.join(destPathFrameworkDebug,"AdExMatSample"))
	shutil.copy(os.path.join(srcPathDebug,"libAARToolkit.dylib"), 			os.path.join(destPathFrameworkDebug,"libAARToolkit.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExDbClient.dylib"), 		os.path.join(destPathFrameworkDebug,"libAdExDbClient.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExLog.dylib"), 				os.path.join(destPathFrameworkDebug,"libAdExLog.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExMatUtil.a"), 				os.path.join(destPathFrameworkDebug,"libAdExMatUtil.a"))
	shutil.copy(os.path.join(srcPathDebug,"libExDbCommon.dylib"), 			os.path.join(destPathFrameworkDebug,"libExDbCommon.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libExMatToolkit.dylib"), 		os.path.join(destPathFrameworkDebug,"libExMatToolkit.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"liblog4cplus-1.0.4UD.dylib"), 	os.path.join(destPathFrameworkDebug,"liblog4cplus-1.0.4UD.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"liblog4cplusUD.dylib"), 			os.path.join(destPathFrameworkDebug,"liblog4cplusUD.dylib"))

	if os.path.exists(os.path.join(destPathFrameworkDebug,"AdExMatSample.dSYM")):
		shutil.rmtree(os.path.join(destPathFrameworkDebug,"AdExMatSample.dSYM"))
	if os.path.exists(os.path.join(destPathFrameworkDebug,"libAARToolkit.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathFrameworkDebug,"libAARToolkit.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathFrameworkDebug,"libAdExDbClient.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathFrameworkDebug,"libAdExDbClient.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathFrameworkDebug,"libAdExLog.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathFrameworkDebug,"libAdExLog.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathFrameworkDebug,"libExMatToolkit.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathFrameworkDebug,"libExMatToolkit.dylib.dSYM"))

	shutil.copytree(os.path.join(srcPathDebug,"AdExMatSample.dSYM"), 			os.path.join(destPathFrameworkDebug,"AdExMatSample.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAARToolkit.dylib.dSYM"), 		os.path.join(destPathFrameworkDebug,"libAARToolkit.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAdExDbClient.dylib.dSYM"), 	os.path.join(destPathFrameworkDebug,"libAdExDbClient.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAdExLog.dylib.dSYM"), 		os.path.join(destPathFrameworkDebug,"libAdExLog.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libExMatToolkit.dylib.dSYM"), 	os.path.join(destPathFrameworkDebug,"libExMatToolkit.dylib.dSYM"))



	# Copy to Release framework.
	shutil.copy(os.path.join(srcPathRelease,"AdExMatSample"), 				os.path.join(destPathFrameworkRelease,"AdExMatSample"))
	shutil.copy(os.path.join(srcPathRelease,"libAARToolkit.dylib"), 		os.path.join(destPathFrameworkRelease,"libAARToolkit.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExDbClient.dylib"), 		os.path.join(destPathFrameworkRelease,"libAdExDbClient.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExLog.dylib"), 			os.path.join(destPathFrameworkRelease,"libAdExLog.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExMatUtil.a"), 			os.path.join(destPathFrameworkRelease,"libAdExMatUtil.a"))
	shutil.copy(os.path.join(srcPathRelease,"libExDbCommon.dylib"), 		os.path.join(destPathFrameworkRelease,"libExDbCommon.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libExMatToolkit.dylib"), 		os.path.join(destPathFrameworkRelease,"libExMatToolkit.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplus-1.0.4UD.dylib"), 	os.path.join(destPathFrameworkRelease,"liblog4cplus-1.0.4UD.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplusUD.dylib"), 		os.path.join(destPathFrameworkRelease,"liblog4cplusUD.dylib"))

	# Copy to debug binary
	shutil.copy(os.path.join(srcPathDebug,"AdExMatSample"), 				os.path.join(destPathBinaryDebug,"AdExMatSample"))
	shutil.copy(os.path.join(srcPathDebug,"libAARToolkit.dylib"), 			os.path.join(destPathBinaryDebug,"libAARToolkit.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExDbClient.dylib"), 		os.path.join(destPathBinaryDebug,"libAdExDbClient.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExLog.dylib"), 				os.path.join(destPathBinaryDebug,"libAdExLog.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libAdExMatUtil.a"), 				os.path.join(destPathBinaryDebug,"libAdExMatUtil.a"))
	shutil.copy(os.path.join(srcPathDebug,"libExDbCommon.dylib"), 			os.path.join(destPathBinaryDebug,"libExDbCommon.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"libExMatToolkit.dylib"), 		os.path.join(destPathBinaryDebug,"libExMatToolkit.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"liblog4cplus-1.0.4UD.dylib"), 	os.path.join(destPathBinaryDebug,"liblog4cplus-1.0.4UD.dylib"))
	shutil.copy(os.path.join(srcPathDebug,"liblog4cplusUD.dylib"), 			os.path.join(destPathBinaryDebug,"liblog4cplusUD.dylib"))

	if os.path.exists(os.path.join(destPathBinaryDebug,"AdExMatSample.dSYM")):
		shutil.rmtree(os.path.join(destPathBinaryDebug,"AdExMatSample.dSYM"))
	if os.path.exists(os.path.join(destPathBinaryDebug,"libAARToolkit.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathBinaryDebug,"libAARToolkit.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathBinaryDebug,"libAdExDbClient.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathBinaryDebug,"libAdExDbClient.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathBinaryDebug,"libAdExLog.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathBinaryDebug,"libAdExLog.dylib.dSYM"))
	if os.path.exists(os.path.join(destPathBinaryDebug,"libExMatToolkit.dylib.dSYM")):
		shutil.rmtree(os.path.join(destPathBinaryDebug,"libExMatToolkit.dylib.dSYM"))

	shutil.copytree(os.path.join(srcPathDebug,"AdExMatSample.dSYM"), 			os.path.join(destPathBinaryDebug,"AdExMatSample.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAARToolkit.dylib.dSYM"), 		os.path.join(destPathBinaryDebug,"libAARToolkit.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAdExDbClient.dylib.dSYM"), 	os.path.join(destPathBinaryDebug,"libAdExDbClient.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libAdExLog.dylib.dSYM"), 		os.path.join(destPathBinaryDebug,"libAdExLog.dylib.dSYM"))
	shutil.copytree(os.path.join(srcPathDebug,"libExMatToolkit.dylib.dSYM"), 	os.path.join(destPathBinaryDebug,"libExMatToolkit.dylib.dSYM"))

	# Copyt to Release binary
	shutil.copy(os.path.join(srcPathRelease,"AdExMatSample"), 				os.path.join(destPathBinaryRelease,"AdExMatSample"))
	shutil.copy(os.path.join(srcPathRelease,"libAARToolkit.dylib"), 		os.path.join(destPathBinaryRelease,"libAARToolkit.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExDbClient.dylib"), 		os.path.join(destPathBinaryRelease,"libAdExDbClient.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExLog.dylib"), 			os.path.join(destPathBinaryRelease,"libAdExLog.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libAdExMatUtil.a"), 			os.path.join(destPathBinaryRelease,"libAdExMatUtil.a"))
	shutil.copy(os.path.join(srcPathRelease,"libExDbCommon.dylib"), 		os.path.join(destPathBinaryRelease,"libExDbCommon.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libExMatToolkit.dylib"), 		os.path.join(destPathBinaryRelease,"libExMatToolkit.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplus-1.0.4UD.dylib"), 	os.path.join(destPathBinaryRelease,"liblog4cplus-1.0.4UD.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplusUD.dylib"), 		os.path.join(destPathBinaryRelease,"liblog4cplusUD.dylib"))

	print "All files copied."

def ArchiveFiles() :
	print "Starting to archiving..."
	cmd7z= "{0} a -r {1} {2}".format(zip7Path, os.path.join(curWDir,"MAC64.7z"), os.path.join(embRootPath,"MAC64/*"))

	os.system(cmd7z);
	print "Archive finished."


def UploadToServer():
	print "start uploading..."
	newEMBFolder = os.path.join(embAutoCopy,embTargetName)
	
	print os.path.join(curWDir,"MAC64.7z")
	print newEMBFolder
	print "rsync {0} rsync:{1}".format(os.path.join(curWDir,"MAC64.7z"),newEMBFolder)

	os.system("rsync {0} rsync:{1}".format(os.path.join(curWDir,"MAC64.7z"),newEMBFolder))
	print "Upload finished."




# Step 1: Sync code from git.
SyncCode()

# Step 2: Build code. Debug/Release
BuildCode()

# Step 3: Copy files.
CopyFiles()

# Step 4: Archive to Mac64.7z
ArchiveFiles()

# Step 5: Upload to //eptbuild/eptstore/thirdparties/autocopy
UploadToServer()

