import os
import os.path
import sys
import shutil

embPreviousName = "May_30_2013"
embTargetName = "May_31_2013"
embPreviousRootPath = "/Users/fengka/Documents/Src/NeutronP4/Neutron/3p/EMB/" + embPreviousName + "/"
embRootPath = "/Users/fengka/Documents/Src/NeutronP4/Neutron/3p/EMB/" + embTargetName + "/"

srcIncludePath = "/Users/fengka/Documents/Src/Materials/include"
srcPathDebug = "/Users/fengka/Documents/Src/Materials/Toolkit/binary/bin/osx_clang_4.0/x64/Debug/"
srcPathRelease = "/Users/fengka/Documents/Src/Materials/Toolkit/binary/bin/osx_clang_4.0/x64/Release/"

destIncludePath = embRootPath + "Mac64/include"
destPathFrameworkDebug = embRootPath + "MAC64/Frameworks/Debug/EMB.framework/"
destPathFrameworkRelease = embRootPath + "MAC64/Frameworks/Release/EMB.framework/"

destPathBinaryDebug = embRootPath + "MAC64/binary/bin/osx_clang_4.0/x64/Debug/"
destPathBinaryRelease = embRootPath + "MAC64/binary/bin/osx_clang_4.0/x64/Release/"

embSrc = "/Users/fengka/Documents/Src/Materials/"

def SyncCode() :
	print "Pulling source code"
	os.chdir(embSrc)
	os.system("git pull")
	print "Pull code finished."

def BuildCode() :

	print "build debug."
	print "build release."


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
	shutil.copy(os.path.join(srcPathDebug,"libcJSON.dylib"), 				os.path.join(destPathFrameworkDebug,"libcJSON.dylib"))
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
	shutil.copy(os.path.join(srcPathRelease,"libcJSON.dylib"), 				os.path.join(destPathFrameworkRelease,"libcJSON.dylib"))
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
	shutil.copy(os.path.join(srcPathDebug,"libcJSON.dylib"), 				os.path.join(destPathBinaryDebug,"libcJSON.dylib"))
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
	shutil.copy(os.path.join(srcPathRelease,"libcJSON.dylib"), 				os.path.join(destPathBinaryRelease,"libcJSON.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libExDbCommon.dylib"), 		os.path.join(destPathBinaryRelease,"libExDbCommon.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"libExMatToolkit.dylib"), 		os.path.join(destPathBinaryRelease,"libExMatToolkit.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplus-1.0.4UD.dylib"), 	os.path.join(destPathBinaryRelease,"liblog4cplus-1.0.4UD.dylib"))
	shutil.copy(os.path.join(srcPathRelease,"liblog4cplusUD.dylib"), 		os.path.join(destPathBinaryRelease,"liblog4cplusUD.dylib"))

	print "All files copied."

def ArchiveFiles() :
	print "Starting to archiving..."
	cmd7z= "/Users/fengka/Documents/Src/NeutronP4/Neutron/main/src/Build/Mac/Tools/7zip/7za a -r /Users/fengka/Mac64.7z {0}".format(embRootPath + "MAC64/*")
	os.system(cmd7z);
	print "Archive finished."

def UploadToServer():
	print "start uploading..."
	print "Upload finished."




# Step 1: Sync code from git.
# SyncCode()

# Step 2: Build code. Debug/Release
BuildCode()

# Step 3: Copy files.
CopyFiles()

# Step 4: Archive to Mac64.7z
ArchiveFiles()

# Step 5: Upload to //eptbuild/eptstore/thirdparties/autocopy
UploadToServer()

